Mutable HtmlComponents 
^^^^^^^^^^^^^^^^^^^^^^
   
.. caution::

   Mutable components within the `oj.Mutable` namespace can only mutate the `classes` attribute via `twsty_tags`. If you want to create HTMLComponent types that can mutate other attributes, see the example usage in `this GitHub repository <https://github.com/ofjustpy/ofjustpy-components/blob/main/src/ofjustpy_components/hierarchy_navigator.py#L17>`_.
   


Below is an example usage for the `oj.Mutable.Button` mutable component

.. code:: python

  mybtn = oj.Mutable.Button(key="mubtn", text="", value="", twsty_tags=[bg/green/1, ...])

Let's say we want to modify the background based on some event. In the
corresponding event handler:

.. code:: python

   def on_click_handler(dbref, msg, to_mutableShell):
   """
   to_mutableShell: a function that returns the mutableShell of the static component
   """
   
   mybtn_ms = to_mutableShell(mybtn)
   mybtn_ms.add_twsty_tags(bg/green/5)

Once the above handler is invoked, the button background color will change to darker color
of green

Checkout the example code snippets in `the OfJustPy examples repository <https://github.com/ofjustpy/ofjustpy/tree/main/examples/mutable_webpages>`_.

Following mutable components are supported. Their kwargs and instance attributes are same as
their corresponding static component version.

.. py:class:: oj.Mutable.Button

.. py:class:: oj.Mutable.Circle

.. py:class:: oj.Mutable.Label

.. py:class:: oj.Mutable.Span

.. py:class:: oj.Mutable.TextInput

.. py:class:: oj.Mutable.Container

.. py:class:: oj.Mutable.Div

.. py:class:: oj.Mutable.StackH

.. py:class:: oj.Mutable.StackV

.. py:class:: oj.Mutable.StackD

.. py:class:: oj.Mutable.ColorSelector
	      
.. py:class:: oj.Mutable.Slider

.. py:class:: oj.Mutable.WebPage

.. py:class:: oj.Mutable.Form
   
HCCStatic
%%%%%%%%%%
Div class types whose css/classes is mutable but childs are static

.. py:class:: oj.HCCStatic.Div
	      
.. py:class:: oj.HCCStatic.StackV
   

HCCMutable
%%%%%%%%%%%

Div class types whose css/classes is static but childs are mutable

.. py:class:: oj.HCCMutable.Div

.. py:class:: oj.HCCMutable.StackV

.. py:class:: oj.HCCMutable.StackH

.. py:class:: oj.HCCMutable.StackW

.. py:class:: oj.HCCMutable.Container

Layout Modifiers
................

.. py:function:: Halign(content, align="center", **kwargs)

   Aligns the HTML component content horizontally.

   :param content: The HTML component to be aligned.
   :type content: Ofjustpy HTML component object 

   :param align: (optional) The horizontal alignment. Default is "center". Other options are start, end, center, between, evenly, around
   :type align: str, optional

   :param kwargs: Additional keyword arguments for styling and attributes.

   :return: An Ofjustpy HTML component with the specified horizontal alignment.

   This function aligns the HTML component horizontally using the provided `align` parameter. You can specify the horizontal alignment using values like "left," "center," or "right."

   Example usage:

   .. code-block:: python

      # Center-align the content
      centered_content = Halign(oj.Mutable.Span(text="This is centered text"), align="center")

      # Left-align the content
      left_aligned_content = Halign(oj.Mutable.Button(text="Left-aligned text"), align="left")

      

.. py:function:: Subsection(heading_text: AnyStr, content, align="center", twsty_tags=[], **kwargs)
   
 Create a subsection with a heading and content.

    :param heading_text: The text for the subsection heading.
    :type heading_text: str

    :param content: The content of the subsection.
    :type content: Ofjustpy HTML component object

    :param align: (optional) The horizontal alignment of the subsection. Default is "center".
    Other options are "start," "end," "center," "between," "evenly," "around."
    :type align: str, optional

    :param twsty_tags: (optional) A list of Tailwind CSS tags for styling.
    :type twsty_tags: List[str], optional

    :param kwargs: Additional keyword arguments for styling and attributes.

    :return: An Ofjustpy HTML component representing the subsection.

    This function creates a subsection with a heading and content. You can specify the horizontal
    alignment of the subsection using the `align` parameter. The `twsty_tags` parameter allows you
    to apply Tailwind CSS styling to the subsection.

    Example usage:

    .. code-block:: python

        # Create a subsection with centered content
        subsection = Subsection(
            heading_text="Section Title",
            content= oj.Mutable.Span(text="This is the subsection content."),
            align="center",
            twsty_tags=["bg-blue-100", "p-4"],
        )

.. py:function:: Subsubsection(heading_text: AnyStr, content, align="center", twsty_tags=[], **kwargs)

  Same as Subsection except heading font is bit smaller.
  
