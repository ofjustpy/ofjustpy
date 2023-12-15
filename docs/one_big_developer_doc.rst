Notes
^^^^^^
- To get event handler of a component
  
  .. code-block:: python
     
     event_function = dbref.get_event_handler("on_" + event_type)
  
  
- A dummy webpage-- for stub.__call__
  
  .. code-block:: python
		  
      class WP:
        def add_component(self, x):
            pass
        pass
    wp = WP()
    
    undock_btn_panel.stub()(wp)

- The route /static corresponds to the root directory from where
  the server is launched.
  
The Vocabulary
^^^^^^^^^^^^^^
- Sharer
- Mixins

  
It all starts with building block mixins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

StaticCore
++++++++++



jpBaseComponentMixin
+++++++++++++++++++++

The `jpBaseComponentMixin` class provides attributes related to working with the JustPy-Svelte framework.

Attributes
..........

- `show`: A Boolean attribute that controls the visibility of the component. Defaults to `True`.

- `debug`: A Boolean attribute that enables or disables debugging for the component. Defaults to `False`.


TwStyMixin
++++++++++
The `TwStyMixin` class defines tailwind and style attributes for HTML components.

Attributes
..........

- `style`: A property to get and set the inline style for the HTML component.
- `twsty_tags`: A list that stores tailwind CSS classes applied to the component.  


Methods
.......
- `remove_twsty_tags(*args)`: Removes specified tailwind tags from the component.
- `add_twsty_tags(*args)`: Adds tailwind tags to the component.
- `replace_twsty_tags(*args)`: Replaces the existing tailwind tags with the ones provided in `*args`.


DOMEdgeMixin
++++++++++++
Attaches  itself to a parent component specified by 'a' kwargs


EventMixinBase
++++++++++++++

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
++++++++++

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
++++++++++++
The `HCTextMixin` class provides a `text` attribute for HC (HTML Component) components such as buttons, spans, and labels.

Attributes
..........

- `text`: A property that represents the text content of the HTML component.


Mutable Mixins
++++++++++++++

Build json mixins:

- StaticCore_JsonMixin
- JsonMixin_Base
- MutableShell_JsonMixin
- HCMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
- HCCStatic_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
- HCCMutable_JsonMixin(JsonMixin_Base)
- DivMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)


Serving a request: the pipeline/workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Uvicorn/nginx opens a port for incoming connection

- browser makes a request

- unit hands over the request to starlette

- startlette invokes the JustpyApp
  - A route is attached to an endpoint
    
.. code-block:: python

  def response(self, func):
       async def funcResponse(request: Request) -> Response:
       # get wp
       # self.get_response_for_load_page(request, wp)
		
   endpoint=self.response(wpfunc)
		
		
   add_route(pth, endpoint)


- The endpoint puts together a response. This is two part:
  1. get wp : the WebPage data structure
  2. call get_response_for_load_page   


- get_response_for_load_page
  puts together all the components into html response

.. code-block:: python

   page_options = {
            "reload_interval": load_page.reload_interval,
            "body_style": load_page.body_style,
            "body_classes": load_page.body_classes,
            "css": load_page.css,
            "head_html": load_page.head_html,
            "body_html": load_page.body_html,
            "display_url": load_page.display_url,
            "dark": load_page.dark,
            "title": load_page.title,
            "redirect": load_page.redirect,
            "highcharts_theme": load_page.highcharts_theme,
            "debug": load_page.debug,
            "events": load_page.events,
            "favicon": load_page.favicon if load_page.favicon else jpconfig.FAVICON,
        }
        if load_page.use_cache:
            page_dict = load_page.cache
        else:
            page_dict = load_page.build_list()
        template_options["tailwind"] = load_page.tailwind
        context = {
            "request": request,
            "page_id": load_page.page_id,
            "justpy_dict": json.dumps(page_dict, default=str),
            "use_websockets": json.dumps(WebPage.use_websockets),
            "options": template_options,
            "page_options": page_options,
            "html": load_page.html,
            "frontend_engine_type": jpconfig.FRONTEND_ENGINE_TYPE,
            "frontend_engine_libs": jpconfig.FRONTEND_ENGINE_LIBS
        }
        # wrap the context in a context object to make it available
        context_obj = Context(context)
        context["context_obj"] = context_obj
        response = templates.TemplateResponse(load_page.template_file, context)

	
- The webpage is served


Post serve: Loading a page
++++++++++++++++++++++++++
Once the page is loaded it opens
a websocket connection
- On browser
  
.. code-block:: python
		
   var ws_url = protocol_string + document.domain;
		   if (location.port) {
			   ws_url += ':' + location.port;
		   }
		   socket = new WebSocket(ws_url);

- on server
  
.. code-block:: python
   @app.websocket_route("/")
   class JustpyEvents(WebSocketEndpoint):
		


   
Working with composed components
+++++++++++++++++++++++++++++++++

Mutable.ColorSelector
......................
- should have on_change event handler
- will hook into this event



Route and Mounts
+++++++++++++++++
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

While request.url_for uses "x:y:z" approach for y mounted x under z
url_path_for uses something else: <-- we are ready to roll
admin_url = app.url_path_for('admin', path="/admin_home")
A element href updater
++++++++++++++++++++++
- when a stub is generated, a callback is issued
  .. code-block:: python  
		  target.request_callback(kwargs.get("session_manager"))

- For A element, a mixin is created with request_callback
  which has href_builder
  which update the href
The updater can be obtained from
oj.href_builder_factory("/hello"),
  
- the endpoint key is used as the name label for the route   


Optimization on hosted applications
++++++++++++++++++++++++++++++++++++

instead of url_for; use URL scheme
at startup_event

.. code-block:: python
		

		from starlette.applications import Starlette
		from starlette.responses import JSONResponse
		from starlette.routing import Route
		from starlette.datastructures import URL

		async def startup_event():
		# Configuration tasks go here
		print("Configuring parameters after the domain is fixed")

		# Example: Build a URL manually
		base_url = URL(scheme="http", host="example.com", port=8000)
		api_url = base_url.replace(path="/api")
		print(f"API URL: {api_url}")

		async def homepage(request):
		return JSONResponse({'message': 'Hello, Starlette!'})

		app = Starlette(routes=[Route('/', homepage)])

		# Register the startup event
		app.add_event_handler('startup', startup_event)

		if __name__ == "__main__":
		import uvicorn

		uvicorn.run(app, host="127.0.0.1", port=8000)

		
		
On to_html, prepare_htmlRender: Early optimization is source of all  evil
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
We can't precompute htmlrender even for passiveDivs and PassiveHCs because
of oj.AC.A whose href is updated upon incoming request object.

Solution 1:
.........
Let this be as it is. Wrap the get_responses_for_load_page into a
cache/opt. stuff which keeps the rendered html and reuses it for
rest of the components.

Solution 2:
............
Somehow fix url_path_for and use base_url. This is by far the best approach if works.


Solution 3:
...........

Final approach:
...............
All htmlcomponents types do not precompute htmlRender.
We didn't need to write separate style of htmlRender for
each one of them.
The code would also would have been much simpler.


Git repo and branches
++++++++++++++++++++++
ofjustpy_engine/no_precompute_htmlRender : The main branch use partial precompute.
If any glitch or bug is seen, quickly more to this branch.


Building a new component
^^^^^^^^^^^^^^^^^^^^^^^^^
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


