import ofjustpy as oj
from py_tailwind_utils import * 
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

num_clicked = [0 for _ in range(100)]
def slip_btn_pair_gen(id):
    num_clicked = 0
    message_slip = MutableSpan_HCType(key=f"msgslip_{id}",
                                  text=f"Button clicked {num_clicked} times",
                                  )

    def on_btn_clicked(dbref, msg, to_ms, id=id):
        global num_clicked
        
        num_clicked[id]+= 1
        message_slip_ms = to_ms(message_slip)
        message_slip_ms.text = f"Button clicked {num_clicked[id]} times"
        pass


    click_counter = oj.AD.Button(key=f"click_counter_{id}",
                                 text="Submit",
                                 on_click = on_btn_clicked
                                 )

    return oj.HCCMutable.StackV(key=f"pair_{id}",
                         childs = [message_slip,
                                   click_counter,

                                   ],
                                twsty_tags = [space/y/2]
                         )
    

bigbox = oj.HCCMutable.Div(childs = [slip_btn_pair_gen(_) for _ in range(100)],
                  twsty_tags = [db.f, flxw.w, space/x/4, space/y/4]
    )
wp_endpoint = oj.create_endpoint(key="example_010",
                                 childs = [bigbox
                                           ],
                                 title="example_010"
                                 )

oj.add_jproute("/", wp_endpoint)
