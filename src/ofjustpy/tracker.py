import logging
import os

if os:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

import json
import logging
import os
import traceback
import typing
from itertools import tee
from typing import get_type_hints
import functools
from typing import Any, NamedTuple
from addict_tracking_changes import Dict
from py_tailwind_utils import dnew
import cachetools
import asyncio
from ofjustpy_engine import report_memory_usage
from py_tailwind_utils import tstr

# This is a global variable
curr_session_manager = None

# session_id to session_mgr map
# if session_mgr already exists for session_id return that.
session_manager_store = {}  # a global variable

logger.debug("Testing if logging is working")


async def purge_session(session_id=None):
    # wait for 2 seconds before purging a session
    await asyncio.sleep(2)
    # remove session_id page entries from AppDB.pageId_to_webpageInstance
    print("Purging pages and removing from session_manager_store")
    report_memory_usage()
    session_manager_store[session_id].purge_pages()
    del session_manager_store[session_id]
    report_memory_usage()

    pass


class SessionManager:
    def __init__(self, request):
        self.stubStore = Dict(track_changes=True)
        self.appstate = Dict(track_changes=True)

        self.session_id = request.session_id
        self.request = request
        # cache (see below) populates the activ_connections with page_ids
        self.active_pages = set()


        # all the tw directives used by app's webpages
        self.all_twsty = set()
        
        
        # all pages that belong to this session_manager
        self.pages = set()

    def track_stub(self, func, *args, **kwargs):
        stub = func(*args, **kwargs, session_manager=self)
        dnew(self.stubStore, stub.id, stub)

        return stub


    def purge_pages(self):
        for wp in self.pages:
            wp.purge_page()

    def schedule_page_removal(self, wp):
        # if self.cleanup_task:
        #     self.cleanup_task.cancel()
        #     self.cleanup_task = None
        # reset cleanup task with delay
        # self.start_cleanup_task()

        try:
            self.active_pages.remove(wp.page_id)
        except KeyError:
            print(f"++++++++++++++++++++ MEGA SCREWUP: {self.session_id}  {page_id}")
            raise ValueError("MEGA SCREWUP")

        # if there are no active pages in this session
        if not self.active_pages:
            print(
                f"@@@SESSION CLEANUP@@@@@@@ : proceed with eviction/cleanup of the session...no active pages {wp.page_id},  , {self.session_id}"
            )

            # should clean things up: eventually
            # WebPage.instances doesn't hold reference to webpages
            # session_mgr_store doesn't hold reference
            # its not in cache.

            # this should cleanup all the mutable element reference

            # del session_mgr_store[self.session_id]
            loop = asyncio.get_event_loop()
            self.purge_task = loop.create_task(purge_session(self.session_id))

        pass


def get_session_manager(request):
    global session_manager_store
    if request.session_id in session_manager_store:
        return session_manager_store[request.session_id]
    session_manager = SessionManager(request)
    session_manager_store[request.session_id] = session_manager

    return session_manager


def trackStub(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return curr_session_manager.track_stub(func, *args, **kwargs)

    return wrapper




class sessionctx:
    def __init__(self, session_mgr, **kwargs):
        global curr_session_manager
        if curr_session_manager is not None:
            raise ValueError(
                f"Fatal error: building new session ctx within an existing one {curr_session_manager} {session_mgr}"
            )
        curr_session_manager = session_mgr
        pass

    def __enter__(self):
        return curr_session_manager

    def __exit__(self, type, value, traceback):
        global curr_session_manager
        curr_session_manager = None
        pass


# ========================= cache management=========================
import cachetools


class LRUCacheWithCallback(cachetools.LRUCache):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def popitem(self):
        key, value = super().popitem()
        wp = value
        logging.info(
            f"====> kicked out from cache: {wp.session_manager.session_id} {wp.page_id}"
        )
        if wp.is_active == False:
            logging.info(
                f"======> Page is kicked out of cache and is not active: proceed with cleanup {wp.session_manager.session_id}   {wp.page_id}"
            )
            wp.session_manager.schedule_page_removal(wp)
        else:
            logging.info(
                "======> Page is kicked out of cache and is  active :== not proceeding to clean"
            )
            wp.is_cached = False
            pass
        return key, value


wp_endpoint_cache = LRUCacheWithCallback(maxsize=4)


def webpage_cache(key):
    def webpage_cache_inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            # if the session_id is scheduled for removal then cancel it.

            cache_key = (request.session_id, key)
            if cache_key in wp_endpoint_cache:
                logging.info(f"================> returning from cache {cache_key}")
                logging.debug(f"================> returning from cache {cache_key}")
                wp = wp_endpoint_cache[cache_key]
                wp.is_active = True
                wp.is_cached = True

                wp.session_manager.active_pages.add(wp.page_id)
                # register the page with session manager
                wp.session_manager.pages.add(wp)
                return wp_endpoint_cache[cache_key]
            wp = func(*args, **kwargs)

            logging.info(
                f"================> not in cache: create a new page: {cache_key}"
            )
            logging.debug(
                f"================> not in cache: create a new page: {cache_key}"
            )
            wp_endpoint_cache[cache_key] = wp
            wp.is_active = True
            wp.is_cached = True
            wp.session_manager.active_pages.add(wp.page_id)
            wp.session_manager.pages.add(wp)
            return wp

        return wrapper

    return webpage_cache_inner
