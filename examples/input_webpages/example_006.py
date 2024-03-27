import ofjustpy as oj

from py_tailwind_utils import *
app = oj.load_app()

clickCount = 0

async def onBtnClick(self, msg, target_of):
    global clickCount
    clickCount += 1
    print("clickCount = ", clickCount)
    pass

    
dl = oj.AD.Datalist(key="aimg",
                    childs=[oj.PC.Option(text="hello", value="hh", twsty_tags=[H/32, W/32])],
                     twsty_tags=[H/32, W/32, bg/green/1],
                on_click = onBtnClick
                )




wp_endpoint = oj.create_endpoint(key="example_006",
                                 childs = [
                                           dl
                                           ],
                                 title="example_006"

                                 )    
oj.add_jproute("/", wp_endpoint)
















