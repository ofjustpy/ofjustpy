import ofjustpy as oj

from ofjustpy.icons import FontAwesomeIcon

from py_tailwind_utils import *
app = oj.load_app()

fa_iconlabels = ["faUser", "faHouse",  "faHeart", "faCamera",  "faEnvelope"]

fa_icons_1x = [FontAwesomeIcon(label=_, size="1x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                               twsty_tags=[bg/pink/500, W/6, H/6],
                              ) for _ in fa_iconlabels
            ]

# fa_icons_2x = [FontAwesomeIcon(label=_, size="2x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=False,

#                               twsty_tags=[bg/pink/500]
#                               ) for _ in fa_iconlabels
#             ]

# fa_icons_3x = [FontAwesomeIcon(label=_, size="3x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=True,
#                               twsty_tags=[bg/pink/500]
#                               ) for _ in fa_iconlabels
#             ]

# fa_icons_4x = [FontAwesomeIcon(label=_, size="4x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=False,
#                               twsty_tags=[bg/pink/500]
#                               ) for _ in fa_iconlabels
#             ]



fa_icons_section_1x = oj.PC.Subsection("FontAwesomeIcons 1x",
                    oj.PC.StackH(childs=fa_icons_1x,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

# fa_icons_section_2x = oj.PC.Subsection("FontAwesomeIcons 2x",
#                     oj.PC.StackH(childs=fa_icons_2x,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )

# fa_icons_section_3x = oj.PC.Subsection("FontAwesomeIcons 3x",
#                     oj.PC.StackH(childs=fa_icons_3x,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )

# fa_icons_section_4x = oj.PC.Subsection("FontAwesomeIcons 4x",
#                     oj.PC.StackH(childs=fa_icons_4x,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )

# flip_options = ["both",  "horizontal","vertical", None, "horizonal", "vertical"

#                 ]

# fa_icons_2x_flip = [FontAwesomeIcon(label=_, size="2x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=True,
#                                flip=flip_options[idx],
#                               twsty_tags=[bg/pink/500]
#                                     ) for idx, _ in enumerate(fa_iconlabels)
#             ]

# fa_icons_section_2x_flip = oj.PC.Subsection("FontAwesomeIcons 2x flip (both, vertical, horizonal)",
#                     oj.PC.StackH(childs=fa_icons_2x_flip,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )
# rotation_options = [90, 180, 270, "null", 90, 270

#                 ]

# fa_icons_2x_rotation = [FontAwesomeIcon(label=_, size="2x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=True,
#                                rotation = rotation_options[idx],
#                               twsty_tags=[bg/pink/500]
#                                     ) for idx, _ in enumerate(fa_iconlabels)
#             ]

# fa_icons_section_2x_rotation = oj.PC.Subsection("FontAwesomeIcons 2x rotation",
#                     oj.PC.StackH(childs=fa_icons_2x_rotation,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )

# pulse_options = [True, False, True, False, True, False, True, False, ]
# fa_icons_2x_pulse = [FontAwesomeIcon(label=_, size="2x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=True,
#                                      pulse=pulse_options[idx],

#                               twsty_tags=[bg/pink/500]
#                                     ) for idx, _ in enumerate(fa_iconlabels)
#             ]

# fa_icons_section_2x_pulse = oj.PC.Subsection("FontAwesomeIcons 2x pulse",
#                     oj.PC.StackH(childs=fa_icons_2x_pulse,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )


# spin_options = [True, False, True, False, True, False, True, False, ]
# fa_icons_2x_spin = [FontAwesomeIcon(label=_, size="2x", 
#                              fixedWidth=True,
#                              # transform = "left-1 rotation-15",
#                               inverse=True,
#                                      spin=spin_options[idx],

#                               twsty_tags=[bg/pink/500]
#                                     ) for idx, _ in enumerate(fa_iconlabels)
#             ]

# fa_icons_section_2x_spin = oj.PC.Subsection("FontAwesomeIcons 2x spin",
#                     oj.PC.StackH(childs=fa_icons_2x_spin,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )


# spin_options = [True, False, True, False, True, False, True, False, ]
# fa_icons_2x_transform = [FontAwesomeIcon(label=_, size="2x", 
                     
#                                          transform = "left-1 rotation-15",
#                                          inverse=True,

#                               twsty_tags=[bg/pink/500]
#                                     ) for idx, _ in enumerate(fa_iconlabels)
#             ]

# fa_icons_section_2x_transform = oj.PC.Subsection("FontAwesomeIcons 2x transform",
#                     oj.PC.StackH(childs=fa_icons_2x_transform,
#                                  twsty_tags=[space/x/8]
                                 
#                                  ),
#                                     section_depth = 10

#                     )

wp_endpoint = oj.create_endpoint(key="fontawesome icons ",
                                 childs = [fa_icons_section_1x,
                                           #fa_icons_section_2x,
                                           # fa_icons_section_3x,
                                           # fa_icons_section_4x,
                                           # fa_icons_section_2x_flip,
                                           # fa_icons_section_2x_rotation,
                                           # fa_icons_section_2x_pulse,
                                           # fa_icons_section_2x_spin,
                                           # fa_icons_section_2x_transform
                                           
                                           ],
                                 title="fontawesome icons",
                                 rendering_type="SSR",
                                 csr_bundle_dir="ssr",
                                 head_html = """<script src="/static/ssr/bundle.iife.js"></script>
                                 """
                                 )


oj.add_jproute("/", wp_endpoint)




    

# <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" class="svg-inline--fa fa-user fa-fw fa-2x bg-pink-500  " role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"></path></svg>

# <svg class="bg-pink-500  " size="2x" fixedwidth="True" inverse="False" viewBox="0 0 448 512" aria-hidden="true" focusable="false" data-prefix="fas" role="img" xmlns="http://www.w3.org/2000/svg"><path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"></path></svg>
