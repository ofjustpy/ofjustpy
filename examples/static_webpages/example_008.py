import ofjustpy as oj

from ofjustpy.icons import FontAwesomeIcon

from py_tailwind_utils import *
app = oj.load_app()

fa_iconlabels = ["faUser", "faHouse",  "faHeart", "faCamera",  "faEnvelope"]

fa_icons = [FontAwesomeIcon(label=_, size="4x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                              beatfade=True,
                              twsty_tags=[bg/pink/500]
                              ) for _ in fa_iconlabels
            ]



fa_icons_section = oj.PC.Subsubsection("FontAwesomeIcons",
                    oj.PC.StackH(childs=fa_icons,
                                 twsty_tags=[space/x/8]
                                 
                                 )
                    )




# house_icon = FontAwesomeIcon(label="faHouse", size="4x", 
#                               fixedWidth=True,
#                               rotation=90,
#                               transform = "left-1 rotation-15",
#                               inverse=True,
#                               beatfade=True,
#                               twsty_tags=[bg/green/500]
#                               )

md_iconlabels = [ ("faCog", "cog"), ("faCoffee", "coffee")
                 ]




md_icons = [FontAwesomeIcon(label=_[0], size="4x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                              beatfade=True,
                              twsty_tags=[bg/pink/500],
                            mdi_label=_[1]
                              ) for _ in md_iconlabels
            ]



md_icons_section = oj.PC.Subsubsection("Material Design Icons",
                    oj.PC.StackH(childs=md_icons,
                                 twsty_tags=[space/x/8]
                                 
                                 )
                    )


coffee_icon = FontAwesomeIcon(label="faCoffee", size="4x", 

                             mdi_label = "coffee",

                              )


wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [fa_icons_section,
                                           md_icons_section],
                                 title="example_008")


oj.add_jproute("/", wp_endpoint)




    


