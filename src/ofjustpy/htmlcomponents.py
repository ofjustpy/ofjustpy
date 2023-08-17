"""
All the components types that ofjustpy offers:

"""
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import List

from py_tailwind_utils import bg
from py_tailwind_utils import conc_twtags
from py_tailwind_utils import db
from py_tailwind_utils import dnew
from py_tailwind_utils import dupdate
from py_tailwind_utils import flx
from py_tailwind_utils import H
from py_tailwind_utils import jc
from py_tailwind_utils import screen
from py_tailwind_utils import twcc2hex

from .htmlcomponents_impl import assign_id
from .htmlcomponents_impl import CS_event_prehook
from .htmlcomponents_impl import CSBase
from .htmlcomponents_impl import event_prehook
from .htmlcomponents_impl import MutableShell_CSMixin
from .htmlcomponents_impl import on_circle_click
from .htmlcomponents_impl import on_mcs_change
from .htmlcomponents_impl import on_scs_click
from .htmlcomponents_impl import SliderBase
from .MHC_types import Button as MButton
from .MHC_types import ChartJS as MChartJS
from .MHC_types import Circle as MCircle
from .MHC_types import Container as MContainer
from .MHC_types import Div as MDiv
from .MHC_types import Form as MForm
from .MHC_types import HCCMutable
from .MHC_types import HCCStatic
from .MHC_types import Label as MLabel
from .MHC_types import Span as MSpan
from .MHC_types import StackD as MStackD
from .MHC_types import StackH as MStackH
from .MHC_types import StackV as MStackV
from .MHC_types import TextInput as MTextInput
from .SHC_types import ActiveComponents as AC
from .SHC_types import PassiveComponents
from .static_core_tracker import uictx
from .ui_styles import sty
from .WebPage_TF import WebPage


class ActiveComponents:
    Span = assign_id(AC.Span)
    Button = assign_id(AC.Button)
    TextInput = assign_id(AC.TextInput)

    Img = assign_id(AC.Img)

    CheckboxInput = assign_id(AC.CheckboxInput)
    A = assign_id(AC.A)
    Textarea = assign_id(AC.Textarea)
    Div = assign_id(AC.Div)
    StackH = assign_id(AC.StackH)
    Select = assign_id(AC.Select)
    Switch = assign_id(AC.Switch)
    class MainColorSelector(AC.Select):
        def __init__(self, *args, **kwargs):
            childs = [
                PassiveComponents.Option(
                    text=option,
                    value=option,
                    twsty_tags=[bg / sty.get_color_tag(option) / 5],
                )
                for option in twcc2hex.keys()
            ]
            super().__init__(*args, **kwargs, childs=childs)

        pass

    MainColorSelector = assign_id(MainColorSelector)
    pass


class HCCStatic:
    Div = assign_id(HCCStatic.Div)
    StackV = assign_id(HCCStatic.StackV)


class Mutable:
    Circle = assign_id(MCircle)
    Button = assign_id(MButton)
    Label = assign_id(MLabel)
    Span = assign_id(MSpan)
    TextInput = assign_id(MTextInput)
    ChartJS = assign_id(MChartJS)
    Div = assign_id(MDiv)
    Container = assign_id(MContainer)
    StackH = assign_id(MStackH)
    StackV = assign_id(MStackV)
    StackD = assign_id(MStackD)

    class Slider(SliderBase):
        def __init__(self, *args, num_iter=range(1, 5), **kwargs):
            key = kwargs.get("key")
            with uictx(f"___{key}"):
                childs = [
                    Mutable.Circle(
                        text=f"c{i}",
                        value=i,
                        key=f"circle_{i}",
                        on_click=lambda *args, slider_core=self: on_circle_click(
                            *args, slider_core=slider_core
                        ),
                    )
                    for i in num_iter
                ]
            super().__init__(
                *args, **kwargs, childs=childs, event_prehook=event_prehook
            )

    class ColorSelector(CSBase):
        def __init__(self, *args, **kwargs):
            # there are two childs
            # one main-color-selector (which is select hc)
            # and other shades-color-selector (which is slider)

            key = kwargs.get("key")
            with uictx(f"___{key}"):
                self.mcs = ActiveComponents.MainColorSelector(
                    key="mcs",
                    on_change=lambda *args, cs_core=self: on_mcs_change(
                        *args, cs_core=cs_core
                    ),
                )

                self.scs = Mutable.Slider(
                    key="scs",
                    num_iter=range(1, 10),
                    on_click=lambda *args, cs_core=self: on_scs_click(
                        *args, cs_core=cs_core
                    ),
                )

            childs = [self.mcs, self.scs]

            super().__init__(
                *args, **kwargs, childs=childs, event_prehook=CS_event_prehook
            )

    ColorSelector = assign_id(ColorSelector)
    Slider = assign_id(Slider)
    WebPage = assign_id(WebPage)
    Form = assign_id(MForm)
