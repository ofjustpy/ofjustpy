"""
A webdev framework that enables development of full-stack webpages and apps purely in Python
"""
__version__ = "1.1.4"
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import os
import sys
import importlib

import ofjustpy_engine as jp
from starlette.routing import Mount, Route

from .ui_styles import set_style, TwStyCtx
import importlib.util
from ofjustpy_engine import *
from . import data_validator as validator
from . import app_code_introspect as aci
from .icons import FontAwesomeIcon
def build_app(*args, **kwargs):
    """
    We maintain only one app per
    python runtime. The global app is stored
    as aci.the_starlette_app.
    build_app should be called only once per runtime
    """

    assert aci.the_starlette_app is None
    app = jp.build_app(*args, **kwargs)
    aci.the_starlette_app = app
    aci.mount_route_stack = [aci.the_starlette_app.router.routes]
    return app


def load_app():
    if aci.the_starlette_app is not None:
        return aci.the_starlette_app

    # the first time load_app is called
    # it will load OJ_APP_MODULE which will
    # call build_app
    OJ_APP_MODULE = "./app"
    if "OJ_APP_MODULE" in os.environ:
        OJ_APP_MODULE = os.environ["OJ_APP_MODULE"]

    sys.path.append(os.path.dirname(OJ_APP_MODULE))
    app_module = importlib.import_module(os.path.basename(OJ_APP_MODULE))
    aci.the_starlette_app = app_module.app
    return aci.the_starlette_app


class MountCtx:
    def __init__(self, mount_point_name):
        self.mount_point_name = mount_point_name

        # create container for routes for this mount point

    def __enter__(self):
        aci.mount_route_stack.append([])

    def __exit__(self, exc_type, exc_value, traceback):
        # covert all the collected routes and make one Mount object()

        # all the routes for this mount point
        routes = aci.mount_route_stack[-1]
        aci.mount_route_stack.pop()

        # create a mount point
        # Routed paths must start with '/'
        mount_obj = Mount(
            "/" + self.mount_point_name, name=self.mount_point_name, routes=routes
        )

        # add point to top container
        aci.mount_route_stack[-1].append(mount_obj)


def add_jproute(path,
                endpoint,
                **kwargs):
    """
    endpoint: is a function that returns WebPage-like object
    wrap endpoint in a function that will return a starlette-response like object
    register that function with starlette at the given path. 
    """
    starlette_endpoint = aci.the_starlette_app.response(endpoint)
    aci.mount_route_stack[-1].append(
        Route(path, starlette_endpoint, name=endpoint.route_name, **kwargs)
    )

    pass



from ofjustpy_engine.static_core_tracker import uictx

from ofjustpy_engine.tracker import (
    get_session_manager,
    sessionctx,
    curr_session_manager,
    webpage_cache,
    webpage_cache_nosession,
    session_manager_store 
)
from .htmlcomponents import (Mutable,
                             HCCMutable,
                             ActiveComponents as AC,
                             PassiveComponents as PC,
                             HCCStatic,
                             ActiveDivs as AD,
                             HUI,
                             SKUI,
                             SKHUI
)
from .SHC_types import     PassiveDivs as PD
from .HC_wrappers import Halign, StackH_Aligned, WithBanner


