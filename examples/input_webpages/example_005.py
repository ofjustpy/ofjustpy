import ofjustpy as oj

from py_tailwind_utils import *
app = oj.load_app()

clickCount = 0

async def onBtnClick(self, msg, target_of):
    global clickCount
    clickCount += 1
    print("clickCount = ", clickCount)
    pass

    
img = oj.AD.Img(key="aimg",
                src="https://via.placeholder.com/150",
                alt="Example image",
                on_click = onBtnClick
                )




wp_endpoint = oj.create_endpoint(key="example_005",
                                 childs = [
                                           img,
                                           ],
                                 title="example_005"

                                 )    
oj.add_jproute("/", wp_endpoint)
















