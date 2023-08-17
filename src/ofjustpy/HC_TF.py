"""
A generator for   non-Div HC component types.
passive, active, mutable components types can be created with
options for other mixins
"""
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine import SHC_types_mixin as SCmixin
from ofjustpy_engine.mutable_HC_TF import classTypeGen as mutableClassTypeGen
from py_tailwind_utils import conc_twtags, tstr
from . import ui_styles

from .TF_impl import gen_Stub_HCActive
from .TF_impl import HCType
from .TF_impl import Stub_HCMutable
from .TF_impl import Stub_HCPassive
from .tracker import trackStub


def gen_HC_type(
    hc_type,
    hc_tag,
    hctag_mixin,
    static_addon_mixins=[],
    staticCoreMixins=[TR.HCTextMixin],
    mutableShellMixins=[TR.TwStyMixin],
    staticCore_addonMixins=[],
    mutableShell_addonMixins=[],
        stytags_getter_func = None,
        **kwargs
):
    """
    static_addon_mixins: apply to passive/active components
    staticCoreMixins, mutableShellMixins apply only to mutable components
    staticCore_addonMixins, mutableShell_addonMixins: apply only to mutable components
    """

    match hc_type:
        case HCType.passive:
            hc_type = SCmixin.staticClassTypeGen(
                taglabel=hc_tag,
                tagtype=hctag_mixin,
                addon_mixins=static_addon_mixins,
                jsonMixinType=SCmixin.PassiveJsonMixin,
            )

            class WithStub(hc_type):
                """
                add stub generator for static objects
                """

                def __init__(self, *args, **kwargs):
                    assert stytags_getter_func
                    stytags = stytags_getter_func()
                    twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                    super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

                def stub(self):
                    return Stub_HCPassive(target=self)

            return WithStub

        case HCType.active:
            hc_type = SCmixin.staticClassTypeGen(
                hc_tag,
                tagtype=hctag_mixin,
                jsonMixinType=SCmixin.JsonMixin,
                attach_event_handling=True,
                addon_mixins=static_addon_mixins,
                **kwargs
            )

            class WithStub(hc_type):
                def __init__(self, *args, **kwargs):
                    assert stytags_getter_func
                    stytags = stytags_getter_func()
                    twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                    super().__init__(*args, **kwargs, twsty_tags=twsty_tags)

                def stub(self):
                    return gen_Stub_HCActive(target=self)

            return WithStub

        case HCType.mutable:
            core_hc_type, mutable_shell_type = mutableClassTypeGen(
                hc_tag,
                hctag_mixin,
                staticCoreMixins=staticCoreMixins,
                mutableShellMixins=mutableShellMixins,
                staticCore_addonMixins=staticCore_addonMixins,
                mutableShell_addonMixins=mutableShell_addonMixins,
            )

            @trackStub
            def genStub(**kwargs):
                assert stytags_getter_func
                stytags = stytags_getter_func()
                twsty_tags = conc_twtags(*stytags, *kwargs.pop("twsty_tags", []))
                return Stub_HCMutable(mutable_shell_type,
                                      twsty_tags=twsty_tags,
                                      **kwargs
                                      )

            class WithStub(core_hc_type):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.kwargs = kwargs

                def stub(self):
                    return genStub(staticCore=self, **self.kwargs)
                    pass

            return WithStub

        case _:
            assert False
