"""
Div containing label and span component
"""
import ofjustpy as oj

from py_tailwind_utils import *
app = oj.load_app()


label = oj.PC.Label(text="labeltext", twsty_tags=[bg/blue/300])
span =  oj.PC.Span(text="spantext", twsty_tags=[bg/green/300])
div = oj.PC.StackV(childs=[label,
                        span
                        ],
                 twsty_tags=[W/"1/2", bg/rose/400,  db.f, jc.center, space/x/8]
                 )
                  


wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs = [div],
                                 title="example_001",
                                 csr_bundle_dir = "hyperui"
                                 )


oj.add_jproute("/", wp_endpoint)

# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')

