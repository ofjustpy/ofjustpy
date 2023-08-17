Tailwind Styled Complex Components
----------------------------------


oj.PC.SubheadingBanner
^^^^^^^^^^^^^^^^^^^^^^

The SubheadingBanner function creates a styled banner with a subheading text. 
Usage


.. code-block:: python

    subheading_banner_instance_ = oj.PC.SubheadingBanner('Heading Text', twsty_tags=[])

Parameters
..........

- **heading_text**: A string representing the text to be displayed as the subheading. This parameter is required.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **heading_text_sty**: A list of Tailwind CSS classes to apply to the heading text. This parameter is optional and defaults to sty.subheading_text.

- **kwargs**: Additional keyword arguments.

Example
.......

.. code-block:: python

    subheading_banner_instance = SubheadingBanner('Heading Text', twsty_tags=[bg/blue/5], heading_text_sty=[fc/gray/1])

This example demonstrates how to create a SubheadingBanner component with a specified key and heading text. The optional twsty_tags parameter is used to apply additional Tailwind CSS classes to style the banner with a blue background and white text.


oj.PC.Subsection
^^^^^^^^^^^^^^^^

The Subsection function creates a subsection component that consists of a heading and content. It utilizes StackV to vertically stack the heading and content, creating a visually appealing subsection.

Usage
.....

.. code-block:: python

    subsection_instance = oj.PC.Subsection('Sample Heading', content_function)

Parameters
..........

- **heading_text**: A string representing the text of the subsection heading. This parameter is required.

- **content_**: A callable function that generates the content to be displayed in the subsection. This parameter is required.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **kwargs**: Additional keyword arguments.


  


oj.PC.Title
^^^^^^^^^^^^

The Title function creates a styled component that displays a title text. It takes a key and a title text as inputs, and displays the title text with the specified alignment.

Usage
.....

.. code-block:: python

    title_instance_ = oj.PC.Title_('My Title', align='end')

Parameters
..........


- **title_text**: A string representing the title text to be displayed. This parameter is required.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **align**: A string specifying the alignment of the title text. Default is set to "center".

- **kwargs**: Additional keyword arguments.




Tailwind Styled Input Components
--------------------------------

TextInput
^^^^^^^^^^
The TextInput function creates a styled input element.

Usage
.....

.. code-block:: python

    labeled_input = TextInput(key='input_key', placeholder="Enter text", on_change=on_input_change)

Parameters
..........

- **key**: A string representing the key for the component instance. This parameter is required.

- **placeholder**: A string representing the placeholder text for the input element. This parameter is required.

- **data_validators**: A list of data validator functions to be applied to the input element. Default is an empty list.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **kwargs**: Additional keyword arguments.


oj.AC.CheckboxInput
^^^^^^^^^^^^^^^^^^^^

The CheckboxInput function creates a styled checkbox input element.

Usage
.....

.. code-block:: python

    checkbox_instance = CheckboxInput(key='checkbox_key', checked=True)

Parameters
..........

- **key**: A string representing the key for the component instance. This parameter is required.


- **checked**: A boolean value indicating whether the checkbox should be initially checked. Default is False.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **kwargs**: Additional keyword arguments.





Complex Mutable Components 
--------------------------

oj.Mutable.StackD
^^^^^^^^^^^^^^^^^

StackD is a dynamic component representing a "Deck" of cards, where each card is a child element. It allows for switching between the child elements, displaying only one at a time.

Usage
......

.. code-block:: python

    stackd_instance = oj.Mutable.StackD(key="my_stackd", child=[Component1, Component2, Component3], height_anchor_key = "component1")

Methods
.......

- **addItems(cgens)**: Adds child elements to the StackD component. The first child element is set as the initially visible card.

- **bring_to_front(id)**: Brings the card with the specified `id` to the front, making it visible and hiding the previous visible card.

Example
.......

.. code-block:: python

    stackd_instance = StackD(childs=[btn1, btn2, btn3])
    stackd_instance.bring_to_front('text_key')





oj.Mutable.Slider
^^^^^^^^^^^^^^^^^

The Slider function creates a custom slider component that displays a set of clickable circles based on the provided itemiter list. It takes a key and a list of items as input, displaying the items as circles within the slider. When a circle is clicked, its outline is updated, and an on-click event is triggered.

Usage
.....

.. code-block:: python

    slider_instance = oj.Mutable.Slider(key='slider_key', num_iter=range(4,12))

Parameters
..........

- **key**: A string representing the key for the component instance. This parameter is required.

- **itemiter**: A list of items to be displayed as clickable circles in the slider. This parameter is required.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **kwargs**: Additional keyword arguments.

Example
.......

.. code-block:: python

    slider_instance = oj.Mutable.Slider(key='slider_key', num_iter= [1, 2, 3], twsty_tags=['bg-gray-200'])

This example demonstrates how to create a Slider component with a specified key and a list of items. The optional twsty_tags parameter is used to apply additional Tailwind CSS classes to style the slider with a gray background.

Note: In the current implementation, the slider component is a custom component and not a built-in HTML slider input element.


oj.Mutable.ColorSelector
^^^^^^^^^^^^^^^^^^^^^^^^

The ColorSelector function creates a custom color selector component that combines a main color selector and a shades slider. It allows users to pick a color and its shade, then triggers an on-click event with the chosen color.

Usage
......

.. code-block:: python

    def on_cs_click(dbref, msg, to_target):
        print ("color selector  changed : ", msg.value)
	
    color_selector_instance = ColorSelector(key='color_selector_key', on_click=on_cs_click)

Parameters
..........

- **key**: A string representing the key for the component instance. This parameter is required.

- **twsty_tags**: A list of Tailwind CSS classes to apply to the component. This parameter is optional.

- **kwargs**: Additional keyword arguments.

Example
^^^^^^^

.. code-block:: python

    color_selector_instance_ = ColorSelector_('color_selector_key', twsty_tags=['bg-gray-200'], on_click=on_cs_click)

This example demonstrates how to create a ColorSelector component with a specified key. The optional twsty_tags parameter is used to apply additional Tailwind CSS classes to style the color selector with a gray background.

Functionality
.............


When the user selects a main color, the shades slider is updated to display shades of the chosen color. If the user clicks on a shade, the component passes the selected color in hexadecimal format to the parent component via an on-click event.

Note: In the current implementation, the ColorSelector component is a custom component and not a built-in HTML color input element.



