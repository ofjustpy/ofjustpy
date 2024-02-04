"""
 Static (Passive and active) types generated using Stub_HC_TF
"""
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.HCType import HCType
from .composed_SHC import generator as HC_generator
from .Div_TF import gen_Div_type
from ofjustpy.HC_TF import gen_HC_type

from .ofjustpy_utils import traverse_component_hierarchy
from .ui_styles import sty
from . import ui_styles


class PassiveDivs:
    Label = gen_Div_type(
        HCType.passive,
        "Label",
        TR.LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.label,
        static_addon_mixins = [TR.HCTextMixin]  
    )
        
    Span = gen_Div_type(
        HCType.passive,
        "Span",
        TR.SpanMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Br = gen_Div_type(
        HCType.passive,
        "Br",
        TR.BrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.br,
        static_addon_mixins = [TR.HCTextMixin]  
    )
    
    Strong = gen_Div_type(
        HCType.passive,
        "Strong",
        TR.StrongMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
        static_addon_mixins = [TR.HCTextMixin]
        
    )
    Code = gen_Div_type(
        HCType.passive,
        "Code",
        TR.CodeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.code,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Pre = gen_Div_type(
        HCType.passive,
        "Pre",
        TR.PreMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.pre,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Li = gen_Div_type(
        HCType.passive,
        "Li",
        TR.LiMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.li,
        static_addon_mixins = [TR.HCTextMixin]  
    )


    P = gen_Div_type(
        HCType.passive,
        "P",
        TR.PMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.P,
        static_addon_mixins = [TR.HCTextMixin]  
        
    )

    Prose = gen_Div_type(
        HCType.passive,
        "P",
        TR.PMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.prose,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Option = gen_Div_type(
        HCType.passive,
        "Option",
        TR.OptionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.prose,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Hr = gen_Div_type(
        HCType.passive,
        "Hr",
        TR.HrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.hr,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Time = gen_Div_type(
        HCType.passive,
        "Time",
        TR.TimeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.time,
        static_addon_mixins = [TR.HCTextMixin],

    )

    Img = gen_Div_type(
        HCType.passive,
        "Img",
        TR.ImgMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.img,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H1 = gen_Div_type(
        HCType.passive,
        "H1",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h1,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H1Div = gen_Div_type(
        HCType.passive,
        "H1Div",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h1,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H2Div = gen_Div_type(
        HCType.passive,
        "H2Div",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h2,
        static_addon_mixins = [TR.HCTextMixin]
    )
    ScriptDiv = gen_Div_type(
    HCType.passive,
    "ScriptDiv",
    TR.ScriptMixin,  
    stytags_getter_func=lambda m=ui_styles: m.sty.script,  
    static_addon_mixins=[TR.HCTextMixin]  
    )

    BlockquoteDiv = gen_Div_type(
        HCType.passive,
        "BlockquoteDiv",
        TR.BlockquoteMixin,  # Assuming you have the BlockquoteMixin class
        stytags_getter_func=lambda m=ui_styles: m.sty.blockquote,  # Adjust as needed
        static_addon_mixins=[TR.HCTextMixin]  # Assuming you want to retain text styling
    )

    H2 = gen_Div_type(
        HCType.passive,
        "H2",
        TR.H2Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h2,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H3 = gen_Div_type(
        HCType.passive,
        "H3",
        TR.H3Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h3,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H3Div = gen_Div_type(
        HCType.passive,
        "H3",
        TR.H3Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h3,
        static_addon_mixins = [TR.HCTextMixin],
    )

        
    H4 = gen_Div_type(
        HCType.passive,
        "H4",
        TR.H4Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h4,
        static_addon_mixins = [TR.HCTextMixin],
    )

    H5 = gen_Div_type(
        HCType.passive,
        "H5",
        TR.H5Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h5,
        static_addon_mixins = [TR.HCTextMixin],
    )

    H6 = gen_Div_type(
        HCType.passive,
        "H6",
        TR.H6Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h6,
        static_addon_mixins = [TR.HCTextMixin],
    )

    A = gen_Div_type(
        HCType.passive,
        "A",
        TR.AMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.A,
        static_addon_mixins = [TR.HCTextMixin],
        
    )

    Legend = gen_Div_type(
        HCType.passive,
        "Legend",
        TR.LegendMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.legend,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Small = gen_Div_type(
        HCType.passive,
        "Small",
        TR.SmallMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.small,
        static_addon_mixins = [TR.HCTextMixin],
    )
    
    # Div component types
    Div = gen_Div_type(        static_addon_mixins = [TR.HCTextMixin])
    Container = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.container,
                             static_addon_mixins = [TR.HCTextMixin],
                             )

    LabelDiv = gen_Div_type(
        HCType.passive,
        "Label",
        TR.LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.label,
        static_addon_mixins = [TR.HCTextMixin],
    )

    SpanDiv = gen_Div_type(
        HCType.passive,
        "Span",
        TR.SpanMixin,
        static_addon_mixins = [TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.span,

    )
    
    PDiv = gen_Div_type(
        HCType.passive,
        "Span",
        TR.PMixin,
        static_addon_mixins = [TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.p,
    )
        

    

    StackV = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackv)

    StackH = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackh)

    StackW = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackw)

    Ul = gen_Div_type(
        HCType.passive,
        "Ul",
        TR.UlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ul,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Ol = gen_Div_type(
        HCType.passive,
        "Ol",
        TR.OlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ol,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Li = gen_Div_type(
        HCType.passive,
        "Li",
        TR.LiMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.li,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Dl = gen_Div_type(
        HCType.passive,
        "Dl",
        TR.DlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dl,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Ul = gen_Div_type(
        HCType.passive,
        "Ul",
        TR.UlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ul,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Optgroup = gen_Div_type(
        HCType.passive,
        "Optgroup",
        TR.OptgroupMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.optgroup,
        static_addon_mixins = [TR.HCTextMixin],
    )


    Details = gen_Div_type(
        HCType.passive,
        "Details",
        TR.DetailsMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.details,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Summary = gen_Div_type(
        HCType.passive,
        "Summary",
        TR.SummaryMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.summary,
        static_addon_mixins = [TR.HCTextMixin],
    )
    
    Datalist = gen_Div_type(
        HCType.passive,
        "Datalist",
        TR.DatalistMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.datalist,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Dt = gen_Div_type(
        HCType.passive,
        "Dt",
        TR.DtMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dt,
        static_addon_mixins = [TR.HCTextMixin],
    )

    DtDiv = gen_Div_type(
        HCType.passive,
        "Dt",
        TR.DtMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dt,
        static_addon_mixins = [TR.HCTextMixin],
    )
    
    DdDiv = gen_Div_type(
        HCType.passive,
        "Dd",
        TR.DdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dd,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Dd = gen_Div_type(
        HCType.passive,
        "Dd",
        TR.DdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dd,
        static_addon_mixins = [TR.HCTextMixin],
    )
    

    # for PyCodeFormatter we need PreDiv/CodeDiv so that new lines are rendered
    # as newlines
    CodeDiv = gen_Div_type(
        HCType.passive,
        "Code",
        TR.CodeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.code,
        static_addon_mixins = [TR.HCTextMixin],
    )

    PreDiv = gen_Div_type(
        HCType.passive,
        "Pre",
        TR.PreMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.pre,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Collapsible = gen_Div_type(
        HCType.passive,
        "Collapsible",
        TR.CollapsibleMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.collapsible,
        static_addon_mixins = [TR.HCTextMixin],
    )

    # ChartJS  = gen_Div_type(HCType.passive, "ChartJS", TR.ChartJSMixin,
    #                        stytags=sty.chartjs
    #                   )

    Nav = gen_Div_type(
        HCType.passive,
        "Nav",
        TR.NavMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.nav,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Section = gen_Div_type(
        HCType.passive,
        "section",
        TR.SectionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.section,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Footer = gen_Div_type(
        HCType.passive,
        "Footer",
        TR.FooterMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.footer,
         static_addon_mixins = [TR.HCTextMixin],

    )

    Header = gen_Div_type(
        HCType.passive,
        "Header",
        TR.HeaderMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.header,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Aside = gen_Div_type(
        HCType.passive,
        "Aside",
        TR.AsideMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.aside,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Article = gen_Div_type(
        HCType.passive,
        "Article",
        TR.ArticleMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.article,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Main = gen_Div_type(
        HCType.passive,
        "Main",
        TR.MainMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.main,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Fieldset = gen_Div_type(
        HCType.passive,
        "Fieldset",
        TR.FieldsetMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.fieldset,
        static_addon_mixins = [TR.HCTextMixin],
    )


    Tr = gen_Div_type(
        HCType.passive,
        "Tr",
        TR.TrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tr,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Table = gen_Div_type(
        HCType.passive,
        "Table",
        TR.TableMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.table,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Thead = gen_Div_type(
        HCType.passive,
        "Thead",
        TR.TheadMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.thead,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Td = gen_Div_type(
        HCType.passive,
        "Td",
        TR.TdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.td,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Th = gen_Div_type(
        HCType.passive,
        "Th",
        TR.ThMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.th,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Address = gen_Div_type(
        HCType.passive,
        "Address",
        TR.AddressMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.address,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Tbody = gen_Div_type(
        HCType.passive,
        "Tbody",
        TR.TbodyMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tbody,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Img = gen_HC_type(
        HCType.passive,
        "Img",
        TR.ImgMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.img,
    )
    Legend = gen_HC_type(
        HCType.passive,
        "Legend",
        TR.LegendMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.legend,
    )
    Small = gen_HC_type(
        HCType.passive,
        "Small",
        TR.SmallMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.small,
    )
    Th = gen_Div_type(
        HCType.passive,
        "Th",
        TR.ThMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.th,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Td = gen_Div_type(
        HCType.passive,
        "Td",
        TR.TdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.td,
        static_addon_mixins = [TR.HCTextMixin],
    )

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
        

class PassiveComponents:
    
    from .icons import (
    Icon_Cog,
    Icon_Teams,
    Icon_Billing,
    Icon_Invoices,
    Icon_Account,
    Icon_Menu,
    Icon_Chevronright,
    Icon_Chevrondown,
    Icon_PaginationLeft,
    Icon_PaginationRight,
    Icon_Minus,
    Icon_EncircledCheckmark,
    Icon_Cross,
    Icon_Preview,
    Icon_Warning,
    Icon_EuroCurrency,
    Icon_BreadcrumbSepArrow,
    Icon_Home,
    Icon_Edit,
    Icon_View,
    Icon_Delete,
    Icon_Emailat,
    Icon_Search,
        Icon_HeartCircle,
        Icon_Facebook,
        Icon_Instagram,
        Icon_Twitter,
        Icon_GitHub,
        Icon_Dribble,
        Icon_ShoutOut,
        Icon_Plus,
        Icon_RightArrow,
        Icon_Openlink,
        Icon_Notification,
        Icon_Squid,
        Icon_IncrementDecrement,
        Icon_ChartUp,
        Icon_ChartDown,
        Icon_PaperMoney,
        Icon_IdCard,
        Icon_AddressPin,
        Icon_PaymentCard,
        Icon_Chevronleft,
        Icon_Degree,
        Icon_Rated,
        Icon_SliderNext,
        Icon_SliderPrev
)
    Label = gen_HC_type(
        HCType.passive,
        "Label",
        TR.LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.label,
    )

    Span = gen_HC_type(
        HCType.passive,
        "Span",
        TR.SpanMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )

    Br = gen_HC_type(
        HCType.passive,
        "Br",
        TR.BrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.br,
    )
    Strong = gen_Div_type(
        HCType.passive,
        "Strong",
        TR.StrongMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
        static_addon_mixins = [TR.HCTextMixin]  
        
    )
    Code = gen_HC_type(
        HCType.passive,
        "Code",
        TR.CodeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.code,
    )

    Pre = gen_HC_type(
        HCType.passive,
        "Pre",
        TR.PreMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.pre,
    )

    Li = gen_HC_type(
        HCType.passive,
        "Li",
        TR.LiMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.li,
    )


    P = gen_HC_type(
        HCType.passive, "P", TR.PMixin, stytags_getter_func=lambda m=ui_styles: m.sty.P
    )

    Prose = gen_HC_type(
        HCType.passive,
        "P",
        TR.PMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.prose,
    )

    Option = gen_HC_type(
        HCType.passive,
        "Option",
        TR.OptionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.prose,
    )

    Hr = gen_HC_type(
        HCType.passive,
        "Hr",
        TR.HrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.hr,
    )

    Time = gen_Div_type(
        HCType.passive,
        "Time",
        TR.TimeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.time,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    Img = gen_HC_type(
        HCType.passive,
        "Img",
        TR.ImgMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.img,
    )

    H1 = gen_HC_type(
        HCType.passive,
        "H1",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h1,
    )

    H1Div = gen_Div_type(
        HCType.passive,
        "H1Div",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h1,
        static_addon_mixins = [TR.HCTextMixin]  
    )

    H2Div = gen_Div_type(
        HCType.passive,
        "H2Div",
        TR.H1Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h2,
        static_addon_mixins = [TR.HCTextMixin]  
    )
    ScriptDiv = gen_Div_type(
    HCType.passive,
    "ScriptDiv",
    TR.ScriptMixin,  
    stytags_getter_func=lambda m=ui_styles: m.sty.script,  
    static_addon_mixins=[TR.HCTextMixin]  
    )

    BlockquoteDiv = gen_Div_type(
        HCType.passive,
        "BlockquoteDiv",
        TR.BlockquoteMixin,  # Assuming you have the BlockquoteMixin class
        stytags_getter_func=lambda m=ui_styles: m.sty.blockquote,  # Adjust as needed
        static_addon_mixins=[TR.HCTextMixin]  # Assuming you want to retain text styling
    )



    H2 = gen_HC_type(
        HCType.passive,
        "H2",
        TR.H2Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h2,
    )

    H3 = gen_HC_type(
        HCType.passive,
        "H3",
        TR.H3Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h3,
    )

    H3Div = gen_Div_type(
        HCType.passive,
        "H3",
        TR.H3Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h3,
        static_addon_mixins = [TR.HCTextMixin]  
    )

        
    H4 = gen_HC_type(
        HCType.passive,
        "H4",
        TR.H4Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h4,
    )

    H5 = gen_HC_type(
        HCType.passive,
        "H5",
        TR.H5Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h5,
    )

    H6 = gen_HC_type(
        HCType.passive,
        "H6",
        TR.H6Mixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.h6,
    )

    A = gen_HC_type(
        HCType.passive, "A", TR.AMixin, stytags_getter_func=lambda m=ui_styles: m.sty.A
    )

    Legend = gen_HC_type(
        HCType.passive,
        "Legend",
        TR.LegendMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.legend,
    )

    Small = gen_HC_type(
        HCType.passive,
        "Small",
        TR.SmallMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.small,
    )
    
    # Div component types
    Div = gen_Div_type()
    Container = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.container)

    LabelDiv = gen_Div_type(
        HCType.passive,
        "Label",
        TR.LabelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.label,
    )

    SpanDiv = gen_Div_type(
        HCType.passive,
        "Span",
        TR.SpanMixin,
        static_addon_mixins = [TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )
    PDiv = gen_Div_type(
        HCType.passive,
        "Span",
        TR.PMixin,
        static_addon_mixins = [TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.p,
    )
        

    

    StackV = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackv)

    StackH = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackh)

    StackW = gen_Div_type(stytags_getter_func=lambda m=ui_styles: m.sty.stackw)

    Ul = gen_Div_type(
        HCType.passive,
        "Ul",
        TR.UlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ul,
    )

    Ol = gen_Div_type(
        HCType.passive,
        "Ol",
        TR.OlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ol,
    )

    Li = gen_Div_type(
        HCType.passive,
        "Li",
        TR.LiMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.li,
    )

    Dl = gen_Div_type(
        HCType.passive,
        "Dl",
        TR.DlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dl,
    )

    Ul = gen_Div_type(
        HCType.passive,
        "Ul",
        TR.UlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.ul,
    )

    Optgroup = gen_Div_type(
        HCType.passive,
        "Optgroup",
        TR.OptgroupMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.optgroup,
    )


    Details = gen_Div_type(
        HCType.passive,
        "Details",
        TR.DetailsMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.details,
    )

    Summary = gen_Div_type(
        HCType.passive,
        "Summary",
        TR.SummaryMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.summary,
    )
    
    Datalist = gen_Div_type(
        HCType.passive,
        "Datalist",
        TR.DatalistMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.datalist,
    )

    Dt = gen_HC_type(
        HCType.passive,
        "Dt",
        TR.DtMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dt,
    )

    DtDiv = gen_Div_type(
        HCType.passive,
        "Dt",
        TR.DtMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dt,
    )
    
    DdDiv = gen_Div_type(
        HCType.passive,
        "Dd",
        TR.DdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dd,
    )
    Dd = gen_HC_type(
        HCType.passive,
        "Dd",
        TR.DdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.dd,
    )
    

    # for PyCodeFormatter we need PreDiv/CodeDiv so that new lines are rendered
    # as newlines
    CodeDiv = gen_Div_type(
        HCType.passive,
        "Code",
        TR.CodeMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.code,
    )

    PreDiv = gen_Div_type(
        HCType.passive,
        "Pre",
        TR.PreMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.pre,
    )
    Collapsible = gen_Div_type(
        HCType.passive,
        "Collapsible",
        TR.CollapsibleMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.collapsible,
    )

    # ChartJS  = gen_HC_type(HCType.passive, "ChartJS", TR.ChartJSMixin,
    #                        stytags=sty.chartjs
    #                   )

    Nav = gen_Div_type(
        HCType.passive,
        "Nav",
        TR.NavMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.nav,
    )

    Section = gen_Div_type(
        HCType.passive,
        "section",
        TR.SectionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.section,
    )

    Footer = gen_Div_type(
        HCType.passive,
        "Footer",
        TR.FooterMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.footer,
         static_addon_mixins = [TR.HCTextMixin],
    )

    Header = gen_Div_type(
        HCType.passive,
        "Header",
        TR.HeaderMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.header,
    )

    Aside = gen_Div_type(
        HCType.passive,
        "Aside",
        TR.AsideMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.aside,
    )

    Article = gen_Div_type(
        HCType.passive,
        "Article",
        TR.ArticleMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.article,
    )
    Main = gen_Div_type(
        HCType.passive,
        "Main",
        TR.MainMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.main,
    )
    Fieldset = gen_Div_type(
        HCType.passive,
        "Fieldset",
        TR.FieldsetMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.fieldset,
    )


    Tr = gen_Div_type(
        HCType.passive,
        "Tr",
        TR.TrMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tr,
    )
    Table = gen_Div_type(
        HCType.passive,
        "Table",
        TR.TableMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.table,
    )

    Thead = gen_Div_type(
        HCType.passive,
        "Thead",
        TR.TheadMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.thead,
    )
    Td = gen_Div_type(
        HCType.passive,
        "Td",
        TR.TdMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.td,
        static_addon_mixins = [TR.HCTextMixin],
    )
    Th = gen_Div_type(
        HCType.passive,
        "Th",
        TR.ThMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.th,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Address = gen_Div_type(
        HCType.passive,
        "Address",
        TR.AddressMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.address,
        static_addon_mixins = [TR.HCTextMixin],
    )

    Tbody = gen_Div_type(
        HCType.passive,
        "Tbody",
        TR.TbodyMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tbody,
        static_addon_mixins = [TR.HCTextMixin],
    )

        
    
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
    Span = gen_HC_type(
        HCType.active,
        "Span",
        TR.SpanMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )

    Button = gen_HC_type(
        HCType.active,
        "Button",
        TR.ButtonMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
    TextInput = gen_HC_type(
        HCType.active,
        "TextInput",
        TR.TextInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
    )

    Img = gen_HC_type(
        HCType.active,
        "Img",
        TR.ImgMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
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

    CheckboxInputBase = gen_HC_type(
        HCType.active,
        "CheckboxInput",
        TR.CheckboxInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
    )

    class CheckboxInput(CheckboxInputBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, event_prehook=ActiveComponents.cb_hook, **kwargs)

    Textarea = gen_HC_type(
        HCType.active,
        "Textarea",
        TR.TextareaMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
    )
    Div = gen_Div_type(HCType.active, hc_tag="ActiveDiv")
    ButtonDiv = gen_Div_type(
        HCType.active,
        "ButtonDiv",
        TR.ButtonMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
    StackH = gen_Div_type(HCType.active,
                          stytags_getter_func=lambda m=ui_styles: m.sty.stackh,
                          hc_tag="AStackH"
                          )
    
    Select = gen_Div_type(
        HCType.active,
        "Select",
        TR.SelectInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.select,
    )

    # HTTP request callback for A component
    class A_HTTPRequestCallbackMixin:
        def __init__(self, *args, **kwargs):
            self.href_builder = kwargs.get("href_builder", None)
            pass

        def request_callback(self, session_manager, *args, **kwargs):
            if self.href_builder:
                self.href_builder(self, session_manager)
            pass

        
    A = gen_HC_type(
        HCType.active,
        "A",
        TR.AMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.A,
        http_request_callback_mixin=A_HTTPRequestCallbackMixin,
    )


    Switch = gen_HC_type(
        HCType.active,
        "Switch",
        TR.SwitchMixin,
        stytags_getter_func=lambda m=ui_styles: [],
    )

    Datalist = gen_Div_type(
        HCType.active,
        "Datalist",
        TR.DatalistMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.datalist,
        static_addon_mixins = [TR.HCTextMixin],
    )


    pass


class ActiveDivs:
    Select = gen_Div_type(
        HCType.active,
        "Select",
        TR.SelectInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.select,
    )
    
    class A_HTTPRequestCallbackMixin:
        def __init__(self, *args, **kwargs):
            self.href_builder = kwargs.get("href_builder", None)
            pass

        def request_callback(self, session_manager, *args, **kwargs):
            if self.href_builder:
                self.href_builder(self, session_manager)
            pass
        
    A = gen_Div_type(
        HCType.active,
        "A",
        TR.AMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.A,
        static_addon_mixins = [TR.HCTextMixin]
        #http_request_callback_mixin=A_HTTPRequestCallbackMixin,
    )
    TextInput = gen_Div_type(
        HCType.active,
        "TextInput",
        TR.TextInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
    )

    Textarea = gen_Div_type(
        HCType.active,
        "Textarea",
        TR.TextInputMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.input,
    )    
    Button = gen_Div_type(
        HCType.active,
        "ButtonDiv",
        TR.ButtonMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
        static_addon_mixins = [TR.HCTextMixin]
        
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

    FormBase = gen_Div_type(
        HCType.active,
        "Form",
        TR.FormMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.form,
    )

    class Form(FormBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, event_prehook=ActiveDivs.form_hook, **kwargs)
            for citem, pitem in traverse_component_hierarchy(self):
                if hasattr(citem, "key"):
                    print(citem.key, " ", citem, " ")
                    if hasattr(citem, "data_validators"):
                        print("child has data_validator ", citem.data_validators)

