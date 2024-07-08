"""
Provide impl for advanced components like Slider,
and ColorSelector

"""
from ofjustpy_engine import HC_Div_type_mixins as TR
from py_tailwind_utils import *
from ofjustpy_engine.HCType import HCType
from .Div_TF import gen_Div_type
from ofjustpy_engine.static_core_tracker import id_assigner
from ofjustpy import ui_styles

def assign_id(hc_gen):
    """
    hc_gen: html component generator
    """

    @id_assigner
    def func(*args, **kwargs):
        return hc_gen(*args, **kwargs)

    return func


# ============================ Slider impl ===========================
class MutableShell_SliderMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        self.selected_circle = None


SliderBase = gen_Div_type(
    HCType.mutable,
    "Slider",
    TR.DivMixin,
    static_core_mixins=[],
    mutable_shell_mixins=[MutableShell_SliderMixin],
    stytags_getter_func = lambda m = ui_styles: m.sty.slider
)


def on_circle_click(dbref, msg, target_of, slider_core=None):
    slider = target_of(slider_core)

    if slider.selected_circle is not None:
        slider.selected_circle.remove_twsty_tags(
            #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
            #shadow.xl2, boxshadow/red/500
            opacity/25
        )
        pass

    slider.selected_circle = dbref
    slider.selected_circle.add_twsty_tags(
        #bg/white, text/gray/8
        #outlinesty._, outline/blue/9, outline/2
        #boxtopo.ring,  ring/2, ring/offset/4, ring/red/500
        #shadow.xl2 , boxshadow/red/500
        opacity/25
    )
    # call the slider div registed function
    slider.app_value = dbref.staticCore.value

    pass


def event_prehook(on_event_callback):
    def hook(dbref, msg, target_of):
        msg.value = dbref.app_value
        return on_event_callback(dbref, msg, target_of)

    return hook


# ================================ end ===============================


class MutableShell_CSMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []

    def __init__(self, *args, **kwargs):
        self.mcs_value = None
        self.scs_value = None
        self.cs_value = None
        # at begining neither mcs, or scs are clicked
        self.component_clicked = None
        pass

    def update_slider(self, colortag):
        """
        scs: the shade selector
        """

        # ColorSelector has 2 components
        # 1: mcs
        # 2: scs
        scs = self.components[1]

        for shade_btn in scs.components:
            shid = int(shade_btn.value)
            new_color = bg / get_color_instance(colortag) / (shid* 100)
            shade_btn.add_twsty_tags(new_color)


# Create a Div type for ColorSelector

CSBase = gen_Div_type(
    HCType.mutable,
    "ColorSelector",
    TR.DivMixin,
    static_core_mixins=[],
    mutable_shell_mixins=[MutableShell_CSMixin],
)


def on_mcs_change(dbref, msg, target_of, cs_core=None):
    """
    the select drop down
    """
    print ("==>Main Selector change called")
    cs_shell = target_of(cs_core)
    cs_shell.mcs_value = msg.value
    cs_shell.component_clicked = "mcs"
    
    pass


def on_scs_click(dbref, msg, target_of, cs_core=None):
    """
    state update when shade is choosen in the selector
    """
    cs_shell = target_of(cs_core)
    cs_shell.scs_value = int(msg.value)

    cs_shell.component_clicked = "scs"
    pass


def CS_event_prehook(on_event_callback):
    def hook(cs_shell, msg, target_of):

        if cs_shell.component_clicked == "mcs":
            cs_shell.update_slider(cs_shell.mcs_value)

        if cs_shell.component_clicked == "scs":
            cs_shell.cs_value = twcc2hex[cs_shell.mcs_value][
                onetonine[cs_shell.scs_value]
            ]
        msg["value"] = cs_shell.cs_value
        # call the user registered event handler
        return on_event_callback(cs_shell, msg, target_of)

    return hook


# ================================ end ===============================
