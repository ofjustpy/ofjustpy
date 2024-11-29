Class Mixin Composition
'''''''''''''''''''''''
WebPageType
+++++++++++
Takes a bunch of mixins and emits a WebPage type object.

Mutable Shell Mixins
::::::::::::::::::::
- StaticCoreSharerMixin
- EventMixin
- WebPageMixin
- HCCMutable_Mixin
- StaticCoreSharerMixin  
  
StaticCoreBaseMixin  
:::::::::::::::::::
- TR.IdMixin,
- TR.TwStyMixin,
- TR.jpBaseComponentMixin,
- EventMixin,
- HCCMutableCore


Passive HC Type
+++++++++++++++

- StaticCore
- HCTextMixin
- KeyMixin
- PassiveJsonMixin

Active HC Type
++++++++++++++
- KeyMixin
- EventMixin
- IdMixin
- StaticCore  
- DataValidators
- http_request_callback_mixin
- HCTextMixin
- JsonMixin


Passive Div Type
++++++++++++++++
- StaticCore
- jsonMixinType == HCCPassiveJsonMixin
- hccMixinType == HCCPassiveMixin

Active Div Type
+++++++++++++++
- StaticCore
- jsonMixinType == HCCJsonMixin
- hccMixinType == HCCPassiveMixin
- TR.EventMixin
- KeyMixin
- TR.IdMixin
- DataValidators
- http_request_callback_mixin

Mutable HC Type
+++++++++++++++
#. StaticCoreMixins: TR.HCTextMixin
#. mutableShellMixins: TR.TwStyMixin, TR.DOMEdgeMixin, HCMutable_JsonMixin
#. Sharer: StaticCoreSharer_BaseMixin, StaticCoreSharer_IdMixin, StaticCoreSharer_EventMixin, HCTextSharerMixin


HCCMutable
++++++++++

Core mixins:
::::::::::::
#. TR.jpBaseComponentMixin,
#. TR.TwStyMixin,
#. TR.PassiveKeyMixin,
#. StaticCore_JsonMixin,
#. hctag_mixin,
#. Prepare_HtmlRenderMixin
#. CoreChildMixin

Shell mixins:
:::::::::::::
#. HCCMixin_MutableChilds
#. RenderHTML_HCCMutableChildsMixin

  

Surface level classes
'''''''''''''''''''''

Mutable Shell
+++++++++++++

Attributes
::::::::::

- staticCore
- classes
- id
- html_tag
- key
- value

  
Methods
:::::::

- get_event_handler
- get_domDict_json
- get_attrs_json
- get_event_handler  

Internal Methods
::::::::::::::::
  
- get_obj_prop_json
- add_register_childs
- components
  
..

  TODO: pytest would be nice
  
WebPage
+++++++
- post_init
  This is called after the webpage object is initialized. Note that this is not
  the same as page_ready which is called after the page has been rendered on the screen.

- update

.. TODO:
   pytest would be nice

ResponsiveStatic_SSR_WebPage
++++++++++++++++++++++++++++
ServerSide rendering
   Created by WebPage_TF::gen_WebPage_type
   
ResponsiveStatic_CSR_WebPage
++++++++++++++++++++++++++++
ClientSide rendering
Created by WebPage_TF::gen_WebPage_type
   


Working with composed components
+++++++++++++++++++++++++++++++++

Mutable.ColorSelector
:::::::::::::::::::::
- should have on_change event handler
- will hook into this event

..

  TODO: pytest would be nice
  

StaitcCore, WithStub, StubGen, Stubs
''''''''''''''''''''''''''''''''''''

.. note::
   For passive components/div no tracker is required. So stub_gen is a
   simple member function.

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

The Stub class created by the `gen_stub` func has couple of roles
depending on Stub type
- publishes key, id property from staticCore
- tells if its a static component
- has `__call__` functor interface

The __call__ functor
++++++++++++++++++++
The functions
- attaches to parent if not already attached
- register_childerns : if not already registered
- build_json if not already build

where register_childs implies calling
- c.stub() : this will call the stub_gen and produce a stub
- stub(self): this will create the component and attach to parent


.. :py:function:: __call__(self, a, attach_to_parent=True)

For static HCs
++++++++++++++
It performs
- attach_to_parent : no action
- register_childerns: no action for HCs
- build_json : already build during initialization
  
For static Divs
+++++++++++++++
- attach_to_parent : no action
- register_childerns: calls add_register_childs

    

Mutable Div
+++++++++++

This interface is invoked by Div constructor.

- for each child `c_`
  
- call `c_.stub()` this will call stub-gen which will register the stub with tracker
  
- call c_(self) : this is calling the call interface which will create the mutable component
  
- if not `c_` is not static then add to spathMaphh
     

#. all stubs call register_childs
#. HC Passive/active/mutable register_childs are noops
#. Div Passive/active stub
   #. register_childrens calls add_register_childs which invokes stub() for all its childs
#. Trackers store references to stubs
#. stub generators : are decorated with tracker hooks

The `register_childs` recursion
+++++++++++++++++++++++++++++++
.. note:: TODO: needs correction
	  
#. webpage init calls add_register_childs
#. which calls  c.stub() (as in gen_stub) for each child c.
#.  the c.__call__ (which now has the target) calls its childs and the recursion continues.

gen_stub()
++++++++++
#. tracker calls gen_stub with session_manager kwargs

is_static()
+++++++++++
is_static is used in two places

1. mutable components do not register static components in their spath
2. Same thing with WebPage.   

Design Gotcha
'''''''''''''
- For passive/active components
  add_register_childs is called by stub
  
- For mutable components add_register_childs is called by init of the mutable objects.  This is done because we want to create mapping from id to the object.

Mutable Div Type Factory
::::::::::::::::::::::::

..

  TODO: is incomplete

HCCStatic:
::::::::::

is_self_mutable=True,
is_child_mutable=False

core_mixins
 - HCCMixin_StaticChilds
 - StaticCoreSharer_HCCStaticMixin
   
shell_mixins:
 - RenderHTML_HCCStaticChildsMixin

HCCMutable:
:::::::::::

is_self_mutable=False,
is_child_mutable=True



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
