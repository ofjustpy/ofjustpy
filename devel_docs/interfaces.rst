
Interface
=========

HTML Components
---------------

JsonMixin
~~~~~~~~~

#. get_obj_props_json
#. get_obj_props_jsondict
#. build_json
#. convert_object_to_jsondict
#. convert_object_to_json
#. get_changed_diff_patch
#. clear_changed_history

Misc
~~~~

#. request_callback
   - components can register a callback
   - after the object is initialized and part of DOM-tree
   - the callback is invoked
     
#. self.data_validators
   - part of form object to perform data validation

#. post_id_assign_callback
   -  this function is called after id has been assigned
      
Core
~~~~

HCC (aka html component container)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. self.components
#. self.domDict["child_item_order"]
#. add_register_childs(self):
   - for each of its child
     - create the stub
       - stub = achild.stub() #stub is misnomer ..it should be genStub
     - call the stub()
       - this call registers the id
	 
RenderHtml
~~~~~~~~~~

#. self.htmlRender_attr
   - TODO: no idea what it is suppose to do
     
#. prepare_htmlRender()
   - set self.htmlRender

..
   technically not a interface..the html is accessed via to_html_iter
   #. self.htmlRender
      - member attribute that holds  the html string for the compnent
      - used only for internal purposes
     

#. to_html_iter()
   - seq of chunks that make up the component html 

HC/Div Mixin
~~~~~~~~~~~~

#. self.id
#. self.key
#. self.show
#. self.debug
#. self.domDict.vue_type
#. self.domDict.events
#. self.domDict["inner_html"]
#. Extra attributes
   
   .. code-block::
            "accesskey",
            "contenteditable",
            "dir",
            "draggable",
            "dropzone",
            "lang",
            "spellcheck",
            "tabindex",
            "title",   
#. self.text
#. self.html_tag
#. add_twsty_tags
#. remove_twsty_tags
#. replace_twsty_tags
#. update_extra_classes
#. self.style
#. self.domDict.event_modifiers = Dict()
#. self.domDict.transition = None
#. self.event_handlers = {}
#. self.event_prehook = kwargs.get("event_prehook", None)   
#. add_prehook
#. remove_event
#. self.events
#. event_propagation
#. has_event_function

   
Stubs
-----
#. register_childrens()
#. self.targets
#. is_static()
#. __call__()
#. extra_classes()
#. twsty_tags(self)
#. id(self)
   
   
