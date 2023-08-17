Passive and Active Html Components Types
----------------------------------------


Passive Components
^^^^^^^^^^^^^^^^^^

.. py:class:: oj.PC.Label
	      
  Inherits :class:`PassiveHCComponent`
  
  :param for_: The 'for' attribute of the <label> element specifies the id of the form control with which the label is associated. The value is the id of a form control element.
  :type for_: str or None, optional

  :param form: The 'form' attribute of the <label> element specifies the id of the form to which the label belongs. The value is the id of a <form> element.
  :type form: str or None, optional
	      
.. py:class:: oj.PC.Span

   Inherits :class:`PassiveHCComponent`


.. py:class:: oj.PC.Code

   Inherits :class:`PassiveHCComponent`

   The `Code` class represents the HTML <code> element, which is used to display inline code.

.. py:class:: oj.PC.Pre

   Inherits :class:`PassiveHCComponent`

   The `Pre` class represents the HTML <pre> element, which is used to display preformatted text.

.. py:class:: oj.PC.Li

   Inherits :class:`PassiveHCComponent`

   The `Li` class represents the HTML <li> element, which is used to define list items within a list.

.. py:class:: oj.PC.P

   Inherits :class:`PassiveHCComponent`

   The `P` class represents the HTML <p> element, which is used to define paragraphs.

.. py:class:: oj.PC.Prose

   Inherits :class:`PassiveHCComponent`

   The `Prose` class represents a block-level component for displaying prose content.

.. py:class:: oj.PC.Option

   Inherits :class:`PassiveHCComponent`


.. py:class:: oj.PC.Hr

   Inherits :class:`PassiveHCComponent`
   The `Hr` class represents the HTML <hr> element, which is used to create a thematic break or horizontal rule in a document.

.. py:class:: oj.PC.Img

   Inherits :class:`PassiveHCComponent`

   
.. py:class:: oj.PC.H1

   Inherits :class:`PassiveHCComponent`

Passive Div Components
^^^^^^^^^^^^^^^^^^^^^^

.. py:class:: oj.PC.Div
	      
   Inherits :class:`PassiveDivComponent`	      

.. py:class:: oj.PC.CodeDiv

   Inherits :class:`PassiveDivComponent`

   The `CodeDiv` class represents a container used for displaying code blocks or code-related content. It provides styling and structure suitable for code presentation.

.. py:class:: oj.PC.PreDiv

   Inherits :class:`PassiveDivComponent`

   The `PreDiv` class represents a container for preformatted text, often used for code snippets or other text where spacing and line breaks should be preserved.

.. py:class:: oj.PC.Collapsible

   Inherits :class:`PassiveDivComponent`

   The `Collapsible` class represents a collapsible container that can expand and collapse to show or hide its content. It is often used for creating expandable sections or content.

   :param hide_banner_text: The text displayed when the content is hidden. It informs the user to click the button to expand.
   :param hide_banner_classes: CSS classes for styling the banner when the content is hidden.
   :param toggler_classes: CSS classes for styling the button that toggles the collapsible content.
			  
.. py:class:: oj.PC.Nav

   Inherits :class:`PassiveDivComponent`

   The `Nav` class represents a navigation container, often used for creating menus, navigation bars, or links to different parts of a website.

.. py:class:: oj.PC.Footer

   Inherits :class:`PassiveDivComponent`

   The `Footer` class represents the HTML <footer> element, which is used to define a footer section at the bottom of a document or a webpage. It typically contains copyright information, contact details, and other footer content.



   
Active HC Components
^^^^^^^^^^^^^^^^^^^^^

.. py:class:: oj.AC.Span
	      
  Inherits :class:`ActiveHCComponent`

  
.. py:class:: oj.AC.Button

   Inherits :class:`ActiveHCComponent`

   The `Button` class represents an HTML <button> element, which is used to create interactive buttons for user interaction.


   :ivar autofocus: Specifies whether the button should automatically get focus when the page loads. Possible values: True or False.
   :ivar disabled: Specifies whether the button should be disabled or not. Possible values: True or False.
   :ivar form: Specifies the form the button belongs to.
   :ivar formaction: Specifies the URL of the file that will process the input control when the form is submitted.
   :ivar formenctype: Specifies how the form-data should be encoded when submitting it to the server. Possible values: "application/x-www-form-urlencoded", "multipart/form-data", or "text/plain".
   :ivar formmethod: Specifies the HTTP method to use when sending form-data. Possible values: "GET" or "POST".
   :ivar formnovalidate: Specifies that the form-data should not be validated on submission. Possible values: True or False.
   :ivar formtarget: Specifies where to display the response received after submitting the form. Possible values: "_blank", "_self", "_parent", "_top", or a custom target name.


.. py:class:: oj.AC.TextInput

   Inherits :class:`ActiveHCComponent`

   :ivar type: The type attribute associated with the element (always "text").
   :ivar autocomplete: Specifies whether the browser should enable autocomplete for the input field.
   :ivar maxlength: Specifies the maximum number of characters allowed in the input field.
   :ivar minlength: Specifies the minimum number of characters required in the input field.
   :ivar pattern: Specifies a regular expression pattern that the input's value must match to be valid.
   :ivar placeholder: Provides a short hint that describes the expected value of the input field.
   :ivar size: Specifies the visible width of the input field.


