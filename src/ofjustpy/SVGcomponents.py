from justpy.htmlcomponents import (svg_tags,
                                   svg_tags_use,
                                   svg_presentation_attributes,
                                   svg_filter_attributes,
                                   svg_animation_attributes,
                                   svg_attr_dict
                                   )

# from ofjustpy.SHC_types import (PassiveComponents as PC,
#                                 ActiveComponents as AC,
#                                 )

from ofjustpy.Div_TF import gen_Div_type

class PassiveComponents:
    pass

    
class Div_SVG_Mixin:
    def __init__(self, *args, **kwargs):
        self.domDict.vue_type = "svg_component"
        self.domDict.html_tag = self.html_tag
        for attr in (
                 self.svg_attributes
        ):
            if attr in kwargs:
                self.attrs[attr] = kwargs.get(attr)
                self.htmlRender_attr.append(f'''{attr}="{self.attrs[attr]}"''')
        pass

Div = gen_Div_type(static_addon_mixins = [Div_SVG_Mixin])

# Note: We should most likely create a Mixin for each 
# tagtype and then create corresponding class

for tag in svg_tags_use:
    c_tag = tag[0].capitalize() + tag[1:]
    setattr(PassiveComponents, c_tag,  type(
        c_tag,
        (Div,),
        {
            "html_tag": tag,
            "svg_attributes": svg_attr_dict.get(tag, [])
            + svg_presentation_attributes
            + svg_filter_attributes,
        },
    ))
