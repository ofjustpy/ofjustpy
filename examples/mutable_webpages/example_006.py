"""
drop down color not working in firefox
"""

#from tailwind_tags import *
from py_tailwind_utils import bg, blue, bd, bdr, gray, H, W, full, pd, space, y
import ofjustpy as oj

app = oj.load_app()
def on_slider_click(dbref, msg, to_target):
    print ("Slider Value changed ")
    print (msg)
    
    pass


with oj.uictx("tlc") as tlctx:
    with oj.uictx("components"):
        myslider = oj.Mutable.Slider( key="slider",
                                   num_iter = range(5,12),
                                   on_click=on_slider_click
                                  )

wp_endpoint = oj.create_endpoint(key="example_006",
                                 childs = [myslider],
                                 title="example_006"
                                 )

oj.add_jproute("/", wp_endpoint)

