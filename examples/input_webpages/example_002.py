import ofjustpy as oj
from py_tailwind_utils import *
app = oj.load_app()

def on_input_change(dbref, msg, to_target):
    print ("on_input_change : Called with ", msg.value)
    pass

color_selector = oj.AC.MainColorSelector(
                                      key="select_drop_down",
                                      twsty_tags=[bg/green/1, W/"1/3"],
                                      on_change=on_input_change
                                      )

wp_endpoint = oj.create_endpoint(key="example_002",
                                 childs = [color_selector],
                                 title="example_002"

                                 )
oj.add_jproute("/", wp_endpoint)

