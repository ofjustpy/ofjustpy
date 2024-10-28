
import ofjustpy as oj
from addict_tracking_changes import Dict
from py_tailwind_utils import tstr, conc_twtags, remove_from_twtag_list, dget
app = oj.load_app()

def on_slider_select(dbref, msg, target_of):
    print ("ON Circle Clicked called ", msg.value)
    pass

with oj.uictx("tlc") as tlctx:
    slider = oj.Mutable.Slider(key = "aslider",
                                num_iter=range(4,12),
                                
                                on_click = on_slider_select
                                )

    
wp_endpoint = oj.create_endpoint(key="example_002",
                                 childs = [slider
                                           ],
                                 title="example_002",
                                 #template_file="production_hosting.html"

                                 )

oj.add_jproute("/", wp_endpoint)

