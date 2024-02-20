Users' Manual
''''''''''''''

#. See `README#Setup <https://github.com/ofjustpy/ofjustpy?tab=readme-ov-file#setup-and-running-ofjustpy-app>`_ on setting up Ofjustpy on your local machine.
   
Webpage programming using Ofjustpy
:::::::::::::::::::::::::::::::::::

The basic paradigm for building out webpages in Ofjustpy is straighforward:

1. Describe the DOM tree using Ofjustpy constructs. This entails:
   
   a. Declaring html components along with their appearance using Tailwind utility classes.
   b. Describe the containment hierarchy and the layout associated within each containment.
      
2. For components that will respond to events on UI, describe handlers (actions) and hook them to events on of the components (see ??).
   
3. Create a function that will return a WebPage instance and declare that as endpoint for a url path (see ??).
   

If you are new to web development, then it would be helpful to go through the `Justpy docs <https://justpy.io/>`_ and its `examples <https://github.com/justpy-org/justpy/tree/master/examples>`_ on which Ofjustpy is based on. 
Also, pay careful attention to known corner cases and suggested workarounds mentioned in `Gotchas <https://ofjustpy.github.io/ofjustpy/Gotchas.html>`_  to keep Ofjutpy engine happy.


A complete demo example  illustrated in the  section below will give the
big picture overview on programming with Ofjustpy.

Programming Paradigms
~~~~~~~~~~~~~~~~~~~~~

Ofjustpy supports two programming paradigms for authoring HTML:

   1. **API-style programming:** This approach uses the Ofjustpy API to construct the DOM-tree. 
      
   2. **Within Python HTML-template style programming:** This approach combines Python code with HTML template style syntax,  resulting in more concise and readable code. See the section titled `Within Python HTML-template style programming`_ for details.


API-style programming
+++++++++++++++++++++
The example below utilizes the Ofjustpy library to create a simple webpage with dynamic components.

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
		      twsty_tags=[W/32, H/32, bg/rose/6],
		      on_click=on_btn_click
		      )
   root_box = [oj.Mutable.Container(childs = [mydeck, mybtn], classes="mx-auto")]		      
   wp_endpoint = oj.create_endpoint(key="static-components",
		    childs = root_box
			      
		    )        
   oj.add_jproute("/", wp_endpoint)
   
.. note::
   
   This example is meant to demonstrate the programmatic aspects of Ofjustpy. For building full featured
   run-of-the-mill webpages see the HyperUI library components and demos.
   
   
The provided code follows the Ofjustpy directives spelled out earlier. Let's break down the code based on the given directives:

*Define the DOM Tree using Ofjustpy Constructs*:
        HTML components, specifically labels, are declared using Ofjustpy's `Mutable.Label` class. Each label has a specified text and key.
        The labels are then organized within a `Mutable.StackD` component named mydeck. The mybtn button is created using `AC.Button`. The DOM-tree is defined by single containment: a root box component  contains the `mydeck` and `mybtn` component. 

*Specify Handlers for Components*:
        The `on_btn_click` function defines a click event handler for `mybtn`. It brings the next label to the front within the mydeck stack, creating a dynamic effect.

*Create a Function Returning a WebPage Instance*:
        Using `create_endpoit` helper function, the `wp_endpoint` created. It is a function that returns a `WebPage` instance. The previously constructed DOM-tree defines the content and look of the page.

*Declare as Endpoint for a URL Path*:
        Finally, the endpoint is added to the root route ("/") using `oj.add_jproute`.


The above example was based on Ofjustpy API calls. In this style, the DOM-tree is constructed
as series of API calls for component creation.

A few more example expressions  using the API-style programming:

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
Ofjustpy also supports an alternative HTML-template style programming. It leverages the Python `with` context to express the DOM-tree. 
The following code example showcases the "Within Python HTML-template style programming" paradigm of Ofustpy.

.. code-block:: python

           with writer_ctx:
            with HCCMutable_Div(classes="relative") as comp_box:
                with HCCMutable_Div(classes="inline-flex items-center overflow-hidden rounded-md border bg-white"):
                    with A(href=href, classes="border-e px-4 py-2 text-sm/none text-gray-600 hover:bg-gray-50 hover:text-gray-700", text=title):
                        pass
                    with Button(key=key, classes="h-full p-2 text-gray-600 hover:bg-gray-50 hover:text-gray-700", on_click=lambda *args, ctx=tlctx:on_menudown_click(*args, ctx=tlctx)):
                        with Icon_Chevrondown():
                            pass
                with HCCMutable_Div(classes="absolute end-0 z-10 mt-2 w-56 rounded-md border border-gray-100 bg-white shadow-lg", role="menu"):
                    with HCCMutable_Div(key="items_box", classes="p-2") as items_box:
                        pass
                    pass

This approach offers several advantages compared to API-based programming:

