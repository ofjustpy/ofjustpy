# mutable divs register childrens
# after calling stub()(wp)

# prepare_htmlRender should be called id assignment
import ofjustpy as oj
from addict import Dict
from py_tailwind_utils import *
request = Dict()
request.session_id = "abc"
sm = oj.get_session_manager(request)
class WP:
    def add_component(self, x):
        pass
    pass
wp = WP()

def on_btn_click(dbref, msg, to_ms):
    pass
        
with  oj.sessionctx(sm):
    with oj.uictx("l0"):
        #mspan = oj.Mutable.Span(key="abc", text="alpha", twsty_tags=[bg/green/1])
        # mspan_shell = mspan.stub()(wp)
        # mspan_shell.add_twsty_tags(fc/green/1)
        # print (mspan_shell.to_html())

        #label = oj.PC.Label(text="labeltext", twsty_tags=[bg/blue/3])
        abtn = oj.AC.Button(key="abc", text="Click Me", value="avalue",
                            on_click = on_btn_click,
                            on_mouseover=on_btn_click)
        print ("------------------------")
        print(abtn.domDict)
        print (abtn.attrs)
        abtn_ms = abtn.stub()(wp)
        print("".join(abtn_ms.to_html_iter()))
        print ("------------------------")
        # ahref = oj.PC.A(text="Click me!", href="https://example.com")
        # pdiv = oj.PC.Div(childs = [label, ahref, abtn], twsty_tags=[pd/y/5])
        # adiv = oj.AC.Div(key="adiv", childs = [pdiv])
        # mdiv = oj.Mutable.Div(key="abc", childs=[mspan, adiv], twsty_tags=[bg/pink/1])
        # print (mdiv.htmlRender_chunk1)
        # mdiv_shell = mdiv.stub()(wp)
        # print ("".join(mdiv_shell.to_html_iter()))

        # active/passive within mutable

