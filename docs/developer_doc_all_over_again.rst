
TBD
~~~
#. attr_tracked_keys
#. domDict_tracked_keys   
#. whats the deal with add_register_childs
#. The whole prepare_htmlRender, build_renderHtml
#. DataValidators
#. http_request_callback_mixin
#. Caching

High level system architecture/code design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two phases
- Declaration phase
- DOM Generation phase

Declaration phase
.................

In declaration phase, each component declares who its  childs are along with
static attributes and initial values for mutable attributes.

DOM Generation phase
....................
Starting from root which is WebPage class



DOM Generation phase
....................
at initialization register-the-childs, which implies calling the
.. code-block:: python

   c_ = c.stub()
   c_(self)
   # add to spathMpa
   
.. note::
   Now when c.stub() is called for passive it directly returns the dummy stub,
   for active/mutual,  c.stub() calls the `stub_gen` func which is getting tracked.
   The `stub_gen` func return `c_` which is a stub and is callable, i.e. it has `__call__`
   member. 
   The c_(self) invokes the __call__ interface of the stub.
   This is where the recursive magic happens.
   Each div calls add_register_components:
   which call stub and __call__ for each of the child. This unravles deep nesting.
   For the call build_json is called to build json based upon the child's json.

.. note: move this to its proper place   
- When is build_json called
called by stub after the childs are registered


Overall Code layout
~~~~~~~~~~~~~~~~~~~


Core Engine
^^^^^^^^^^^
.. note::
   
   #. forked from justpy

      
jpcore
""""""

utilities.py
............

.. py:function:: create_delayed_task

.. py:function:: run_task

.. py:function:: print_request

.. py:function:: find_files


jpconfig
......

All the configuration parameters
for ofjustpy. Some maybe legacy from justpy.

JpConfig
........

Loads jpconfig and justpy.env. Updates jpconfig with justpy.env values

template.py
...........

.. note::

   We are most likely not using this.
   Confirmed: not being used in justpy_app:: get_response_for_load_page

provides:

.. py:class:: PageOptions
	      
.. note::
   Most likely not in use. Check

.. py:class:: JustpyApp

   .. py:method:: route_as_text
   .. py:method:: add_jproute
   .. py:method:: mount_routes
   .. py:method:: requires
      .. note::
	 usage not clear
   .. py:method:: add_route
      .. note::
	 usage not clear
	 
   .. py:method:: response
   .. py:method:: get_page_for_func
   .. py:method:: handle_session_cookie
   .. py:method:: set_cookie
			     
		 
AppDB
.....
global datastructures to maintain bookkeeping/mapping
from pageID to webpages and their sockets

#. pageId_to_webpageInstance
#. pageId_to_websockets
#. loop
   
justpy_app.py
.............

.. py:function:: uvicorn_server_control_center

.. py:class:: JustpyAjaxEndpoint(HTTPEndpoint)

	      .. note::
		 most likely not in use

		 
justpy.py
"""""""""
.. py:function:: build_app
   .. note::
      needs a separate section of its own
	      

.. py:function:: initial_func
   .. note::
      TODO: needs to be implemented
      

.. py:function:: server_error_func
   .. note::
      TODO: needs to be implemented

.. py:function:: convert_dict_to_object
   .. note::
      TODO: remove it most likely not in use
      
.. py:function:: redirect
   .. note::
      TODO: needs to be implemented
      
.. py:function:: report_memory_usage

.. note::
   mutable_HC_TF.py
   tailwind_svelte_component_mixins.py
   HCType.py
   static_core_tracker.py
   TF_impl.py
   __init__.py
   HC_type_mixins_extn.py

   
      
ofjustpy
^^^^^^^^

__init__.py
"""""""""""


Serving a request: the pipeline/workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Uvicorn/nginx-unit opens a port for incoming connection

2. browser makes a request   

3. unit hands over the request to starlette

4. startlette invokes the JustpyApp


5. The endpoint puts together a response. This is two part:
   5a. get wp : the WebPage data structure
   5b. call get_response_for_load_page

.. code-block:: python

  def response(self, func):
       async def funcResponse(request: Request) -> Response:
       # get wp
       # self.get_response_for_load_page(request, wp)
		
   endpoint=self.response(wpfunc)
		
		
  add_route(pth, endpoint)

