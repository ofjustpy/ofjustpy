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

        mspan = oj.Mutable.Span(key="aspan", text="hello", on_click=on_span_click)
        mdiv = oj.HCCMutable.StackV(childs = [mspan], twsty_tags=[bg/green/100])
        print(mdiv.htmlRender_chunk1)
        mdiv_shell  = mdiv.stub()(wp)
        print ( "".join(mdiv_shell.to_html_iter()))
        
        # mspan_mshell = mspan.stub()(wp)
        # print(mspan_mshell.to_html())
