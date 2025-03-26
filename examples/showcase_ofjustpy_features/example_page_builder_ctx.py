import macropy.activate
import ofjustpy as oj
from py_tailwind_utils import *
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
oj.set_style("un")
app = oj.load_app()
def page_builder(childs):
    sideMenu = SimpleSideMenu("See also")
    sideMenu.add_flat_item("categories", "Categories", value="categories")
    sideMenu.add_flat_item("recentposts", "Recent Posts", value="recent posts")
    sideMenu.add_flat_item("popularposts", "Popular Posts", value="popular posts")
    sideMenu.add_flat_item("relatedposts", "Related Posts", value="related posts")



    # top level navigation

    header_panel = oj.PD.StackH(childs = [oj.PD.Span(key="navigation", text="Navigation", pcp=[fw.bold]), 
                                           oj.PD.A(key="history", href="#", text="History"),
                                           oj.PD.A(key="index", href="#", text="Index"),
                                           oj.PD.A(key="tags", href="#", text="Tags"),
                                           oj.PD.A(key="user", href="#", text="User"),
                                           ],
                                 )

    
    footer_panel = oj.PD.StackH(childs = [oj.PD.Span( text="Navigation", pcp=[fw.bold]), 
                                           oj.AD.A(key="about", href="#", text="About Us"),
                                           oj.AD.A(key="facebook", href="#", text="Facebook"),
                                           oj.AD.A(key="linkedin", href="#", text="LinkedIn"),
                                           oj.AD.A(key="twitter", href="#", text="Twitter"),
                                           ],
                                 )
    
    full_page = oj.PD.StackH(childs = [sideMenu,
                           oj.PD.StackV(childs = [header_panel,
                                                  oj.PD.Div(childs=childs),
                                                  footer_panel
                                                  ]
                                        )
                           ]
                 )

    return [full_page]


with oj.PageContentBuilderCtx(page_builder):
    # content for blog_page_
    blog_pagebody_topic_1 = oj.PD.Div(childs = [oj.PD.Span(text="content for blog topic 1")
                                                ]

                                      )
    blog_page_topic_1 = oj.create_endpoint("wp_blog_page_topic_1",
                                     [blog_pagebody_topic_1],
                                     title = "Blog topic 1",
                                     )
    
    oj.add_jproute("/blog_page_topic_1", blog_page_topic_1)

    blog_pagebody_topic_2 = oj.PD.Div(childs = [oj.PD.Span(text="content for blog topic 2")
                                                ]

                                      )
    blog_page_topic_2 = oj.create_endpoint("wp_blog_page_topic_2",
                                     [blog_pagebody_topic_2],
                                     title = "Blog topic 2",
                                     )
    
    oj.add_jproute("/blog_page_topic_2", blog_page_topic_2)
    
