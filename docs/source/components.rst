Components
~~~~~~~~~~

Ofjustpy provides all the usual elementary html components that serve as building block
for a webpage.

.. important::

   Checkout the super cool and ultra useful visual style editor for Ofjustpy webpages.
   Essentially, script the webpage in Python, edit the styling/look-and-fell visually.


.. important::

   Ofjustpy has two very cool components: a simple to use, program, and customize  Hierarchy Navigator and desktop style Dockbar to minimize components and put it on bar.

.. important::

   HyperUI is a clean, fast, asthetically pleasing  UI component library written with tailwind utility classes. Ofjustpy provides HyperUI components as first class components that can incorporated with other components and manipulated using the same API's. 


Pre-styled vs. customizable components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Although, Ofjustpy provides tools to work with tailwind utility classes,
components in Ofjustpy, by default, are un-styled, i.e,  there is no
tailwind styling hard-wired to them. 

Falling short of providing full-fledge pre-styled component library, Ofjustpy
provides several assets and utilities to help with layout and styling of components
and webpages.


#. Ofjustpy provide useful passive container and composite components, that help quickly put together a complex UI-rich page quickly. For e.g.:
   
   a. Title
   b. SubheadingBanner
   c. Section
   d. StackH, StackG, StackV (to layout components in horizontal, vertical, and or grid)
      
