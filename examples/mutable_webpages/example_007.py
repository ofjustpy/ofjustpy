"""
drop down color not working in firefox
"""

#from tailwind_tags import *
from py_tailwind_utils import bg, blue, bd, bdr, gray, H, W, full, pd, space, y
import ofjustpy as oj
from addict_tracking_changes import Dict
app = oj.load_app()

def on_cs_click(dbref, msg, to_target):
    print ("color selector  changed : ", msg.value)
    print ("the base color:", dbref.mcs_value)
    print ("the color shade:", dbref.scs_value)
    
    pass

with oj.uictx("wp_cs"):
    color_selector = oj.Mutable.ColorSelector(
                                      key="CS",
                                      on_click=on_cs_click
                                      )


wp_endpoint = oj.create_endpoint(key="example_007",
                                 childs = [color_selector],
                                 title="example_007"

                                 )

oj.add_jproute("/", wp_endpoint)

