import ofjustpy as oj
from py_tailwind_utils import *
app = oj.load_app()
def on_input_change(dbref, msg, target_of):
    print ("on_input_change : Called with ", msg.value)
    pass

option1 = oj.PC.Option( value="option1", label="Option 1", disabled=True, twsty_tags=[bg/green/100])
option2 = oj.PC.Option( value="option2", label="Option 2", twsty_tags=[bg/blue/400],
                           )
option3 = oj.PC.Option( value="option3", label="Option 3"
                           )

def on_input_change(dbref, msg, target_of):
    pass
select_input = oj.AC.Select(key="select_drop_down",
                                      childs=[option1, option2, option3],
                                      name="example_select",
                                      form="example_form",
                                      required=True,
                                      size=1,
                                      default = "options3",
                                      twsty_tags=[bg/green/100, W/"1/3"],
                                      on_change=on_input_change,
                                #on_click = on_input_change
                                      )

def on_click(dbref, msg, target_of):
    print ("in div handler: ", msg.value)
    pass


adiv = oj.AC.Div(key="adiv",
                 on_click = on_click,
                 childs = [select_input],
                 twsty_tags=[H/64, W/"1/2", bg/green/100]
                           
                 )

wp_endpoint = oj.create_endpoint(key="example_003",
                                 childs = [adiv],
                                 title="example_003"
                                 )

oj.add_jproute("/", wp_endpoint)

