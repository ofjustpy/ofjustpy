"""
 Static (Passive and active) types generated using Stub_HC_TF
"""
from ofjustpy_engine import HC_Div_type_mixins as TR

from .composed_SHC import generator as HC_generator
from .Div_TF import gen_Div_type
from .HC_TF import gen_HC_type
from .HC_TF import HCType
from .ofjustpy_utils import traverse_component_hierarchy
from .ui_styles import sty
from . import ui_styles

class PassiveComponents:
    Label = gen_HC_type(HCType.passive, "Label", TR.LabelMixin,
                        stytags_getter_func = lambda m=ui_styles: m.sty.label
                        )

    Span = gen_HC_type(HCType.passive,
                       "Span",
                       TR.SpanMixin,
                       stytags_getter_func = lambda m=ui_styles: m.sty.span
                       )
    Code = gen_HC_type(HCType.passive, "Code", TR.CodeMixin,
                        stytags_getter_func=lambda m=ui_styles: m.sty.code)

    Pre = gen_HC_type(HCType.passive, "Pre", TR.PreMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.pre)
    
    Li = gen_HC_type(HCType.passive, "Li", TR.LiMixin,
                     stytags_getter_func = lambda m=ui_styles: m.sty.li
                     )

    P = gen_HC_type(HCType.passive, "P",
                    TR.PMixin,
                    stytags_getter_func = lambda m=ui_styles: m.sty.P
                    )

    Prose = gen_HC_type(HCType.passive, "P", TR.PMixin,
                        stytags_getter_func = lambda m=ui_styles: m.sty.prose
                        )

    Option = gen_HC_type(HCType.passive, "Option", TR.OptionMixin,
                         stytags_getter_func = lambda m=ui_styles: m.sty.prose
                         )

    Hr = gen_HC_type(HCType.passive, "Hr", TR.HrMixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.hr)

    Img = gen_HC_type(HCType.passive, "Img", TR.ImgMixin,
                      stytags_getter_func=lambda m=ui_styles: m.sty.img)

    H1 = gen_HC_type(HCType.passive, "H1", TR.H1Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h1)

    H2 = gen_HC_type(HCType.passive, "H2", TR.H2Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h2)

    H3 = gen_HC_type(HCType.passive, "H3", TR.H3Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h3)

    H4 = gen_HC_type(HCType.passive, "H4", TR.H4Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h4)

    H5 = gen_HC_type(HCType.passive, "H5", TR.H5Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h5)

    H6 = gen_HC_type(HCType.passive, "H6", TR.H6Mixin,
                     stytags_getter_func=lambda m=ui_styles: m.sty.h6)
    
    A = gen_HC_type(HCType.passive, "A", TR.AMixin, stytags_getter_func=lambda
                    m=ui_styles: m.sty.A)


    # Div component types
    Div = gen_Div_type()
    Container = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.container)

    LabelDiv = gen_Div_type(HCType.passive, "Label", TR.LabelMixin,
                            stytags_getter_func=lambda m=ui_styles: m.sty.label)

    StackV = gen_Div_type(stytags_getter_func=lambda m=ui_styles:
                          m.sty.stackv)

    StackH = gen_Div_type(stytags_getter_func=lambda m=ui_styles:
                          m.sty.stackh)

    StackW = gen_Div_type(stytags_getter_func=lambda m=ui_styles:
                          m.sty.stackw)

    Ul = gen_Div_type(HCType.passive, "Ul", TR.UlMixin,
                      stytags_getter_func=lambda m=ui_styles: m.sty.ul)

    # for PyCodeFormatter we need PreDiv/CodeDiv so that new lines are rendered
    # as newlines
    CodeDiv = gen_Div_type(HCType.passive, "Code", TR.CodeMixin,
                        stytags_getter_func=lambda m=ui_styles: m.sty.code)

    PreDiv = gen_Div_type(HCType.passive, "Pre", TR.PreMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.pre)
    Collapsible = gen_Div_type(HCType.passive, "Collapsible", TR.CollapsibleMixin,
                               stytags_getter_func=lambda m=ui_styles: m.sty.collapsible)


    # ChartJS  = gen_HC_type(HCType.passive, "ChartJS", TR.ChartJSMixin,
    #                        stytags=sty.chartjs
    #                   )



    Nav = gen_Div_type(HCType.passive, "Nav", TR.NavMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.nav)

    Footer = gen_Div_type(HCType.passive, "Footer", TR.FooterMixin,
                          stytags_getter_func=lambda m=ui_styles: m.sty.footer)


    (
        Halign,
        Valign,
        SubheadingBanner,
        SubsubheadingBanner,
        Subsection,
        Subsubsection,
        Title,
        SubTitle,
        StackG,
        TitledPara,
    ) = HC_generator(Span, StackV, Div, H3, Prose)