def create_endpoint_impl(wp_template):

    match (jpconfig.SESSIONS, jpconfig.CACHE_WEBPAGES):
        case (True, True):
            @webpage_cache(wp_template.id)
            def wp_endpoint(request, *args, **kwargs):
                sm = get_session_manager(request)
                with sessionctx(sm):
                    wp_ = wp_template.stub()
                    wp = wp_(request, *args, **kwargs)
                    wp.post_init(session_manager=sm)
                    wp.to_json_optimized = True
                    wp.session_manager = sm
                return wp
            wp_endpoint.route_name = wp_template.key
            return wp_endpoint
    
        case (True, False):
            def wp_endpoint(request, *args, **kwargs):
                print("Sessions are enabled, but webpage caching is disabled.")
                sm = get_session_manager(request)
                with sessionctx(sm):
                    wp_ = wp_template.stub()
                    wp = wp_(request, *args, **kwargs)
                    wp.post_init(session_manager=sm)
                    wp.to_json_optimized = True
                    wp.session_manager = sm
                return wp
            wp_endpoint.route_name = wp_template.key
            return wp_endpoint
        
        case (False, True):
            @webpage_cache_nosession(wp_template.id)
            def wp_endpoint(request, *args, **kwargs):
                wp_ = wp_template.stub()
                wp = wp_(request, *args, **kwargs)
                wp.post_init(session_manager=None)
                wp.to_json_optimized = True
                return wp
            wp_endpoint.route_name = wp_template.key
            return wp_endpoint
    
        case (False, False):
            def wp_endpoint(request, *args, **kwargs):
                wp_ = wp_template.stub()
                wp = wp_(request, *args, **kwargs)
                wp.post_init(session_manager=None)
                wp.to_json_optimized = True
                return wp
            wp_endpoint.route_name = wp_template.key
            return wp_endpoint
                
        case _:
            print("Unknown state.")

        


def default_page_builder(key=None,
                         childs=[],
                         rendering_type="CSR",
                         request_handler = None, 
                         **kwargs):
    # by default we perform client side rendering
    # its more powerful -- incorporates svelte components

    if rendering_type == "CSR":
        return Mutable.ResponsiveStatic_CSR_WebPage(
            key=key,
            childs=childs,
            request_handler=request_handler,
            
            cookie_state_attr_names=aci.the_starlette_app.cookie_state_attr_names,
            **kwargs,
        )
    if rendering_type == "SSR":
        return Mutable.ResponsiveStatic_SSR_WebPage(key=key,
                                                    childs =childs,

                                                    cookie_state_attr_names=aci.the_starlette_app.cookie_state_attr_names,
                                                    request_handler=request_handler,
                                                    **kwargs
                                                   )

    assert False
    


def default_pagecontent_builder(key, childs):
    return childs

def get_pagecontent_builder():
    if aci.pagecontent_builder is None:
        return default_pagecontent_builder
    return aci.pagecontent_builder

def get_page_builder():
    if aci.page_builder is None:
        return default_page_builder
    return aci.page_builder

def create_endpoint(key, childs,  **kwargs):
    """
    allows oj.create_endpoint to be used from within the PageBuilderCtx.
    Note: currently PageBuilderCtx cannot be nested
    """

    pagecontent_builder = get_pagecontent_builder()
    pagecontent_childs = pagecontent_builder(key, childs)
    page_builder = get_page_builder()
    wp_template = page_builder(key, childs=pagecontent_childs,
                                    **kwargs)
    
    wp_endpoint = create_endpoint_impl(wp_template)
    return wp_endpoint



    


class PageContentBuilderCtx:
    def __init__(self, pagecontent_builder):
        self.pagecontent_builder = pagecontent_builder
        
        # create container for routes for this mount point

    def __enter__(self):
        aci.pagecontent_builder = self.pagecontent_builder
        
    def __exit__(self, exc_type, exc_value, traceback):
        aci.pagecontent_builder = default_pagecontent_builder
        

class PageBuilderCtx:
    def __init__(self, page_builder):
        self.page_builder = page_builder
        
        # create container for routes for this mount point

    def __enter__(self):
        aci.page_builder = self.page_builder
        
    def __exit__(self, exc_type, exc_value, traceback):
        aci.page_builder = default_page_builder

def href_builder_factory(route_name):
    """
    Use this function-factory to create href attribute updater for oj.AC.A component.
    oj.AC.A(key="back_to_examples_index",
                href_builder = oj.href_builder_factory("examples:index"),
          )
    When A is instantiated (for a page), href builder will
    find the url for the route label and update the href attribute accordingly
    """

    def href_updater(Acomp_ref, session_manager, route_name=route_name):
        url = session_manager.request.url_for(route_name)
        logger.debug(f"GOT url for {route_name} : {url}")
        logger.debug(f"GOT url for {route_name} : {type(url)}")
        # Replace 'http' with 'https'
        url = url.replace(scheme="https")
        # it seems we are getting
        # assert url.startswith("http")
        Acomp_ref.href = str(url)  # "https" + url[4:]
        # Acomp_ref.href = url

    return href_updater
