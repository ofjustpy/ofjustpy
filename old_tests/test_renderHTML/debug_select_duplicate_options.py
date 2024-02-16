import ofjustpy as oj
from py_tailwind_utils import *

def on_input_change(dbref, msg, target_of):
    print ("on_input_change : Called with ", msg.value)
    pass

option1 = oj.PC.Option(value="option1", label="Option 1", disabled=True, pcp=[bg/green/1])
option2 = oj.PC.Option(value="option2", label="Option 2", pcp=[bg/blue/4])
option3 = oj.PC.Option(value="option3", label="Option 3")

childs = [option1, option2, option3]
#childs=[]
# # Create Select instance with multiple attributes and list of option instances using cgens
select_input = oj.AC.Select(
                                      key="select_drop_down",
                                      childs = childs,
                                      name="example_select",
                                      form="example_form",
                                      required=True,
                                      size=1,
                                      default = "options3",
                                      twsty_tags=[bg/green/1, W/"1/3"],
                                      on_change=on_input_change
                                      )
#print (select_input.to_html())

# print (select_input.components)
# from xml.dom import minidom
# dom = minidom.parseString(select_input.to_html())
# formatted_xml = dom.toprettyxml()

# print (formatted_xml)
