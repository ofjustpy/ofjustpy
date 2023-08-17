"""
Defines all the mixins that will make
up the WebPage class type.

The mixins can be used to define: passive, active, or mutable Webpage.
Currently, only mutable WebPage type is being created.
WebPageMixin provides all the heavy lifting code that WebPage class is required
to do: like handling events, talking to frontend, etc. 

"""
import json

from addict_tracking_changes import Dict
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.WebPage_type_mixin import WebPageMixin
from ofjustpy_engine.jpcore import jpconfig

from .tracker import trackStub

class EventMixin(TR.EventMixinBase):
    allowed_events = [
        "click",
        "visibilitychange",
        "page_ready",
        "result_ready",
        "keydown",
        "keyup",
        "keypress",
    ]

class StaticCoreBaseMixin(
    TR.IdMixin,
    TR.jpBaseComponentMixin,
    EventMixin,
):
    def __init__(self, *args, **kwargs):
        self.domDict = Dict()
        self.attrs = Dict()
        self.key = kwargs.get("key", None)
        assert self.key is not None
        TR.IdMixin.__init__(self, *args, **kwargs)
        TR.jpBaseComponentMixin.__init__(self, **kwargs)

        # We haven't yet jsonified domDict.event_modifiers
        EventMixin.__init__(self, *args, **kwargs)

        # json_domDict is initialized after id is assigned
        self.json_domDict = None
        self.json_attrs = None

    def get_domDict_json(self):
        # json_domDict is jsonified after tracker has assigned a ID
        if not self.json_domDict:
            self.json_domDict = json.dumps(self.domDict, default=str)[1:-1]
        return self.json_domDict

    def get_attrs_json(self):
        if not self.json_attrs:
            self.json_attrs = json.dumps(self.attrs, default=str)[1:-1]
        return self.json_attrs


class HCCMutableCore(
    StaticCoreBaseMixin,
):
    # behaves same as StaticCoreBaseMixin
    #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.childs = kwargs.get("childs")

class CookieMixin:
    """
    handle cookies via asgi-signing middleware
    """
    class CookieData:
        def __init__(self):
            self.data = {}
            

    def __init__(self, *args, **kwargs):
        session_manager = kwargs.get("session_manager")
        self.cookie_state_attr_names  = kwargs.get('cookie_state_attr_names')
        # a mapping from cookie attr name to
        # the middleware object 
        self.cookie_middleware_objs = {}

        for _ in kwargs.get('cookie_state_attr_names', []):
            if not hasattr(session_manager.request.state, _):
                setattr(session_manager.request.state,
                        _,
                        CookieMixin.CookieData()
                        )
            assert  hasattr(session_manager.request.state,
                            f"{_}_middleware_obj"
                            )
            self.cookie_middleware_objs[_] = getattr(session_manager.request.state,
                                                     f"{_}_middleware_obj"
                                                     )
                    
        self.request_state = session_manager.request.state
        self.flush_cookies_flag = False

    def get_cookie_json(self):
        serialized_data = {}
        
        for state_attribute_name  in self.cookie_state_attr_names:
            attr_cookie = getattr(self.session_manager.request.state, state_attribute_name)
            cookie_middleware_obj = mobj = self.cookie_middleware_objs[state_attribute_name]
            signed_data = cookie_middleware_obj.sign(attr_cookie.data)
            serialized_data[state_attribute_name] = {
                "cookie_name": mobj.cookie_name,
                "cookie_ttl": mobj.cookie_ttl,
                "signed_data": signed_data,
                "cookie_properties": {
                    "path": mobj.cookie_properties["path"],
                    "domain": mobj.cookie_properties["domain"],
                    "secure": mobj.cookie_properties["secure"],
                    "httponly": mobj.cookie_properties["httponly"],
                    "samesite": mobj.cookie_properties["samesite"],
                },
            }
        json_data = json.dumps(serialized_data, indent=2)
        
        return f"""{{ "type": "update_cookies",  "data" : {json_data} }}"""
    def set_cookie(self, k, v, cn=None):

        if cn == None:
            cn = self.cookie_state_attr_names[0]
            
        getattr(self.request_state, cn).data[k] = v
        pass

    def get_cookie(self, k, cn=None):
        if cn == None:
            cn = self.cookie_state_attr_names[0]
        assert k in getattr(self.request_state, cn).data
        return getattr(self.request_state, cn).data[k]
    
    def has_cookie(self,k, cn=None):
        if cn == None:
            cn = self.cookie_state_attr_names[0]
        return k in getattr(self.request_state, cn).data

    def set_flush_cookies(self, flag=True):
        self.flush_cookies_flag = flag





