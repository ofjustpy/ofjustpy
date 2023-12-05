class WP:
    def add_component(self, x):
        pass
    pass
wp = WP()

import ofjustpy as oj
from py_tailwind_utils import *
request = Dict()
request.session_id = "abc"
sm = oj.get_session_manager(request)
with  oj.sessionctx(sm):
    with oj.uictx("l0"):
        input_color = oj.HC_wrappers.WithBanner("select color:",
                                                oj.Mutable.ColorSelector(key="utility_class_color"),
                                                content_type="mutable",
                                                height_tag = H/8
                                                )

        selection_panel = oj.HCCMutable.Subsubsection("Input Panel",
                                      oj.HCCMutable.StackV(childs = [
                                          oj.HCCMutable.StackH(childs = [input_color,
                                                                         ])
                                                          
                                                          ]
                                                )
                                      )
        selection_panel.stub()(wp)
