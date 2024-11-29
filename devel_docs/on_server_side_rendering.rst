HTMLRender: From python objects to  html
''''''''''''''''''''''''''''''''''''''''
We can't precompute htmlrender even for passiveDivs and PassiveHCs because
of oj.AC.A whose href is updated upon incoming request object.

.. note:: TODO: fix/correct/complete this

build_renderHTML logic
++++++++++++++++++++++
within Stub_HCPassive.__call__  -- after register_childrens build_renderHtml is called
covers calls for HCPassive, DivPassive

within Stub_HCActive.__call__  -- after register_childrens build_renderHtml is called
covers calls for DivActive




renderHtml design/arch
++++++++++++++++++++++
- staticCore has prepare_htmlRender
- is called by gen_Stub_X
- provides chunk1, chunk3

- mutableShell.to_html_iter
  uses chunk1, chunk2 etc. to piece together html


#. *DivMutable*  RenderHTML_HCCMutableChildsMixin
   
#. *DivHCCMutable* RenderHTML_HCCMutableChildsMixin
   
#. *DivHCCStatic*  HCCMixin_StaticChilds, RenderHTML_HCCStaticChildsMixin

#. *HCCPassiveMixin*
