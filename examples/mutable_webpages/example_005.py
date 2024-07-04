 # deck example
import ofjustpy as oj
from py_tailwind_utils import *

app = oj.load_app()

labels = [oj.Mutable.Label(text="mytext1", key="mylabel1", twsty_tags=[W/8]),
          oj.Mutable.Label(text="mytext2", key="mylabel2"),
          oj.Mutable.Label(text="mytext3", key="mylabel3"),
          oj.Mutable.Label(text="mytext4", key="mylabel4"),
          ]

mydeck = oj.Mutable.StackD(key="mydeck",
                           childs=labels,
                           height_anchor_key="mylabel3",
                           
                           twsty_tags=[W/"1/2"])


def on_btn_click(dbref, msg, target_of):
    wp_ms = msg.page
    request = wp_ms.session_manager.request
    idx = request.state.btn_idx 
    mydeck_shell = target_of(mydeck)
    mydeck_shell.bring_to_front(labels[idx].id)
    idx = (idx + 1)%4
    request.state.btn_idx  = idx
    pass

        
mybtn = oj.AC.Button(key="mybtn",
                   text="abtn",
                   twsty_tags=[W/64, H/8, bg/yellow/300],
                   on_click=on_btn_click
                   )
def on_mutableShell_create(wp_ms):
    """
    wp_ms: webpage mutable shell
    
    """
    request = wp_ms.session_manager.request
    request.state.btn_idx = 1
    pass

tlc = oj.HCCMutable.Valign(oj.HCCMutable.Halign(oj.HCCMutable.StackV(childs = [mydeck,
                                           mybtn
                                     ],
                           twsty_tags=[space/y/8, pd/4]
                                                ), 
                           twsty_tags=[W/full]
                           )
                           )

              
wp_endpoint = oj.create_endpoint(key="example_005",
                                 childs = [tlc
                                           ],
                                 title = "example_005",
                                 post_mutableshell_create_callback = on_mutableShell_create

                                 )

oj.add_jproute("/", wp_endpoint)