#. **Explicit Hierarchy/Component Nesting**: HTML structure is naturally reflected in the code, making component relationships self-evident and easy to follow.
#. **Minimal Boilerplate**: Compared to API-based methods, this approach requires significantly less repetitive keywords and syntax, streamlining development.
#. **Unified Solution**: It eliminates the need for separate templating systems and data transfer between languages, simplifying the overall process.

One drawback of this in-Python template system its does allows only limited set of Python expressions.

.. 
  .. note::

     See event_handling and mutable_component section
     for performing server side and browser side UI manipulations
     in response to events on the browser.

..
  .. include:: event_handling.rst


HTML Components in Ofjustpy
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. TODO: style manipuation (just the static kinds, and base styles)

Ofjustpy has support for all the usual basic html components (Div, Button, Span, Label, etc.). Their styling is customized using Tailwind constructs. Refer to `Reference`  section for
list of all the components, their arguments and usage.


Pre-styled vs. customizable components
++++++++++++++++++++++++++++++++++++++
Although, Ofjustpy provides tools to work with tailwind utility classes,
components in Ofjustpy, by default, are un-styled, i.e,  there is no
tailwind styling hard-wired to them. 

Falling short of providing full-fledge pre-styled component library, Ofjustpy
provides several assets and utilities to help with layout and styling of components
and webpages.

.. important::
   
   As mentioned before, Ofjustpy provides customizable elementry and composite components. If you would like more off-the-shelf pre-fabricated and opinionated components consider `Justpy (with Quasar components) <https://justpy.io/quasar_tutorial/introduction/>`_ or `NiceGUI  <https://nicegui.io/>`_
   
Component Types
+++++++++++++++
Ofjustpy, boradly, defines 2 kinds of components: static vs mutable. Static components are further classified into Passive and Active, while mutable components come in three variety: HCCMutable, HCCStatic, Mutable.

Passive Components
++++++++++++++++++
As name suggests, these do not respond to UI events and also do not undergo any changes. Ofjustpy maintains only a single copy of such components (see `examples/static_webpages <https://github.com/ofjustpy/ofjustpy/tree/main/examples/static_webpages>`_ for usage).

Examples of passive components:

#. oj.PD.Label
#. oj.PD.P
#. oj.PD.Img
   
etc.

Active Components
+++++++++++++++++
Active components in OfjustPy allow you to create elements that trigger actions when users interact with them. These components have three key characteristics:

#. **Identifiers**: Each active component has a unique identifier associated with it, usually defined using the key keyword argument. 
   
#. **Event handlers**: You can attach event handlers to active components to respond to user interactions. These handlers are functions that execute code when specific events occur, such as clicking a button or changing text input.
   
See `examples/input_components <https://github.com/ofjustpy/ofjustpy/tree/main/examples/input_webpages>`_)  for usage.

List of active components:

#. oj.AC.Button
#. oj.AC.TextInput
#. oj.AC.CheckboxInput
#. oj.AC.Select
#. oj.AC.A    

and so on.

See `SHC_types.py <https://github.com/ofjustpy/ofjustpy/blob/main/src/ofjustpy/SHC_types.py>`_ for Passive/Active Divs

   
Mutable Components
++++++++++++++++++
Mutable components can handle events and also mutate, i.e., change appearances.

.. important::

   Mutable components within the `oj.Mutable` namespace can only mutate the `classes` attribute via `twsty_tags`. If you want to create HTMLComponent types that can mutate other attributes, see the example usage in `this GitHub repository <https://github.com/ofjustpy/ofjustpy-components/blob/main/src/ofjustpy_components/hierarchy_navigator.py#L17>`_.

Below is an example usage for the `oj.Mutable.Button` mutable component

.. code:: python

  mybtn = oj.Mutable.Button(key="mubtn", text="", value="", twsty_tags=[bg/green/1, ...])

Let's say we want to modify the background based on some event. In the
corresponding event handler:

.. code:: python

   def on_click_handler(dbref, msg, to_mutableShell):
   """
   to_mutableShell: a function that returns the mutableShell of the static component
   """
   
   mybtn_ms = to_mutableShell(mybtn)
   mybtn_ms.add_twsty_tags(bg/green/5)

Once the above handler is invoked, the button background color will change to darker color
of green.

Examples of mutable components include:

#. oj.Mutable.Button
#. oj.Mutable.Label
#. oj.Mutable.Container and so on.

#. Checkout the example code snippets in `the OfJustPy mutable examples repository <https://github.com/ofjustpy/ofjustpy/tree/main/examples/mutable_webpages>`_.

#. See `README <https://github.com/ofjustpy/ofjustpy?tab=readme-ov-file#hccmutable-components>`_ for
details on HCCMutable and HCCStatic components. 

#. See `MHC_types.py <https://github.com/ofjustpy/ofjustpy/blob/main/src/ofjustpy/MHC_types.py>`_ for list of all Mutable, HCCMutable, and HCCStatic components.

