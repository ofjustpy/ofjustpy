import ofjustpy as oj
from py_tailwind_utils import *

def on_input_change(dbref, msg, to_ms):
    print ('input changed')
    print (msg.value)
    pass

def on_submit_click(dbref, msg, to_ms):
    # put of global variable for test to pick it up
    
    pass


def on_click(dbref, msg, to_ms):
    pass
    
username_input = oj.WithBanner("Username", oj.AC.TextInput(key="username",
                                                           placeholder = "Username",
                                                           data_validators = [oj.validator.InputRequired(),
                                                                              oj.validator.Length(min=5, max=8)
                                                                              ],
                                                           on_change = on_input_change
                                                           )
                               )

submit_btn = oj.AC.Button(key="submit",
                    text="Analyze CSV file",
                    )
    
# username_input_ = oj.LabeledInput_("username",
#                                            "Username",
#                                            "username",
#                                            data_validators = [oj.validator.InputRequired(),
#                                                               oj.validator.Length(min=5, max=8)
#                                                               ]
#                                            ).event_handle(oj.change,
#                                                           on_input_change
#                                                           )
        
#         all_inputs_ = oj.StackV_("all_inputs",
#                                  cgens = [username_input_,
#                                           email_input_,
#                                           password_,
#                                           confirm_password_]
#                                  )
        

myform = oj.AD.Form(key="aform",
                    childs = [username_input, submit_btn],
                    on_submit=on_submit_click
           )

# make sure to initialize the form-request-state-data
def post_init(wp, session_manager=None):
    print("post_init called")
    assert "session_manager" is not None
    request = wp.session_manager.request
    request.state.form_data["/aform"] = {}
    pass

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="test_form",
                                 childs = [myform],
                                 title = "example_007",
                                 csr_bundle_dir="hyperui",
                                 post_init = post_init,
                                 rendering_type="SSR",
                                 head_html =  """<script src="https://cdn.tailwindcss.com"></script> """

                              )

oj.add_jproute("/", wp_endpoint)

                   
