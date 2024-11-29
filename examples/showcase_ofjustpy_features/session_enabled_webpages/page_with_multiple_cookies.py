from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
app = oj.load_app()


def event_handler(dbref, msg, to_ms):
    request = msg.page.session_manager.request
    print(request.state.cart_items)
    request.state.cart_items = {'aval' :1}
    pass

alabel = oj.Mutable.Label(key="alabel", text="Your Session ID: ")

btn = oj.AC.Button(key="abtn",
                 text="Get session",
                 twsty_tags=[W/64, H/8, bg/rose/100],
                 on_click = event_handler
                 )



wp_endpoint = oj.create_endpoint(key="expose_session_id",
                                 childs = [alabel,
                                           btn,
                                           #session_clear_btn 
                                           ],
                                 title="Expose session id"
                                 )
oj.add_jproute("/", wp_endpoint)
