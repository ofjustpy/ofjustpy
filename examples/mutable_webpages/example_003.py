"""
drop down color not working in firefox
"""

from py_tailwind_utils import bg, blue, bd, bdr, gray, H, W, full, pd, space, y
import ofjustpy as oj
from addict_tracking_changes import Dict

def on_slider_select(dbref, msg, target_of):
    print ("ON Circle Clicked called ")
    pass

with oj.uictx("tlc") as tlctx:
    sliders = [oj.Mutable.Slider(key = f"aslider_{i}",
                                num_iter=range(4,12),
                                
                                on_click = on_slider_select
                                )
               for i in range(10)
               ]

    

wp_endpoint = oj.create_endpoint(key="example_003",
                                 childs = sliders,

                                 title="example_003"
                                 )

oj.add_jproute("/", wp_endpoint)
app = oj.load_app()
