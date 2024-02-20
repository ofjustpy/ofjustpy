"""
Demo showcase using collapsible div implemented in svelte

"""

import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict
app = oj.load_app()
collapse_box = oj.PC.Collapsible(hide_banner_text="Expand for TextInput code",
                                 hide_banner_classes = [min/W/"1/2", W/"2/3"],
                                 childs=[oj.PC.Span(text="tifc", twsty_tags=[H/64])],
                                 twsty_tags=[bd/gray/5, bd/1, W/"2/3", overflowx.auto]
                                 )

wp_endpoint = oj.create_endpoint(key="example_005",
                                 childs = [collapse_box],
                                 title="example_005"
                                 )
oj.add_jproute("/", wp_endpoint)

