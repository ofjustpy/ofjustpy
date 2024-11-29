.. Kavya documentation master file, created by
   sphinx-quickstart on Wed Nov 13 08:59:22 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Kavya documentation
===================

Kavya is a Python-based full-stack web development framework designed to simplify the creation of complex, responsive, and visually appealing websites. It enables developers to build well-structured web pages using purely Python APIs and constructs, without requiring advanced development skills.

Framework Features
------------------

#. **Full-stack in Python**: With Kavya, developers write all code—including frontend user interfaces and backend logic—using Python. This is particularly appealing to developers who are already familiar with Python.
   
   -  Additionally, one doesn't need to learn and manage multiple languages like Jinja2 templating, JavaScript, HTML, and CSS. The entire functionality of a webpage/website can be expressed using pure Python.
     
#. **Ease of Use**: The primary design goal of Kavya is to make web development easier without sacrificing functionality. The framework emphasizes developer productivity by minimizing boilerplate code, providing intuitive APIs, and offering a consistent development experience that scales well with project complexity.
   
#. **Server-driven Architecture**: Kavya employs a server-driven architecture, meaning all client-side events (such as button clicks, form submissions, etc.) are sent to the server for processing. 

   - *Client UI Manipulation from server-side Python*: The server side event handlers, in Kavya, are pure Python functions. All UI manipulations are done within server side Python runtime . Example below illustrates this.

     .. code-block::

	def on_btn_click_event_handler(...):
           ...
	   mutable_abtn.add_twsty_tags(bg/green/100)
	   ...

     When event is triggered on the browser, Kavya invokes the corresponding event handler on server which manipulates the UI objects. 
     
   - *Programmatic Ergonomics (UI update)*: In the above example, the one line of code shown is  all the code required to change the background color of the button on the browser. Kavya handles all the necessary calculations (to compute the new UI), communication (sending new UI data to browser) and execution (updating the UI on the browser). 

   - *Integrated webapp state management*: One advantage of this server side event handling approach is that it provides an integrated development enviornment where backend logic and UI processing is done is one location. In Kavya, a typical work template  for event handlers in Python looks as follows:
     
     .. code-block::
	
	def on_btn_click_event_handler(dbref, msg, to_ms):
	   # do server side processing
	   # call methods to manipulate UIs
	   ...
	   ...

     This approach significantly simplifies the process of tracking and reasoning about the overall state of the web application.


   - *Efficient Responsive UI*:  The UI updates from server to the browser is lean and efficient. Instead of
     sending the entire updated DOM-tree, in Kavya, only the changes (or diffs) are send to the client. The browser runtime updates the UI based on the diff. This diff-based approach makes enables building  webpage responsive.
          
   

#. **UI style manipulation and themes**: In Kavya, all styling is done using Tailwind classes. Kavya offers advanced support for Tailwind CSS by providing a built-in mini data model that allows Tailwind directives to be written as native Python expressions. Example below illustrates tailwind directive `bg-green-100 text-blue-100 flex-row`  written as Python expression:
   
   .. code-block:: javascript

      mytags = [bg/green/100, fc/blue/100, flx.row]
      

   Kavya provides powerful utilities for manipulating Tailwind classes—adding, removing, or merging them seamlessly. For instance, if you want to overwrite the background color in the above example from green to blue, you can use the `conc_twtags` function to merge directives while overriding the existing background color:  

   .. code-block::
      
      classes = tstr(conc_twtags(*mytags, bg/blue/100))
   
  
   This smart merging of Tailwind styles makes it especially useful for theme customization, as you can easily modify or update styles without resorting to low-level string manipulation. Kavya builds upon this capability to provide the functionality of cascading themes. You could have a *page wide theme*, which can be overwritten by a *theme for part of the page*, which can be overwritten by *utility definition for individual elements*.
   
   
#. **Ease of Development, Code Modularity and Maintainence**: In web development, there is an inherent conflict between code organization, modularity, and ease of use. This arises because an event handler may need to refer to any component on the webpage. The straightforward way to achieve this is to have all components of the webpage exposed in the same scope as the event handler—an approach that severaly compromises code modularity.

   In Kavya, we have introduced constructs called `uictx` to address this issue. With `uictx`, you can organize components into a hierarchy independent of the DOM-tree hierarchy. This hierarchy is made available to all event handlers, enabling components to be accessed through traversals within the hierarchy. In this way, both code modularity and ease of development are preserved.

   - Another important benefit of using `uictx` is that components can be organized based on the application's logical structure rather than being constrained by the DOM-tree. This allows developers to create a structure that better aligns with the application's state and behavior, making the code more maintainable and intuitive.
     
   
#. **In-Python HTML authoring**: Instead of using an external template-based html rendering system, in Kavya HTML authoring of the webpage is done entirely with Python. Kavya offers two approaches to HTML authoring. 
   
   - Botton-up API-based HTML construction: This approach uses the Kavya API to construct the DOM-tree in bottom up fashion. You begin by creating individual components using the Kavya API, then progressively nest these elements within container components to form the desired hierarchical structure of the DOM tree. Typical pattern for bottom up programming looks as follows:
     
     .. code-block::

      e1 = vy.PC.Span()
      e2 = vy.PC.Button()
      ...
      ...
      c1 = vy.PC.StackH(childs = [e1, e2, ...])

      # define more components and containers

      e1 = ...
      e2 = ...
      ...
      c2 = vy.PC.StackG(childs = [e1, e2, ...])

      ...
      ...

      tlc = vy.PC.Container(childs = [c1, c2, ..])

      
   - Top-down In-Python template-like html construction: This approach combines Python code with HTML template style syntax, i.e., we   program from the top-level root component and then progressively declare its children and their subsequent childrens.  This style results in a more concise and readable codebase.  A typical template for top down style will look as follows:

     .. code-block::
      
      with writer_ctx:
       with Container(...):
	   with StackH(...):
	       with Span(...):
		   pass
	       with Button(...):
		   pass
	       ...
	       ...
	       ...
	   with StackG(...):
	       with Span(...):
		   pass
	       ...
	       ...
	       ...

	   ...
	   ...
	   ...

	   
     In this approach, the  containment is implicitly expressed based on indentation level -- which makes the code lot more succient. It also is easier to read since it has the same structure as native HTML.




#. **Component-based UI**:  Kavya, currently supports three component libraries: `HyperUI`, `ShadcnUI`, `SkeletonUI`. In line with the goals of Kavya, UI components of these libraries are accessible from within Python. 

.. 
    TODO: give links

     
