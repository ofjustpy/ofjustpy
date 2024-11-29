# [Ofjustpy](https://github.com/ofjustpy/ofjustpy)
[![Python versions](https://img.shields.io/badge/Python-3.11-green)](https://pypi.python.org/pypi/ofjustpy)
[![Tests Status](https://github.com/ofjustpy/ofjustpy/blob/main/badge_tests.svg)](https://github.com/ofjustpy/ofjustpy/actions)
[![Coverage Status](https://github.com/ofjustpy/ofjustpy/blob/main/badge_coverage.svg)](https://github.com/ofjustpy/ofjustpy/actions)
[![Flake8 Status](https://github.com/ofjustpy/ofjustpy/blob/main/badge_flake8.svg)](https://github.com/ofjustpy/ofjustpy/actions)

[![Documentation](https://img.shields.io/badge/doc-latest-blue.svg)](https://ofjustpy.github.io/ofjustpy/)
[![PyPI](https://img.shields.io/pypi/v/addict-tracking-changes.svg)](https://pypi.python.org/pypi/ofjustpy)
[![Downloads](https://pepy.tech/badge/addict-tracking-changes)](https://pepy.tech/project/)
[![Downloads per week](https://pepy.tech/badge/addict-tracking-changes/week)](https://pepy.tech/project/ofjustpy)
[![GitHub stars](https://img.shields.io/github/stars/ofjustpy/addict-tracking-changes.svg)](https://github.com/ofjustpy/ofjustpy/stargazers)


See live demo of a website build completely using ofjustpy at [https://ofjustpy.webworks.monallabs.in](https://ofjustpy.webworks.monallabs.in)

# Ofjustpy: A Full-Stack Web Development Framework in Python

**Features:**

* **Single language**: Ofjustpy allows you to build full-featured web pages using only the Python programming language. You don't need to learn and manage multiple languages like Jinja2 templating, JavaScript, HTML, and CSS. The entire functionality of a webpage can be expressed using pure Python.
   
2. **Emphasis on API Design**:  Much emphasis has been put on API design and programmatic constructs in order
to be able to build complex responsive webpages and websites with codebase that easy to read and maintain. 

3. **Scalable and efficient**: Ofjustpy enables programmers to write scalable and efficient webpage code. It maintains only a single copy of static components, regardless of the number of connections opened. Data copying per connection and per event is minized. Even for mutable components, only a single copy of the component's static portion is maintained.  Additionally, communication is efficient as it transmits only the changes (diff) to the UI to the frontend.


4. **Composibility**:  Ofjustpy allows users to easily build reusable components and incorporate them into their codebase. See [htmlcomponents.py](src/ofjustpy/htmlcomponents.py) and [ofjustpy-components](https://github.com/ofjustpy/ofjustpy-components) for  simple to complex components build using Ofjustpy framework. 

5. **Tailwind CSS Support**: Ofjustpy provides first-class and native support for Tailwind CSS constructs, enabling complex manipulation (add, remove, update classes) of the frontend UI through pure Python expressions.

6. **Async Processing**: Like its predecessor Justpy, Ofjustpy utilizes an asynchronous webserver stack that includes Starlette, ASGI, asyncio, and async/await. This architecture enables Ofjustpy to efficiently handle concurrent connections, even on single-core hardware or virtual environments, without the need for OS-level multi-threading.

7. **Technology Stack**:
The tech stack of ofjustpy consists of Svelte (as the frontend UI engine), 
websockets (for communication between browser and server), Starlette (the async webserver), 
amd Tailwind (for layout and design). 

## Gallery 

- See live demo of a website build completely using ofjustpy at [https://ofjustpy.webworks.monallabs.in](https://ofjustpy.webworks.monallabs.in)

- See [examples](https://ofjustpy.webworks.monallabs.in/examples/index) for a collection of 
basic tutorial examples of webpages build using ofjustpy. 

- See [Basic capabilities demo](https://ofjustpy.webworks.monallabs.in/demo_basic_capabilities) for 
webpage showing basic html components 

- See [Advanced capabilities demo](https://ofjustpy.webworks.monallabs.in/demo_advanced_capabilities)
for webpage illustrating advanced components (hierarchy navigator,  pagination) in action. 

## Setup and running ofjustpy app

1. Setup python environment and install ofjustpy
```
python3 -m venv venv
./venv/bin/activate
pip install ofjustpy
```
2. Download example codes
```
git clone https://github.com/ofjustpy/ofjustpy.git
cd ofjustpy/examples/static_webpages
```

3. Configure via justpy.env  

Create file `justpy.env` and add BASE_URL to the host machine ip or name as follows:
```
BASE_URL=http://192.168.0.105:8000/
```

4. Set env variable `OJ_APP_MODULE` to the file containing the oj app. 
If in the `examples/static_webpages` directory, use:
```
export OJ_APP_MODULE="../the_app"
```

5. Launch uvicorn with host and port arguments
```
uvicorn --host 192.168.0.105 example_001:app
```

6. Running into problems?. Raise issue at https://github.com/ofjustpy/ofjustpy/issues


## Webpage programming using Ofjustpy
The basic paradigm for building out webpages in Ofjustpy is straighforward:
1. Create components and containers
2. Describe their layout and appearance using tailwind constructs
3. For components that will respond to events on UI, describe handlers (actions) for those 
events 

If you are new to web development, then it would be helpful to go through the [justpy docs](https://justpy.io/) and its [examples](https://github.com/justpy-org/justpy/tree/master/examples) on which Ofjustpy is based on. 
Also, pay careful attention to known corner cases and suggested workarounds mentioned in [Gotchas](https://ofjustpy.github.io/ofjustpy/Gotchas.html)  to keep Ofjutpy engine happy 

The demo example illustrates the three paradigms for building out webpages:
```python
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



```
### Components and their types in Ofjustpy
Ofjustpy, boradly, defines  2 kinds of components: static vs mutable. 
Static components are further classified into Passive and Active, 
while mutable components come in three variety: HCCMutable, HCCStatic, Mutable. 

#### Passive Components
As name suggests, these do not respond to UI events and also do not undergo 
any changes. Ofjustpy maintains only a single copy of such components  (see [examples/static_webpages](examples/static_webpages))
Examples of passive  components:
1. oj.PC.Label
2. oj.PC.P
3. oj.PC.Img

etc. See [SHC_types.py](src/ofjustpy/SHC_types.py) for list of all passive components. 

#### Active Components
Active components handle events but like passive do not mutate. 
Active components require an additional key/id argument (see [examples/input_components](examples/input_components)). 
Examples of active  components:
1. oj.AC.Button
2. oj.AC.TextInput
3. oj.AC.CheckboxInput
4. oj.AC.Select
5. oj.AC.A

and so on. See [SHC_types.py](src/ofjustpy/SHC_types.py) for list of all active components


#### Mutable components
Mutable components can handle events and also mutate, i.e., change 
appearances. See [examples/mutable_webpages](examples/mutable_webpages) for usage. 
Examples of mutable components include:
1. oj.Mutable.Button
2. oj.Mutable.Label
3. oj.Mutable.Container
and so on. See [MHC_types.py](src/ofjustpy/MHC_types.py) for list of all mutable components. 


#### HCCMutable Components
These are div  components 
that contain mutable childrens. 
The div itself is not mutable (see [examples/mutable_webpages/example_004.py](examples/mutable_webpages/example_004.py)). 
HCCMutable components offer minor space optimization 
over Mutable divs. 
Examples of HCCMutable components:
1. oj.HCCMutable.Div
2. oj.HCCMutable.StackV
3. oj.HCCMutable.StackW
4. oj.HCCMutable.Subsection
See [MHC_types.py](src/ofjustpy/MHC_types.py) for list of all HCCMutable components. 

#### HCCStatic Components
These are div components
that itself are mutable but 
they contain static (passive or active) components. 
Examples of HCCStatic components:
1. oj.HCCStatic.Div
2. oj.HCCStatic.StackV

See [MHC_types.py](https://github.com/ofjustpy/ofjustpy/blob/09fe497badc74d306de3e1e019dcad251de08c11/src/ofjustpy/MHC_types.py#L168C12-L168C12) for list of all HCCStatic components. 



#### Tailwind-derived higher-order components
In addition to standard HTML components (like, Div, Span, Button, etc.),
Ofjustpy offers advanced components that offer complex functionality. These
are build using Tailwind CSS constructs, Svelte, and Python. 

1. Containers to juxtapose child components
StackH, StackV, StackG, StackW : Stack components horizontally, vertically, grid, and wrap around. See examples [examples/static_webpages/example_001.py](examples/static_webpages/example_001.py),  
[examples/static_webpages/example_002.py](examples/static_webpages/example_002.py) for StackV, [examples/static_webpages/example_004.py](examples/static_webpages/example_004.py) for StackG, [examples/static_webpages/example_002.py](examples/static_webpages/example_002.py) for StackW. 


2. StackD: 
Deck the items on top of each other. See examples [examples/mutable_webpages/example_005.py](examples/mutable-webpages/example_005.py), [examples/mutable_webpages/example_008.py](examples/mutable-webpages/example_008.py)

3. Slider
A component with discreet value buttons to select a value.
See examples [examples/mutable_webpages/example_002.py](examples/mutable_webpages/example_002.py),  [examples/mutable_webpages/example_003.py](examples/mutable_webpages/example_003.py), [examples/mutable_webpages/example_006.py](examples/mutable_webpages/example_006.py).


4. ColorSelector
Component create select  drop down option for all tailwind preset color values. 
See example [examples/mutable_webpages/example_007.py](examples/mutable_webpages/example_007.py)

See ofjustpy-components github repo for collection of advanced components. 


## The Ofjustpy paradigms: app module, TwStyCtx, MountCtx, PageBuilderCtx
### App module
Ofjustpy requires that starlette app be defined in its own file lets say 
"theapp.py". Then set the `OJ_APP_MODULE` to set the location of the `theapp.py`
relative to directory from where the webserver is being launched. 


```bash
export OJ_APP_MODULE="../the_app"
```
A sample example of `theapp.py` looks as follows:
```python
from asgi_signing_middleware import SerializedSignedCookieMiddleware

import ofjustpy as oj
csrf_middleware = Middleware(CSRFMiddleware,
                                secret=csrf_secret,
                                field_name = csrf_cookie_name)

signed_cookie_middleware = Middleware(SerializedSignedCookieMiddleware,
                               secret=b'a very, very secret thing',  
                               state_attribute_name='messages',  
                               cookie_name='my_cookie',
                               cookie_ttl=60 * 5,  
                               )


auth_middleware =     Middleware(AuthenticationMiddleware,
                                 backend=BasicAuthBackend(),
                                 on_error=lambda _, exc: PlainTextResponse("error during authentication", status_code=401)
                                 )



app =  oj.load_app([auth_middleware,
                    signed_cookie_middleware,
                    csrf_middleware
                    ])
```

### User defined default sty module and TwSty context
The default UI style of a component is determined by its type. For each component type (e.g., Button, Span), a style is defined in the snowsty.py module, which resides within the src/ofjustpy directory.
You can customize the default style by registering a style file 
with Ofjustpy.  To load your custom style, set the OJSTY environment variable accordingly.
Please note that the default style for a component can be overridden using the `twsty_tags` directive. You can also modify the style programmatically throu TwStyCtx context expression.
Ofjustpy provides two style definitions `snowsty` and `un`. The `un` style does not 
add any styling to the components. 

An example illustrate style switching:
```python
with oj.TwStyCtx("un"):
    oj.Button(..., twsty_tags = []) # Draw a with un default styling 
oj.Button(..., twsty_tags = []) # use dnowsty as default styling
```


### Customizing Default Styling in Ofjustpy

In Ofjustpy, the default UI style for a component is determined by its type. Each component type, such as Button or Span, has a predefined style located in the `snowsty.py` module within the `src/ofjustpy` directory.

To personalize the default styling, you can register a custom style file with Ofjustpy. To make use of your custom style, simply set the `OJSTY` environment variable accordingly.

Please bear in mind that you have the flexibility to override the default style for a component using the `twsty_tags` directive. 


In addition to setting `OJSTY`, you can programmatically modify the style using the `TwStyCtx` context expression.

Ofjustpy offers two predefined style definitions: `snowsty` and `un`. The `un` style, in particular, refrains from adding any additional styling to the components.

Here's an example to illustrate style switching:

```python
with oj.TwStyCtx("un"):
    oj.Button(..., twsty_tags=[])  # Draws with the 'un' default styling
oj.Button(..., twsty_tags=[])  # Uses 'snowsty' as the default styling
```

By following these guidelines, you can easily tailor the default styles in Ofjustpy to suit your project's aesthetic preferences.




### MountContext
The MountContext construct simplifies the process of mounting all the routes defined in a module. Consider the following example:


```python
with oj.MountCtx("examples"):
   with oj.MountCtx("static_webpages"):    
       static_webpage_module = importlib.import_module("examples.static_webpages",
                                                            )
															
```
In the above example, all the routes 
defined within the examples.static_webpages will be mounted under
`examples/static_webpages` path. 
MountCtx enable a plug-and-play approach for adding modules and defining routes. 
This means you can import the module into multiple web app codes without needing to modify the module code for each app. This flexibility simplifies the process of extending and reusing modules across different applications.



### PageBuilder Context
The PageBuilderCtx context is used to modify or post-process webpage endpoints defined within a module. Let's consider the following example:
```python
def page_builder(edir):
    """
    We need edir to find the example directory within which the example is located.
    
    """
    def page_builder_inner(key, childs, **kwargs):
        title = kwargs.get('title')
        nav_buttons = //define a list of navigation buttons
        

        return oj.Mutable.WebPage(key=key,
                               childs = [oj.HCCMutable.StackV(childs = [oj.HCCMutable.Div(childs=childs),
                                                                oj.PC.Hr(twsty_tags=[bg/green/1]),
                                                                nav_buttons],
                                                      twsty_tags= [space/y/8]
                                                      )
                                         ],

                               **kwargs
                               )

    return page_builder_inner



with oj.PageBuilderCtx(page_builder("mutable_webpages")):
    with oj.MountCtx("input_components"):
        input_components_module = importlib.import_module("examples.input_components",
                                                            )
															
```															
In the above example, the `oj.PageBuilderCtx` context is used to post-process all endpoints defined within the `examples.input_components` module. Specifically, it allows for the addition of navigation buttons at the bottom of each page generated by the endpoints in this module. This structured approach simplifies the task of modifying and enhancing the behavior of web pages associated with the `input_components` module by applying a consistent post-processing step to all of them.

