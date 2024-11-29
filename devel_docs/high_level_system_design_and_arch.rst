High level system architecture/code working
'''''''''''''''''''''''''''''''''''''''''''

There are two phases
- Declaration phase
- DOM Generation phase

Declaration phase
+++++++++++++++++
  
In declaration phase, each component declares who its  childs are along with
static attributes and initial values for mutable attributes.


DOM Generation phase
++++++++++++++++++++
Starting from root which is WebPage class
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

..
   TODO move this to its proper place
   
- When is build_json called? called by stub after the childs are registered

MutableShell/StaticCore/WithStub architecture
+++++++++++++++++++++++++++++++++++++++++++++
Every component type has a static core which is defined as
collection of mixins.

.. py:class: StaticCoreType
   
#. WithStub(StaticCoreType)
   Static core is wrapped in With_stub which has stub function
   
#. All constructor args/kwargs are passed on to StaticCore. The is where theme sty (via stytags_getter_func) is conc with twsty_tags and applied to static code.

.. code-block:: python
		  
     stytags = stytags_getter_func()
     twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
     super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

#. WithStub.stub
The stub is called by ofjustpy when rendering the components and registering them with tracker

.. py:function: def stub(self)
   
#. stub function invokes `gen_stub` which generates the Stub.
#. gen_stub is tracked by the tracker.

.. note:: TODO: needs correction
	  
.. code-block:: python
		
   @trackStub
   def gen_stub(target, **kwargs):
   
       target.request_callback(kwargs.get("session_manager"))
       return Stub(target=target, **kwargs)

#. `request_callback` is a post-processor. Is called after staticCore has been initialized for a request object. Used for decoding url from an endpoint. 

#. For passive/active components: mutable shell is same as static-core.

   
HC/Div Data structures
''''''''''''''''''''''
All HC/Div type use two dictionaries
- domDict
- attrs

#. domDict attributes are used to svelte rendering engine to craft a  html object
# attrs are directly passed as attrs to html object   

ThirdParty
----------

#. https://github.com/FortAwesome/Font-Awesome.git

#. https://github.com/google/material-design-icons.git
#.  https://github.com/Templarian/MaterialDesign-SVG.git   

    