#. **Client Side and Server Side rendering**:

..
   TODO:description
   



		
Technical Merits
----------------

The design and implementation of Kavya is primarly focussed on programmatic ergonomics. However,
we have introduced optimizations and efficiencies to the framework so as to minimize the memory footprint and runtime overhead. 


Space and Runtime efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Space Efficiency
   
   - Shared Static Components: Non-mutable html elements of webpage such as title, footers etc. share a single copy  across all sessions. 
     
   -  Mutable Components: For components that mutate during runtime, only the dynamic parts, such as text fields, have unique instances per user. Non-mutable attributes of mutable components are shared across client session to minimize memory usage.

#. Runtime Efficiency
   
   - Minimized Data Copying: Kavya has been designed to avoid  unnecessary data copying per connection and per event. This not only results in lower memory footprint but significantly improves the response time. 

     
#. Communication Efficiency
   
   
   - Minimized communication Overhead per UI update : On events (e.g., button clicks), only the ui changes (diffs) are send to the browser, reducing bandwidth and improving response speed.
     
   - State Management & Delta Updates : The browser runtime, does not have to parse entire UI. It only has to scan,
     the much smaller diff, and apply necessary changes to UI -- leading much faster and responsive webpage. 

#. Efficient Concurrency
   
   - Asynchronous Processing: Integration with ASGI (Starlette) allows non-blocking handling of multiple requests, maintaining responsiveness on single-threaded setups.
     
   - Scalability: Running multiple processes across cores or nodes enhances scalability for increased workloads.

#. Rendering Efficiency
   
   - Svelte Runtime: Browser-side Svelte runtime improves rendering speed.
     
   - Diff-Based Updates: Only modified parts are updated, keeping UI changes fast.
	


.. _gallery:

Gallery
-------

#. See live demo of a website build completely using kavya at
   - `Kavya Demos <https://kavya.webworks.monallabs.in/demos>`_

#. See `examples <https://kavya.webworks.monallabs.in/examples/index>`_ for a collection of  basic tutorial examples of webpages build using Kavya. 


#. See `Basic capabilities demo  <https://kavya.webworks.monallabs.in/demo_basic_capabilities>`_ for  webpage showing basic html components. 

#. See `Advanced capabilities demo <https://kavya.webworks.monallabs.in/demo_advanced_capabilities>`_ for webpage illustrating advanced components (hierarchy navigator,  pagination) in action.

   
Techonolgy Stack
----------------

The Kavya stack includes:

#. Svelte (Frontend Engine): Kavya’s browser runtime is build on top of Svelte javascript library.
#. Tailwind (Styling): All UI styling in Kavya is done via Tailwind.
#. Websockets (Server-Browser Communication): Enables real-time server-browser interaction.
#. Starlette (ASGI Request Processing): Asynchronous framework for handling requests and routing.
#. ASGI Middleware: Adds functions like logging, authentication, and authorization.
#. UI Component Libraries: Includes HyperUI, Shadcn, SkeletonUI, FontAwesome, and Material Icons.

In addition, various Python constructs, such as mixins and context management, along with libraries like addict, asyncio, and JSON, are employed in assembling the Kavya framework.   
As Kavya builds applications on the ASGI framework, you can use Uvicorn and Nginx Unit as web servers for applications created with Kavya. 


Running Kavya app
-----------------


#. Getting Kavya 
   - Not on pip; Grab the docker container.

     
#. Activate Kavya environment

   .. code-block::
      
      . ~/Execution/kvaya/bin/activate
      . ~/Execution/kvaya/env.sh
      
#. Switch to the run directory, i.e,  the directory from which the webserver will be lauched

   .. code-block::

      cd <webapp-run-dir>
      

#. Create/Configure `kvaya.env`
   
   - Add BASE_URL to the host machine ip or name as follows:

     .. code-block::
	
	BASE_URL=http://192.168.0.105:8000/

   - In Kavya,  non-static webpages, i.e., pages with active and or mutable components,  require session. To enable session also add following to `kvaya.env`

     .. code-block::

	SESSIONS=True
	SECRET_KEY="alphabeta45324"

     .. caution::
	The above key is no longer secret. In production, change to a  strong secret key. 
	
	
#. Setup client binaries
   
   - If building server side rendering pages
     
     .. code-block::
	
	mkdir -p static/ssr
	TBD

   - If client side rendering
     
     - with Hyperui component library

     .. code-block::

	TBD

     - for Shadcnui and SkeletonUI component library
       
       - see advanced-usage documentation
	 
   
#. Create `the_app.py` 

   .. code-block::
      
      import kavya as vy
      app = vya.build_app()


#. Choose one of the example/demo apps to run

   .. code-block::

      uvicorn --host <myhostip> --port 8000  ./ demo_var_length_list:app

   .. note::
      
      The host and port have to be same as what is provided for `BASE_URL` in `kavya.env`

Webpage programming using Kavya
-------------------------------
If you are new to web development, then it would be helpful to go through the `justpy docs <https://justpy.io/>`_ and its `examples <https://github.com/justpy-org/justpy/tree/master/examples>`_ on which Kavya is based on. 
If you are familiar with Python programming and all webdev principles then best way to get a feel for Kavya programming
is through the examples and sample codes (see :ref:`gallery`). Here we provide a very high level quick walkthrough of programmatics
for webdevelopment. At the least, webdevelopment include being able to achieve following:

#. Creating HTML components and building webpage DOM tree
#. Handling events
#. Styling the components
#. Updating UI for responsive pages


.. caution::
   Also, pay careful attention to known corner cases and suggested workarounds mentioned in `Gotchas <https://kavya.github.io/ofjustpy/Gotchas.html>`_  to keep Kavya engine happy


Dom-tree, events, and UI styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First we show how to achieve the first 3 tasks using the two programmatic styles supported in Kavya: API-based and in-Python html template based. 

API-based approach
++++++++++++++++++

The example below illustrates API-based programming to build a dynamic responsive webpage: 