6. The webpage is served


Post serve: Loading a page
""""""""""""""""""""""""""
Once the page is loaded, the browser side code opens
a websocket connection

On browser
^^^^^^^^^^
.. code-block:: python
		
   var ws_url = protocol_string + document.domain;
		   if (location.port) {
			   ws_url += ':' + location.port;
		   }
		   socket = new WebSocket(ws_url);

		   

On server
^^^^^^^^^
.. code-block:: python
   @app.websocket_route("/")
   class JustpyEvents(WebSocketEndpoint):

Routes/Mounts/Reverse lookups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a Mount includes a name, then submounts should use a {prefix}:{name} style for reverse URL lookups.

.. code-block:: python

   routes = [
       Mount("/users", name="users", routes=[
	   Route("/", user, name="user_list"),
	   Route("/{username}", user, name="user_detail")
       ])
   ]


.. code-block:: python

   # We can use the following to return URLs...
   url = request.url_for("users:user_list")
   url = request.url_for("users:user_detail", username=...)

Mounted applications may include a path=... parameter

.. code-block:: python
  routes = [
    ...
    Mount("/static", app=StaticFiles(directory="static"), name="static")
]

In the above StaticFiles is a mounted app.

url_for is used as follows with path parameter:
.. code-block:: python

  request.url_for("static", path="/test_mount_url_for.py")

While request.url_for uses "x:y:z" approach for z mounted under y mounted x 

url_path_for uses something else: <-- we are ready to roll

admin_url = app.url_path_for('admin', path="/admin_home")



Working with composed components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mutable.ColorSelector
......................
- should have on_change event handler
- will hook into this event

  
Events
~~~~~~

Tests
"""""

How to invoke event_handler attached to a component

.. code-block:: python
		
   ss = wp.session_manager.stubStore
   event_data = Dict()
   event_data.page = wp
   asyncio.run(run_event_function(pspan,
				   'mouseenter',
				   event_data,`
				   stubStore=ss)


OJ Internal Mixins/Types/API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. ResponsiveStatic_SSR_WebPage : ServerSide rendering
   Created by WebPage_TF::gen_WebPage_type
   
#. ResponsiveStatic_CSR_WebPage : ClientSide rendering
   Created by WebPage_TF::gen_WebPage_type
   



WebPageMixin
""""""""""""
#. get_changed_diff_patch

WebPageType
"""""""""""
.. py:function: gen_WebPage_type

Takes a bunch of mixins and emits a WebPage type object.

Mutable Shell Mixins
.....................
- StaticCoreSharerMixin
- EventMixin
- WebPageMixin
- HCCMutable_Mixin
- StaticCoreSharerMixin  
  
StaticCoreBaseMixin  
...................
- TR.IdMixin,
- TR.TwStyMixin,
- TR.jpBaseComponentMixin,
- EventMixin,
- HCCMutableCore

  
 

HC/Div Type mixins
""""""""""""""""""
Building block mixins for HC/Div Types: Passive, Active, Mutable


StaticCore Mixin
^^^^^^^^^^^^^^^^

jpBaseComponentMixin
+++++++++++++++++++++

The `jpBaseComponentMixin` class provides attributes related to working with the JustPy-Svelte framework.

Attributes
..........
#. `show`: A Boolean attribute that controls the visibility of the component. Defaults to `True`.

#. `debug`: A Boolean attribute that enables or disables debugging for the component. Defaults to `False`.


TwStyMixin
^^^^^^^^^^
The `TwStyMixin` class defines tailwind and style attributes for HTML components.

Attributes
..........

#. `style`: A property to get and set the inline style for the HTML component.
#. `twsty_tags`: A list that stores tailwind CSS classes applied to the component.  


Methods
.......

#. `remove_twsty_tags(*args)`: Removes specified tailwind tags from the component.
#. `add_twsty_tags(*args)`: Adds tailwind tags to the component.
#. `replace_twsty_tags(*args)`: Replaces the existing tailwind tags with the ones provided in `*args`.

DOMEdgeMixin
++++++++++++
Attaches  itself to a parent component specified by 'a' kwargs


EventMixinBase
^^^^^^^^^^^^^^

Attributes
...........

