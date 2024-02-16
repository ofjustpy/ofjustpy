Users' Manual
''''''''''''''

#. See `README#Setup <https://github.com/ofjustpy/ofjustpy?tab=readme-ov-file#setup-and-running-ofjustpy-app>`_ on setting up Ofjustpy on your local machine.
   
Webpage programming using Ofjustpy
:::::::::::::::::::::::::::::::::::

The basic paradigm for building out webpages in Ofjustpy is straighforward:

1. Describe the DOM tree using Ofjustpy construct. This entails:
   
   a. Declaring html components along with their appearance using tailwind utility classes
   b. Describe layout and containment hierarchy of the components
   c. The root component of this hierachy is instance of WebPage like class
2. For components that will respond to events on UI, describe handlers (actions) and hook them to events on the components (see ??).
3. Create a function that will return a WebPage instance and declare that as endpoint for a url path (see ??).
   

If you are new to web development, then it would be helpful to go through the `justpy docs <https://justpy.io/>`_ and its `examples <https://github.com/justpy-org/justpy/tree/master/examples>`_ on which Ofjustpy is based on. 
Also, pay careful attention to known corner cases and suggested workarounds mentioned in `Gotchas <https://ofjustpy.github.io/ofjustpy/Gotchas.html>`_  to keep Ofjutpy engine happy.


A complete demo example  illustrated next will give the big picture overview on programming
with Ofjustpy:

.. code-block:: python
		
   import ofjustpy as oj
   from py_tailwind_utils import *


   labels = [oj.Mutable.Label(text="mytext1", key="mylabel1"),
	     oj.Mutable.Label(text="mytext2", key="mylabel2"),
	     oj.Mutable.Label(text="mytext3", key="mylabel3"),
	     oj.Mutable.Label(text="mytext4", key="mylabel4"),
	     ]

   mydeck = oj.Mutable.StackD(key="mydeck",
			      childs=labels,
			      height_anchor_key="mylabel1",

			      twsty_tags=[W/"1/2"])

   idx = 1
   def on_btn_click(dbref, msg, target_of):
       global idx
       mydeck_shell = target_of(mydeck)
       mydeck_shell.bring_to_front(labels[idx].id)
       idx = (idx + 1)%4
       pass


   mybtn = oj.AC.Button(key="mybtn",
		      text="abtn",
		      pcp=[W/32, H/32, bg/rose/6],
		      on_click=on_btn_click
		      )
   wp_endpoint = oj.create_endpoint(key="static-components",
		    childs = [mydeck,
			      mybtn
			      ]
		    )        
   oj.add_jproute("/", wp_endpoint)

HTML Components in Ofjustpy: Creating, Styling and Layout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: style manipuation (just the static kinds, and base styles)

Ofjustpy has support for all the usual basic html components (Div, Button, Span, Label, etc.).
Additionally, Ofjustpy provides several type variations over these component types, namely:

#. PassiveComponents
#. ActiveComponents
#. PassiveDivs
#. ActiveDivs
#. Mutable
#. HCCMutable
#. HCCStatic
   
These types provide additional hints to the framework that allow it optimize the runtime
and efficiently serve webpages. See

#. `SHC_types.py <https://github.com/ofjustpy/ofjustpy/blob/main/src/ofjustpy/SHC_types.py>`_ for Passive/Active components/divs
#. `MHC_types.py <https://github.com/ofjustpy/ofjustpy/blob/main/src/ofjustpy/MHC_types.py>`_ for Mutable, HCCMutable, and HCCStatic components.

   
For a detailed discussion on these component types see `README <https://github.com/ofjustpy/ofjustpy?tab=readme-ov-file#components-and-their-types-in-ofjustpy>`_.

.. TODO: point to hyperui components
   
All styling in Ofjustpy is done either through tailwind utility classes or through style attribute.

.. note::

   Discussion on styling using CSS or tailwind is outside the scope of our work.
   See `using tailwind in ofjustpy <https://github.com/ofjustpy/py-tailwind-utils>`_ for more details.

.. TODO: point to proper tailwind resources
  
.. important::
   
   Ofjustpy support two different programming styles to describe the webpage components and layout structure:
   
   1. API-style usage as collection of interconnected functions
   2. Alternatively, you can describe the html in more natural html-like syntax but within Python. This style is more succient and readable but less powerful then API-style.

API-style programming
+++++++++++++++++++++

The code snippets belows illustrates declaration, styling and containment usage of componens.

.. code-block:: python
		
   # create a passive span component with text hello. Tailwind style is "bg-green-100 text-xl"
   hello_comp = oj.PC.Span(text="hello", classes = "bg-green-100 text-xl")

   # create a active button component 
   submit_btn = oj.AC.Button(key="abtn", text="Submit", classes="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded")

   # create a div box which vertically stacks hello_comp and submit_btn
   box = oj.PC.StackV(childs = [hello_comp, submit_btn], classes="p-4 m-4 space-y-4")

