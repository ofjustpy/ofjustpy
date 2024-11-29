Caching
-------

#. ofjustpy_engine.tracker
   
   .. code-block::
      wp_endpoint_cache = LRUCacheWithCallback(maxsize=4)
WebPage lifecycle
^^^^^^^^^^^^^^^^^

On Initialization
+++++++++++++++++

Reference to page is stored in

#. In AppDB
   - AppDB.pageId_to_webpageInstance[self.page_id] = self
     
Only When session is enabled
""""""""""""""""""""""""""""
#. Within Page stub
   - stub.target

#. Stub maintains a reference. the stub is  maintained in
   - session_manager.stubStore

#. a reference inside the cache
   - wp_endpoint_cache

     
On Page Disconnect
''''''''''''''''''

for sessions pages: 

#. page.is_active counter is decremented

   .. code-block::
      
      self.is_active = False
      
If the counter reaches zero and the page is not cached,
then it is removed from session_manager.active_pages.

for nosession page:

#. is_active counter is decremented
#. if it reaches zero and is not cached
   - then purge_page
     
#. when cache evicted then
   - if is_active is zero
     - then purge_page


SessionManager lifecycle
^^^^^^^^^^^^^^^^^^^^^^^^

Every session manager maintains a list of active_pages.

#. Pages are added to active_pages if they are requested
from cache or initialized.

#. A page is Removed from active_pages, if page.is_active counter
   reaches 0, and is_cached is False

#. If active_pages is empty, then purge_session is scheduled.
   Wait for 2 seconds before purging a session.

   


