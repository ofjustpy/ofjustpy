"""
Mutable types generated using HC_TF and Div_TF
"""
import logging

logger = logging.getLogger(__name__)

from py_tailwind_utils import (
    conc_twtags,
    jc,
    db,
    flx,
    H,
    screen,
    invisible,
    ppos,
    ovf,
    auto,
    dupdate,
    dnew,
    W,
    full,
    max as twmax,
    cc,
)

from py_tailwind_utils import db, flx
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine import mutable_TF_impl as mutable_TF_mixins
from . import ui_styles
from ofjustpy_engine.HCType import HCType

from .HC_TF import gen_HC_type
from .Div_TF import gen_Div_type
from typing import List, AnyStr, Callable, Any
from .SHC_types import PassiveComponents as PC

# Only buttons have static value attribute
Button = gen_HC_type(
    HCType.mutable,
    "Button",
    TR.ButtonMixin,
    mutableShell_addonMixins=[mutable_TF_mixins.StaticCoreSharer_ValueMixin],
    stytags_getter_func=lambda m=ui_styles: m.sty.button,
)

Circle = gen_HC_type(
    HCType.mutable,
    "Circle",
    TR.ButtonMixin,
    mutableShell_addonMixins=[mutable_TF_mixins.StaticCoreSharer_ValueMixin],
    stytags_getter_func=lambda m=ui_styles: m.sty.circle,
)

Label = gen_HC_type(
    HCType.mutable,
    "Label",
    TR.LabelMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.label,
)

Span = gen_HC_type(
    HCType.mutable,
    "Span",
    TR.SpanMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.span,
)

TextInput = gen_HC_type(
    HCType.mutable,
    "TextInput",
    TR.TextInputMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.input,
)


class ChartJSBaseMixin:
    # There is nothing in the static
    # core for mutable chart
    # everything belongs to mutable shell
    def __init__(self, *args, **kwargs):
        pass


class ChartJSMixin:
    vue_type = "ChartJS"

    # chart_types = [] #TODO
    def __init__(self, *args, **kwargs):
        # self.cjs_cfg = kwargs.get('cjs_cfg')

        self.chart_name = kwargs.get("chart_name")
        self.domDict.cjs_cfg = kwargs.get("cjs_cfg")
        self.domDict.vue_type = "ChartJS"
        self.domDict.class_name = "ChartJS"
        # self.domDict.chart_type = self.cjs_cfg.type
        # self.domDict.chart_options = self.cjs_cfg.options
        # self.domDict.chart_data = self.cjs_cfg.data
        self.domDict.canvas_id = self.id  # "canvas_" + self.chart_name

    def update_chart(self, spath, value):
        # we might have to update the domDict as well
        try:
            dnew(self.domDict.cjs_cfg, spath, value)

            # print(
            #     f"--------------------------------------> called update chart with {spath} ",
            #     id(self),
            # )

        except Exception as e:
            # uvicorn runtime without Crash can eat up exception
            print("exception in chart_update ", e)
            raise e

    # def update_chart_debug(self):
    #     spath = "/options/scales/x/title/text"
    #     dnew(self.cjs_cfg, spath, "new_title")


ChartJS = gen_HC_type(
    HCType.mutable,
    "ChartJS",
    hctag_mixin=ChartJSBaseMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.chartjs,
    mutableShell_addonMixins=[ChartJSMixin],
)


# div's css and child both are mutable
Div = gen_Div_type(HCType.mutable, "Div", TR.DivMixin)
StackH = gen_Div_type(
    HCType.mutable,
    "Div",
    TR.DivMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.stackh,
)
StackV = gen_Div_type(
    HCType.mutable,
    "StackV",
    TR.DivMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.stackv,
)


class StackDMixin:
    """
    create visual stack over components. Only one component is visible.
    The deck components have to be mutable.
    height_anchor_key: The key of the component which will determine the
    height of the deck.This is required to keep the height unchanged
    when it is shuffled.
    """

    svelte_safelist = [W/full, H/twmax, ovf/auto, ppos.absolute, invisible]
    
        
    attr_tracked_keys = []
    domDict_tracked_keys = []

    def __init__(self, *args, **kwargs):
        height_anchor_key = kwargs.get("height_anchor_key")

        for dbref in self.components:
            if dbref.staticCore.key == height_anchor_key:
                dbref.add_twsty_tags(W / full, H / twmax)
            else:
                dbref.add_twsty_tags(W / full, H / twmax, ovf / auto, ppos.absolute)
            dbref.add_twsty_tags(invisible)
        self.selected_card_spath = self.components[0].id
        selected_dbref = self.spathMap[self.selected_card_spath]
        selected_dbref.remove_twsty_tags(invisible)

    def bring_to_front(self, spath):
        """
        spath: the target component which needs to be brought in front
        """
        tapk = spath
        if tapk in self.spathMap.keys():
            # hide the current front
            self.spathMap[self.selected_card_spath].add_twsty_tags(invisible)
            # make the selected card visible
            selected_dbref = self.spathMap[tapk]
            selected_dbref.remove_twsty_tags(invisible)
            self.selected_card_spath = tapk

        else:
            logger.debug(
                f"debug: deck  does not have card {spath}..skipping bring to front"
            )
        pass


