React Framework
'''''''''''''''
#. appstate
#. ui_app_trmap_iter
#. action_module
#. ojr.ReactDomino

Definations and Vocabulary
++++++++++++++++++++++++++

appstate
::::::::
Every session has an appstate which is a dictionary of type addict_tracking_changes.
As the name suggests, it is used to keep track of state of the webapp. It has inbuilt
feature to track changes over the stored data. 
Webapp function is codified into various actions that are trigged contigent to the appstate
changes.



UI Event handling to appstate update
++++++++++++++++++++++++++++++++++++
1. Define in ui_app_trmap: a mapping from event-idpath to appstate-storepath.
   For e.g. see code below:
   
   .. code-block:: python
		   
      ui_app_trmap = [ ('/mouseenter_hcobj', '/update_sty_hcobj/selected_hcobj', None)
    ]
    
   Here, event-idpath '/mouseenter_hcobj' is mapped to '/update_sty_hcobj/selected_hcobj' appstate-storepath.
   
   An event handler is configured as follows:
   
   .. code-block:: python
		   
      @ojr.ReactDomino
      def on_click(dbref, msg, to_ms):
          # do some useful work here
	  # collect relevant ui and app values here
          reutrn '/mouseenter_hcobj', dbref

   OJ middleware will make sure that when on_click event handler is invoked, then appstate is updated.
   
2. Attach actions to appstate changes

   Actions can be hooked to appstate-storepaths. For e.g.
   .. code-block:: python

      def sample_server_side_action(appstate, arg, wp):
      """
      appctx=/update_sty_hcobj/apply_attr_value_to_utility_class
      """
      pass
    
   Here the action `sample_server_side_action` is hooked to appstate-storepath
   `/update_sty_hcobj/apply_attr_value_to_utility_class`. Whenever the value changes
   for this appstate-storepath changes the corresponding action is triggered.
   OJ acts as clearinghouse between events and actions

Gotchas
:::::::
# In  state-changed based programming
 # if an action is hooked to a access-path
# then don't change the access-path in the action
