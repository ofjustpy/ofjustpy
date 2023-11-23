Code Notes for type generators/factory
+++++++++++++++++++++++++++++++++++++++
1. For Passive/Active HCType generators are in `SHC_types_mixin.py`
2. Active types has keyMixin and Idmixin
3. Passive types have PassiveKeyIdMixin that yield id(self) as id and key
4. HCCMutable, HCCStatic, Mutable are generated from `mutable_Div_TF.py`

   

Component Type Design Methodology
+++++++++++++++++++++++++++++++++

StaticCoreType
..............
Every component type has a static core which is defined as
collection of mixins.

.. py:class: StaticCoreType

	      
WithStub(StaticCoreType)
........................
Static core is wrapped in With_stub which has stub function

.. py:class: WithStub(StaticCoreType)

 All constructor args/kwargs are passed on to StaticCore.
 The is where theme sty (via stytags_getter_func) is conc with twsty_tags and
 applied to static code.

.. code-block:: python
		  
     stytags = stytags_getter_func()
     twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
     super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

WithStub.stub
.............

The stub is called by ofjustpy when rendering the components and registering them with tracker

.. py:function: def stub(self)
         		   
stub function calls another `gen_stub` which generates the Stub.
gen_stub is tracked also tracked by the tracker.


.. code-block:: python
		
   @trackStub
   def gen_stub(target, **kwargs):
   
       target.request_callback(kwargs.get("session_manager"))
       return Stub(target=target, **kwargs)

- `request_callback` is a post-processor. Is called after staticCore has been initialized for a
  request object. Used for decoding url from an endpoint. 
  For passive/active components: mutable shell is same as static-core.

  
The Stub  class
................

The Stub class created by the `gen_stub` func has couple of roles
depending on Stub type

- publishes key, id property from staticCore
- tells if its a static component
- has `__call__` functor interface

  

The __call__ functor
....................
The functions
- attaches to parent if not already attached
- register_childerns : if not already registered
- build_json if not already build

where register_childs implies calling
- c.stub() : this will call the stub_gen and produce a stub
- stub(self): this will create the component and attach to parent


.. :py:function:: __call(self, a, attach_to_parent=True)

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
		


  
High level overview:
++++++++++++++++++++

There are two phases
- Declaration phase
- DOM Generation phase

Declaration phase
.................

In declaration phase, for each component div we declare its child.

DOM Generation phase
....................
Starting from root which is WebPage class
at initialization register-the-childs, which implies calling the
.. code-block:: python

   c_ = c.stub()
   c_(self)
   # add to spathMpa

.. note::
   Now when c.stub() is called for passive it directly returns the dummy stub,
   for active/mutual it call the `stub_gen` func is getting tracked.
   The c_(self) invokes the __call__ interface of the stub.
   This is where the recursive magic happens.
   Each div calls add_register_components:
   which call stub and __call__ for each of the child. This unravles deep nesting.
   For the call build_json is called to build json based upon the child's json.

   

- 

  
  
  
  
    

WebPage Type
+++++++++++++
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



Mutable Div Type Factory
+++++++++++++++++++++++++

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
 
