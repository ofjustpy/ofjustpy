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
from py_tailwind_utils import invisible
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
from py_tailwind_utils import sl


from .tracker import trackStub
from .ui_styles import sty


def generator(Span, StackV, Div, H3, Para, PassiveDiv=None):
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
            twsty_tags=conc_twtags(*sty.halign(align), *twsty_tags), childs=[content]
        )

        return target

    def Valign(
        content: Callable, height_tag=H / screen, align="center", pcp=[], **kwargs
    ):
        """
        tstub: target stub, i.e., the one needs to be aligned
        """
        return PassiveDiv(
            childs=[content],
            twsty_tags=conc_twtags(*sty.valign(align), height_tag),
            **kwargs,
        )

    def SubheadingBanner(
        heading_text: AnyStr,
        twsty_tags: List = [],
        heading_text_sty=sty.subheading_text,
        **kwargs,
    ):
        spanl = Span(
            text=heading_text,
            twsty_tags=[
                *heading_text_sty,
                # use exact 1/3 of overall space for large screen
                *variant(W / "1/3", rv="md"),
                # for small  screen use full width
                *variant(W / full, rv="sm:max-md"),
            ],
        )
        spanm = Span(
            text=heading_text,
            twsty_tags=[
                *heading_text_sty,
                invisible,
                *variant(W / "1/3", rv="md"),
                # hide for small screen; noop is required to
                # not pollute the hidden.modifier_chain
                *variant(noop / hidden, rv="sm:max-md"),
            ],
        )
        spanx = Span(
            text=heading_text,
            twsty_tags=[
                *heading_text_sty,
                invisible,
                *variant(W / "1/3", rv="md"),
                # hide for small screen; noop is required to
                # not pollute the hidden.modifier_chain
                *variant(noop / hidden, rv="sm:max-md"),
            ],
        )

        target = Div(
            twsty_tags=conc_twtags(*twsty_tags, *sty.subheading_box),
            childs=[spanl, spanm, spanx],
        )

        return target

    def SubsubheadingBanner(
        heading_text: AnyStr,
        twsty_tags: List = [],
        heading_text_sty=sty.subheading_text,
        **kwargs,
    ):
        return SubheadingBanner(
            heading_text,
            twsty_tags=twsty_tags,
            heading_text_sty=sty.subsubheading_text,
            **kwargs,
        )

    def Subsection(
        heading_text: AnyStr, content: Callable, align="center", twsty_tags=[], **kwargs
    ):
        return StackV(
            twsty_tags=twsty_tags,
            childs=[SubheadingBanner(heading_text), Halign(content, align=align)],
        )

    def Subsubsection(
        heading_text: AnyStr,
        content: Callable,
        twsty_tags: List = [],
        align="center",
        **kwargs,
    ):
        return StackV(
            twsty_tags=twsty_tags,
            childs=[SubsubheadingBanner(heading_text), Halign(content, align=align)],
        )

    def Title(title_text: AnyStr, twsty_tags=[], align="center", **kwargs):
        return Halign(
            Span(
                text=title_text,
                twsty_tags=conc_twtags(*sty.title_text, *twsty_tags),
                **kwargs,
            ),
            align=align,
        )

    def SubTitle(title_text: AnyStr, twsty_tags=[], align="center", **kwargs):  #
        return Halign(
            Span(
                text=title_text, twsty_tags=conc_twtags(*sty.subtitle_text, *twsty_tags)
            ),
            align=align,
        )

    class StackG(Div):
        def __init__(self, *args, **kwargs):
            num_rows = kwargs.pop("num_rows", 2)
            num_cols = kwargs.pop("num_cols", 2)
            twsty_tags = kwargs.pop("twsty_tags", [])
            twsty_tags = [*twsty_tags, *sty.stackG(num_cols, num_rows)]
            # already taken care by SHC_types.HCCMixin
            # self.components = kwargs.get('childs')
            super().__init__(*args, twsty_tags=twsty_tags, **kwargs)

    def TitledPara(heading_text,
                   content,
                   twsty_tags=[],
                   fix_sty_section_nesting=False,
                   **kwargs):
        if fix_sty_section_nesting:
            # display content across the entire width
            # add margin to give effect of content nested
            # within title
            twsty_tags = conc_twtags(*twsty_tags, pd/sl/4, W/full)
            content.add_twsty_tags(pd/sl/4, W/full)
        
        return StackV(
            childs=[H3(text=heading_text), content], twsty_tags=twsty_tags, **kwargs
        )

    return (
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
    )
