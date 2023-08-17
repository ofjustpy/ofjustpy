
HtmlComponents Type Zoo
-----------------------

List of all the component types, their corresponding StaticCores, gen_stub, Stub classes

HtmlComponent type zoo
^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   For passive components/div no tracker is required. So stub_gen is a
   simple member function.

+----------------+------------+--------------------+-----------------+
| CompType       | Mutability | stub_gen           | StubType        |
+================+============+====================+=================+
| HC             | Passive    | stub               | Stub_HCPassive  |
+----------------+------------+--------------------+-----------------+
| HC             | Active     | gen_Stub_HCActive  | Stub_HCActive   |
+----------------+------------+--------------------+-----------------+
| HC             | Mutable    | gen_stub_HCMutable | Stub_HCMutable  |
+----------------+------------+--------------------+-----------------+
| Div            | Passive    | stub               | Stub_DivPassive |
+----------------+------------+--------------------+-----------------+
| Div            | Active     | gen_Stub_DivActive | Stub_DivActive  |
+----------------+------------+--------------------+-----------------+
| HCCMutable Div | Passive    | stub               | Stub_HCCMutable |
+----------------+------------+--------------------+-----------------+
| mutable  Div   | Mutable    | gen_Stub_DivMutable| Stub_DivMutable |
+----------------+------------+--------------------+-----------------+
| HCCStatic Div  | Mutable    | gen_Stub_DivMutable| Stub_DivMutable |
+----------------+------------+--------------------+-----------------+
|                |            |                    |                 |
+----------------+------------+--------------------+-----------------+


