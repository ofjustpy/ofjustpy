import ofjustpy as oj


from starlette.testclient import TestClient
from py_tailwind_utils import *
from starlette.routing import Mount, Route
app  = oj.load_app()

from starlette.responses import PlainTextResponse

# async def hello(request):
#     return PlainTextResponse("Hello, Starlette!")


# from starlette.routing import Mount, Route
# oj.aci.mount_route_stack[-1].append(Route("/hello", hello, name="hello")
#                                  )

# href to hello
with oj.MountCtx("hello"):
    hello_endpoint = oj.create_endpoint(key="hello",
                       childs = [oj.PC.Span(text="hello")],
                       )
    oj.add_jproute("/", hello_endpoint)
    
hello_href = oj.AC.A(key="hello_href",
                     title="example index",
                     text=f"Back to examples index",
                     href_builder = oj.href_builder_factory("hello:hello"),
                     twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                 shadow/gray/2,
                                 shadow.md
                                 ]

                     )
async def invoke_test(request):
    request.session_id = "abc"
    sm = oj.get_session_manager(request)
    with  oj.sessionctx(sm):
        print(app.url_path_for("hello:hello"))
        href_stub = hello_href.stub()
        print(href_stub.target.to_html())
        
    return PlainTextResponse("Hello, Starlette!")

oj.aci.mount_route_stack[-1].append(Route("/", invoke_test, name="invoke_test")
                                 )

client = TestClient(app)
response = client.get('/')
