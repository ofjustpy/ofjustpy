HTMLComponent Abstract Base Types
---------------------------------

.. py:class:: BaseComponent

    :param show: A Boolean attribute that controls the visibility of the component.
    :type show: bool
    :default show: True

    :param debug: A Boolean attribute that enables or disables debugging for the component.
    :type debug: bool
    :default debug: False

    :param twsty_tags: is a list of tailwind tags (see py_tailwind_utils)
    :type twsty_tags: list, optional
    :default twsty_tags: []
    
    :param style: A property to get and set the inline style for the HTML component.
    :ivar style: A property to get and set the inline style for the HTML component.
    :type style: str

    :ivar classes: A list that stores Tailwind CSS classes applied to the component.
    :type classes: list

    :param key: A key to be associated with the component.
    :ivar key: A key to be associated with the component.
    :type key: str, optional


    .. method:: remove_twsty_tags(*args)

      Removes specified Tailwind tags from the component.

      :param `*args`: A variable number of arguments representing the specified Tailwind tags to remove.
      :type `*args`: str

    .. method:: add_twsty_tags(*args)

      Adds Tailwind tags to the component.

      :param `*args`: A variable number of arguments representing the specified Tailwind tags to add.
      :type `*args`: str

    .. method:: replace_twsty_tags(*args)

      Replaces the existing Tailwind tags with the ones provided in `*args`.

      :param `*args`: A variable number of arguments representing the specified Tailwind tags to replace.
      :type `*args`: str

		   


		 
.. py:class:: PassiveHCComponent
	      
    Inherits :class:`BaseComponent`
    
    :ivar text: The text 
    :param text: The text content to be displayed within the component.
    :type text: str, optional
		

.. py:class:: PassiveDivComponent

    Inherits :class:`BaseComponent`
	      
    :param childs: A list of child components to be associated with the parent.
    :type childs: list

    :ivar components: The list of child components associated with the parent.
			  


.. py:class:: ActiveBaseComponent

   Inherits :class:`BaseComponent`	      
	      
   :param event_prehook: A prehook function to be applied to all event handlers.
   :type event_prehook: Callable, optional

   :param on_click: handler for click event
   :type event_modifiers: Callable, optional

   :param on_mouseover: handler for mouseover event
   :type event_modifiers: Callable, optional

   :param on_mouseout: handler for mouseout event
   :type event_modifiers: Callable, optional

   :param on_mouseenter: handler for mouseenter event
   :type event_modifiers: Callable, optional

   :param on_mouseleave: handler for mouseleave event
   :type event_modifiers: Callable, optional

   :param on_input: handler for input event
   :type event_modifiers: Callable, optional

   :param on_change: handler for change event
   :type event_modifiers: Callable, optional

   :param on_after: handler for after event
   :type event_modifiers: Callable, optional

   :param on_before: handler for before event
   :type event_modifiers: Callable, optional

   :param on_keydown: handler for keydown event
   :type event_modifiers: Callable, optional

   :param on_keyup: handler for keyup event
   :type event_modifiers: Callable, optional

   :param on_keypress: handler for keypress event
   :type event_modifiers: Callable, optional

   :param on_focus: handler for focus event
   :type event_modifiers: Callable, optional

   :param on_blur: handler for blur event
   :type event_modifiers: Callable, optional

   :param on_submit: handler for submit event
   :type event_modifiers: Callable, optional

   :param on_dragstart: handler for dragstart event
   :type event_modifiers: Callable, optional

   :param on_dragover: handler for dragover event
   :type event_modifiers: Callable, optional

   :param on_drop: handler for drop event
   :type event_modifiers: Callable, optional

   :param on_click__out: handler for click__out event
   :type event_modifiers: Callable, optional
			  


.. py:class:: ActiveHCComponent
	      
   Inherits :class:`ActiveBaseComponent`
   
   :ivar text: The text 
   :param text: The text content to be displayed within the component.
   :type text: str, optional


.. py:class:: ActiveDivComponent
	      
   Inherits :class:`ActiveBaseComponent`

   :param childs: A list of child components to be associated with the parent.
   :type childs: list

   :ivar components: The list of child components associated with the parent.



	      

   
