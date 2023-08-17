"""
Hello world static webpage
"""
import ofjustpy as oj
from py_tailwind_utils import *
app = oj.load_app()

title = oj.PC.Title("A hello world page", twsty_tags=[bg/pink/"100/20"])

body = oj.PC.Halign(oj.PC.Prose(text="Hello world! This page was written using ofjustpy python  framework ",
                          twsty_tags=[fz.lg, shadow._, shadow/gray/400, ta.center]
                          ),
                 twsty_tags=[mr/st/8]
                )

footer = oj.PC.Halign(oj.PC.Prose(text="Thats all folks! Hope you got the broad drift of this framework", twsty_tags=[mr/st/64, ta.right]), "end"
                )



tlc = oj.PC.Container(
                  childs = [title,
                           body,
                           footer],
    twsty_tags=[H/"screen", bg/gray/"100/20"])            


wp_endpoint = oj.create_endpoint(key="example_003",
                                 childs = [tlc],
                                 title="example_003"
                                 )

oj.add_jproute("/", wp_endpoint)