class HCCMutable_Mixin:
    """
    contains id/event/reactive childs
    adding children and building json is delayed
    """

    def __init__(self, *args, **kwargs):
        # childs are assumed to be mutable
        # and are added via add_components
        self.components = []
        self.spathMap = Dict(track_changes=True)
        self.add_register_childs()

    def add_register_childs(self):
        for c in self.staticCore.childs:
            # register the child (only active child will register)
            c_ = c.stub()
            # attach the child as part of self.target.components
            c_(self)
            # staic components do not have ref/id/spath for
            # them to be tracked
            if not c_.is_static():
                self.spathMap[c_.id] = c_.target

    def add_component(self, child, position=None, slot=None):
        """
        add a component

        Args:
            child: the component to add
            position: the position to add to (append if None)
            slot: if given set the slot of the child
        """
        if slot:
            child.slot = slot
        if position is None:
            self.components.append(child)
        else:
            self.components.insert(position, child)

        return self


class StaticCoreSharerMixin:
    def __init__(self, *args, **kwargs):
        pass
    
    @property
    def events(self):
        return self.staticCore.events

    def get_event_handler(self, event_type):
        return self.staticCore.event_handlers[event_type]

    

def gen_WebPage_type(staticCoreMixins=[], mutableShellMixins=[]):

    if jpconfig.USE_COOKIE_MIDDLEWARE:
        print ("generating WebPageType: Use cookie-middleware == ", jpconfig.USE_COOKIE_MIDDLEWARE, type(jpconfig.USE_COOKIE_MIDDLEWARE))
        mutableShellMixins.append(CookieMixin)
        
    class WebPage_MutableShell(WebPageMixin,
                               HCCMutable_Mixin,
                               StaticCoreSharerMixin,
                               *mutableShellMixins):
        def __init__(self, *args, **kwargs):
            # should be part StaticCoreSharerBaseMixin:
            self.staticCore = kwargs.get("staticCore")
            WebPageMixin.__init__(self, *args, **kwargs)
            HCCMutable_Mixin.__init__(self, *args, **kwargs)
            StaticCoreSharerMixin.__init__(self, *args, **kwargs)
            
            for _ in mutableShellMixins:
                _.__init__(self, *args, **kwargs)

        def react(self):
            # Not sure what the purpose of this is
            pass

        @property
        def id(self):
            return self.staticCore.id

    class Stub_WebPage:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        @classmethod
        def is_static(cls):
            return False

        def __call__(self, *args, **kwargs):
            
            self.target = WebPage_MutableShell(*args,
                                               **kwargs, **self.kwargs)
            post_MutableShell_create_callback = self.kwargs.get('post_mutableshell_create_callback',
                                                                None
                                                                )
            if post_MutableShell_create_callback:
                post_MutableShell_create_callback(self.target)
            return self.target

        @property
        def key(self):
            return self.kwargs.get("key")

        @property
        def id(self):
            return self.kwargs.get("staticCore").id

    @trackStub
    def gen_Stub_WebPage(*args, **kwargs):
        page_stub = Stub_WebPage(*args, **kwargs)
        return page_stub

    class WebPage_StaticCore(HCCMutableCore, *staticCoreMixins):
        def __init__(self, *args, **kwargs):
            HCCMutableCore.__init__(self, **kwargs)
            self.key = kwargs.get("key")
            self.id = None
            for _ in staticCoreMixins:
                _.__init__(self, *args, **kwargs)
            self.kwargs = kwargs
            self.args = args

        def stub(self):
            return gen_Stub_WebPage(*self.args, staticCore=self,  **self.kwargs)

    return WebPage_StaticCore


WebPage = gen_WebPage_type()