.. TODO: give link for detailed list of all components
   

Within Python HTML-template style programming
+++++++++++++++++++++++++++++++++++++++++++++

TODO

Creating webpage endpointk
~~~~~~~~~~~~~~~~~~~~~~~~~~
Once all the components are declared, we can proceed to create a endpoint.
.. note::
   
   An endpoint is a function that takes a `Starlette request <>`_ object as
   input and returns a `Response <>`_ like object. Endpoints are tied to a path.
   When on browser, this path is entered, the Starlette invokes the endpoint to gets
   the response and ships it to the frontend.

In Ofjustpy, endpoint is created via helper function `oj.create_endpoint`.    
.. code-block:: python

   wp_endpoint = oj.create_endpoint(key="my-first-webpage",
		    childs = [mydeck,
			      mybtn
			      ],
			      title="The webpage title",
			      classes="bg-green-100"
			      )

Next, attach the endpoint to relative path as follows:

.. code-block:: python

   oj.add_jproute("/x/y/z", wp_endpoint, name="my-first-webpage")

The name keyword arg is used to get the url associated with the endpoint.
For example:
.. code-block:: python

   url = app.url_path_for("my-first-webpage")

will return the relative path attached to the endpoint with name "my-first-webpage".
See section `Reverse URL lookups <https://www.starlette.io/routing/>`_ for details
on reverse lookup on paths with arguments.

.. note::
   
   We will revisit url lookup later when address mount points.
   

.. TODO    clarify the methods and name argument to Route construct.
   
   
App programming using Ofjustpy
::::::::::::::::::::::::::::::
An app for our current purpose is a collection of endpoints and their associated routes.
We will outline a few quality-of-life enhancements we have made in Ofjustpy over Starlette.


Page Builder
~~~~~~~~~~~~
Page builder is a utility-mechanism of Ofjustpy, to non-intrusively, manipulate page content
by hooking into `create_endpoint` function. In terms of functionality this is
similar to what offered in Django or other templating based framework. In other framework,
a system of template inheritance is used where one can extend from base template
and override some of the blocks.

Here we use python function wrappers to achieve customization to set of webpages.
The Ofjustpy approach is less intrusive. 



For example, lets say we want to add "nav" button to all the webpages being created
in the file `admin_endpoints.py`.


.. code-block:: python

   def nav_page_builder(key, childs, **kwargs):
    nav_buttons = oj.PC.Div(childs = []) #define a list of navigation buttons
    childs_with_nav = oj.HCCMutable.Div(childs = [ oj.HCCMutable.Div(childs=childs),
                                          oj.PC.Hr(twsty_tags=[bg/green/1]),
                                          nav_buttons

                                         ]
                               )
       
       return oj.default_page_builder(key, childs_with_nav, **kwargs)
       

   with oj.PageBuilderCtx(page_builder):
    admin_endpoints_module = importlib.import_module("admin_endpoints"
                                                     )

						    
   
Routes and Mounts
~~~~~~~~~~~~~~~~~

An endpoint can be attached to  relative path as follows:

.. code-block:: python

   oj.add_jproute("/x/y/z", wp_endpoint, name="my-first-webpage")

Ofjustpy also provides helper expressions to make is easier to mount an sub-app (i.e.,
a collection of endpoints) on to route prefix

.. code-block:: python
		
   with oj.MountCtx("examples"):
       oj.add_jproute(examples_index_endpoint, "/")
       with oj.MountCtx("static_webpages"):    
	   static_webpage_module = importlib.import_module("examples.static_webpages",
                                                                )


In the above example, all the routes defined within the examples.static_webpages will be mounted under `examples/static_webpages` path. The `examples_index_endpoint` will be attached
to `/examples/` relative url path. 
MountCtx enable a plug-and-play approach for adding modules and defining routes. This means you can import the module into multiple web app codes without needing to modify the module code for each app. This flexibility simplifies the process of extending and reusing modules across different applications.								

TBD:
::::

#. Mutable Components
#. Tailwind style manipulation at runtime
#. Default styling by component types and overriding
#. Keyword argument `extra_classes` for non tailwind styles
#. Middlewares
#. HyperUI components and derived components
#. Forms and data-validators
#. Event handling and making webpage responsive
#. exception_handlers
#. on_startup/on_shutdown or lifespan
#. session manager/appstate to store runtime data 
#. uictx
#. uvicorn or nginx-unit
#. Testing
   
   #. Isolated webpage testing -- Simpler invoke webpage instance and event-handlers using mock data
      
   #. Request/response testing using TestClient
      
#. Query Parameters

#. File upload/download

#. Cookies

#. Svelte Safelist
   