In addition to these, Ofjustpy also implements the `HyperUI <https://www.hyperui.dev/>`_ ui library kit. 
HyperUI is a clean, fast, asthetically pleasing  UI component library written with tailwind utility classes. Ofjustpy provides HyperUI components as first class components that can be incorporated with other components and manipulated as native.

Event Handling
~~~~~~~~~~~~~~

Ofjustpy simplifies web development by handling browser events directly within Python, eliminating the need for JavaScript manipulation. Because events are handled on the server, server side manipulations are straighforward obvious. Because client side UI's can also be controled from the same event handler (see following section), Ofjustpy event handling has other advantages:

#. **Unified Event Handling**:

#. **Clean Code**:You define event handlers as Python functions, making your code more readable and maintainable.
      
#. **Reduced Complexity**: Ofjustpy eliminates the need for separate JavaScript code for server-side interactions, offering a simpler and less error-prone development experience.
    

Both active and mutable components can have events attached to them. Event handlers receive two arguments:

#. dbref: A reference to the HTML component that triggered the event.
#. msg: A dictionary containing information like the event type, component value, and page instance.

An example of an event handler function signature:

.. code-block:: python
		
   async def on_button_click(dbref, msg, to_mutable_shell=None):
       # perform server side and client side manipulation

       pass

You can attach event handlers in two ways:

#. During Component Instantiation: Pass the function as an argument:
   
   .. code-block:: python

      oj.AC.Button(text="ABC", \.\.\., on_click=on_button_click)

#. Using the on Method: Attach after creating the component:

   .. code-block:: python

      button = oj.AC.Button(text="Click Me")
      button.on("click", on_button_click)
   
Here are some commonly used events:

    #. click: Occurs when a user clicks on an element.
    #. mouseenter: Occurs when the mouse enters an element.
    #. mouseout: Occurs when the mouse leaves an element.
    #. mouseleave: Similar to mouseout, but fires only when the mouse leaves the entire element area.
    #. input: Occurs when the value of an input element changes (e.g., typing in a text box).
    #. change: Occurs when the value of an element is committed (e.g., selecting an option from a dropdown).
    #. submit: Occurs when a form is submitted.

    
Making Responsive UI
++++++++++++++++++++

Making responsive UI entails manipulating the DOM structure of the webpage in the browser.
Ofjustpy makes this uncomplicated as well.
Programmers are relieved from the manual burden of meticulous state management, dealing with Python runtime and browser runtime communications, and performing JavaScript manipulations to alter the UI state.


Ofjustpy provides  the ability to modify attributes of HTML components that is reflected transparently on the browser, eliminating the need for additional code to execute client-side logic. This approach contrasts with other frameworks such as Django, which rely on templates, or browser-side frameworks that require additional code to execute server-side logic.


For a component to change its UI-state, it needs to be registered as a mutable component.
Following that a event handler can modify the component as long as it has access to the component.
The example below shows a component 

.. code:: python

	  
   mutable_comp = oj.Mutable.Span(key="mspan", text="hello", twsty_tags=[bg/green/1])
   
   def on_click_handler(dbref, msg, to_mutableShell):
   """
   to_mutableShell: a function that returns the mutableShell of the static component
   """
   
   mutable_comp_shell = to_mutableShell(mutable_comp)
   mutable_comp_shell.add_twsty_tags(bg/green/5)

Thats it. Ofjustpy will make sure that on the browser side the component corresponding to
`mutable_comp` has the new background color.


.. note:: 

   See section `mutable components`_ for more details on space efficient implementation
   of mutable shell.
   
   
   
   
To recap:
#. We did not had to manually compute the state diff of UI
#. Collect all the UI changes and serialize them
#. Ship them to frontend
#. Unserialize and gather the UI for the components
#. Apply the changes.

Ofjustpy handles all the sundry heavylifting without the need for  additional directives.



Creating webpage endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~
Once all the components are declared and DOM-tree specified, we can proceed to create a endpoint.

.. note::
   
   An endpoint is a function that takes a `Starlette request <https://www.starlette.io/requests/>`_ object as
   input and returns a `Response <https://www.starlette.io/responses/>`_ like object. Endpoints are tied to a path.
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

The name keyword argument is used to get the url associated with the endpoint.
For example:

.. code-block:: python

   url = app.url_path_for("my-first-webpage")

will return the relative path attached to the endpoint with name "my-first-webpage".
See section `Reverse URL lookups <https://www.starlette.io/routing/>`_ for details
on reverse lookup on paths with arguments.

.. note::
   
   We will revisit url lookup later when address mount points.
   

.. TODO    clarify the methods and name argument to Route construct.
   
   
App programming in Ofjustpy
:::::::::::::::::::::::::::
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

    
.. 
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