- `event_modifiers`: A dictionary to store event modifiers.
- `transition`: Stores transition information for the component.
- `event_handlers`: A dictionary that associates event types with their corresponding event handling functions.
- `event_prehook`: A prehook function to be applied to all event handlers.
- `allowed_events`: A list of allowed event types.
  
Methods
.......

- `set_keyword_events(**kwargs)`: Sets event handlers based on keyword arguments.
- `on(event_type, func, *, debounce, throttle, immediate)`: Attaches an event handler to the component.
- `add_prehook(prehook_func)`: Applies a prehook function to all registered event handlers.
- `remove_event(event_type)`: Removes a specified event from the component.
- `has_event_function(event_type)`: Checks if an event handler function for a specific event type exists.
- `add_event(event_type)`: Adds an event type to the allowed events list.
- `get_event_handler(event_type)`: Retrieves the event handler function for a specific event type.
- `add_allowed_event(event_type)`: Adds an event type to the allowed events list.

EventMixin
^^^^^^^^^^

Attributes:
...........

allowed_events (list): A list of event types that can be handled by this class. These events include:
        - "click"
        - "mouseover"
        - "mouseout"
        - "mouseenter"
        - "mouseleave"
        - "input"
        - "change"
        - "after"
        - "before"
        - "keydown"
        - "keyup"
        - "keypress"
        - "focus"
        - "blur"
        - "submit"
        - "dragstart"
        - "dragover"
        - "drop"
        - "click__out"

	  
HCTextMixin
^^^^^^^^^^^
The `HCTextMixin` class provides a `text` attribute for HC (HTML Component) components such as buttons, spans, and labels.

Attributes
..........

- `text`: A property that represents the text content of the HTML component.

KeyMixin
^^^^^^^^
Attributes:
...........

key: str
    
IdMixin Class
^^^^^^^^^^^^^

The `IdMixin` class provides a mixin for handling object identifiers.

Attributes
..........
- `id`: A property that allows getting and setting the identifier for the object.
  


  

Mixins for Json
^^^^^^^^^^^^^^^
Build json mixins:

- StaticCore_JsonMixin
- JsonMixin_Base
- MutableShell_JsonMixin
- HCMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
- HCCStatic_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
- HCCMutable_JsonMixin(JsonMixin_Base)
- DivMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)

  


Mixins for Child components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. CoreChildMixin
#. HCCMixin_StaticChilds
#. HCCMixin_MutableChilds
#. HCCStaticMixin, HCCPassiveMixin, HCCActiveMixin (they are all the same)