#. Advanced un-styled responsive components such as:

   a. StackD: StackD is a dynamic component representing a "Deck" of cards, where each card is a child element. It allows for switching between the child elements, displaying only one at a time.
   b. Slider: The Slider function creates a custom slider component that displays a set of clickable circles based on the provided itemiter list. It takes a key and a list of items as input, displaying the items as circles within the slider. When a circle is clicked, its outline is updated, and an on-click event is triggered.

   c. ColorSelector: For demonstration of mutable/responsive behaviour purposes only. The ColorSelector function creates a custom color selector component that combines a main color selector and a shades slider. It allows users to pick a color and its shade, then triggers an on-click event with the chosen color.

   d. Pagination: Break a large collection of display elements across a collection of pages. Check out the demo and usage at [demo_paginate](demos/demo_paginate.py).

   e. Dockbar: Plug in this component to have a bar on your page to minimize page components. See the demo/example code at [demo_dock_undock](demos/demo_dock_undock.py) for usage.
      
   f. A simple component to display a Python enum type as a select HTML component.

   e. HierarchyNavigator: Display a nested [dict/addict/addict-tracking-changes](https://github.com/ofjustpy/addict-tracking-changes) dictionary as hierarchical navigation. Check out the demo/example code at [demo_hinav](demos/demo_hierarchy_navigation_using_italian_cuisine.py).
      
      

We have also made available wide collection of HyperUI components via Ofjustpy. Because
they are pure tailwind based components, they can be incorporated and manipulated alongwith
the native components using the same Ofjustpy constructs. Especially, useful are the TextInput,
Select, Tabs, etc.

As mentioned before, Ofjustpy provides customizable elementry and composite components. If you would like more off-the-shelf pre-fabricated and opinionated components consider Justpy (with Quasar plugin) or NiceGUI.

Using elementary components
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ofjustpy broadly provides two components: static and mutable. Static components do not change their look/content, which mutable components are allowed to change the text or the style or both.

Here we will discuss static components usage. See mutable for discussion on mutable components.
Static components itself are exists in one of two types: passive and active. Passive components
are anonymous (i.e., they don't have an id) do not respond to events, which active components
have an identifier and have event handlers associated with them.


Every html tag type (span, button, etc.) is represented through a mixin class. Below is the list of all the tag mixins currently support. Each mixin takes keyword args that is applicable to that particular tag type. For e.g. `placeholder` is applicable to `input` html entity, while `autocomplete` is applicable to `form` html entity. See `HC_type_mixins_extn` for all the mixins
currently supported in Ofjustpy.



Using Passive Components
++++++++++++++++++++++++
Passive Components are declared within `oj.PD` namespace.

.. TODO:
   List out all the common arguments
   
.. code-block::

   hello = oj.PD.Span(text="Hello", classes="bg-green-100")
   world = oj.PD.Span(text="World", classes="bg-blue-100")
   oj.PD.StackH(childs = [hello, world], classes="space-x-2 m-4")

List of all passive components:

#. oj.AD.Label 
#. oj.AD.Span 
#. oj.AD.Strong 
#. oj.AD.Code 
#. oj.AD.Pre 
#. oj.AD.Li 
#. oj.AD.P 
#. oj.AD.Prose 
#. oj.AD.Option 
#. oj.AD.Hr 
#. oj.AD.Time 
#. oj.AD.Img 
#. oj.AD.H1 
#. oj.AD.H1Div 
#. oj.AD.H2Div 
#. oj.AD.ScriptDiv 
#. oj.AD.BlockquoteDiv 
#. oj.AD.H2 
#. oj.AD.H3 
#. oj.AD.H3Div 
#. oj.AD.H4 
#. oj.AD.H5 
#. oj.AD.H6 
#. oj.AD.A 
#. oj.AD.Legend 
#. oj.AD.Small 
#. oj.AD.Div 
#. oj.AD.Container 
#. oj.AD.LabelDiv 
#. oj.AD.SpanDiv 
#. oj.AD.PDiv 
#. oj.AD.StackV 
#. oj.AD.StackH 
#. oj.AD.StackW 
#. oj.AD.Ul 
#. oj.AD.Ol 
#. oj.AD.Li 
#. oj.AD.Dl 
#. oj.AD.Ul 
#. oj.AD.Optgroup 
#. oj.AD.Details 
#. oj.AD.Summary 
#. oj.AD.Datalist 
#. oj.AD.Dt 
#. oj.AD.DtDiv 
#. oj.AD.DdDiv 
#. oj.AD.Dd 
#. oj.AD.CodeDiv 
#. oj.AD.PreDiv 
#. oj.AD.Collapsible 
#. oj.AD.Nav 
#. oj.AD.Section 
#. oj.AD.Footer 
#. oj.AD.Header 
#. oj.AD.Aside 
#. oj.AD.Article 
#. oj.AD.Main 
#. oj.AD.Fieldset 
#. oj.AD.Tr 
#. oj.AD.Table 
#. oj.AD.Thead 
#. oj.AD.Td 
#. oj.AD.Th 
#. oj.AD.Address 
#. oj.AD.Tbody 
#. oj.AD.Img 
#. oj.AD.Legend 
#. oj.AD.Small 
#. oj.AD.Th 
#. oj.AD.Td
   

Using Active Component
++++++++++++++++++++++

Active components are defined in `oj.AD` name space. They have additional `key` argument.

.. TODO

   See event handlers for associating event handling
   


.. code-block:: python

   def on_input_change(dbref, msg, to_ms):
       pass
       
   labeled_input = oj.AD.TextInput(key='input_key', placeholder="Enter text", on_change=on_input_change)

   
List of all active components:

#. oj.AD.Select
   
#. oj.AD.A
	      
#. oj.AD.Button
#. oj.AD.TextInput
#. oj.AD.Textarea
#. oj.AD.Form
#. oj.AD.Div
#. oj.AD.StackH
#. oj.AD.Switch
#. oj.AD.Datalist
#. oj.AD.CheckboxInput
#. oj.AD.Img

Event handling
##############

Event handlers are functions that take 3 arguments.



Component Specific argument
+++++++++++++++++++++++++++
Components have their own specific attribute keyword arguments.

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

   :ivar for_: The 'for' attribute of the <label> element specifies the id of the form control with which the label is associated. The value is the id of a form control element.

  :ivar form: The 'form' attribute of the <label> element specifies the id of the form to which the label belongs. The value is the id of a <form> element.

#. Optgroup
   
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Composite components are those that are dervied
by putting together simpler components together.

.. note::

   Ofjustpy, as of now,  is primarly focussed on how the structural/programatics
   aspects and not so much on the styling.
   The styling of the these components is not at par with other popular ui-library.
   However, the components are easy to customize using tailwind utility classes.
   See HyperUI for inspirations on how configure the styling for a more publishibale
   looks.
   
   We also recommend to try out our visual editor to style the composite components
   to your liking.

   If you want prefabricated/opiniated off-the-shelf component consider checking out
   Justpy (with Quasar UI library) or NiceGUI.

SubheadingBanner
++++++++++++++++
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
+++++++++++++++++++

Usage same as `SubheadingBanner`.


Subsection
++++++++++

Subsection
++++++++++

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
+++++++++++++

Same as Subsection

Title
+++++

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
++++++

.. py:class:: StackG(*args, **kwargs)

   A class representing a grid with customizable styling.

   :param num_rows: An integer representing the number of rows in the stack grid (default is 2).
   :param num_cols: An integer representing the number of columns in the stack grid (default is 2).
   :param twsty_tags: A list of Tailwind CSS classes to apply to the stack. This parameter is optional.
   :param kwargs: Additional keyword arguments that can be passed to the parent class constructor.

TitledPara
++++++++++

.. py:function:: TitledPara(heading_text, content, twsty_tags=[], fix_sty_section_nesting=False, **kwargs)

   Display a titled paragraph with customizable styling.

   :param heading_text: A string representing the text to be displayed as the title of the paragraph. This parameter is required.
   :param content: The content of the paragraph. This can be a string or an object with a compatible representation.
   :param twsty_tags: A list of Tailwind CSS classes to apply to the titled paragraph. This parameter is optional.
   :param fix_sty_section_nesting: A boolean indicating whether to adjust styling for nested sections. If True, the content is displayed across the entire width with added margin to give the effect of being nested within the title. Default is False.
   :param kwargs: Additional keyword arguments that can be passed to the function.


.. note::

   See Mutable Pages section for responsive components
   
