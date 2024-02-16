from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient

app = Starlette()
app.router.routes.append(Route("/", None, name="deferred_route"))
async def deferred_endpoint(request):
    return JSONResponse({"message": "Deferred Endpoint"})

Y = app.router.routes[0]
Y.endpoint = deferred_endpoint
client = TestClient(app)

