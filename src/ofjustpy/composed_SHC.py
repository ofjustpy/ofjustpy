from typing import Any
from typing import AnyStr
from typing import Callable
from typing import List

from py_tailwind_utils import bg
from py_tailwind_utils import black
from py_tailwind_utils import cc
from py_tailwind_utils import conc_twtags
from py_tailwind_utils import db
from py_tailwind_utils import full
from py_tailwind_utils import fz
from py_tailwind_utils import get_color_instance
from py_tailwind_utils import green
from py_tailwind_utils import H
from py_tailwind_utils import hidden
from py_tailwind_utils import lv
from py_tailwind_utils import jc
from py_tailwind_utils import noop
from py_tailwind_utils import offset
from py_tailwind_utils import onetonine
from py_tailwind_utils import outline
from py_tailwind_utils import screen
from py_tailwind_utils import tstr
from py_tailwind_utils import twcc2hex
from py_tailwind_utils import variant
from py_tailwind_utils import W
from py_tailwind_utils import pd
from py_tailwind_utils import sl, st, sb, mr, fw, space, y


#from .ui_styles import sty
import ofjustpy as oj

def generator(Span, StackV, Div, H3, H5, Para,  PassiveDiv=None):
    """ """
    if not PassiveDiv:
        PassiveDiv = Div

    # Although there is a generic Halign in HC_wrappers.py
    # here we create one using the Div provided
    def Halign(content: Callable, align="center", twsty_tags=[], key=None, **kwargs):
        """
        tstub: target stub, i.e., the one needs to be aligned
        """
        target = PassiveDiv(
            twsty_tags=conc_twtags(*oj.ui_styles.sty.halign(align), *twsty_tags), childs=[content]
        )

        return target

    def Valign(
        content: Callable, height_tag=H / screen, align="center", twsty_tags=[], **kwargs
    ):
        """
        tstub: target stub, i.e., the one needs to be aligned
        """
        return PassiveDiv(
            childs=[content],
            twsty_tags=conc_twtags(*oj.ui_styles.sty.valign(align), height_tag, *twsty_tags),
            **kwargs,
        )

    def SubheadingBannerImpl(
            heading_text: AnyStr,
            twsty_tags: List = [],
            heading_text_sty = oj.ui_styles.sty.subheading_text,  #[fw.bold]
        **kwargs,
    ):
        spanl = Span(
            text=heading_text,
            twsty_tags=[
                pd/sl/2, pd/st/2, pd/sb/2, 
                # use exact 1/3 of overall space for large screen
                *variant(W / "1/3", rv="md"),
                # for small  screen use full width
                *variant(W / full, rv="sm:max-md"),
            ],
        )
        spanm = Span(
            text=heading_text,
            twsty_tags=[
                pd/sl/2, pd/st/2, pd/sb/2,
                lv.iv,
                *variant(W / "1/3", rv="md"),
                # hide for small screen; noop is required to
                # not pollute the hidden.modifier_chain
                *variant(noop / hidden, rv="sm:max-md"),
            ],
        )
        spanx = Span(
            text=heading_text,
            twsty_tags=[
                pd/sl/2, pd/st/2, pd/sb/2,
                lv.iv,
                *variant(W / "1/3", rv="md"),
                # hide for small screen; noop is required to
                # not pollute the hidden.modifier_chain
                *variant(noop / hidden, rv="sm:max-md"),
            ],
        )

        target = Div(
            twsty_tags=conc_twtags(*twsty_tags, mr/st/4, *heading_text_sty),
            childs=[spanl, spanm, spanx],
        )

        return target

    def SubheadingBanner(
        heading_text: AnyStr,
        twsty_tags: List = [],
            section_depth = 0,
        **kwargs,
    ):
        """
        subheading and subsubheading are same except:
        subheading is fw.bold
        subsubheading is fw.medium
        """

        section_title_sty = oj.ui_styles.sty.section_title_sty[section_depth]

        return SubheadingBannerImpl(
            heading_text,
            twsty_tags=twsty_tags,
            heading_text_sty=section_title_sty,
            **kwargs,
        )

    def Subsection(heading_text: AnyStr, content: Callable, align="center", twsty_tags=[],
                   childs = [],
                   section_depth = 0, 
                   
                   **kwargs
                   ):
        return StackV(
            twsty_tags=[*twsty_tags, space/y/2],
            childs=[SubheadingBanner(heading_text, section_depth=section_depth), Halign(content, align=align), *childs],
        )

    # def Subsubsection(heading_text: AnyStr,
    #                   content: Callable,
    #                   twsty_tags: List = [],
    #                   align="center",
    #                   childs = [],
    #                   **kwargs,
    #                   ):
    #     return StackV(
    #         twsty_tags=twsty_tags,
    #         childs=[SubsubheadingBanner(heading_text), Halign(content, align=align), *childs],
    #     )

    def Title(title_text: AnyStr, twsty_tags=[], align="center", **kwargs):
        return Halign(
            Span(
                text=title_text,
                twsty_tags=conc_twtags(*oj.ui_styles.sty.title_text, *twsty_tags),
                **kwargs,
            ),
            align=align,
        )

    def SubTitle(title_text: AnyStr, twsty_tags=[], align="center", **kwargs):  #
        return Halign(
            Span(
                text=title_text, twsty_tags=conc_twtags(*oj.ui_styles.sty.subtitle_text, *twsty_tags)
            ),
            align=align,
        )

    class StackG(Div):
        def __init__(self, *args, **kwargs):
            num_rows = kwargs.pop("num_rows", 2)
            num_cols = kwargs.pop("num_cols", 2)
            twsty_tags = kwargs.pop("twsty_tags", [])
            twsty_tags = [*twsty_tags, *oj.ui_styles.sty.stackG(num_cols, num_rows)]
            super().__init__(*args, twsty_tags=twsty_tags, **kwargs)

    def TitledPara(
            heading_text,
            twsty_tags=[],
            fix_sty_section_nesting=False,
            childs= [],
            section_depth = 0,
            **kwargs
    ):
        if fix_sty_section_nesting:
            # display content across the entire width
            # add margin to give effect of content nested
            # within title
            twsty_tags = conc_twtags(*twsty_tags, pd / sl / 4, mr/st/2, space/y/1,  W / full)
            for _ in childs:
                _.add_twsty_tags(pd / sl / 4)
                    


        twsty_tags = conc_twtags(*oj.ui_styles.sty.titledPara, *twsty_tags)
        title_sty = oj.ui_styles.sty.section_title_sty[section_depth]
        return StackV(childs=[H5(text=heading_text,
                                 twsty_tags=title_sty
                                 ),
                              *childs
                              ],
                      twsty_tags=twsty_tags,
                      **kwargs
        )

    return (
        Halign,
        Valign,
        SubheadingBannerImpl,
        SubheadingBanner,
        Subsection,
        #Subsubsection,
        Title,
        SubTitle,
        StackG,
        TitledPara,
    )
