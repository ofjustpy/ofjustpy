Component Type Mixins
'''''''''''''''''''''
The mixins that are glued to make different types of htmlcomponents, Passive, Active, Mutable, HCCMutable,
HCCStatic.

Foundational Mixins
+++++++++++++++++++

StaticCore
::::::::::

jpBaseComponentMixin
::::::::::::::::::::

The `jpBaseComponentMixin` class provides attributes related to working with the JustPy-Svelte framework.

Attributes
..........

- `show`: A Boolean attribute that controls the visibility of the component. Defaults to `True`.

- `debug`: A Boolean attribute that enables or disables debugging for the component. Defaults to `False`.

.. 
   :TODO:
   some pytest on these attributes would be good


TwStyMixin
::::::::::
  
The `TwStyMixin` class defines tailwind and style attributes for HTML components.

Attributes
..........

- `style`: A property to get and set the inline style for the HTML component.
- `twsty_tags`: A list that stores tailwind CSS classes applied to the component.  


Methods
.......
- `remove_twsty_tags(*args)`: Removes specified tailwind tags from the component.
- `add_twsty_tags(*args)`: Adds tailwind tags to the component.
- `replace_twsty_tags(*args)`: Replaces the existing tailwind tags with the ones provided in `*args`.
   
   
.. 
   :TODO:
   some pytest on these attributes would be good

   
DOMEdgeMixin
::::::::::::
Attaches  itself to a parent component specified by 'a' kwargs

EventMixinBase
::::::::::::::


Attributes
...........

- `event_modifiers`: A dictionary to store event modifiers.
- `transition`: Stores transition information for the component.
- `event_handlers`: A dictionary that associates event types with their corresponding event handling functions.
- `event_prehook`: A prehook function to be applied to all event handlers.
- `allowed_events`: A list of allowed event types.
  
Methods
.......

- `set_keyword_events(**kwargs)`: Sets event handlers based on keyword arguments.
- `on(event_type, func, *, debounce, throttle, immediate)`: Attaches an event handler to the component.
- `add_prehook(prehook_func)`: Applies a prehook function to all registered event handlers.
- `remove_event(event_type)`: Removes a specified event from the component.
- `has_event_function(event_type)`: Checks if an event handler function for a specific event type exists.
- `add_event(event_type)`: Adds an event type to the allowed events list.
- `get_event_handler(event_type)`: Retrieves the event handler function for a specific event type.
- `add_allowed_event(event_type)`: Adds an event type to the allowed events list.


EventMixin
::::::::::

Attributes:
...........

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

.. 
   :TODO:
   some pytest on these attributes would be good

HCTextMixin
:::::::::::

The `HCTextMixin` class provides a `text` attribute for HC (HTML Component) components such as buttons, spans, and labels.

Attributes
..........
- `text`: A property that represents the text content of the HTML component.

  
Mixins for Json
+++++++++++++++

#. StaticCore_JsonMixin
#. JsonMixin_Base
#. MutableShell_JsonMixin
#. HCMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
#. HCCStatic_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)
#. HCCMutable_JsonMixin(JsonMixin_Base)
#. DivMutable_JsonMixin(MutableShell_JsonMixin, JsonMixin_Base)

..
  TODO
  some pytest would be nice

Mixins for Child components
+++++++++++++++++++++++++++
#. CoreChildMixin
#. HCCMixin_StaticChilds
#. HCCMixin_MutableChilds
#. HCCStaticMixin, HCCPassiveMixin, HCCActiveMixin (they are all the same)


Mixins for Server Side HTML rendering
+++++++++++++++++++++++++++++++++++++

Sharer mixins
+++++++++++++

- HCTextSharerMixin
- TwStySharerMixin  

  
   
WebPageMixin
++++++++++++

#. get_changed_diff_patch

   
