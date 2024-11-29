"""
a mutable label, and a static button.
button click changes style/class of the mutable label
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
app = oj.load_app()

alabel = oj.Mutable.Label(key="alabel", text="Your Session ID: ")
def on_btn_click(dbref, msg, target_of):
    # get label's mutable shell
    session_manager = msg.page.session_manager
    print("session_id = ", session_manager.session_id)
    label_shell = target_of(alabel)
    
    # modify label's classes via twsty_tags
    label_shell.add_twsty_tags(bg/blue/500, fc/rose/600, fz.xl, fw.extrabold)
    pass
       
btn = oj.AC.Button(key="abtn",
                 text="Get session",
                 twsty_tags=[W/64, H/8, bg/rose/100],
                 on_click = on_btn_click
                 )


# def on_session_clear_btn_click(dbref, msg, to_ms):
#     request = msg.page.session_manager.request
#     request["session"] = {}
    
# session_clear_btn = oj.AC.Button(key="clear_session",
#                  text="Clear session cookie",
#                  twsty_tags=[W/64, H/8, bg/rose/100],
#                  on_click = on_session_clear_btn_click
#                  )



wp_endpoint = oj.create_endpoint(key="expose_session_id",
                                 childs = [alabel,
                                           btn,
                                           #session_clear_btn 
                                           ],
                                 title="Expose session id"
                                 )
oj.add_jproute("/", wp_endpoint)

