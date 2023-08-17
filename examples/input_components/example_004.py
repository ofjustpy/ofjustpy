"""
drop down color not working in firefox
"""

#from tailwind_tags import *
from py_tailwind_utils import bg, blue, bd, bdr, gray, H, W, full, pd, space, y
import ofjustpy as oj
from addict_tracking_changes import Dict

def on_btn_click(dbref, msg, to_target):
    print ("id clicked ", dbref.id, " ", msg.value)
    pass

app = oj.load_app()
with oj.uictx("wp_mcs"):
    mcs = oj.AC.MainColorSelector(key = "my_color_selector",
                                  on_click = on_btn_click
                                             )


wp_endpoint = oj.create_endpoint(key="example_004",
                                 childs = [mcs
                                           ],
                                 title="MainColorSelector"
                                 )    
oj.add_jproute("/", wp_endpoint)

app = oj.load_app()
