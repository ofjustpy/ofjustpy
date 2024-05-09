"""
Showcases different input components
"""
import ofjustpy as oj
app = oj.load_app()
from py_tailwind_utils import *

def on_input_change(dbref, msg, target_of):
    print ("on_input_change : Called with ", msg.value)
    pass

text_input = oj.AC.TextInput(key="key_ti",
                                      placeholder="Enter something...",
                                      autocomplete=True,
                                      maxlength=20,
                                      minlength=5,
                                      pattern="^[a-zA-Z0-9]*$",
                                      #readonly=False,
                                      required=True,
                                      size=30,
                                      twsty_tags=[bg/blue/"100/50", min/W/"1/2", W/"1/3", H/8],
                                      on_change = on_input_change

                                      )

checkbox_input = oj.AC.CheckboxInput(key="key_cb",
                                              checked=False,
                                              disabled=False,
                                              debug=True,
                                              twsty_tags=[bg/blue/400, W/"1/3"],
                                              on_change= on_input_change
                                            
                                              )

textarea_input = oj.AC.Textarea(id=None, key="myTextarea",
                                          rows=10,
                                          cols=30,
                                          disabled=False,
                                          #readonly=False,
                                          wrap="hard",
                                          maxlength=200,
                                          minlength=50,
                                          debug=True,
                                         text="we could add lots of text", 
                                          twsty_tags=[bg/green/100, W/"1/3"],
                                          on_change = on_input_change
                                          )
# pure static elements
option1 = oj.PC.Option(value="option1", label="Option 1", disabled=True, twsty_tags=[bg/green/100])
option2 = oj.PC.Option(value="option2", label="Option 2", twsty_tags=[bg/blue/400])
option3 = oj.PC.Option(value="option3", label="Option 3")

childs = [option1, option2, option3]

# # Create Select instance with multiple attributes and list of option instances using cgens
select_input = oj.AC.Select(
                                      key="select_drop_down",
                                      childs = childs,
                                      name="example_select",
                                      form="example_form",
                                      required=True,
                                      size=1,
                                      default = "options3",
                                      twsty_tags=[bg/green/100, W/"1/3"],
                                      on_change=on_input_change
                                      )


wp_endpoint = oj.create_endpoint(key="example_001",
                                 childs = [text_input,
                                           checkbox_input,
                                           textarea_input,
                                           select_input

                                           ],
                                 title="Example 001"

                                 )
oj.add_jproute("/", wp_endpoint)



