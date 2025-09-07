from .parse_svg_component import parse as parse_svg_component
from .HC_TF import gen_HC_type
from ofjustpy_engine.HCType import HCType
from ofjustpy_engine import HC_Div_type_mixins as TR
from . import ui_styles

class fontawesomeBaseComponentMixin:
    def __init__(self, *args, **kwargs):
        """

        """
        self.domDict.vue_type = "fontawesome_component"

        self.domDict.events = []
        self.domDict.show = kwargs.get("show", True)
        self.domDict.debug = kwargs.get("debug", False)
        pass



class updateFAClasses:
    """
    post process to apply fontawesome classes to self.domDict.classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        """
        self.update_extra_classes("svg-inline--fa fa-user fa-fw fa-2x")

        pass
        
    
    
FontAwesomeIcon = gen_HC_type(HCType.passive,
                              "FontAwesomeIcon",
                              TR.FontAwesomeIconMixin,
                              stytags_getter_func=lambda m=ui_styles: m.sty.fontawesome,
                              baseComponentMixinType = fontawesomeBaseComponentMixin,
                              static_addon_mixins = [updateFAClasses]
                              )

class lucideBaseComponentMixin:
    def __init__(self, *args, **kwargs):
        """

        """
        self.domDict.vue_type = "lucide_component"

        self.domDict.events = []
        self.domDict.show = kwargs.get("show", True)
        self.domDict.debug = kwargs.get("debug", False)
        pass

    
LucideIcon = gen_HC_type(HCType.passive,
                              "LucideIcon",
                              TR.LucideIconMixin,
                              stytags_getter_func=lambda m=ui_styles: m.sty.lucide,
                              baseComponentMixinType = lucideBaseComponentMixin,
                              )
