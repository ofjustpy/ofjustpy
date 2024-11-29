Code Layout
=============

kavya/__init__.py
-----------------
#. build_app(*args, **kwargs)
#. load_app()
#. class MountCtx
#. def add_jproute(path,
#. def create_endpoint_impl(wp_template):
#. page_builder(key=None,
#. def set_pagecontent_builder(pagecontent_builder)
#. def href_builder_factory(route_name):
#. href_builder_factory(route_name)
#. class PageBuilderCtx

   
ui_styles.py
------------
#. class TwStyCtx:
   

snowsty/transparentsty/unsty
----------------------------



SVGcomponents.py
----------------
#. class Div_SVG_Mixin

   
parse_svg_component.py
----------------------
#. def parse(svg_content):
#.    

ofjustpy_utils.py
-----------------
#. def get_svelte_safelist(stubStore):

#. def traverse_component_hierarchy(rdbref):

#. def csrfprotect(func):

MHC_types.py
------------

#. class ChartJSMixin

#. class StackDMixin:

#. class HCCStatic:

#. class HCCMutable:

   
justpy_svg_tags.py
------------------

#. svg_tags


icons.py
--------

#. FontAwesomeIcon = gen_HC_type
   
htmlcomponents_impl.py
----------------------

#. def assign_id(hc_gen)

#. class MutableShell_SliderMixin:

#. class MutableShell_CSMixin

#. def CS_event_prehook(on_event_callback):
   
htmlcomponents.py
-----------------
#. class ActiveComponents:

#. class ActiveDivs:
    
#. class HCCStatic:

#. class Mutable:

   
kavya/HC_wrappers.py
--------------------

#. Halign

#. StackH_Aligned

#. WithBanner   

kavya/generate_WebPage_response_mixin.py
----------------------------------------
#. class ResponsiveStatic_SSR_ResponseMixin
#. class ResponsiveStatic_CSR_ResponseMixin:

HC_TF.py
--------
#. def gen_HC_type(

HC_wrappers.py
--------------
#. def Halign(
   

kavya/app_code_introspect
-------------------------
#. user_model = None

#. the_starlette_app = None

#. mount_route_stack = None

#. pagecontent_builder = None

#. load_models(): # not working
   - load sqlalchemy/user_model using
#. get_user_model() # not working
#. set_sqlalchemy_session(session):
#. get_app():
   
kavya/data_validator.py
-----------------------

#. validate(validation_chain, data, stubStore)

#. def InputRequired():

#. def EqualTo(other_spath):

#. def Email(

#. def Length(min=-1, max=-1):

kavya/db_middleware.py
----------------------

#. class DBSessionMiddleware

kavya/Div_TF.py
---------------

#. def gen_Div_type(
   

core_engine/middlewares.py
--------------------------
#. class DBSessionMiddleware:

core_engine/session_middlewares
-------------------------------
#. class SessionMiddleware:
   
core_engine/jpcore/utilites
---------------------------
#. async def create_delayed_task(task, delay, loop):
#. def run_task(task):
#. def print_request(request):
#. def find_files(path: str, ext: str) -> list:
   


core_engine/jpcore/template
---------------------------
#. class Context:
#. class PageOptions:



core_engine/jpcore/justpy_config
--------------------------------
#. class JpConfig(Config):
   

core_engine/jpcore/justpy_app
-----------------------------
#. def target_of(item, stubStore):
#. async def run_event_function(
#. async def handle_event(data_dict, com_type=0, page_event=False):
#. class JustpyApp(Starlette):
#. class JustpyAjaxEndpoint(HTTPEndpoint):
#. def uvicorn_server_control_center(


core_engine/jpcore/jpconfig
---------------------------

#. CRASH = None
#. COOKIE_MAX_AGE = None
#. CRASH = None
#. DEBUG = None
#. FAVICON = None
#. FRONTEND_ENGINE_TYPE = None
#. FRONTEND_ENGINE_LIBS = None
#. HOST = None
#. LATENCY = None
#. LOGGING_LEVEL = None
#. MEMORY_DEBUG = None
#. NO_INTERNET = None
#. PORT = None
#. SECRET_KEY = None
#. SESSION_COOKIE_NAME = "session"
#. SESSIONS = None
#. SSL_CERTFILE = None
#. SSL_KEYFILE = None
#. SSL_VERSION = None
#. STATIC_DIRECTORY = None
#. STATIC_NAME = None
#. STATIC_ROUTE = None
#. TAILWIND = None
#. UVICORN_LOGGING_LEVEL = None
#. VERBOSE = None
#. BASE_URL = None
#. USE_COOKIE_MIDDLEWARE = False
#. USE_SVELTE_SKELETON = True
#. SQLALCHEMY_DB_CONNECTION_URL = None
#. SQLALCHEMY_BASENAME = None
#. SQLALCHEMY_DBMODELS_PYMODULE_NAME  = None
#. AUTH_USER_MODEL = None
#. # Webpage caching
#. CACHE_WEBPAGES=True
#. NOSESSION_WEBPAGE_CACHESIZE = 10
#. SESSION_WEBPAGE_CACHESIZE = 10
   




core_engine/jpcore/AppDB.py
---------------------------
global datastructures to maintain bookkeeping/mapping
from pageID to webpages and their sockets

#. pageId_to_webpageInstance
#. pageId_to_websockets
#. loop


core_engine/WebPage_type_mixin.py
---------------------------------
#. class WebPageType(Enum):
#. class WebPageMixin:


core_engine/tailwind_svelte_component_mixin
-------------------------------------------
#. CollapsibleMixin:
#. class SwitchMixin:


core_engine/tracker.py
----------------------
#. curr_session_manager
#. session_manager_store
#. async def purge_session(session_id=None):
#. class SessionManager:
#. def get_session_manager(request):
#. def trackStub(func):
#. class sessionctx:
#. class LRUCacheWithCallback(cachetools.LRUCache):
#. wp_endpoint_cache
#. class NoSession_LRUCacheWithCallback(cachetools.LRUCache):
#. nosession_webpage_cache =
#. def webpage_cache_nosession(key):
#. def webpage_cache(key):


   

core_engine/static_core_tracker
-------------------------------
#. hierarchy_tracker
#. curr_hierarchy_tracker   
#. class uictx:
#. def id_assigner
   

core_engine/TF_impl (misnomer should be stubs.py)
-------------------------------------------------

#. Stub_HCStatic
#. Stub_HCPassive(Stub_HCStatic)
#. Stub_DivPassive(Stub_HCPassive)
#. Stub_HCActive(Stub_HCStatic)
#. Stub_DivActive(Stub_HCActive)
#. gen_Stub_HCPassive(target, **kwargs):
#. gen_Stub_DivPassive(target, **kwargs):
#. gen_Stub_HCActive(target, **kwargs):
#. gen_Stub_HCMutable(mutable_shell_type, **kwargs):
#. gen_Stub_DivActive(target, **kwargs):
#. gen_Stub_HCCMutable(*args, **kwargs):
#. Stub_HCMutable:   
#. Stub_DivMutable:
#. Stub_HCCStatic(Stub_DivMutable):
#. Stub_HCCMutable:
#. gen_Stub_DivMutable(mutableShell_type, **kwargs):
#. Stub_WebPage:
#. def gen_Stub_WebPage(*args, **kwargs):



core_engine/mutable_HC_TF
-------------------------

#. HCTextSharerMixin
#. TwStySharerMixin
#. HCTextPropertyMixin
#. RenderHTMLMixin



   
core_engine/mutable_TF_impl
---------------------------

#. StaticCore_HCRenderHTMLTemplateMixin
#. StaticCore_JsonMixin
#. JsonMixin_Base
#. MutableShell_JsonMixin
#. HCMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
#. HCCStatic_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
#. HCCMutable_JsonMixin(JsonMixin_Base)
#. DivMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
#. CoreChildMixin
#. HCCMixin_MutableChilds
#. Prepare_HtmlRenderMixin
#. RenderHTML_HCCMutableChildsMixin
#. RenderHTML_HCCStaticChildsMixin
#. HCCMixin_StaticChilds:
#. StaticCoreSharer_BaseMixin
#. StaticCoreSharer_EventMixin
#. StaticCoreSharer_ClassesMixin
#. StaticCoreSharer_IdMixin
#. StaticCoreSharer_ValueMixin
#. StaticCoreSharer_HCCStaticMixin





core_engine/mutable_Div_TF.py
-----------------------------
#. classTypeGen
   

core_engine/justpy.py
---------------------
#. build_app()
   

core_engine/HCType.py
---------------------
#. HCType(Enum)
   
   
core_engine/HC_type_mixins_extn
-------------------------------

#. LabelMixin
#. InputMixin
#. TextInputMixin(InputMixin):
#. CheckboxInputMixin(InputMixin)   
#. RadioInputMixin(InputMixin)
#. TextareaMixin(InputMixin)
#. OptionMixin
#. SelectInputMixin(InputMixin):
#. HrMixin
   
core_engine/HC_Div_type_mixins
------------------------------

#. IdMixin
#. KeyMixin
#. PassiveKeyMixin
#. jpBaseComponentMixin
#. HTMLBaseComponentExtnMixin
#. HCTextMixin
#. DivMixin
#. SvelteSafelistMixin
#. TwStyMixin
#. DOMEdgeMixin
#. EventMixinBase


core_engine/SHC_types_mixin.py
------------------------------

JsonMixins
~~~~~~~~~~

#. StaticJsonMixin

#. PassiveJsonMixin(StaticJsonMixin)

#. ActiveJsonMixin(StaticJsonMixin)

#. HCCPassiveJsonMixin
   - For  divs with passive components

#. HCCJsonMixin(StaticJsonMixin)
   - for divs with non-passive childs
     - obj_json is not precomputed
       - call to build_json rebuilds obj_json
	 
Misc. Mixins
~~~~~~~~~~~~

#. HTTPRequestCallbackMixin
#. DataValidators

Core Mixins
~~~~~~~~~~~

#. StaticCore
    - provides
      - self.domDict
      - self.attrs
	
Div/Containers Mixins
~~~~~~~~~~~~~~~~~~~~~

#. HCCStaticMixin
   - self.components
   - add_register_childs(self):
     
#. HCCPassiveMixin(HCCStaticMixin):

#. HCCActiveMixin(HCCStaticMixin):

RenderHTMLMixin
~~~~~~~~~~~~~~~
#. PassiveHC_RenderHTMLMixin
   
#. ActiveDiv_RenderHTMLMixin
   
#. ActiveHC_RenderHTMLMixin

#. PassiveDiv_RenderHTMLMixin


   
Component Type Generator
~~~~~~~~~~~~~~~~~~~~~~~~
#. staticClassTypeGen



