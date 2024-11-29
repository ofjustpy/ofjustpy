"""
static pages with no session
"""


import ofjustpy as oj
from starlette.testclient import TestClient

app = oj.load_app()
infobox = oj.PC.Span(text="Hello World")

# def on_page_ready(dbref, msg, to_ms_func):
#     print("page rendered and now ready to display")
#     pass

    
wp_endpoint_csr = oj.create_endpoint(key="CSR_nosession_passive",
                                 childs=[infobox
                                         ],
                                 title="CSR Nosession",
                                 #on_page_ready = on_page_ready
                                 )
oj.add_jproute("/csr", wp_endpoint_csr)


wp_endpoint_ssr = oj.create_endpoint(key="SSR_nosession_passive",
                                     childs=[infobox
                                             ],
                                     title="SSR Nosession",
                                     rendering_type="SSR"
                                     #on_page_ready = on_page_ready
                                     )
oj.add_jproute("/ssr", wp_endpoint_ssr)

