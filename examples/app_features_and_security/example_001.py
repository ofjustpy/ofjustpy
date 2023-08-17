"""
demos implanting cookie via oj-signed-middleware
and reading/writing the cookie via response and via websockets (for non-httpsonly cookies)
"""

import ofjustpy as oj

from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
from py_tailwind_utils import *
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy.TF_impl import HCType
from ofjustpy.ui_styles import sty
from ofjustpy import ui_styles
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy.HC_TF import gen_HC_type

app = oj.load_app()
session_dict = {}

Span_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Span",
        TR.SpanMixin,
        staticCoreMixins=[TR.TwStyMixin],
        mutableShellMixins=[TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )
)


infobox = Span_HCType(key="aspan",
                        text=f'This text needs to be changed',
                        )

def on_btn_click(dbref, msg, ms_target_func):
    ms_infobox = ms_target_func(infobox)
    mypage = msg.page
    num_clicks = mypage.get_cookie('num_clicks')
    print("obtained num_clicks from cookie = ", num_clicks, " ", type(num_clicks))
    num_clicks = num_clicks + 1

    ms_infobox.text =f'Number of Click Events: {num_clicks}'
    mypage.set_cookie("num_clicks", num_clicks)
    print("setting cooking to be flushed out")
    mypage.set_flush_cookies(True)
    
    pass


btn = oj.Mutable.Span(key="show_clicks_btn",
                      text=f'Change Span text',
                      on_click=on_btn_click
                      )

async def on_page_ready(dbref, msg, ms_target_func):
    # wp is already mutableShell Page
    wp = msg.page
    ms_infobox = ms_target_func(infobox)
    num_clicks = wp.get_cookie('num_clicks')
    ms_infobox.text =f'Number of Click Events: {num_clicks}'
    
    pass
    
def on_mutableShell_create(wp_ms):
    if wp_ms.has_cookie('num_clicks'):
        print("====> reading from cookie", wp_ms.get_cookie('num_clicks'))
        
    else:
        wp_ms.set_cookie("num_clicks", 5)
    pass
    
    
wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs=[btn, infobox
                                         ],
                                 title="Example 001",
                                 post_mutableshell_create_callback = on_mutableShell_create,
                                 on_page_ready = on_page_ready
                                 )
oj.add_jproute("/", wp_endpoint)
