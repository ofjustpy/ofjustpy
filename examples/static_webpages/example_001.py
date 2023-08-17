"""
Div containing label and span component
"""
import ofjustpy as oj

from py_tailwind_utils import *

route_prefix = ""
label = oj.PC.Label(text="labeltext", twsty_tags=[bg/blue/3])
span =  oj.PC.Span(text="spantext", twsty_tags=[bg/green/3])
div = oj.PC.StackV(childs=[label,
                        span
                        ],
                 twsty_tags=[W/"1/2", bg/rose/4,  db.f, jc.center, space/x/8]
                 )
                  


wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs = [div],
                                 title="example_001")


oj.add_jproute("/", wp_endpoint)
app = oj.load_app()
