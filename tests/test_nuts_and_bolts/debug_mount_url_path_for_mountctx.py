from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from starlette.routing import Route
from starlette.requests import Request
from starlette.routing import Mount
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.testclient import TestClient



async def admin_home(request):
    # Get the base URL
    base_url = request.base_url

    # Use url_path_for to generate the URL for the "home" endpoint
    admin_url = request.url_for('pz:admin:admin_home')
    print ("admin_url = ", admin_url)

    # Create an HTML response with an <a> element
    html_content = f'<a href="{admin_url}">Go to Home</a>'
    return PlainTextResponse(html_content)

async def pz_home(request):
    # Get the base URL
    base_url = request.base_url

    # Use url_path_for to generate the URL for the "home" endpoint
    admin_url = request.url_for('pz:admin:admin_home')
    print ("admin_url = ", admin_url)

    # Create an HTML response with an <a> element
    html_content = f'<a href="{admin_url}">Go to Home</a>'
    return PlainTextResponse(html_content)

app = Starlette()
mount_route_stack = [app.router.routes]

# add a route
#mount_route_stack[-1].append(Route("/admin_home", admin_home, name="admin_home"))
#print(app.url_path_for("admin_home"))
# create a set of routes
to_be_mounted_routes = [Route("/admin_home", admin_home, name="admin_home")
    ]
mount_obj = Mount("/admin", name = "admin", routes=to_be_mounted_routes)
mount_route_stack[-1].append(mount_obj)

print(app.url_path_for("admin:admin_home"))
async def homepage(request):
    print(app.url_path_for('home'))
    pz_url = app.url_path_for('pz:pz_home')
    print(pz_url)

    admin_url = app.url_path_for('pz:admin:admin_home')
    print (admin_url)
    return PlainTextResponse('Hello, Starlette!')
