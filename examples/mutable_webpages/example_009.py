import ofjustpy as oj
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.HC_TF import gen_HC_type
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles

app = oj.load_app()
MutableSpan_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Span",
        TR.SpanMixin,
        staticCoreMixins=[],
        mutableShellMixins=[TR.HCTextMixin, TR.TwStyMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )
)


num_clicked = 0
message_slip = MutableSpan_HCType(key="msgslip",
                              text=f"Button clicked {num_clicked} times",
                              )

def on_btn_clicked(dbref, msg, to_ms):
    global num_clicked
    num_clicked += num_clicked
    message_slip_ms = to_ms(message_slip)
    message_slip_ms.text = f"Button clicked {num_clicked} times"
    pass


click_counter = oj.AD.Button(key="click_counter",
                             text="Submit",
                             on_click = on_btn_clicked
                             )
wp_endpoint = oj.create_endpoint(key="example_009",
                                 childs = [message_slip,
                                           click_counter
                                           ],
                                 title="example_009"
                                 )

oj.add_jproute("/", wp_endpoint)
