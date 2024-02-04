from .SVGcomponents import PassiveComponents as SVGPassiveComponents
from lxml import etree
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import  tstr

def parse(svg_content):
    """
    comp_kwargs: The component arguments like title, description of  the alert box
    """
    parser = etree.HTMLParser()
    root = etree.fromstring(svg_content, parser)
    rlt = "./body"
    element = root.find(f"{rlt}/*[1]")
    return parse_recurse(element)
    
def parse_recurse(element):
    """
    comp_kwargs: The component arguments like title, description of  the alert box
    """
    twsty_tags = []
    if 'class' in element.attrib:

        twsty_tags = encode_twstr(element.attrib['class'])
        decoded = tstr(*twsty_tags)
        for _ in element.attrib['class'].split():
            if _ not in decoded:
                print("==============Mismatch==================")
                print ("encoding class = ", element.attrib['class'])
                print("Encoded decode = ",  tstr(*twsty_tags))
                print("===================EnD====================")
                assert False
        del element.attrib['class']


    component_generator= None
    f = None
    tag = element.tag
    c_tag = tag[0].capitalize() + tag[1:]
    component_generator = getattr(SVGPassiveComponents, c_tag)
    childs = [parse_recurse(_) for _ in element]
    K = component_generator(**element.attrib, childs=childs, twsty_tags=twsty_tags)

    return K
