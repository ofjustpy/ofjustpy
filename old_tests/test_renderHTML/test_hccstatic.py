import ofjustpy as oj
from py_tailwind_utils import *

request = Dict()
request.session_id = "abc"
class WP:
    def add_component(self, x):
        pass
    pass
wp = WP()

sm = oj.get_session_manager(request)
def on_span_click(dbref, msg, to_ms):
    pass
with  oj.sessionctx(sm):
    with oj.uictx("l0"):
        label = oj.AC.Span(key = "aspan", text="labeltext", twsty_tags=[bg/blue/300])
        sdiv = oj.HCCStatic.StackV(key="sdiv", childs = [label], twsty_tags=[bg/green/100])
        sdiv_shell  = sdiv.stub()(wp)
        print ( "".join(sdiv_shell.to_html_iter()))
