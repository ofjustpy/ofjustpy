import ofjustpy as oj
from py_tailwind_utils import *
app = oj.load_app()


with oj.uictx("deckdemo") as  deckdemo:
    btn1 = oj.Mutable.Button(key="mybtn1",
                              value="/mybtn2",
                              text="Click me1 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )

    btn2 = oj.Mutable.Button(key="mybtn2",
                              value="/mybtn1",
                              text="Click me2 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )
            
    thedeck = oj.Mutable.StackD(key = "thedeck",
                                childs = [ btn1, btn2
                               ]
                      )
    def on_btn_click(dbref, msg, target_of):
        target = dget(deckdemo, msg.value)
        ms_thedeck = target_of(thedeck)
        ms_thedeck.bring_to_front(target_of(target).id)
        pass


    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)
    
    
wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [thedeck],
                                 title="example_008"
                                 )
oj.add_jproute("/", wp_endpoint)

