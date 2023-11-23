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
        print ("on_btn_click")
        
        target = dget(deckdemo, dbref.value)
        print (target)
        ms_thedeck = target_of(thedeck)
        print (ms_thedeck)
        ms_thedeck.bring_to_front(target_of(target).id)
        pass

    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)
    btn1.prepare_htmlRender()
    btn2.prepare_htmlRender()
    print (btn1.htmlRender_chunk1)
    print (btn1.htmlRender_chunk2)
    print (btn1.htmlRender_chunk3)
    
    
wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [thedeck],
                                 title="example_008"
                                 )

oj.add_jproute("/", wp_endpoint)