class ActiveComponents:
    Span = gen_HC_type(HCType.active, "Span", TR.SpanMixin, 
                       stytags_getter_func = lambda m=ui_styles: m.sty.button
                       )

    Button = gen_HC_type(HCType.active, "Button", TR.ButtonMixin, 
                         stytags_getter_func = lambda m=ui_styles: m.sty.button
                         )
    TextInput = gen_HC_type(HCType.active,
                            "TextInput",
                            TR.TextInputMixin,
                            stytags_getter_func = lambda m=ui_styles: m.sty.input
    )

    Img = gen_HC_type(HCType.active,
                      "Img",
                      TR.ImgMixin,
                      stytags_getter_func = lambda m=ui_styles: m.sty.input
                      )

    # ========================= CheckboxInput ========================
    def cb_hook(ufunc):
        """
        a wrapper over user event handler to
        update msg.value with checked value
        """

        def wrapper(dbref, msg, to_shell):
            print("cb_hook wrapper invoked")

            msg.value = msg.checked
            return ufunc(dbref, msg, to_shell)

        return wrapper

    CheckboxInputBase = gen_HC_type(HCType.active,
                                    "CheckboxInput",
                                    TR.CheckboxInputMixin,
                                    stytags_getter_func = lambda m=ui_styles: m.sty.input
    )

    class CheckboxInput(CheckboxInputBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, event_prehook=ActiveComponents.cb_hook, **kwargs)

    Textarea = gen_HC_type(HCType.active,
                           "Textarea",
                           TR.TextareaMixin,
                           stytags_getter_func = lambda m=ui_styles: m.sty.input

    )
    Div = gen_Div_type(HCType.active, hc_tag="ActiveDiv")
    StackH = gen_Div_type(stytags_getter_func=lambda m=ui_styles:
                          m.sty.stackh, hc_tag="AStackH")
    Select = gen_Div_type(HCType.active,
                          "Select",
                          TR.SelectInputMixin, 
                          stytags_getter_func = lambda m=ui_styles: m.sty.select
                          )

    def form_hook(ufunc):
        """
        a pre-hook called before user function is called.
        pre-hook will perform data validation before invoking user response
        """

        def validate_wrapper(dbref, msg, to_shell_target):
            print("invoking from pre-hook")
            print("num comps = ", len(dbref.components))
            print(type(dbref))
            # for citem in dbref.components:
            for citem, pitem in traverse_component_hierarchy(dbref):
                if hasattr(citem, "key"):
                    print(citem.key, " ", citem, " ")
                    print(msg.value)
                    if hasattr(citem, "data_validators"):
                        print("child has data_validator ", citem.data_validators)

            return ufunc(dbref, msg, to_shell_target)
            pass

        return validate_wrapper

    FormBase = gen_Div_type(HCType.active,
                            "Form",
                            TR.FormMixin,
                            stytags_getter_func = lambda m=ui_styles: m.sty.form
                            )

    class Form(FormBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, event_prehook=ActiveComponents.form_hook, **kwargs)
            for citem, pitem in traverse_component_hierarchy(self):
                if hasattr(citem, "key"):
                    print(citem.key, " ", citem, " ")
                    if hasattr(citem, "data_validators"):
                        print("child has data_validator ", citem.data_validators)

    #HTTP request callback for A component
    class A_HTTPRequestCallbackMixin:
        def __init__(self, *args, **kwargs):
            self.href_builder = kwargs.get('href_builder', None)
            pass

        def request_callback(self, session_manager, *args, **kwargs):
            if self.href_builder:
                self.href_builder(self, session_manager)
            pass
        
    A = gen_HC_type(HCType.active, "A", TR.AMixin,
                    stytags_getter_func = lambda m=ui_styles: m.sty.A,
                    http_request_callback_mixin = A_HTTPRequestCallbackMixin
                    )

    Switch = gen_HC_type(HCType.active, "Switch", TR.SwitchMixin,
                         stytags_getter_func = lambda m=ui_styles: []
                         )
    

    pass