class StackDSvelteSafelist:
    """
    """
    svelte_safelist = [W/full, H/twmax, ovf/auto, ppos.absolute, invisible]

    def __init__(self, *args, **kwargs):
        pass
    
StackD = gen_Div_type(
    div_type=HCType.mutable,
    hc_tag="StackD",
    hctype_mixin=TR.DivMixin,
    static_core_mixins = [StackDSvelteSafelist],
    mutable_shell_mixins=[StackDMixin],
    
    stytags_getter_func=lambda m=ui_styles: [db.f, flx.one, ppos.relative],
)


class FormShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []

    def __init__(self, *args, **kwargs):

        # register the input value for all the input components
        # within this form
        self.input_component_value_map = {}
        pass

    def register_new_input(self, key, value):
        """ """
        self.input_component_value_map[key] = value

    pass


FormBase = gen_Div_type(
    div_type=HCType.mutable,
    hc_tag="Form",
    hctype_mixin=TR.FormMixin,
    mutable_shell_mixins=[FormShellMixin],
    stytags_getter_func=lambda m=ui_styles: m.sty.form,
)


def traverse(dbref):
    """
    traverse child/component hierarchy
    """
    if hasattr(dbref, "childs"):
        for c in dbref.childs:
            yield from traverse(c)
            if hasattr(c, "event_handlers"):
                yield c

    # active components has components to store child components
    if hasattr(dbref, "components"):
        for c in dbref.components:
            yield from traverse(c)
            if hasattr(c, "event_handlers"):
                yield c


def form_hook(ufunc):
    """
    a pre-hook called before user function is called.
    pre-hook will perform data validation before invoking user response
    """

    def validate_wrapper(dbref, msg, to_shell_target):
        # print("invoking from pre-hook")
        for c in traverse(dbref):
            # TODO: look for data-validators in c and
            # verify its input
            
            pass
        return ufunc(dbref, msg, to_shell_target)
        pass

    return validate_wrapper


class Form(FormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, event_prehook=form_hook, **kwargs)

        def eh_hook(ufunc):
            def redirector(dbref, msg, target_of):
                print("hooked in event_handler")
                print("we should call ufunc")

                # locate form_mutable_shell to hold the value
                ms = target_of(self)
                if "value" in msg.keys():
                    ms.register_new_input(dbref.id, msg.value)
                elif "checked" in msg.keys():
                    ms.register_new_input(dbref.id, msg.checked)
                print(ms.input_component_value_map)
                ufunc(dbref, msg, target_of)

            return redirector

        for input_component in traverse(self):
            input_component.add_prehook(eh_hook)


Container = gen_Div_type(
    div_type=HCType.mutable,
    hc_tag="Container",
    hctype_mixin=TR.DivMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.container,
)


class HCCStatic:
    # div's css is mutable but childs are static
    Div = gen_Div_type(HCType.hcc_static_div, "HCCStaticDiv", TR.DivMixin)
    StackV = gen_Div_type(
        HCType.hcc_static_div,
        "HCCStaticDiv",
        TR.DivMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.stackv,
    )


class HCCMutable:
    # The div css is static; but childs are mutable;
    Div = gen_Div_type(HCType.hcc_mutable_div, "HCCMutableDiv", TR.DivMixin)
    StackV = gen_Div_type(
        HCType.hcc_mutable_div,
        "Div",
        TR.DivMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.stackv,
    )

    StackH = gen_Div_type(
        HCType.hcc_mutable_div,
        "Div",
        TR.DivMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.stackh,
    )

    StackW = gen_Div_type(
        HCType.hcc_mutable_div,
        "Div",
        TR.DivMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.stackw,
    )

    Container = gen_Div_type(
        HCType.hcc_mutable_div,
        "Div",
        TR.DivMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.container,
    )

    def Halign(content, align="center", **kwargs):
        """ """
        twsty_tags = conc_twtags(
            *ui_styles.sty.halign(align), *kwargs.pop("twsty_tags", [])
        )
        return HCCMutable.Div(childs=[content], twsty_tags=twsty_tags)

    def Subsection(
        heading_text: AnyStr, content: Callable, align="center", twsty_tags=[], **kwargs
    ):
        return HCCMutable.StackV(
            twsty_tags=twsty_tags,
            childs=[
                PC.SubheadingBanner(heading_text),
                HCCMutable.Halign(content, align=align),
            ],
        )

    def Subsubsection(
        heading_text: AnyStr,
        content: Callable,
        twsty_tags: List = [],
        align="center",
        **kwargs,
    ):
        return HCCMutable.StackV(
            twsty_tags=twsty_tags,
            childs=[
                PC.SubsubheadingBanner(heading_text),
                HCCMutable.Halign(content, align=align),
            ],
        )
