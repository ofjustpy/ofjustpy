Building a new component
''''''''''''''''''''''''
Passive
+++++++


Active
++++++
- Create mixin
- generate the class

.. code-block:: python
		
   from ofjustpy_engine.HCType import HCType
   from ofjustpy.Div_TF import gen_Div_type
   from ofjustpy import ui_styles
   from .mixins import (AccordionItemMixin)


   class ActiveComponents:
       AccordionItem = gen_Div_type(
	   HCType.active,
	   "FB_AccordionItem",
	   AccordionItemMixin,
	   stytags_getter_func=lambda m=ui_styles: m.sty.label,
       )
       pass

- assign_id       