.. code-block::  python
		 
   import kavya as vy
   from py_tailwind_utils import *


   labels = [vy.Mutable.Label(text="mytext1", key="mylabel1"),
	     vy.Mutable.Label(text="mytext2", key="mylabel2"),
	     vy.Mutable.Label(text="mytext3", key="mylabel3"),
	     vy.Mutable.Label(text="mytext4", key="mylabel4"),
	     ]

   mydeck = vy.Mutable.StackD(key="mydeck",
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


   mybtn = vy.AC.Button(key="mybtn",
		      text="abtn",
		      pcp=[W/32, H/32, bg/rose/6],
		      on_click=on_btn_click
		      )
		      
   wp_endpoint = vy.create_endpoint(key="static-components",
		    childs = [mydeck,
			      mybtn
			      ]
		    )        
   vy.add_jproute("/", wp_endpoint)


The above code creates a ''deck''  of labels. Only the top label is visible.
The button, when clicked cycles through the labels. Note that there is no
extra javascript, html template, etc code required either to render the page or to
dynamically change the UI on the page. Furthermore, all the background work
of computing the diff with changed UI, sending it to browser, and updating the page
is handled by the Kavya framework.

.. note::
   
   This example is meant to demonstrate the programmatic aspects of Ofjustpy. For building full featured
   run-of-the-mill webpages see the HyperUI library components and demos.
   

Let's break down the code based on the given directives:

#. **Define the DOM Tree using Kavya APIs**: The order of steps for building out the DOM-tree in Kavya API-based approach entails:
   
   - Declaring individual components alongwith their attributes
   - Defining the nesting among components.

In the above example, components are declared using APIs:.

#. `vy.Mutable.Label`: to declare labels whose text can be modified at runtime
#. `vy.AC.Button`: to declare an "active" button that can respond to user actions on the browser, such as a click or mouseover.

#. `vy.Mutable.Deck`: A mutable container type whose behaviour is to keep only one of its child component visible at at a time. It has method `bring_to_front` allows you to programmatically make a specific child component the visible one. This is particularly useful for implementing features such as tabbed interfaces, step-based workflows, or other UI elements where switching between views is required.

Finally `vy.create_endpoint` API is used to finalize the DOM tree and associate with an endpoint. As final step the endpoint attached to URL via the `vy.add_jproute` method. 


#. **Specify Handlers for Components**: Define Python function for event handling events triggered on the component. The `on_btn_click` function defines a click event handler for `mybtn`. It brings the next label to the front within the mydeck stack, creating a dynamic effect.

*Create a Function Returning a WebPage Instance*:
        Using `create_endpoit` helper function, the `wp_endpoint` created. It is a function that returns a `WebPage` instance. The previously constructed DOM-tree defines the content and look of the page.

*Declare as Endpoint for a URL Path*:
        Finally, the endpoint is added to the root route ("/") using `oj.add_jproute`.

A few more example expressions  using the API-style programming:

.. code-block:: python
		
   # create a passive span component with text hello. Tailwind style is "bg-green-100 text-xl"
   hello_comp = oj.PC.Span(text="hello", classes = "bg-green-100 text-xl")

   # create a active button component 
   submit_btn = oj.AC.Button(key="abtn", text="Submit", classes="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded")

   # create a div box which vertically stacks hello_comp and submit_btn
   box = oj.PC.StackV(childs = [hello_comp, submit_btn], classes="p-4 m-4 space-y-4")

   
In-Python HTML-template based approach
++++++++++++++++++++++++++++++++++++++

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

The drawback of this in-Python template system its does allows only limited set of Python expressions and limits reusability.



	
HTML Component Types
~~~~~~~~~~~~~~~~~~~~

Kavya, broadly, defines  2 kinds of components: `Static` vs `Mutable`. 
Static components are further classified into `Passive` and `Active`, 
while Mutable components come in three variety: `HCCMutable`, `HCCStatic`, `Mutable`. 

Passive Components
++++++++++++++++++
As the name suggests, these do not respond to UI events and also do not undergo any changes. 
Kavya maintains only a single copy of such components (see `examples/static_webpages <examples/static_webpages>`_). 

Some examples of passive components:

1. `vy.PC.Label`
2. `vy.PC.P`
3. `vy.PC.Img`

See `SHC_types.py <src/kvaya/SHC_types.py>`_ for a list of all passive components.




Active Components
+++++++++++++++++

Active components handle events but, like passive components, do not mutate. 
Active components require an additional key/id argument (see `examples/input_components <examples/input_components>`_).

Examples of active components:

1. `vy.AC.Button`
2. `vy.AC.TextInput`
3. `vy.AC.CheckboxInput`
4. `vy.AC.Select`
5. `vy.AC.A`

and so on. See `SHC_types.py <src/ofjustpy/SHC_types.py>`_ for a list of all active components.

See the :ref:`event_handle` section on attaching event handlers to active components.





Mutable components
++++++++++++++++++
Mutable components can handle events and also mutate, i.e., change appearances. 
See `examples/mutable_webpages <examples/mutable_webpages>`_ for usage.

Examples of mutable components include:

1. `vy.Mutable.Button`
2. `vy.Mutable.Label`
3. `vy.Mutable.Container`

and so on. See `MHC_types.py <src/ofjustpy/MHC_types.py>`_ for a list of all mutable components.




HCCMutable Components
+++++++++++++++++++++

These are div components that contain mutable children. 
However, the div itself is not mutable (see `examples/mutable_webpages/example_004.py <examples/mutable_webpages/example_004.py>`_). 
HCCMutable components offer minor space optimization over mutable divs.

1. `vy.HCCMutable.Div`
2. `vy.HCCMutable.StackV`
3. `vy.HCCMutable.StackW`
4. `vy.HCCMutable.Subsection`

See `MHC_types.py <src/ofjustpy/MHC_types.py>`_ for a list of all HCCMutable components.




HCCStatic Components
++++++++++++++++++++
These are div components that are mutable but contain static (passive or active) components. 

Examples of HCCStatic components:

1. `vy.HCCStatic.Div`
2. `vy.HCCStatic.StackV`

See `MHC_types.py <src/ofjustpy/MHC_types.py>`_ for a list of all HCCStatic components.   
See `MHC_types.py <https://github.com/ofjustpy/ofjustpy/blob/09fe497badc74d306de3e1e019dcad251de08c11/src/ofjustpy/MHC_types.py#L168C12-L168C12>`_ for a list of all HCCStatic components.


Component Styling, Themes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kavya also offers advanced support for Tailwind CSS by providing a built-in mini data model that allows Tailwind directives to be written as native Python expressions. This makes it even more intuitive to style components programmatically. Instead of manually writing strings of class names, you can use the following syntax for a more structured and Pythonic way to define styles:

Component Styling
+++++++++++++++++


Themes
++++++

Kavya supports a `theme`-based approach of defining UI styles, allowing for a more structured and reusable method of styling components. Instead of manually styling each component individually, a `theme` defines default styles that apply to various component types (e.g., `Button`, `Span`, `Div`). This theme-based approach simplifies the process of ensuring consistent styling throughout the application.

The *theme* describes a set of predefined styles, represented as lists of *Tailwind CSS directives*, which are applied to specific components. These directives can be combined to control aspects like font size, font weight, margin, padding, and colors, using Kavya's Python-native expression syntax.

For each component type (e.g., Button, Span), a style is defined in the `defaultsty.py` module, which resides within the src/ofjustpy directory.
You can change the default style by registering your own style file 
with Kavya.  To load your custom style, set the OJSTY environment variable accordingly.

.. code-block::
   
   export VYSTY="mycustomsty"

The style file is simply a listing of all component types, each mapped to an array of tailwind directives that together form its default style. Below illustration shows a sample entry for default style file:

.. code-block::
   
   from py_tailwind_utils import *
   h1 = [xl3, fw.bold,  mr/sl/2, fc/slate/700]

   h2 = [fz.lg, fw.semibold, mr / sl / 2,  fc/slate/700]  # "prose", "prose-2xl"


   para = [
       base,
       fw.light,
       relaxed,
       mr / st / 0,
       mr / sb / 4,
   ]

   ul = [mr / 2, pd / 2, lst.disc]
   ol = [mr / 2, pd / 2, W / "1/2", lst.disc]
   img = [mr / 2, pd / 2]


   button = [
       bg / gray / 100,
       fc / gray / 600,
       mr / sr / 1,
       mr / sb / 1,
       pd / x / 4,
       pd / y / 2,
       bold,
       boxtopo.outline,
       shadow._,
       shadow.sm,
       tt.u,
       *hover(shadow.md, bg / gray / 200, outline / 4, bdr.md),
   ]

In the above theme declaration:

- `h1`: Defines the style for an `<h1>` element, which uses the `xl3` font size (extra-large 3), bold font weight (`fw.bold`), a left margin (`mr/sl/2`), and a font color (`fc/slate/700`).

- `h2`: Defines the style for an `<h2>` element, with a large font size (`fz.lg`), semi-bold font weight (`fw.semibold`), left margin (`mr/sl/2`), and slate color (`fc/slate/700`).

- `para`: Defines the style for paragraph elements (`<p>`). It uses a base font size, light font weight (`fw.light`), relaxed line height (`relaxed`), no margin on the top (`mr/st/0`), and a bottom margin (`mr/sb/4`).

  


When a component is initialized, based on its type, they style mentioned for that type in the default style files is first applied.

Kavya provides a way to override the default styleset and switch to a different styleset for a subset of components of the webapge. 
For e.g., lets say you have `titlepanel.py` which defines  styles to make components more decorative or visually more appealing for the title panel. 

.. code-block::

   vy.Button(...)  # applies style from 'defaultsty' 
   with vy.TwStyCtx("titlepanel"):

     vy.Button(...)  # Uses 'titlepanel' to style the components

   vy.Button(...)  # back to 'defaultsty'

This feature of using style context comes in very handy when we have to change style for a component from a  UI component library. Oftens it is quite cumbersome to access the internal sub-components of a complex component like CTA but we can use
the Kavya's TwStyCtx feature to change style of the internal component unobstrusively.



Overriding default theme
########################


In Kavya, individual components have the ability to override the styling directives of an overarching theme. This can be useful when you want to apply a consistent style through a theme but need to customize specific components with different properties.

For instance, if the default theme specifies that buttons should be styled with `[bg/green/200, fsz.xl]` (light green background and extra-large font size), you can override certain styles like the background color using the `twsty_tags` keyword argument.

.. code-block:: python

   import mytheme
   with vy.TwStyCtx(mytheme):
    abtn = vy.PD.Button(..., twsty_tags=[bg/blue/200])

In this case:
- The `bg/blue/200` directive overrides the button's background color to light blue, while other directives from the **mytheme** such as the font size (`fsz.xl`) remain intact.

This pattern ensures that you can maintain both theme-wide consistency and granular control over component-specific styling.





.. _event_handle:

Event Handling
~~~~~~~~~~~~~~

Kavya, streamlines UI-event handling by taking care of most of glue and plubming code required in a server driven framework. In Kavya, all aspects of event handling is controlled from Python. This eliminates the need for developers to explicitly manage communication and syncrhonization between the client and the server. To handle events, the end developer has to simply:
  
#. Define event handlers in Python
#. Attach them to components declared earlier
#. Within the event handler, users can define both:
   
   - server side actions as well as
   - client side UI changes
      

Kavya makes sure that when a event is triggered on the frontend then

#. collect event and UI data and send them to server
#. the corresponding event handler in Python is invoked
   - with event data passed to the handler
#. collect UI changes made during event handler execution and ship them to the server
#. apply all UI changes in the browser, without requiring explicit coding overhead.
    
      

Kavya's approach for event handling has some obvious advantage.

#. Unified webapp state management: Handling events on the server side enables seamless manipulation of both server-side and browser-side states within a single environment, reducing complexity and potential errors.
   
#. Minimal Boilerplate: Kavya significantly reduces the need for repetitive code when interacting with UI elements, resulting in cleaner and more maintainable codebases.

#. Transparent Client-Server Handling:
   
   - Server-side event handlers issue directives as if working with local components.
   - Kavya efficiently transmits those directives to the browser for seamless UI updates.



Both active and mutable components can have events attached to them. Event handlers receive three arguments:

#. dbref: A reference to the HTML component that triggered the event.
#. msg: A dictionary containing information like the event type, component value, and page instance.
#. **to_mutable_shell**: Is a function object that is applicable on mutable objects (more on this later).      

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

Mutable UI
++++++++++

Kavya provides Python APIs to manipulate the UI of mutable components. 
It provides  the ability to modify attributes of HTML components that is reflected transparently on the browser, eliminating the need for additional code to execute client-side logic. This approach contrasts with other frameworks such as Django, which rely on templates, or browser-side frameworks that require additional code to execute server-side logic.


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

To recap:

#. We did not had to manually compute the state diff of UI
#. Collect all the UI changes and serialize them
#. Ship them to frontend
#. Unserialize and gather the UI for the components
#. Apply the changes.

Ofjustpy handles all the sundry heavylifting without the need for  additional directives.
Also,  notice how Kavya's support of tailwind utility classes, namely, python objects to express tailwind directives and manipulation utilities (add, remove, merge) of tailwind classes makes dynamic UI handling easy  and intutitive.
Furthermore, Kavya engine executes the ui update pipeline *efficiently*. It

-  minimizes latency and communication overhead for ui updates by sending only the changes (aka diffs) in UI state to the frontend. 

Form and data validation
++++++++++++++++++++++++

..
  TODO

  
Circular references, Code ergonomics, and Uictx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quite often, an event handler may need to access objects that are not in the scope of event handler (either defined further down in code or in some other module). 
This situation is similar to the circular dependency problem commonly in programming.
The straightforward approach is to declare the component but postpone the event
handling declarations until all the dependent objects have been created. Then attach the event handler using
the `on` method as shown above.
While this approach works, it comes with a significant drawback—it compromises the natural code structure, leading to reduced code readability, maintainability, and overall programmatic ergonomics.



Kavya offers the powerful uictx (UI Context) construct that can be used to establish an alter-
native hierarchy, enhancing programmatic control and organization.

Let's examine an example to better understand the concept. Here, we will demonstrate the process of creating a simple webpage using Kavya's component programmability:

.. code-block:: python
		
   import kavya as vy
   with vy.uictx("mywp") as mywp:
      with vy.uictx("header") as headerctx:
          homelink = vy.AD.A(key="Home", target="http://www.mywebsite/Home", text="Home Page")
	  deplink = vy.AD.A(key="Departments", target="http://www.mywebsite/DepartmentList", text="List of Departments")
	  # layout: arrange the hyperlinks horizontally 
	  navlinks = vy.PD.StackH(childs = [homelink, deplink])
	  header_panel = vy.PD.Subsection("Navigation Panel", childs=[navlinks])

      with vy.uictx("body") as bodyctx:
          bodytext = vy.PD.Prose(text="The body content of the webpage. This is placeholder. To be replaced with components design for body ")
	  body_panel = vy.PD.Subsection("Navigation Panel", cgens=[bodytext])
	  
      with vy.uictx("footer") as footerctx:
         content = vy.Mutable.Span(key="content", text="This is a placeholder for footer content")
	 footer_panel = vy.PD.Subsection(cgens=[content])

      # putting it all together
      tlc = vy.PD.Container(cgens = [ header_panel,
					   body_panel,
					   footer_panel]
			   )
   # build the webpage
   endpoint = vy.create_endpoint(key="homepage", childs=[tlc])
   vy.add_jproute("/home", endpoint)
   

In this example, we define various sections of the webpage (header, body, and footer) using the `uictx` context manager. We first create the `header`, `body`, and `footer` components with their respective content and then arrange them within their corresponding panels. Finally, we put everything together in a top-level container (`tlc`) and build the webpage. The code is organized and easy to read, thanks to the component programmability provided by Kavya.
There is lesser congnitive load and the resulting codebase is  relatively stable and readable, but can still evolve to meet changes in visual layout requirements.


Component access path on uictx hierarchy
++++++++++++++++++++++++++++++++++++++++

Lets turn our focus to how `uictx` based hierarchy solves the `Circular name dependency` issue.
The `uictx` imposes a hierarchical structure over the components. We can therefore access
a component via an access over this hierarchy. This indirect access to components, instead of
directly refering to the object variable breaks the circular name dependency.

For example, let's consider the code snippet presented earlier. In this case, we have three main sections: the header, body, and footer. Each section is defined within its respective uictx context manager:

.. code-block:: python

   with vy.uictx("mywp") as mywp:
       with vy.uictx("header") as headerctx:
           ...
       with vy.uictx("body") as bodyctx:
           ...
       with vy.uictx("footer") as footerctx:
           ...

Suppose we want to access and modify the content of the footer section.
We can simply use the uictx hierarchy to access the footer component directly:

.. code-block:: python

   footer_content = mywp.footer.content.target
   footer_content.text = "Changed footer status"
   

As mentioned before, the other advantages of `uictx` is modularity and reusability.
We can now define in separate different files and the variable names no longer need
to be within the same scope as event handler is being defined. We can easily incorporate
a different implementation of header, footer or body panel by a different implementation file.




UI Component Library
~~~~~~~~~~~~~~~~~~~~

HyperUI
+++++++

We have also made available wide collection of HyperUI components via Ofjustpy. Because
they are pure tailwind based components, they can be incorporated and manipulated alongwith
the native components using the same Ofjustpy constructs. Especially, useful are the TextInput,
Select, Tabs, etc.


..
   TODO: put hyperlink to live hyperUI demo page

   
ShadcnUI
++++++++

SkeletonUI
++++++++++

Fontawesome Icons
+++++++++++++++++


SVGComponents
+++++++++++++

Styling Helpers/Modifiers
+++++++++++++++++++++++++

#. Halign

#. StackH_Aligned

#. WithBanner

Icons
+++++
FontAwesomeIcon

#. Use fill to change the color
#. use the enclosing div size W and H to change the size   


   

Tailwind-styled containers/advanced components
++++++++++++++++++++++++++++++++++++++++++++++

In addition to standard HTML components (like, Div, Span, Button, etc.),
Ofjustpy offers advanced components that offer complex functionality. These
are build using Tailwind CSS constructs, Svelte, and Python.

For e.g.:
   
a. *vy.PD.Title*
b. *vy.PD.SubheadingBanner*
c. *vy.PD.Section*

and so on   
      
Advanced un-styled mutable and responsive components
++++++++++++++++++++++++++++++++++++++++++++++++++++

Mutable composite components that respond to user actions:

#. StackH, StackV, StackG, StackW : Stack components horizontally, vertically, grid, and wrap around. See examples:
   
   - `example_001.py <examples/static_webpages/example_001>`_
   - `example_002.py <examples/static_webpages/example_002>`_ for StackV
   - `example_004.py <examples/static_webpages/example_004>`_ for StackG
   - `example_002.py <examples/static_webpages/example_002>`_ for StackW

     
#. *StackD*: StackD is a dynamic component representing a "Deck" of cards, where each card is a child element. It allows for switching between the child elements, displaying only one at a time. See examples:
   
   - `example_005.py <examples/mutable-webpages/example_005.py>`_
   - `example_008.py <examples/mutable-webpages/example_008.py>`_
   

     
    
      
#. *Slider*: The Slider function creates a custom slider component that displays a set of clickable circles based on the provided itemiter list. It takes a key and a list of items as input, displaying the items as circles within the slider. When a circle is clicked, its outline is updated, and an on-click event is triggered. See examples:

   - `example_002.py <examples/mutable_webpages/example_002.py>`_
   - `example_003.py <examples/mutable_webpages/example_003.py>`_
   - `example_006.py <examples/mutable_webpages/example_006.py>`_



#. *ColorSelector*: For demonstration of mutable/responsive behaviour purposes only. The ColorSelector function creates a custom color selector component that combines a main color selector and a shades slider. It allows users to pick a color and its shade, then triggers an on-click event with the chosen color. See example
   
   - `example_007.py <examples/mutable_webpages/example_007.py>`_

     

#. *Pagination*: Break a large collection of display elements across a collection of pages. Check out the demo and usage at [demo_paginate](demos/demo_paginate.py).

#. *Dockbar*: Plug in this component to have a bar on your page to minimize page components. See the demo/example code at [demo_dock_undock](demos/demo_dock_undock.py) for usage.
      
#. A simple component to display a Python enum type as a select HTML component.

#. *HierarchyNavigator*: Display a nested [dict/addict/addict-tracking-changes](https://github.com/ofjustpy/addict-tracking-changes) dictionary as hierarchical navigation. Check out the demo/example code at [demo_hinav](demos/demo_hierarchy_navigation_using_italian_cuisine.py).





Creating webpage endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~

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

Arguments to create endpoint are  applied to webpage creation. 
Additional arguments to create endpoint include:

#. head_html : Allows you to add custom HTML inside the `<head>` section of the page.

   .. code-block::
      <html>
      <head>
      ... {head_html} ...
      </head>
      </html>

   

   
#. `body_style`, `body_classes`,`body_html`: Used to customize the `<body>` section of the webpage.
   - body_style: Adds inline styles to the <body> tag.
   - body_classes: Specifies CSS classes for the <body> tag.
   - body_html: Inserts custom HTML content directly inside the <body> tag.   
   
   .. code-block::

      <body {body_style} {body_classes}>
      ... {body_html} ...
      </body>

   




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



Client Side vs. Server Side Rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Website/App programming in Ofjustpy
-----------------------------------

An app or website for our current purpose is a collection of endpoints and their associated routes.
We will outline a few quality-of-life enhancements we have made in Ofjustpy over Starlette.


PageBuilder (WebPage Template) in Kavya
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Kavya, instead of relying on traditional template engines like Jinja2, you can use the PageBuilder context to achieve a similar goal: generating multiple pages that share common elements. This approach offers flexibility and consistency while avoiding the need to manage external template engines.

PageBuilder is a context-based mechanism that applies a predefined layout or structure (such as headers, footers, or side menus) to all pages created within its scope. It ensures that common facets are consistently added to multiple endpoints, simplifying maintenance and enhancing reusability.

Below is an example of how to use the PageBuilderCtx to define and apply a common layout to multiple endpoints:


.. code-block::
   
   def page_builder(childs):
      sideMenu = SimpleSideMenu("See also")
      header_panel = vy.PD.StackH(...)
      footer_panel = vy.PD.StackV(...)
      full_page = vy.PD.StackH(childs = [sideMenu,
                           vy.PD.StackV(childs = [header_panel,
                                                  vy.PD.Div(childs=childs),
                                                  footer_panel
                                                  ]
                                        )
                           ]
                 )
      return [full]


   with oj.PageBuilderCtx(page_builder):
       endpoint1 = vy.create_endpoint(childs=[..], ...)
       vy.add_jproute("/endpoint1", endpoint1)
       
       vy.create_endpoint(childs=[...],... )
       vy.add_jproute("/endpoint2", endpoint2)
       
       import module_with_endpoints
       

In this example, the webpages served by endpoint1, endpoint2, and all endpoints defined within the module module_with_endpoints will be retrofitted with the same common layout and structures defined in the `page_builder` function.


 
Routes and Mounts
~~~~~~~~~~~~~~~~~

An endpoint can be attached to  relative path as follows:

.. code-block:: python

   vy.add_jproute("/x/y/z", wp_endpoint, name="my-first-webpage")

Ofjustpy  provides helper expressions to make is easier to mount an sub-app (i.e.,
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

Middlewares
~~~~~~~~~~~
  
..
  TODO: reference manual

Sessions
~~~~~~~~

#. To enable session, add following to  Kavya's config file, `kavya.env`,:
   
   .. code-block::
      
      SESSIONS=True
      SECRET_KEY="alphabeta45324"

   .. caution::
      The above key is no longer secret. In production, change to a  strong secret key. 

#. You can access session id from event handlers as follows:

   .. code-block::

      def an_event_handler(dbref, msg, to_mutable_shell):
         session_id = msg.page.session_manager.session_id

#. On the browser `session_id` is stored in the cookie named `session`. To use a different cookie name for the session, modify the SESSION_COOKIE_NAME in config file

   .. code-block::

      SESSION_COOKIE_NAME=<cookie-name-for-session>


#. Additional data can be added to the session by modifying the request.session dictionary. This allows you to dynamically store information that will persist across a user's session. Here's an example:
   
   .. code-block::
      
      def an_event_handler(dbref, msg, to_mutable_shell):
          request = msg.page.session_manager.request
	  request.session[another_key] = another_value

   
Cookies
~~~~~~~

Adding cookies in Kavya is a two step process:

#. First, config each cookie using `vy.cookie_cfg`
#. Pass the configs along with secret keys to the app builder `vy.build_app`


*Create Cookie Config*: create cookie config which includes cookie name along with other cookie parameters as shown in sample code below:

.. code-block::
   
   cart_items_cookie_cfg = oj.cookie_cfg("cart_items",
   state_attr_name = "cart_items",
               max_age = 14 * 24 * 60 * 60,  # 14 days, in seconds
               path="/",
               domain=None,
               secure = False,
               httponly = False,
               samesite= "lax"
	       )
	       
   # config other cookies
   user_prefs_cookie_cfg = ...

   ...

*Pass config to App builder* Cookies are added during app construction, in the `the_app.py`.

.. code-block::
   
   app  = oj.build_app(cookie_cfg_iter= [cart_items_cookie_cfg,
                                      user_prefs_cookie_cfg,
				      ...
				      ...
				      ...
                                      ],

                    cookie_signer_secret_keys = [ secret_key_cart_item,
	                                          secret_key_user_prefs
						]
                    )
		    


The cookies can be accessed and modified in event handler via `request` object.
The `state_attr_name` defined in  cookie config has the cookie values.
The example below shows access and modification of `cart_items` cookie in an event handler:

.. code-block::
   
   def event_handler(dbref, msg, to_ms):
    request = msg.page.session_manager.request
    print(request.state.cart_items)
    request.state.cart_items = {'aval' :1}
    pass

    
LifeSpans
~~~~~~~~~

CSRF
~~~~
maybe


Browser Runtime and Tree Shaking
--------------------------------


  
API references
--------------

Components specific keyword arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: Button
	      
   :ivar autofocus: Specifies whether the button should automatically get focus when the page loads. Possible values: True or False.
   :ivar disabled: Specifies whether the button should be disabled or not. Possible values: True or False.
   :ivar form: Specifies the form the button belongs to.
   :ivar formaction: Specifies the URL of the file that will process the input control when the form is submitted.
   :ivar formenctype: Specifies how the form-data should be encoded when submitting it to the server. Possible values: "application/x-www-form-urlencoded", "multipart/form-data", or "text/plain".
   :ivar formmethod: Specifies the HTTP method to use when sending form-data. Possible values: "GET" or "POST".
   :ivar formnovalidate: Specifies that the form-data should not be validated on submission. Possible values: True or False.
   :ivar formtarget: Specifies where to display the response received after submitting the form. Possible values: "_blank", "_self", "_parent", "_top", or a custom target name.

		     

.. py:class:: TextInput
	      
   :ivar type: The type attribute associated with the element (always "text").
   :ivar autocomplete: Specifies whether the browser should enable autocomplete for the input field.
   :ivar maxlength: Specifies the maximum number of characters allowed in the input field.
   :ivar minlength: Specifies the minimum number of characters required in the input field.
   :ivar pattern: Specifies a regular expression pattern that the input's value must match to be valid.
   :ivar placeholder: Provides a short hint that describes the expected value of the input field.
   :ivar size: Specifies the visible width of the input field.
	       

.. py:class::  Img
   
   :ivar alt: A text description of the image, providing a textual alternative for users who cannot see the image.
   :ivar crossorigin: A CORS settings attribute that indicates how the element handles crossorigin requests. Possible values: 'anonymous', 'use-credentials'.
   :ivar height: The intrinsic height of the image, in pixels. Must be a positive integer.
   :ivar ismap: Indicates that the image is part of a server-side image map. Value should be a boolean: True or False.
   :ivar longdesc: A URL to a more detailed description of the image.
   :ivar sizes: The sizes attribute for the image.
   :ivar src: The source URL of the image.
   :ivar srcset: The srcset attribute for responsive images.
   :ivar usemap: Specifies a client-side image map for the image.
   :ivar width: The intrinsic width of the image, in pixels. Must be a positive integer.

.. py:class::  CheckboxInput
  

     :ivar checked: Specifies whether the checkbox is initially checked (True) or unchecked (False). The value is a boolean.


.. py:class::  Textarea

   :ivar cols: Specifies the visible width of the textarea in average character widths. Must be a positive integer.
   :ivar rows: Specifies the visible number of lines in the textarea. Must be a positive integer.
   :ivar wrap: Specifies how the text in the textarea is to be wrapped when submitted in a form. Possible values are "soft" (text wrapped for appearance only) and "hard" (text wrapped for both appearance and submitted text).
   :ivar placeholder: Provides a short hint that describes the expected value of the textarea.

.. py:class::  Select

   :ivar autofocus: Specifies whether the select element should automatically get focus when the page loads. Possible values: True or False.
   :ivar default: Specifies the default value for the select element.
   :ivar disabled: Specifies whether the select element should be disabled or not. Possible values: True or False.
   :ivar form: Specifies the form to which the select element belongs (form's id).
   :ivar multiple: Specifies that multiple options can be selected at once. If present, the attribute does not need a value.
   :ivar name: Specifies the name for the select element.
   :ivar required: Specifies whether the select element is required to have a value selected. Possible values: True or False.
   :ivar size: Specifies the number of visible options in the dropdown list.

.. py:class::  Form

   :ivar accept_charset: Specifies the character encodings to be used for form submission. A space-separated list of character encoding names (e.g., "UTF-8 ISO-8859-1").
   :ivar action: Specifies the URL where form data should be submitted when the form is submitted. It can be an absolute or relative URL.
   :ivar autocomplete: Specifies whether the browser should enable autocomplete for the entire form. Values: 'on' or 'off'.
   :ivar enctype: Specifies how the form data should be encoded when submitted to the server. Possible values are 'application/x-www-form-urlencoded' (default), 'multipart/form-data' (required for file uploads), or 'text/plain'.
   :ivar method: Specifies the HTTP method to use when submitting the form data. Possible values: 'get' (default) or 'post'.
   :ivar name: Specifies a name for the form, which can be used for scripting purposes, such as referencing the form from JavaScript.
   :ivar novalidate: A boolean attribute. When present, it specifies that the form should not be validated when submitted.
   :ivar target: Specifies where the response received after submitting the form should be displayed. Possible values include '_blank' (new window or tab), '_self' (same frame), '_parent' (parent frame), '_top' (full window body), or a named frame.


.. py:class::  A

   :ivar href: Specifies the URL to which the hyperlink points.
   :ivar title: Specifies the title of the linked document.
   :ivar rel: Specifies the relationship between the current document and the linked document.
   :ivar download: Specifies that the target will be downloaded when the link is clicked.
   :ivar target: Specifies where to open the linked document. Values can include '_blank', '_self', '_parent', '_top', or a named frame.
   :ivar scroll: Specifies whether scrolling is enabled when the hyperlink is clicked (True or False).
   :ivar scroll_option: Specifies the type of scrolling when the hyperlink is clicked. Values can be "auto" or "smooth" (default is "smooth").
   :ivar block_option: Specifies the vertical alignment of the target element when scrolling. Values can be "start", "center", "end", or "nearest" (default is "start").
   :ivar inline_option: Specifies the horizontal alignment of the target element when scrolling. Values can be "start", "center", "end", or "nearest" (default is "nearest").

.. py:class::  Label


  :ivar form: The 'form' attribute of the <label> element specifies the id of the form to which the label belongs. The value is the id of a <form> element.

  :ivar for_: The 'for' attribute of the <label> element specifies the id of the form control with which the label is associated. The value is the id of a form control element.
	      

.. py:class:: Optgroup
   
   :ivar disabled: Specifies whether the entire option group should be disabled. A boolean attribute with values 'True' or 'False'.
		    
   :ivar label: Provides a label or name for the option group. It is a string used for organizing and categorizing the options within the group.
		    

.. py:class::  Fieldset

   :ivar disabled: A boolean attribute specifying whether the fieldset should be disabled or not.
   :ivar form: Specifies the form element to which the fieldset belongs. It can be an ID or a name of a form.
   :ivar name: Provides a name for the fieldset, which can be used for scripting purposes or referencing from JavaScript.

.. py:class::  Colgroup

   :ivar span: Specifies the number of columns a colgroup element should span. It is an integer value representing the number of columns.

.. py:class::  Style

   :ivar type: Specifies the style sheet language of the embedded style block. It typically has a value of "text/css".
   :ivar media: Specifies the media type for which the styles are intended. It is used to define different styles for different devices or media types.
   :ivar scoped: A boolean attribute. When present, it indicates that the styles contained within the style element are intended only for the parent element and its children.


.. py:class::  Blockquote

   :ivar cite: Specifies the source of the quotation or the reference to the original work. It is a URL or a textual reference providing context for the quoted content.

	       

.. py:class::  Script

   :ivar async: A boolean attribute. When present, it indicates that the script should be executed asynchronously.
   :ivar charset: Specifies the character encoding for the external script file.
   :ivar defer: A boolean attribute. When present, it indicates that the script execution should be deferred until the HTML document has been fully parsed.
   :ivar src: Specifies the URL of an external script file.
   :ivar type: Specifies the media type of the script. It is typically set to "text/javascript" or another valid MIME type.
	       

.. py:class::  Meta


   :ivar charset: Specifies the character encoding for the document.
   :ivar content: Provides the value associated with the meta information.
   :ivar http-equiv: Provides an HTTP header for the information/value specified in the content attribute. It is used for specifying the pragma, cache control, or refresh.
   :ivar name: Specifies a name for the metadata. It is used for specifying metadata like keywords, description, etc.


.. py:class::  Table
   
   :ivar border: Specifies the width of the border around the table. It is typically used to control the visual presentation of the table borders.
   :ivar cellpadding: Specifies the amount of space between the cell content and the cell border on each side of the cell.
   :ivar cellspacing: Specifies the amount of space between cells in the table.
   :ivar width: Specifies the width of the table. It can be a pixel value, a percentage, or another valid CSS value.


.. py:class::  Tr
	       
   :ivar align: Specifies the horizontal alignment of the content within the cell. Values can be 'left', 'center', 'right', 'justify', or 'char'.
   :ivar bgcolor: Sets the background color of the cell. It can be a color name, a hex value, or a valid CSS color.
   :ivar char: Specifies the character to align vertically when the 'valign' attribute is set to 'char'.
   :ivar charoff: Specifies the offset for aligning characters vertically when the 'valign' attribute is set to 'char'.
   :ivar valign: Specifies the vertical alignment of the content within the cell. Values can be 'top', 'middle', 'bottom', 'baseline', or 'top'.

   :param \**kwargs:
        See below

   :Keyword Arguments:
        * *extra* (``list``) --
          Extra stuff
        * *supplement* (``dict``) --
          Additional content		 

	  

Using Composite Components
++++++++++++++++++++++++++

SubheadingBanner
````````````````

The SubheadingBanner function creates a styled banner with a subheading text.

.. py:function:: oj.PD.SubheadingBanner

   The SubheadingBanner function creates a styled banner with a subheading text. 

   :param  heading_text: A string representing the text to be displayed as the subheading. This parameter is required.

   :param twsty_tags: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

   :param heading_text_sty: A list of Tailwind CSS classes to apply to the heading text. This parameter is optional and defaults to sty.subheading_text.

   :param \**kwargs: See below

      :Keyword Arguments:

	 * *TBD* --
	   
	   TBD




SubsubheadingBanner
```````````````````

Usage same as `SubheadingBanner`.


Subsection
``````````

The Subsection function creates a subsection component that consists of a heading and content. It utilizes StackV to vertically stack the heading and content, creating a visually appealing subsection.

.. py:function:: Subsection(heading_text: AnyStr, content: Callable, align="center", twsty_tags=[], childs=[], **kwargs)

   Display a subsection with customizable styling.

   :param heading_text: A string representing the text to be displayed as the subsection heading. This parameter is required.
   :param content: A component representing the content of the subsection. This parameter is required.
   :param align: A string representing the alignment of the subsection (default is "center"). Valid values are "center", "left", "right".
   :param twsty_tags: A list of Tailwind CSS classes to apply to the subsection. This parameter is optional.
   :param childs: A list of child elements for the subsection. This parameter is optional.
   :param kwargs: Additional keyword arguments that can be passed to the function.

   Usage example:

   .. code-block:: python

      subsection_instance = Subsection('Subsection Heading', oj.PD.Prose(text="..."), align="left", twsty_tags=['text-blue-500'], childs=[child_1, child_2], custom_arg="value")


      
Subsubsection
`````````````

Same as Subsection

Title
`````

The Title function creates a styled component that displays a title text. It takes a key and a title text as inputs, and displays the title text with the specified alignment.
SubTitle also has similar usage.

.. py:function:: Title(title_text: AnyStr, twsty_tags=[], align="center", **kwargs)

   Display a title with customizable styling.

   :param title_text: A string representing the text to be displayed as the title. This parameter is required.
   :param twsty_tags: A list of Tailwind CSS classes to apply to the title. This parameter is optional.
   :param align: A string representing the alignment of the title (default is "center"). Valid values are "center", "left", "right".
   :param kwargs: Additional keyword arguments that can be passed to the function.

   Usage example:

   .. code-block:: python

      title_instance = Title('My Title', twsty_tags=['text-4xl', 'font-bold'], align="left", custom_arg="value")


StackG
``````

.. py:class:: StackG(*args, **kwargs)

   A class representing a grid with customizable styling.

   :param num_rows: An integer representing the number of rows in the stack grid (default is 2).
   :param num_cols: An integer representing the number of columns in the stack grid (default is 2).
   :param twsty_tags: A list of Tailwind CSS classes to apply to the stack. This parameter is optional.
   :param kwargs: Additional keyword arguments that can be passed to the parent class constructor.

TitledPara
``````````

The TitledPara function in the oj.PC module is used to create a titled paragraph component.

.. py:function:: TitledPara(heading_text, content, twsty_tags=[], fix_sty_section_nesting=False, **kwargs)

   Display a titled paragraph with customizable styling.

   :param heading_text: A string representing the text to be displayed as the title of the paragraph. This parameter is required.
   :param content: The content of the paragraph. This can be a string or an object with a compatible representation.
   :param twsty_tags: A list of Tailwind CSS classes to apply to the titled paragraph. This parameter is optional.
   :param fix_sty_section_nesting: A boolean indicating whether to adjust styling for nested sections. If True, the content is displayed across the entire width with added margin to give the effect of being nested within the title. Default is False.
   :param kwargs: Additional keyword arguments that can be passed to the function.

		  
.. toctree::
   :maxdepth: 6
   :caption: Contents:

