"""
Type factory for Div data types.
5 types of divs: passive, active, hccMutable, mutable, and hccStatic
Static divs i.e., passive or active div can only store static components.
"""
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine import SHC_types_mixin as SCmixin
from ofjustpy_engine.mutable_Div_TF import classTypeGen as mutableClassTypeGen
from py_tailwind_utils import conc_twtags

from .TF_impl import gen_Stub_DivActive
from .TF_impl import gen_Stub_DivMutable
from .TF_impl import HCType
from .TF_impl import Stub_DivPassive
from .TF_impl import gen_Stub_DivPassive
from .TF_impl import gen_Stub_HCCMutable
from .tracker import trackStub

def gen_Div_type(
    div_type=HCType.passive,
    hc_tag="PassiveDiv",
    hctype_mixin=TR.DivMixin,
    static_addon_mixins=[],     
    static_core_mixins=None,
    mutable_shell_mixins=None,
    stytags_getter_func=None,
):
    if not static_core_mixins:
        static_core_mixins = []

    if not mutable_shell_mixins:
        mutable_shell_mixins = []

    match div_type:
        case HCType.passive:
            hc_type = SCmixin.staticClassTypeGen(
                hc_tag,
                tagtype=hctype_mixin,
                hccMixinType=SCmixin.HCCPassiveMixin,
                jsonMixinType=SCmixin.HCCPassiveJsonMixin,
                make_container=True,
            )

            class WithStub(hc_type):
                """
                add stub generator for static objects
                """

                def __init__(self, *args, **kwargs):
                    stytags = []
                    if stytags_getter_func:
                        stytags = stytags_getter_func()
                    twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                    super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

                def stub(self, **kwargs):
                    """
                    tracker will add session_manager to the stub call
                    """
                    return gen_Stub_DivPassive(self)


            return WithStub
        case HCType.active:
            hc_type = SCmixin.staticClassTypeGen(
                hc_tag,
                tagtype=hctype_mixin,
                hccMixinType=SCmixin.HCCMixin,
                jsonMixinType=SCmixin.HCCJsonMixin,
                make_container=True,
                attach_event_handling=True,
            )

            class WithStub(hc_type):
                def __init__(self, *args, **kwargs):
                    stytags = []
                    if stytags_getter_func:
                        stytags = stytags_getter_func()
                    twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                    super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

                def stub(self):
                    return gen_Stub_DivActive(target=self)

            return WithStub

        case HCType.hcc_mutable_div:
            # This is essentially ContainerMSHC/Deck
            # twsty-tags is shared
            static_core_mixins.append(TR.SvelteSafelistMixin)
            core_hc_type, mutable_shell_type = mutableClassTypeGen(
                hc_tag=hc_tag,
                hctag_mixin=hctype_mixin,
                static_core_mixins=static_core_mixins,
                mutable_shell_mixins=mutable_shell_mixins,
            )

            class WithStub(core_hc_type):
                def __init__(self, *args, **kwargs):
                    # twsty_tags is part of the static core and therefore should be part
                    # of static core
                    stytags = []
                    if stytags_getter_func:
                        stytags = stytags_getter_func()
                    twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                    super().__init__(*args, **kwargs, twsty_tags=twsty_tags)
                    self.kwargs = kwargs


                def stub(self, **kwargs):
                    # directly create stub
                    return gen_Stub_HCCMutable(mutable_shell_type, staticCore=self, **self.kwargs)
                    
                    pass

            return WithStub

        case HCType.mutable:  # implies div is css mutable and contains mutable children
            static_core_mixins.append(TR.SvelteSafelistMixin)
            core_hc_type, mutable_shell_type = mutableClassTypeGen(
                hc_tag=hc_tag,
                hctag_mixin=hctype_mixin,
                static_core_mixins=static_core_mixins,
                mutable_shell_mixins=mutable_shell_mixins,
                is_self_mutable=True,
                is_childs_mutable=True,
            )

            class WithStub(core_hc_type):
                def __init__(self, *args, **kwargs):
                    stytags = []
                    if stytags_getter_func:
                        stytags = stytags_getter_func()
                    self.twsty_tags = conc_twtags(
                        *stytags, *kwargs.pop("twsty_tags", [])
                    )
                    super().__init__(*args, **kwargs)
                    self.kwargs = kwargs

                def stub(self):
                    return gen_Stub_DivMutable(
                        mutable_shell_type,
                        staticCore=self,
                        twsty_tags=self.twsty_tags,
                        **self.kwargs,
                    )
                    pass

                def add_twsty_tags(self, *args):
                    """
                    all twsty_tags modifications are stored in twsty_tags and then
                    passed to the mutable
                    """
                    self.twsty_tags = conc_twtags(*args, *self.twsty_tags)

            return WithStub

        case HCType.hcc_static_div:  # implies div is css mutable and contains mutable children
            static_core_mixins.append(TR.SvelteSafelistMixin)
            core_hc_type, mutable_shell_type = mutableClassTypeGen(
                hc_tag=hc_tag,
                hctag_mixin=hctype_mixin,
                is_childs_mutable=False,
                is_self_mutable=True,
                static_core_mixins=static_core_mixins

            )

            class WithStub(core_hc_type):
                def __init__(self, *args, **kwargs):
                    # The TwstyMixin is part of shell and not the core
                    stytags = []
                    if stytags_getter_func:
                        stytags = stytags_getter_func()

                    self.twsty_tags = conc_twtags(
                        *stytags, *kwargs.pop("twsty_tags", [])
                    )
                    super().__init__(*args, **kwargs)
                    self.kwargs = kwargs

                def stub(self):
                    return gen_Stub_DivMutable(
                        mutable_shell_type,
                        staticCore=self,
                        twsty_tags=self.twsty_tags,
                        **self.kwargs,
                    )
                    pass

            return WithStub
