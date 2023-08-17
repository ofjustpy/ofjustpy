"""
a mutable label, and a static button.
button click changes style/class of the mutable label
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict

alabel = oj.Mutable.Label(key="alabel", text="Sample Label")
def on_btn_click(dbref, msg, target_of):
    # get label's mutable shell
    label_shell = target_of(alabel)
    
    # modify label's classes via twsty_tags
    label_shell.add_twsty_tags(bg/blue/5, fc/rose/6, fz.xl, fw.extrabold)
    pass
       
btn = oj.AC.Button(key="abtn",
                 text="ChangeFont",
                 twsty_tags=[W/32, H/32, bg/rose/6],
                 on_click = on_btn_click
                 )

wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs = [alabel,
                                           btn
                                           ],
                                 title="example_001"
                                 )
oj.add_jproute("/", wp_endpoint)
app = oj.load_app()
