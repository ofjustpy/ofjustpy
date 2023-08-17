"""
a 2D grid of tailwind default color palette

"""
import ofjustpy as oj

from py_tailwind_utils import *


all_colors = [slate , gray , zinc , neutral , stone , red , orange , amber , yellow , lime , green , emerald , teal , cyan , sky , blue , indigo , violet , purple , fuchsia , pink , rose]

all_btns = [oj.PC.StackW(childs = [oj.PC.Label(twsty_tags=[bg/cp/k, mr/x/2, W/6, H/6])
                                 for k in range(100,1000,100)
                                 ],
                       twsty_tags=[mr/y/1]
                        )
             for cp in all_colors]
    
panel = oj.PC.StackV(childs=all_btns)
                    
wp_endpoint = oj.create_endpoint(key="example_002",
                                 childs = [panel],
                                 title="example_002"
                                 )    
oj.add_jproute("/", wp_endpoint)




app = oj.load_app()
