
Building block mixins
^^^^^^^^^^^^^^^^^^^^^

StaticCore
**********

jpBaseComponentMixin
'''''''''''''''''''''
The `jpBaseComponentMixin` class provides attributes related to working with the JustPy-Svelte framework.

Attributes
----------

- `show`: A Boolean attribute that controls the visibility of the component. Defaults to `True`.

- `debug`: A Boolean attribute that enables or disables debugging for the component. Defaults to `False`.

  
TwStyMixin
''''''''''
The `TwStyMixin` class defines tailwind and style attributes for HTML components.

Attributes
----------

- `style`: A property to get and set the inline style for the HTML component.
- `twsty_tags`: A list that stores tailwind CSS classes applied to the component.  


Methods
-------
- `remove_twsty_tags(*args)`: Removes specified tailwind tags from the component.
- `add_twsty_tags(*args)`: Adds tailwind tags to the component.
- `replace_twsty_tags(*args)`: Replaces the existing tailwind tags with the ones provided in `*args`.

  
DOMEdgeMixin
'''''''''''''
Attaches  itself to a parent component specified by 'a' kwargs

EventMixinBase
**************

Attributes
----------

- `event_modifiers`: A dictionary to store event modifiers.
- `transition`: Stores transition information for the component.
- `event_handlers`: A dictionary that associates event types with their corresponding event handling functions.
- `event_prehook`: A prehook function to be applied to all event handlers.
- `allowed_events`: A list of allowed event types.
  
Methods
-------

- `set_keyword_events(**kwargs)`: Sets event handlers based on keyword arguments.
- `on(event_type, func, *, debounce, throttle, immediate)`: Attaches an event handler to the component.
- `add_prehook(prehook_func)`: Applies a prehook function to all registered event handlers.
- `remove_event(event_type)`: Removes a specified event from the component.
- `has_event_function(event_type)`: Checks if an event handler function for a specific event type exists.
- `add_event(event_type)`: Adds an event type to the allowed events list.
- `get_event_handler(event_type)`: Retrieves the event handler function for a specific event type.
- `add_allowed_event(event_type)`: Adds an event type to the allowed events list.

  

EventMixin
*************

Attributes:
----------

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
***********
The `HCTextMixin` class provides a `text` attribute for HC (HTML Component) components such as buttons, spans, and labels.
Attributes
----------

- `text`: A property that represents the text content of the HTML component.


  
KeyMixin
*********

Attributes:
----------

key: str
    

JsonMixin

  PassiveJsonMixin

  HCCJsonMixin

  HCCPassiveJsonMixin


HCCMixin
  HCCMixin
  HCCPassiveMixin
  HCCActiveMixin

  
IdMixin Class
=============

The `IdMixin` class provides a mixin for handling object identifiers.

Public Attributes
-----------------

- `id`: A property that allows getting and setting the identifier for the object.





DataValidators

http_request_callback_mixin





Passive HC Type
^^^^^^^^^^^^^^^^
- StaticCore
- HCTextMixin
- KeyMixin
- PassiveJsonMixin
  
  
Active HC Type
^^^^^^^^^^^^^^^

- KeyMixin
- EventMixin
- IdMixin
- StaticCore  
- DataValidators
- http_request_callback_mixin
- HCTextMixin
- JsonMixin


Passive Div Type
^^^^^^^^^^^^^^^^^
- StaticCore
- jsonMixinType == HCCPassiveJsonMixin
- hccMixinType == HCCPassiveMixin
  

Active Div Type
^^^^^^^^^^^^^^^^
- StaticCore
- jsonMixinType == HCCJsonMixin
- hccMixinType == HCCPassiveMixin
- TR.EventMixin
- KeyMixin
- TR.IdMixin
- DataValidators
- http_request_callback_mixin

  
Building block mixins  for Mutable Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SharerMixins
*************
HCTextSharerMixin
'''''''''''''''''
text

TwStySharerMixin
'''''''''''''''''
twsty_tags

Mutable HCType

Type A:
StaticCoreMixins: TR.HCTextMixin
mutableShellMixins: TR.TwStyMixin, TR.DOMEdgeMixin, HCMutable_JsonMixin
Sharer: StaticCoreSharer_BaseMixin,
        StaticCoreSharer_IdMixin,
        StaticCoreSharer_EventMixin
	HCTextSharerMixin
	

build_renderHTML logic
''''''''''''''''''''''
within Stub_HCPassive.__call__  -- after register_childrens build_renderHtml is called
covers calls for HCPassive, DivPassive

within Stub_HCActive.__call__  -- after register_childrens build_renderHtml is called
covers calls for DivActive




renderHtml design/arch
''''''''''''''''''''''
- staticCore has prepare_htmlRender
- is called by gen_Stub_X
- provides chunk1, chunk3

- mutableShell.to_html_iter
  uses chunk1, chunk2 etc. to piece together html


DivMutable  RenderHTML_HCCMutableChildsMixin  
DivHCCMutable RenderHTML_HCCMutableChildsMixin  
DivHCCStatic  HCCMixin_StaticChilds, RenderHTML_HCCStaticChildsMixin

.HCCPassiveMixin
