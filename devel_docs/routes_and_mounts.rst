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
   url_path_for uses something else: <-- we are ready to roll
   admin_url = app.url_path_for('admin', path="/admin_home")

A element href updater
++++++++++++++++++++++

- when a stub is generated, a callback is issued
  .. code-block:: python
		  
     target.request_callback(kwargs.get("session_manager"))

- For A element, a mixin is created with request_callback which has href_builder which update the href The updater can be obtained from `oj.href_builder_factory("/hello")`,
  
- the endpoint key is used as the name label for the route   
