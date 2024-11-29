import ofjustpy as oj

from py_tailwind_utils import *
app = oj.load_app()

fa_iconlabels = ["faUser", "faHouse",  "faHeart", "faCamera",  "faEnvelope"]

fa_icons_1x = [oj.FontAwesomeIcon(label=_, size="1x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                              twsty_tags=[bg/pink/500]
                              ) for _ in fa_iconlabels
            ]

fa_icons_2x = [oj.FontAwesomeIcon(label=_, size="2x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=False,

                              twsty_tags=[bg/pink/500]
                              ) for _ in fa_iconlabels
            ]

fa_icons_3x = [oj.FontAwesomeIcon(label=_, size="3x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                              twsty_tags=[bg/pink/500]
                              ) for _ in fa_iconlabels
            ]

fa_icons_4x = [oj.FontAwesomeIcon(label=_, size="4x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=False,
                              twsty_tags=[bg/pink/500]
                              ) for _ in fa_iconlabels
            ]



fa_icons_section_1x = oj.PC.Subsection("FontAwesomeIcons 1x",
                    oj.PC.StackH(childs=fa_icons_1x,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

fa_icons_section_2x = oj.PC.Subsection("FontAwesomeIcons 2x",
                    oj.PC.StackH(childs=fa_icons_2x,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

fa_icons_section_3x = oj.PC.Subsection("FontAwesomeIcons 3x",
                    oj.PC.StackH(childs=fa_icons_3x,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

fa_icons_section_4x = oj.PC.Subsection("FontAwesomeIcons 4x",
                    oj.PC.StackH(childs=fa_icons_4x,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

flip_options = ["both",  "horizontal","vertical", None, "horizonal", "vertical"

                ]

fa_icons_2x_flip = [oj.FontAwesomeIcon(label=_, size="2x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                               flip=flip_options[idx],
                              twsty_tags=[bg/pink/500]
                                    ) for idx, _ in enumerate(fa_iconlabels)
            ]

fa_icons_section_2x_flip = oj.PC.Subsection("FontAwesomeIcons 2x flip (both, vertical, horizonal)",
                    oj.PC.StackH(childs=fa_icons_2x_flip,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )
rotation_options = [90, 180, 270, "null", 90, 270

                ]

fa_icons_2x_rotation = [oj.FontAwesomeIcon(label=_, size="2x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                               rotation = rotation_options[idx],
                              twsty_tags=[bg/pink/500]
                                    ) for idx, _ in enumerate(fa_iconlabels)
            ]

fa_icons_section_2x_rotation = oj.PC.Subsection("FontAwesomeIcons 2x rotation",
                    oj.PC.StackH(childs=fa_icons_2x_rotation,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

pulse_options = [True, False, True, False, True, False, True, False, ]
fa_icons_2x_pulse = [oj.FontAwesomeIcon(label=_, size="2x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                                     pulse=pulse_options[idx],

                              twsty_tags=[bg/pink/500]
                                    ) for idx, _ in enumerate(fa_iconlabels)
            ]

fa_icons_section_2x_pulse = oj.PC.Subsection("FontAwesomeIcons 2x pulse",
                    oj.PC.StackH(childs=fa_icons_2x_pulse,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )


spin_options = [True, False, True, False, True, False, True, False, ]
fa_icons_2x_spin = [oj.FontAwesomeIcon(label=_, size="2x", 
                             fixedWidth=True,
                             # transform = "left-1 rotation-15",
                              inverse=True,
                                     spin=spin_options[idx],

                              twsty_tags=[bg/pink/500]
                                    ) for idx, _ in enumerate(fa_iconlabels)
            ]

fa_icons_section_2x_spin = oj.PC.Subsection("FontAwesomeIcons 2x spin",
                    oj.PC.StackH(childs=fa_icons_2x_spin,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )


spin_options = [True, False, True, False, True, False, True, False, ]
fa_icons_2x_transform = [oj.FontAwesomeIcon(label=_, size="2x", 
                     
                                         transform = "left-1 rotation-15",
                                         inverse=True,

                              twsty_tags=[bg/pink/500]
                                    ) for idx, _ in enumerate(fa_iconlabels)
            ]

fa_icons_section_2x_transform = oj.PC.Subsection("FontAwesomeIcons 2x transform",
                    oj.PC.StackH(childs=fa_icons_2x_transform,
                                 twsty_tags=[space/x/8]
                                 
                                 ),
                                    section_depth = 10

                    )

wp_endpoint = oj.create_endpoint(key="fontawesome icons ",
                                 childs = [fa_icons_section_1x,
                                           fa_icons_section_2x,
                                           fa_icons_section_3x,
                                           fa_icons_section_4x,
                                           fa_icons_section_2x_flip,
                                           fa_icons_section_2x_rotation,
                                           fa_icons_section_2x_pulse,
                                           fa_icons_section_2x_spin,
                                           fa_icons_section_2x_transform
                                           
                                           ],
                                 title="fontawesome icons",
                                 csr_bundle_dir = "hyperui"
                                 )


oj.add_jproute("/", wp_endpoint)




    


