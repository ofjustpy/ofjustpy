"""
Only Halign for now
"""
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import List

from py_tailwind_utils import cc
from py_tailwind_utils import conc_twtags
from py_tailwind_utils import db
from py_tailwind_utils import flx
from py_tailwind_utils import H
from py_tailwind_utils import jc
from py_tailwind_utils import noop
from py_tailwind_utils import screen

from .htmlcomponents import HCCMutable
from .htmlcomponents import PassiveComponents as PC
from .ui_styles import sty


def Halign(content, align="center", content_type="passive", **kwargs):
    """
    there isn't yet settled way to find the type of  content,
    i.e. if it is a passive or mutable type.  Hence content_type
    is the required as a fix.
    """
    twsty_tags = conc_twtags(*sty.halign(align), *kwargs.pop("twsty_tags", []))
    match content_type:
        case "active":
            return PC.Div(childs=[content], twsty_tags=twsty_tags)
        case "passive":
            return PC.Div(childs=[content], twsty_tags=twsty_tags)
        case "mutable":
            return HCCMutable.Div(childs=[content], twsty_tags=twsty_tags)


def StackH_Aligned(
    content, content_type="passive", valign="center", halign="center", **kwargs
):
    """
    for content which are to be stacked horizontally wrap then around two divs so that
    1- they all have same height
    2- they are positioned vertically and horizontally in center
    Use flex-1
    so that all of them have same vertical height.
    Use justify-center and items center to horizontally and vertically align them
    Use items center to verti
    """

    match content_type:
        case "passive":
            valigned = PC.Div(childs=[content], twsty_tags=sty.valign(valign))
            return PC.Div(childs=[valigned], twsty_tags=[flx.one, *sty.halign(valign)])
        case "active":
            # passive/active should be same
            assert False
        case "mutable":
            # the width/height of content is not changed; place the content at the center
            #
            valigned = HCCMutable.Div(
                childs=[content], twsty_tags=sty.valign(valign)
            )  # adjust height of valigned and place it horizontally centered
            return HCCMutable.Div(
                childs=[valigned], twsty_tags=[flx.one, *sty.valign(valign)]
            )


def WithBanner(
    banner_text: AnyStr,
    content,
    content_type="passive",
    twsty_tags: List = [],
    **kwargs,
):
    match content_type:
        case "passive":
            return PC.StackH(
                childs=[
                    PC.Valign(PC.Span(text=banner_text), height_tag=H/8),
                    content,
                ],
                twsty_tags=twsty_tags,
                **kwargs,
            )
        case "active":
            assert False
        case "mutable":
            return HCCMutable.StackH(
                childs=[
                    PC.Valign(PC.Span(text=banner_text), height_tag=H/8),
                    content,
                ],
                twsty_tags=twsty_tags,
                **kwargs,
            )
