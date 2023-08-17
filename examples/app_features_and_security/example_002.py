"""
demos page_ready event handling
"""
import ofjustpy as oj
from starlette.testclient import TestClient

app = oj.load_app()
infobox = oj.PC.Span(text="Hello World")

def on_page_ready(dbref, msg, to_ms_func):
    print("page rendered and now ready to display")
    pass
    
wp_endpoint = oj.create_endpoint(key="example_002",
                                 childs=[infobox
                                         ],
                                 title="Example 002",
                                 on_page_ready = on_page_ready
                                 )
oj.add_jproute("/", wp_endpoint)
