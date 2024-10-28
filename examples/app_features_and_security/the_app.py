import ofjustpy as oj
import os

# cookie_secret_keys = []
# if 'OJ_COOKIE_SECRET_KEYS' in os.environ:
#     cookie_secret_keys = os.environ['OJ_COOKIE_SECRET_KEYS'].split()
#     print("cookie_secret_keys ", cookie_secret_keys)
app  = oj.build_app(
    #cookie_signer_secret_keys = [_.encode('utf8') for _ in cookie_secret_keys]

)

if 'session_manager' in kwargs:
    self.session_manager = kwargs.get("session_manager")
    self.page_id = (
        self.session_manager.session_id + ":" + self.staticCore.id
    )
else:
    # SESSIONS is not enabled; session_id is not set; 
    self.session_manager = None
    self.page_id = (None, 
                    self.staticCore.id
                    )
