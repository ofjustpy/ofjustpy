import ofjustpy as oj
from starlette.middleware import Middleware
from asgi_signing_middleware import SerializedSignedCookieMiddleware

import os

cookie_secret_keys = []
if 'OJ_COOKIE_SECRET_KEYS' in os.environ:
    cookie_secret_keys = os.environ['OJ_COOKIE_SECRET_KEYS'].split()
    print("cookie_secret_keys ", cookie_secret_keys)
app  = oj.build_app(
    cookie_signer_secret_keys = [_.encode('utf8') for _ in cookie_secret_keys]
)

