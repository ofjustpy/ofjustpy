Layout Modifiers
^^^^^^^^^^^^^^^^


.. py:function:: oj.Halign(content, align="center", content_type="passive",  **kwargs)

   Aligns the HTML component content horizontally.

   :param content: The HTML component to be aligned.
   :type content: Ofjustpy HTML component object 

   :param align: (optional) The horizontal alignment. Default is "center". Other options are start, end, center, between, evenly, around
   :type align: str, optional

   :param content_type: "passive", "active",  or "mutable"
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

.. py:function:: oj.PC.Valign(content: Callable, height_tag=H / screen, align="center", twsty_tags=[], **kwargs)
		 
   :param content: The HTML component to be aligned.
   :type content: Ofjustpy HTML component object 

   :param align: (optional) The vertical alignment. Default is "center". Other options are start, end, center, between, evenly, around
   :type align: str, optional

   :param height_tag: default h-screen. The height of the enclosing div within which
		      the content component is aligned.
		      
   :param kwargs: Additional keyword arguments for styling and attributes.

   :return: An Ofjustpy HTML component with the specified horizontal alignment.

   This function aligns the HTML component horizontally using the provided `align` parameter. You can specify the horizontal alignment using values like "left," "center," or "right."

   Example usage:

   .. code-block:: python

      # Center-align the content
      centered_content = Halign(oj.Mutable.Span(text="This is centered text"), align="center")

      # Left-align the content
      left_aligned_content = Halign(oj.Mutable.Button(text="Left-aligned text"), align="left")
      
    
.. py:function:: oj.StackH_Aligned(content, content_type="passive", valign="center", halign="center", **kwargs)

    for content which are to be stacked horizontally wrap then around two divs so that
    1- they all have same height
    2- they are positioned vertically and horizontally in center
    
		 
.. py:function:: oj.Mutable.Halign(content, align="center", **kwargs)

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
