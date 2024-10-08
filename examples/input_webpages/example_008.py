"""
Button and event handling example
"""

import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict
app = oj.load_app()
def mouseover_action(dbref, msg, target_of):
    print ("in mouseover_action")
    # buttons msg do not have value
    #print (msg)
    print (dbref.value)
    pass

def dblclick_action(dbref, msg, target_of):
    print ("in doubleclick action")
    # buttons msg do not have value
    #print (msg)
    print (dbref.value)
    pass


# lets create six buttons
idx = 1
abtn = oj.AC.Button(key=f"btn_{idx}",
                     twsty_tags = [fc/rose/300,
                                         ta.center,
                                         bdr.lg,
                                         bd/gray/300,
                                         boxtopo.bd,
                                         fw.medium,
                                         *build_gradient_expr(gray/200, gray/200, gray/100),
                                         shadow/gray/200,
                                         shadow.md
                                         ],
                    #on_mouseover = mouseover_action,
                    on_submit = dblclick_action,
                    on_click = mouseover_action,
                    text=f"abtn_{idx}",
                    value = idx
                    )
                           
       
wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [abtn],
                                 title="example_008"
                                 )

oj.add_jproute("/", wp_endpoint)