Mixins for Server Side HTML rendering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sharer mixins
^^^^^^^^^^^^^
- HCTextSharerMixin
- TwStySharerMixin  

  
HC/Div Types (passive, active, mutable, hccmutable, hccstatic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Passive HC Type
"""""""""""""""
- StaticCore
- HCTextMixin
- KeyMixin
- PassiveJsonMixin

Active HC Type
""""""""""""""

- KeyMixin
- EventMixin
- IdMixin
- StaticCore  
- DataValidators
- http_request_callback_mixin
- HCTextMixin
- JsonMixin
  
Passive Div Type
""""""""""""""""
- StaticCore
- jsonMixinType == HCCPassiveJsonMixin
- hccMixinType == HCCPassiveMixin

Active Div Type
^^^^^^^^^^^^^^^^
- StaticCore
- jsonMixinType == HCCJsonMixin
- hccMixinType == HCCPassiveMixin
- TR.EventMixin
- KeyMixin
- TR.IdMixin
- DataValidators
- http_request_callback_mixin



Mutable HC Type
"""""""""""""""
StaticCoreMixins: TR.HCTextMixin
mutableShellMixins: TR.TwStyMixin, TR.DOMEdgeMixin, HCMutable_JsonMixin
Sharer: StaticCoreSharer_BaseMixin,
        StaticCoreSharer_IdMixin,
        StaticCoreSharer_EventMixin
	HCTextSharerMixin
	


HCCMutable
""""""""""
Core mixins:
^^^^^^^^^^^^
#. TR.jpBaseComponentMixin,
#. TR.TwStyMixin,
#. TR.PassiveKeyMixin,
#. StaticCore_JsonMixin,
#. hctag_mixin,
#. Prepare_HtmlRenderMixin
#. CoreChildMixin

Shell mixins:
^^^^^^^^^^^^^
#. HCCMixin_MutableChilds
#. RenderHTML_HCCMutableChildsMixin


HC/Div Type Factory
~~~~~~~~~~~~~~~~~~~
Type factory for active/passive/mutable, hccmutable, hccstatic types

Code Layout
^^^^^^^^^^^
In Top to bottom order:
#. SHC_types, MHC_types
#. HC_TF, Div_TF
#. mutable_Div_TF, mutable_HC_TF, SHC_types_mixin (This is essentially static_HC_TF/static_Div_TF in one)
#. TF_impl, mutable_TF_impl

#. For Passive/Active HCType generators are in `SHC_types_mixin.py`
#. Active types has keyMixin and Idmixin
#. Passive types have PassiveKeyIdMixin that yield id(self) as id and key
#. HCCMutable, HCCStatic, Mutable are generated from `mutable_Div_TF.py`

#. ofjustpy_engine/HC_type_mixins_extn.py
   Mixins for html components like Span, A, Form

#. ofjustpy_engine/tailwind_svelte_component_mixins.py
   SwitchMixin, CollapsibleMixin

#. ofjustpy_engine/mutable_HC_TF.py
   Mixins for Mutable Components
   
#. ofjustpy_engine/mutable_TF_impl.py

   Mixins for Mutable Components:
       StaticCore_JsonMixin,
       JsonMixin_Base,
       MutableShell_JsonMixin,
       HCMutable_JsonMixin,
       HCCStatic_JsonMixin,
       HCCMutable_JsonMixin,
       DivMutable_JsonMixin,
       CoreChildMixin,
       HCCMixin_MutableChilds,
       HCCMixin_StaticChilds,
       StaticCoreSharer_BaseMixin,
       StaticCoreSharer_EventMixin,
       StaticCoreSharer_ClassesMixin,
       StaticCoreSharer_IdMixin,
       StaticCoreSharer_ValueMixin,
       StaticCoreSharer_HCCStaticMixin

       
Code design/architecture   
^^^^^^^^^^^^^^^^^^^^^^^^
Every component type has a static core which is defined as
collection of mixins.

.. py:class: StaticCoreType

#. WithStub(StaticCoreType)
   Static core is wrapped in With_stub which has stub function

 All constructor args/kwargs are passed on to StaticCore.
 The is where theme sty (via stytags_getter_func) is conc with twsty_tags and
 applied to static code.

.. code-block:: python
		  
     stytags = stytags_getter_func()
     twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
     super().__init__(*args, **kwargs, twsty_tags=twsty_tags)
     
#. WithStub.stub
The stub is called by ofjustpy when rendering the components and registering them with tracker

.. py:function: def stub(self)
   
stub function invokes `gen_stub` which generates the Stub.
gen_stub is tracked by the tracker.

.. note:: TODO: needs correction
	  
.. code-block:: python
		
   @trackStub
   def gen_stub(target, **kwargs):
   
       target.request_callback(kwargs.get("session_manager"))
       return Stub(target=target, **kwargs)

#. `request_callback` is a post-processor. Is called after staticCore has been initialized for a
  request object. Used for decoding url from an endpoint. 

#. For passive/active components: mutable shell is same as static-core.
       
Mutable Div Type Factory
+++++++++++++++++++++++++

.. note:: TODO: is incomplete
HCCStatic: 
.............

is_self_mutable=True,
is_child_mutable=False

core_mixins
 - HCCMixin_StaticChilds
 - StaticCoreSharer_HCCStaticMixin
   
shell_mixins:
 - RenderHTML_HCCStaticChildsMixin

HCCMutable: 
.............

is_self_mutable=False,
is_child_mutable=True
 


Stubs and Stub generators
~~~~~~~~~~~~~~~~~~~~~~~~~
The Stub class created by the `gen_stub` func has couple of roles
depending on Stub type
- publishes key, id property from staticCore
- tells if its a static component
- has `__call__` functor interface

The __call__ functor
""""""""""""""""""""
The functions
- attaches to parent if not already attached
- register_childerns : if not already registered
- build_json if not already build

where register_childs implies calling
- c.stub() : this will call the stub_gen and produce a stub
- stub(self): this will create the component and attach to parent


.. :py:function:: __call__(self, a, attach_to_parent=True)

For static HCs
''''''''''''''
It performs
- attach_to_parent : no action
- register_childerns: no action for HCs
- build_json : already build during initialization
  
For static Divs
''''''''''''''''
- attach_to_parent : no action
- register_childerns: calls add_register_childs

    

Mutable Div
'''''''''''

This interface is invoked by Div constructor.

- for each child `c_`
   - call  c_.stub() this will call stub-gen which will register the stub with tracker
   - call c_(self) : this is calling the call interface which will create the mutable component
   - if not c_ is not static then add to spathMaphh
     
.. code-block:: python
		


#. all stubs call register_childs
#. HC Passive/active/mutable register_childs are noops
#. Div Passive/active stub
   #. register_childrens calls add_register_childs which invokes stub() for all its childs
#. Trackers store references to stubs
#. stub generators : are decorated with tracker hooks
   
+----------------+------------+--------------------+-----------------+
| CompType       | Mutability | stub_gen           | StubType        |
+================+============+====================+=================+
| HC             | Passive    | stub               | Stub_HCPassive  |
+----------------+------------+--------------------+-----------------+
| HC             | Active     | gen_Stub_HCActive  | Stub_HCActive   |
+----------------+------------+--------------------+-----------------+
| HC             | Mutable    | gen_stub_HCMutable | Stub_HCMutable  |
+----------------+------------+--------------------+-----------------+
| Div            | Passive    | stub               | Stub_DivPassive |
+----------------+------------+--------------------+-----------------+
| Div            | Active     | gen_Stub_DivActive | Stub_DivActive  |
+----------------+------------+--------------------+-----------------+
| HCCMutable Div | Passive    | stub               | Stub_HCCMutable |
+----------------+------------+--------------------+-----------------+
| mutable  Div   | Mutable    | gen_Stub_DivMutable| Stub_DivMutable |
+----------------+------------+--------------------+-----------------+
| HCCStatic Div  | Mutable    | gen_Stub_DivMutable| Stub_DivMutable |
+----------------+------------+--------------------+-----------------+
|                |            |                    |                 |
+----------------+------------+--------------------+-----------------+

The `register_childs` recursion
"""""""""""""""""""""""""""""""
.. note:: TODO: needs correction
	  
#. webpage init calls add_register_childs
   #. which calls  c.stub() (as in gen_stub) for each child c.
   #  the c.__call__ (which now has the target) calls
  its childs and the recursion continues.

gen_stub()
""""""""""
#. tracker calls gen_stub with session_manager kwargs

is_static()
"""""""""""
is_static is used in two places

1. mutable components do not register static components in their spath
2. Same thing with WebPage.
   
   
  
Design Gotcha
"""""""""""""
- For passive/active components
add_register_childs is called by stub
- For mutable components
add_register_childs is called by
init of the mutable objects
This is done because we want to create
mapping from id to the object.



HC/Div Data structures
~~~~~~~~~~~~~~~~~~~~~~
All HC/Div type use two dictionaries
- domDict
- attrs

#. domDict attributes are used to svelte rendering engine to craft a  html object
# attrs are directly passed as attrs to html object

  

Surface Level Classes and APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Webpage
"""""""

post_init:
^^^^^^^^^
This is called after the webpage object is initialized. Note that this is not
the same as page_ready which is called after the page has been rendered on the screen.

#. Webpage should behave like a proper component
   


Mutable Shell/StaticCore
~~~~~~~~~~~~~~~~~~~~~~~~

#. stubStore.target will yield the mutableShell

   
React Framework
~~~~~~~~~~~~~~~
#. appstate
#. ui_app_trmap_iter
#. action_module
#. ojr.ReactDomino

   
Definations and Vocabulary
""""""""""""""""""""""""""
appstate
^^^^^^^^
Every session has an appstate which is a dictionary of type addict_tracking_changes.
As the name suggests, it is used to keep track of state of the webapp. It has inbuilt
feature to track changes over the stored data. 
Webapp function is codified into various actions that are trigged contigent to the appstate
changes.



UI Event handling to appstate update
""""""""""""""""""""""""""""""""""""
1. Define in ui_app_trmap: a mapping from event-idpath to appstate-storepath.
   For e.g. see code below:
   
   .. code-block:: python
		   
      ui_app_trmap = [ ('/mouseenter_hcobj', '/update_sty_hcobj/selected_hcobj', None)
    ]
    
   Here, event-idpath '/mouseenter_hcobj' is mapped to '/update_sty_hcobj/selected_hcobj' appstate-storepath.
   
   An event handler is configured as follows:
   
   .. code-block:: python
		   
      @ojr.ReactDomino
      def on_click(dbref, msg, to_ms):
          # do some useful work here
	  # collect relevant ui and app values here
          reutrn '/mouseenter_hcobj', dbref

   OJ middleware will make sure that when on_click event handler is invoked, then appstate is updated.
   
2. Attach actions to appstate changes

   Actions can be hooked to appstate-storepaths. For e.g.
   .. code-block:: python

      def sample_server_side_action(appstate, arg, wp):
      """
      appctx=/update_sty_hcobj/apply_attr_value_to_utility_class
      """
		   pass
    
   Here the action `sample_server_side_action` is hooked to appstate-storepath
   `/update_sty_hcobj/apply_attr_value_to_utility_class`. Whenever the value changes
   for this appstate-storepath changes the corresponding action is triggered.
   OJ acts as clearinghouse between events and actions

Gotchas
"""""""
# In  state-changed based programming
# if an action is hooked to a access-path
# then don't change the access-path in the action


HTMLRender: From python objects to  html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We can't precompute htmlrender even for passiveDivs and PassiveHCs because
of oj.AC.A whose href is updated upon incoming request object.

.. note:: TODO: fix/correct/complete this

build_renderHTML logic
''''''''''''''''''''''
within Stub_HCPassive.__call__  -- after register_childrens build_renderHtml is called
covers calls for HCPassive, DivPassive

within Stub_HCActive.__call__  -- after register_childrens build_renderHtml is called
covers calls for DivActive




renderHtml design/arch
''''''''''''''''''''''
- staticCore has prepare_htmlRender
- is called by gen_Stub_X
- provides chunk1, chunk3

- mutableShell.to_html_iter
  uses chunk1, chunk2 etc. to piece together html


DivMutable  RenderHTML_HCCMutableChildsMixin  
DivHCCMutable RenderHTML_HCCMutableChildsMixin  
DivHCCStatic  HCCMixin_StaticChilds, RenderHTML_HCCStaticChildsMixin

.HCCPassiveMixin



Solution 1:
^^^^^^^^^^^
Let this be as it is. Wrap the get_responses_for_load_page into a
cache/opt. stuff which keeps the rendered html and reuses it for
rest of the components.

Solution 2:
^^^^^^^^^^^
Somehow fix url_path_for and use base_url. This is by far the best approach if works.


Solution 3:
^^^^^^^^^^^

Final approach:
...............
All htmlcomponents types do not precompute htmlRender.
We didn't need to write separate style of htmlRender for
each one of them.
The code would also be much simpler.


Git repo and branches
~~~~~~~~~~~~~~~~~~~~~
ofjustpy_engine/no_precompute_htmlRender : The main branch use partial precompute.
If any glitch or bug is seen, quickly move to this branch.


Building a new component
~~~~~~~~~~~~~~~~~~~~~~~~
Passive
.......


Active
.......
- Create mixin
- generate the class

.. code-block:: python
   from ofjustpy_engine.HCType import HCType
   from ofjustpy.Div_TF import gen_Div_type
   from ofjustpy import ui_styles
   from .mixins import (AccordionItemMixin)


   class ActiveComponents:
       AccordionItem = gen_Div_type(
	   HCType.active,
	   "FB_AccordionItem",
	   AccordionItemMixin,
	   stytags_getter_func=lambda m=ui_styles: m.sty.label,
       )
       pass

- assign_id       



  
Misc FAQs
~~~~~~~~~
- What happens if mutable content is placed under static
  Static components like to call 'kwargs[a].add_component'
  at initialization time which is not available.

.. note:: 

   329.     def __init__(self, *args, **kwargs):

   330.         if "a" in kwargs:

   331.             if kwargs["a"] is not None:

   332.                 kwargs["a"].add_component(self)

   333.
  
