#. Mutable Shell/StaticCore: stubStore.target will yield the mutableShell


#. A dummy webpage-- for stub.__call__
  
  .. code-block:: python
		  
      class WP:
        def add_component(self, x):
            pass
        pass
    wp = WP()
    
    undock_btn_panel.stub()(wp)

    
#. The  route `/static`  corresponds to the root directory from where the webserver (uvicorn)j is launched.

Perform event invoke test (without selenium)
++++++++++++++++++++++++++++++++++++++++++++

How to invoke event_handler attached to a component

.. code-block::
		
   ss = wp.session_manager.stubStore
   event_data = Dict()
   event_data.page = wp
   asyncio.run(run_event_function(pspan,
				   'mouseenter',
				   event_data,`
				   stubStore=ss)

Routes and Mounts
+++++++++++++++++

#. If a Mount includes a name, then submounts should use a {prefix}:{name} style for reverse URL lookups.

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

   

#. Mounted applications may include a path=... parameter

.. code-block:: python
		
  routes = [
    ...
    Mount("/static", app=StaticFiles(directory="static"), name="static")
    ]

#. In the above StaticFiles is a mounted app.

url_for is used as follows with path parameter:
.. code-block:: python
		
   request.url_for("static", path="/test_mount_url_for.py")
   
#. While request.url_for uses "x:y:z" approach for y mounted x under z
   url_path_for uses something else: 
   admin_url = app.url_path_for('admin', path="/admin_home")

A element href updater
++++++++++++++++++++++

- when a stub is generated, a callback is issued
  .. code-block:: python
		  
     target.request_callback(kwargs.get("session_manager"))

- For A element, a mixin is created with request_callback which has href_builder which update the href The updater can be obtained from `oj.href_builder_factory("/hello")`,
  
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



FAQs
++++

#. HCCMutable classes don't have assign_id

  Because the container itself is not mutable.

- What happens if mutable content is placed under static?
  
  Static components like to call 'kwargs[a].add_component'
  at initialization time which is not available.

..
  329.     def __init__(self, *args, **kwargs):

  330.         if "a" in kwargs:

  331.             if kwargs["a"] is not None:

  332.                 kwargs["a"].add_component(self)

  333.

  334.
  
- Margins and spacing
  good to make rule of thumbs: mr/y/2 for within div,
  mr/y/4 for across div within section
  mr/y/8 for across div across sections







   
