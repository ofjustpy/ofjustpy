"""
Img 

"""

import ofjustpy as oj

from py_tailwind_utils import *
app = oj.load_app()

img = oj.PC.Img(src="https://via.placeholder.com/150", alt="Example image")




wp_endpoint = oj.create_endpoint(key="example_007",
                                 childs = [
                                           img,
                                           ],
                                 title="example_007"

                                 )    
oj.add_jproute("/", wp_endpoint)




