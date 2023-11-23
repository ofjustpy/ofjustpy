"""
Provides stubs for different types
HC/Div types.
Stubs enable bottom up creation
of DOM-tree. User declare stubs instead of
actual HC-instance.
At last when page is created, stubs.__call__ method
is invoked to create the real HC-instance.

Stubs also create/refresh json_obj of the object.

1. Stub_HCStatic:
 - no childs
 -
2. Stub_HCPassive
 -
3. Stub_HCActive
- build_json

4. Stub_DivActive

5. Stub_HCMutable
- track staticCore
- mutableShell_type
- on __call__: create mutableShell
- build_json

6. Stub_DivMutable

7. Stub_HCCMutable

mutable Stubs are generated via gen_Stub generated
so that the instance can be tracked on stubStore
"""
from aenum import Enum

from .tracker import trackStub


class HCType(Enum):
    passive = "passive"  # implies static div/hc; for div implies passive/active childs
    active = "active"  # implies active div/hc; for div imples passive/active childs
    mutable = (
        "css_mutable"  # implies mutable div/hc; if div then imples css-mutable childs
    )
    hcc_mutable_div = "hcc_mutable"  # for div only; twstags is static/unmutable; only childs are mutable
    hcc_static_div = "static_hcc_div"  # for div only; twstags of div is mutable; but childs are static/active


class StubTag:
    pass


class Stub_HCStatic(StubTag):
    def __init__(self, *args, **kwargs):
        self.target = kwargs.get("target")

    def register_childrens(self):
        # HC are not div elements and do not
        # contain childrens

        pass

    @classmethod
    def is_static(cls):
        return True

    def __call__(self, a, attach_to_parent=True):
        """
        if the both parent and child are static
        then child is already attached at setup/initialized time

        """

        if attach_to_parent:
            # if parent is static then childs are declared
            # during setup/initialization
            a.add_component(self.target)
        self.register_childrens()

        if not self.target.obj_json:
            self.target.build_json()

        return self.target

    
    @property
    def twsty_tags(self):
        return self.target.twsty_tags
    
    @property
    def id(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    @property
    def key(self):
        raise NotImplementedError("Subclasses must implement this method")

    @property
    def svelte_safelist(self):
        """
        svelte_safelist is for all the twtags introduced
        during event handler. 
        passive components do not have event handlers
        """
        return []
    
    pass


class Stub_HCPassive(Stub_HCStatic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    @classmethod
    def is_static(cls):
        return True

    def register_childrens(self):
        # HC are not div elements and do not
        # contain childrens

        pass


class Stub_DivPassive(Stub_HCPassive):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    @classmethod
    def is_static(cls):
        return True

    def register_childrens(self):
        self.target.add_register_childs()
        # all the childs have been added
        
        # for achild in self.target.components:
        #     #call the child stubs -- so that
        #     #active childs can be registered
        #     #but ignore the stubs as the child
        #     #is already registered.
        #     stub = achild.stub()
        #     # invoke __call_ of stub
        #     # to assign id, build json
        #     stub(self, attach_to_parent=False)


class Stub_HCActive(Stub_HCStatic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    @classmethod
    def is_static(cls):
        return True

    def __call__(self, a, attach_to_parent=True):
        """
        if the both parent and child are static
        then child is already attached at setup/initialized time

        """
        # The container has active childs.
        # They need to be registered with stubStore of a session.
        # Because the childs are static they are already
        # attached to the container during setup phase
        self.register_childrens()

        assert self.target.id is not None
        if self.target.obj_json is None:
            # now that id has been assigned
            # build the json
            self.target.build_json()

        if attach_to_parent:
            # if parent is static then childs are declared
            # during setup/initialization
            a.add_component(self.target)

        return self.target

    @property
    def key(self):
        return self.target.key

    @property
    def id(self):
        """ """
        return self.target.id



class Stub_DivActive(Stub_HCActive):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def register_childrens(self):
        """
        active divs register their children post id assignment
        """
        self.target.add_register_childs()

    @classmethod
    def is_static(cls):
        return True

    @property
    def id(self):
        """ """
        return self.target.id
    
    @property
    def svelte_safelist(self):
        return self.target.svelte_safelist

def gen_Stub_HCPassive(target, **kwargs):
    return Stub_HCPassive(target=target)

def gen_Stub_DivPassive(target, **kwargs):
    return Stub_DivPassive(target=target)

@trackStub
def gen_Stub_HCActive(target, **kwargs):
    """
    since events are associated with the
    components, they need to be assigned an id
    """
    target.request_callback(kwargs.get("session_manager"))
    # id has been assigned we can render html now
    return Stub_HCActive(target=target, **kwargs)

@trackStub
def gen_Stub_HCMutable(mutable_shell_type, **kwargs):
    return Stub_HCMutable(
        mutable_shell_type, **kwargs
    )
            
@trackStub
def gen_Stub_DivActive(target, **kwargs):
    """
    since events are associated with the
    components, they need to be assigned an id
    """
    return Stub_DivActive(target=target, **kwargs)

def gen_Stub_HCCMutable(*args, **kwargs):
    """
    since events are associated with the
    components, they need to be assigned an id
    """
    #kwargs.get("staticCore").prepare_htmlRender()
    return Stub_HCCMutable(*args, **kwargs
                        
                    )



# =========================== mutable Stub ===========================
class Stub_HCMutable:
    def __init__(self, mutableShell_type, **kwargs):
        # assert 'staticCore' in kwargs
        # self.staticCore = staticCore #kwargs.get('staticCore')
        self.mutableShell_type = mutableShell_type  # kwargs.pop('mutableShell_type')
        self.kwargs = kwargs

    def __call__(self, a):
        self.target = self.mutableShell_type(**self.kwargs, a=a)
        self.target.build_json()
        
        return self.target

    @classmethod
    def is_static(cls):
        return False

    @property
    def key(self):
        return self.kwargs.get("staticCore").key

    @property
    def twsty_tags(self):
        return self.kwargs.get('twsty_tags')

    @property
    def svelte_safelist(self):
        return self.kwargs.get("staticCore").svelte_safelist

    
    @property
    def id(self):
        """
        key property is only applicable for
        MutableDiv -- i.e. Css and HCC mutable div
        and not for HCCMutableDiv which are considered passive.
        Exception should not be raised since tracker is not
        associated with HCCMutableDiv
        """
        assert self.kwargs.get("staticCore").id
        return self.kwargs.get("staticCore").id


# ================================ end ===============================

# TODO: need to refactor all the Stub 
class Stub_DivMutable:
    """
    childs are  mutable.
    div's css(twsty_tags) don't mutate ;
    """

    def __init__(self, mutableShell_type, **kwargs):
        self.kwargs = kwargs
        self.mutableShell_type = mutableShell_type
        # for active elements this will get overridden by tracker
        pass

    @classmethod
    def is_static(cls):
        return False

    def __call__(self, a, attach_to_parent=True):
        # create the component
        # no key/id for HCC mutable
        self.target = self.mutableShell_type(**self.kwargs, a=a)
        # child stubs are invoked by the mutableShell
        self.target.build_json()
        return self.target

    @property
    def key(self):
        """
        key property is only applicable for
        MutableDiv -- i.e. Css and HCC mutable div
        and not for HCCMutableDiv which are considered passive.
        Exception should not be raised since tracker is not
        associated with HCCMutableDiv
        """
        return self.kwargs.get("staticCore").key

    @property
    def twsty_tags(self):
        return self.kwargs.get('twsty_tags')
    
    @property
    def id(self):
        """
        key property is only applicable for
        MutableDiv -- i.e. Css and HCC mutable div
        and not for HCCMutableDiv which are considered passive.
        Exception should not be raised since tracker is not
        associated with HCCMutableDiv
        """
        return self.kwargs.get("staticCore").id


    @property
    def svelte_safelist(self):
        return self.kwargs.get('staticCore').svelte_safelist

class Stub_HCCStatic(Stub_DivMutable):
    """
    add_register_childs is called by the 
    """
    def __call__(self, a, attach_to_parent=True):
        # create the component
        # no key/id for HCC mutable
        self.target = self.mutableShell_type(**self.kwargs, a=a)
        self.target.build_json()

        return self.target
    
    
class Stub_HCCMutable:
    """
    childs are  mutable.
    div's css(twsty_tags) don't mutate ;
    """

    def __init__(self, mutableShell_type, **kwargs):
        self.kwargs = kwargs
        self.mutableShell_type = mutableShell_type
        # for active elements this will get overridden by tracker
        pass

    @classmethod
    def is_static(cls):
        return True

    def __call__(self, a, attach_to_parent=True):
        # create the component
        # no key/id for HCC mutable

        self.target = self.mutableShell_type(**self.kwargs, a=a)
        # child stubs are invoked by the mutableShell
        self.target.build_json()
        return self.target

    @property
    def twsty_tags(self):
        return self.kwargs.get("staticCore").twsty_tags
    
    @property
    def key(self):
        """
        key property is only applicable for
        MutableDiv -- i.e. Css and HCC mutable div
        and not for HCCMutableDiv which are considered passive.
        Exception should not be raised since tracker is not
        associated with HCCMutableDiv
        """
        return self.kwargs.get("staticCore").key

    @property
    def svelte_safelist(self):
        return self.kwargs.get("staticCore").svelte_safelist


@trackStub
def gen_Stub_DivMutable(mutableShell_type, **kwargs):
    return Stub_DivMutable(mutableShell_type, **kwargs)


class Stub_WebPage:
    def __init__(self, mutableShell_type, *args, **kwargs):
        self.mutableShell_type = mutableShell_type
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def is_static(cls):
        return False

    def __call__(self, *args, **kwargs):
        self.target = self.mutableShell_type(*args, *self.args,  **kwargs, **self.kwargs)
        post_MutableShell_create_callback = self.kwargs.get(
            "post_mutableshell_create_callback", None
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

    @property
    def twsty_tags(self):
        return self.kwargs.get('twsty_tags', [])

    @property
    def svelte_safelist(self):
        return self.kwargs.get("staticCore").svelte_safelist
        return []
    
@trackStub
def gen_Stub_WebPage(*args, **kwargs):
    page_stub = Stub_WebPage(*args, **kwargs)
    return page_stub    
