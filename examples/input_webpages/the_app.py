import ofjustpy as oj
from starlette.middleware import Middleware
from starlette.requests import Request
class InitRequestStateMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            request = Request(scope)
            # Initialize request.state
            request.state.form_data = {}

        await self.app(scope, receive, send)

app  = oj.build_app(middlewares=[Middleware(InitRequestStateMiddleware)
                                 ])
