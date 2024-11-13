from py_tailwind_utils import *


def get_stackg_endpoint(oj):
    compg = oj.PD.StackG(num_rows=2, num_cols=2)
    wp_endpoint = oj.create_endpoint(key="stackg",
                                     childs = [compg]
                                     )
    return wp_endpoint


def get_stackd_endpoint(oj):
    btn1 = oj.Mutable.Button(key = "mybtn1",
                      value = "/mybtn2",
                      text = "Click me1",
                      twsty_tags = [bg/blue/"100/50"],
                      )

    btn2 = oj.Mutable.Button(key = "mybtn2",
                      value = "/mybtn1",
                      text = "Click me2",
                      twsty_tags = [bg/blue/"100/50"],
                      )

    mydeck = oj.Mutable.StackD(key="mydeck",
                             childs = [btn1, btn2]
                             )

    #TODO: can't use msg.value
    def on_btn_click(dbref,msg, to_ms):
        mydeck_ms = to_ms(mydeck)
        mydeck_ms.bring_to_front(dbref.value)
        pass
    btn1.on('click', on_btn_click)
    btn1.on('click', on_btn_click)
    
    wp_endpoint = oj.create_endpoint(key="stackd",
                       childs = [mydeck]
                       )
    return wp_endpoint
