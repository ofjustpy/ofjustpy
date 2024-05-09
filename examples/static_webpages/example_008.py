import ofjustpy as oj

from ofjustpy.icons import FontAwesomeIcon

from py_tailwind_utils import *
app = oj.load_app()


coffee_icon = FontAwesomeIcon(label="faCoffee", size="4x", 
                              fixedWidth=True,
                              rotation=90,
                              transform = "left-1 rotation-15",
                              inverse=True,
                              beatfade=True,
                              twsty_tags=[bg/green/500]
                              )

wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [coffee_icon],
                                 title="example_008")


oj.add_jproute("/", wp_endpoint)




    


