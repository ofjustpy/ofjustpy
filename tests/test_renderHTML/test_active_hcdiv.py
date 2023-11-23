import ofjustpy as oj
from addict import Dict
request = Dict()
request.session_id = "abc"
sm = oj.get_session_manager(request)
with  oj.sessionctx(sm):
    with oj.uictx("l0"):
        aspan = oj.AC.Span(key="aspan", text="abc")

        adiv = oj.AC.Div(key="adiv", childs = [aspan])

        # active divs within passive

        pdiv = oj.PC.Div(childs = [adiv])
        


        # passive within active
        adivo = oj.AC.StackH(key="adivox", childs=[pdiv])
        print (adivo.to_html())
