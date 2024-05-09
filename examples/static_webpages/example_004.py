"""
an stackG (grid) container with active buttons

"""

import ofjustpy as oj
from py_tailwind_utils import *
from addict_tracking_changes import Dict
app = oj.load_app()
def mouseover_action(dbref, msg, target_of):
    print ("in mouseover_action")
    # buttons msg do not have value
    #print (msg)
    print (dbref.value)
    pass


# lets create six buttons
all_btns = [oj.AC.Button(key=f"btn_{idx}",
                     twsty_tags = [fc/rose/300,
                                         ta.center,
                                         bdr.lg,
                                         bd/gray/300,
                                         boxtopo.bd,
                                         fw.medium,
                                         *gradient(gray/200, gray/200, gray/100),
                                         shadow/gray/200,
                                         shadow.md
                                         ],
                           on_mouseover = mouseover_action,
                         text=f"abtn_{idx}",
                         value = idx
                           
                      ) for idx in range(6)
            ]

grid = oj.PC.StackG(num_cols=1,
                 num_rows=2,
                 twsty_tags=[*variant(G/cols/1, rv="sm"),
                             *variant(G/cols/2, rv="md"),
                                *variant(G/cols/3, rv="lg")
                                ],
                           childs = all_btns
                           )


wp_endpoint = oj.create_endpoint(key="example_004",
                                 childs = [grid],
                                 title="example_004"
                                 )

oj.add_jproute("/", wp_endpoint)

