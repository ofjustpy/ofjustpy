import ofjustpy as oj
from ofjustpy_engine.jpcore import jpconfig

from starlette.testclient import TestClient

app  = oj.load_app()

from starlette.responses import PlainTextResponse

async def hello(request):
    print ("hello endpoint invoked")
    print (request.url_for("static", path="/"))
    return PlainTextResponse("Hello, Starlette!")
from starlette.routing import Mount, Route
print(oj.aci.mount_route_stack)
oj.aci.mount_route_stack[-1].append(Route("/", hello, name="hello")
                                 )

print(jpconfig.STATIC_ROUTE)
print(jpconfig.STATIC_DIRECTORY)
print(jpconfig.STATIC_NAME)



client = TestClient(app)
response = client.get('/')
print(response)