.. py:class:: oj.AC.Img

   Inherits :class:`ActiveHCComponent`

   The `Img` class represents the HTML <img> element, used to display images in a document.

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

 
.. py:class:: oj.AC.CheckboxInput

   Inherits :class:`ActiveHCComponent`

   The `CheckboxInput` class represents an HTML <input> element with a checkbox, allowing users to select or deselect an option.

  :ivar checked: Specifies whether the checkbox is initially checked (True) or unchecked (False). The value is a boolean.
		 
.. py:class:: oj.AC.Textarea

   Inherits :class:`ActiveHCComponent`

   The `Textarea` class represents an HTML <textarea> element, which provides a multiline text input area for users.

   :ivar cols: Specifies the visible width of the textarea in average character widths. Must be a positive integer.
   :ivar rows: Specifies the visible number of lines in the textarea. Must be a positive integer.
   :ivar wrap: Specifies how the text in the textarea is to be wrapped when submitted in a form. Possible values are "soft" (text wrapped for appearance only) and "hard" (text wrapped for both appearance and submitted text).
   :ivar placeholder: Provides a short hint that describes the expected value of the textarea.

 
.. py:class:: oj.AC.Div

   Inherits :class:`ActiveHCComponent`

   The `Div` class represents the HTML <div> element, used for structuring and styling content within a document.

.. py:class:: oj.AC.StackH

   Inherits :class:`ActiveHCComponent`

   The `StackH` class represents a horizontal stack container for aligning and arranging elements horizontally within a container.

.. py:class:: oj.AC.Select

   Inherits :class:`ActiveHCComponent`

   The `Select` class represents an HTML <select> element, used to create dropdown lists for user selection.

   :ivar autofocus: Specifies whether the select element should automatically get focus when the page loads. Possible values: True or False.
   :ivar default: Specifies the default value for the select element.
   :ivar disabled: Specifies whether the select element should be disabled or not. Possible values: True or False.
   :ivar form: Specifies the form to which the select element belongs (form's id).
   :ivar multiple: Specifies that multiple options can be selected at once. If present, the attribute does not need a value.
   :ivar name: Specifies the name for the select element.
   :ivar required: Specifies whether the select element is required to have a value selected. Possible values: True or False.
   :ivar size: Specifies the number of visible options in the dropdown list.
	       
.. py:class:: oj.AC.Form

   Inherits :class:`ActiveHCComponent`

   The `Form` class represents an HTML <form> element, which is used to create user input forms for submitting data.

   :ivar accept_charset: Specifies the character encodings to be used for form submission. A space-separated list of character encoding names (e.g., "UTF-8 ISO-8859-1").
   :ivar action: Specifies the URL where form data should be submitted when the form is submitted. It can be an absolute or relative URL.
   :ivar autocomplete: Specifies whether the browser should enable autocomplete for the entire form. Values: 'on' or 'off'.
   :ivar enctype: Specifies how the form data should be encoded when submitted to the server. Possible values are 'application/x-www-form-urlencoded' (default), 'multipart/form-data' (required for file uploads), or 'text/plain'.
   :ivar method: Specifies the HTTP method to use when submitting the form data. Possible values: 'get' (default) or 'post'.
   :ivar name: Specifies a name for the form, which can be used for scripting purposes, such as referencing the form from JavaScript.
   :ivar novalidate: A boolean attribute. When present, it specifies that the form should not be validated when submitted.
   :ivar target: Specifies where the response received after submitting the form should be displayed. Possible values include '_blank' (new window or tab), '_self' (same frame), '_parent' (parent frame), '_top' (full window body), or a named frame.

		 
.. py:class:: oj.AC.A

   Inherits :class:`ActiveHCComponent`

   The `A` class represents an HTML <a> (anchor) element, used for creating hyperlinks within a document.

   :ivar href: Specifies the URL to which the hyperlink points.
   :ivar title: Specifies the title of the linked document.
   :ivar rel: Specifies the relationship between the current document and the linked document.
   :ivar download: Specifies that the target will be downloaded when the link is clicked.
   :ivar target: Specifies where to open the linked document. Values can include '_blank', '_self', '_parent', '_top', or a named frame.
   :ivar scroll: Specifies whether scrolling is enabled when the hyperlink is clicked (True or False).
   :ivar scroll_option: Specifies the type of scrolling when the hyperlink is clicked. Values can be "auto" or "smooth" (default is "smooth").
   :ivar block_option: Specifies the vertical alignment of the target element when scrolling. Values can be "start", "center", "end", or "nearest" (default is "start").
   :ivar inline_option: Specifies the horizontal alignment of the target element when scrolling. Values can be "start", "center", "end", or "nearest" (default is "nearest").

			
.. py:class:: oj.AC.Switch

   Inherits :class:`ActiveHCComponent`

   The `Switch` class represents a switch component, often used for on/off or toggle functionality within a user interface.
  
