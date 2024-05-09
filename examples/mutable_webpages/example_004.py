import ofjustpy as oj
from py_tailwind_utils import *
app = oj.load_app()        
mylabel1 = oj.Mutable.Label(text="label-text-1", key="mylabel1")
mydiv = oj.HCCMutable.Div(twsty_tags=[W/"1/2"], childs=[mylabel1])

def on_btn_click(dbref, msg, target_of):
    shell_mylabel1 = target_of(mylabel1)
    shell_mylabel1.add_twsty_tags(bg/blue/500, fc/rose/600, fz.xl, fw.extrabold)
    pass


mybtn =  oj.AC.Button(key="mybtn",
                      text="abtn", twsty_tags=[W/32, H/32, bg/rose/600],
                      on_click=on_btn_click
                      )

wp_endpoint = oj.create_endpoint(key="example_004",
                                 childs = [mydiv, mybtn],
                                 title="example_004"
                                 )

oj.add_jproute("/",
                wp_endpoint)

