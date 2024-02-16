Mutable Components
^^^^^^^^^^^^^^^^^^

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
their corresponding static component version (`also see <https://github.com/ofjustpy/ofjustpy/blob/main/src/ofjustpy/MHC_types.py>`_). 

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

Containers for Mutable containers:
++++++++++++++++++++++++++++++++++

HCCStatic
'''''''''


Div class types whose css/classes is mutable but childs are static

.. py:class:: oj.HCCStatic.Div
	      
.. py:class:: oj.HCCStatic.StackV

	      

HCCMutable
''''''''''
Div class types whose css/classes is static but childs are mutable

.. py:class:: oj.HCCMutable.Div

.. py:class:: oj.HCCMutable.StackV

.. py:class:: oj.HCCMutable.StackH

.. py:class:: oj.HCCMutable.StackW

.. py:class:: oj.HCCMutable.Container

	      

	      

Using Mutable Composite Components
++++++++++++++++++++++++++++++++++

StackD
''''''

StackD is a dynamic component representing a "Deck" of cards, where each card is a child element. 

.. py:class:: StackD
	      
   :param height_anchor_key: Fix the height of the component to the height this component will be created.
			     
   .. py:method:: bring_to_front(id)
		  



Usage:
......

.. code-block:: python

   stackd_instance = oj.Mutable.StackD(childs=[btn1, btn2, btn3])
   stackd_instance.bring_to_front('text_key')

.. TODO: refer to code and live demo



    
Slider
''''''

The Slider function creates a custom slider component that displays a set of clickable circles based on the provided itemiter list. It takes a key and a list of items as input, displaying the items as circles within the slider. When a circle is clicked, its outline is updated, and an on-click event is triggered.


.. py:class:: Slider

   :ivar num_iter: list of items to be displayed as clickable circles in the slider. This parameter is required.

Usage
.....

.. code-block:: python

    slider_instance = oj.Mutable.Slider(key='slider_key', num_iter= [1, 2, 3], twsty_tags=['bg-gray-200'])

    
ColorSelector
'''''''''''''

The ColorSelector function creates a custom color selector component that combines a main color selector and a shades slider. It allows users to pick a color and its shade, then triggers an on-click event with the chosen color.

.. note::
   
   This is not a general purpose container. Its build primarly to a) demo component programing in Python, and b) has specific use case where Tailwind default colors are to be selected for a component.
   


   
   
Paginate
''''''''

.. py:function:: Paginate(key, childs, page_container_gen, num_pages=10, chunk_size=100, twsty_tags=[], stackd_tags=[H / screen], **kwargs)

   Paginate a list of items into multiple pages with customizable styling.

   :param key: A unique key identifying the paginated content. 
   :param childs: A list of components to be paginated. 
   :param page_container_gen: A callable function that generates a container for each paginated page. 
   :param num_pages: An integer representing the number of pages to display .
   :param chunk_size: An integer representing the number of items to display per page.
   :param stackd_tags: The exact height of the stackD used in the paginate section.


Usage
......

TDB (See code and live demo)



Dockbar
'''''''
  
Plug in this component to have a bar on your page to minimize page components. See the demo/example code at [demo_dock_undock](demos/demo_dock_undock.py) for usage.

.. py:class:: Dockbar

   A class representing a dockbar with dockable items and labels.

   .. py:method:: __init__(dockable_items, dock_labels, *args, wdiv_type=HCCStatic.Div, **kwargs)

      Initialize the Dockbar instance.

      :param dockable_items: A list of dockable items to be displayed in the dockbar. This parameter is required.
      :param dock_labels: A list of labels corresponding to the dockable items. This parameter is required.
      :param args: Positional arguments that can be passed to the parent class constructor.
      :param wdiv_type: The type of div used for the dockable items (default is HCCStatic.Div). If the items being docked are mutable, use Mutable.Div.
      :param kwargs: Additional keyword arguments that can be passed to the parent class constructor.

		     
   Assuming that the item being docked are static items. If they are Mutable then use general mutable Mutable.Div for wdiv_type.

Usage
......

TDB (See code and live demo)

BiSplitView
'''''''''''

Display a list of components across two columns. Each column is a vertically stacked collection of cells that holds the given components.

.. py:function:: BiSplitView(childs: List, hc_types, twsty_tags=[], **kwargs)

   :param childs: A list of components to be displayed in the split view. 
   :param hc_types: A dictionary containing fields:
                  - *part_viewer*: A view function for the parts
                  - *full_viewer*: A viewer to stack the part view for full view
		    
Usage
......

See the demo/example code at [demo_BiSplitView](demos/demo_two_column_stackv.py).  


HierarchyNavigator
''''''''''''''''''

.. py:class:: HierarchyNavigator(hierarchy, callback_child_selected, max_childs=20, max_depth=6, *args, **kwargs)

   A class for displaying a nested dictionary with hierarchical navigation.

   :param hierarchy: A nested dictionary to be displayed as hierarchical navigation. This parameter is required.
   :param callback_child_selected: A callback function to be invoked when a child is selected in the hierarchical navigation. This parameter is required.
   :param max_childs: An integer representing the maximum number of child items to be displayed at each level (default is 20).
   :param max_depth: An integer representing the maximum depth of the hierarchical navigation (default is 6).



Usage
.....
TBD: 
Check out the demo/example code at [demo_hinav](demos/demo_hierarchy_navigation_using_italian_cuisine.py).
	
SlideShow
'''''''''
A class representing a slideshow with a grid of door cards on one side and a deck of info cards on the other side (side by side view). The slideshow consists of a grid of door cards on one side and a deck of info cards on the other side, displayed in a side-by-side view. The info card for the door card currently under focus is brought to the top.
   
.. py:class:: SlideShow(key, slide_labels, slide_info, height_anchor_label, *args, **kwargs)

   :param key: A unique key identifying the slideshow. 
   :param slide_labels: A list of labels for the door cards. 
   :param slide_info: A list of information for the info cards. 
   :param height_anchor_label: The label that controls the height of the resulting slideshow panel. 

   .. note::

      The *height_anchor_label* controls the height of the resulting slideshow panel.


      
