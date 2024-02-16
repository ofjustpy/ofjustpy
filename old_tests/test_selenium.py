import pytest
import os
import rpyc
import sys
import time
import logging
import ofjustpy as oj
from ofjustpy_engine.jpcore.justpy_app import uvicorn_server_control_center
import asyncio


from py_tailwind_utils import (tstr,
                           W,
                           full,
                           jc,
                           twcc2hex,
                           bg,
                           onetonine,
                           fz,
                           get_color_instance,
                           outline,
                           offset,
                           black,
                           outline,
                           green,
                           W,
                            H,
                            screen,
                           conc_twtags,
                           hidden,
                           db,
                               invisible,
                               cc,
                               noop,
                               blue
                           )

from ofjustpy.htmlcomponents_impl import assign_id
from function_pipes import pipe, pipe_bridge
from ofjustpy.HC_TF import gen_HC_type
from ofjustpy.TF_impl import HCType
from ofjustpy.ui_styles import sty
from ofjustpy_engine import HC_Div_type_mixins as TR
# ============================ setup logs ============================
try:
    os.remove("test_selenium.log")
except:
    pass

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(filename="launcher.log",
                    level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger(__name__)
# ================================ end ===============================
    



@pytest.fixture(scope="session", autouse=True)
def session_setup():
    server_port =  9324
    # ======== test setup; start browser + page loader service =======

    os.system(f"""
    python3 browser_page_loader_service.py {server_port} > browser_page_loader_service.out 2> browser_page_loader_service.err&
    """)
    time.sleep(6)

    retry_counter = 0
    while True:
        try:
            conn = rpyc.connect("localhost", server_port)
            break
        except Exception as e:
            retry_counter += 1
            pass
        if retry_counter == 6:
            print ("unable to setup test")
            sys.exit()
        
    

    # ============================== end =============================
    yield conn
    # ==================== test teardown: shutdown ===================

    
    try: 
        conn.root.stop()

    except Exception as e:
        print ("caught exception ", e)
    # ============================== end =============================
    pass


@pytest.fixture(autouse=True)
def per_test_setup():
    # launch uvicorn server
    app = oj.build_app()
    webserver_controller = uvicorn_server_control_center("localhost", 8000, app)
    asyncio.run(webserver_controller.start())
    asyncio.run(asyncio.sleep(1))

    yield app

    print ("tear down post test run")
    try:
        asyncio.run(webserver_controller.stop())
    except Exception as e:
        print ("usual exception when closing uvicorn server")
        
    asyncio.run(asyncio.sleep(10))
    #print (page_source)


#@pytest.mark.skip(reason="Skipping this test for now")
def test_test1(session_setup, per_test_setup):
    # define an app
    conn = session_setup 
    app = per_test_setup


    ButtonType = assign_id(gen_HC_type(HCType.mutable,
                             "TextTwMutableButton",
                             hctag_mixin = TR.ButtonMixin,
                             staticCoreMixins= [],
                             mutableShellMixins = [TR.HCTextMixin, TR.TwStyMixin],
                             stytags = sty.button
                                  )
                           )

    


    
    # build webpage template
    clickCount = 0
    async def onBtnClick(self, msg, target_of):
        nonlocal clickCount
        clickCount += 1
        btn_ms = target_of(self)
        btn_ms.text = f"I WAS CLICKED {clickCount+1} TIMES"
        
        
    btn1 = ButtonType(key="btn1",
                      text="Not clicked yet",
                      on_click = onBtnClick
                      )
    wp_template = oj.Mutable.WebPage(key="wp_test1",
                                     childs = [btn1
                                               ]
                                     )
    wp_test1 = oj.create_endpoint(wp_template)
    app.add_jproute("/wp_test1", wp_test1)
    
    page_source = conn.root.load_page("http://127.0.0.1:8000/wp_test1", "wp_test1")

    # query the browser
    btn_text = conn.root.get_element_text("/btn1")
    assert "NOT CLICKED YET" == btn_text.upper()
    for i in range(2, 7):
        conn.root.submit_element("/btn1")
        asyncio.run(asyncio.sleep(1))
        btn_text = conn.root.get_element_text("/btn1")
        assert f"I was clicked {i} times".upper() ==  btn_text.upper()


#@pytest.mark.skip(reason="Skipping this test for now")
def test_components_part1(session_setup, per_test_setup):
    # Load the webpage
    conn = session_setup 
    app = per_test_setup
    li1 = oj.PC.Li(text="List item 1")
    li2 = oj.PC.Li(text="List item 2")
    li3 = oj.PC.Li(text="List item 3")
    ul = oj.PC.Ul(childs=[li1, li2, li3])
    p = oj.PC.P(text="This is a Paragraph")
    div = oj.PC.Div(childs=[p, ul])
    wp_components_part1 = oj.create_endpoint(oj.Mutable.WebPage(key="wp_test1",
                                                                childs = [div
                                                                          ]
                                                                )
                                             )
    
    app.add_jproute("/check_components_part1", wp_components_part1)
    
    # use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/check_components_part1", "wp_check_components_part1")

    # Check if the paragraph is rendered correctly
    res_val = conn.root.check_if_tag_text_pair_exists("p", "This is a Paragraph")
    assert res_val

    res_val = conn.root.check_if_tag_text_pair_exists("li", "List item 1")
    assert res_val

    res_val = conn.root.check_if_tag_text_pair_exists("li", "List item 2")
    assert res_val


    res_val = conn.root.check_if_tag_text_pair_exists("li", "List item 3")
    assert res_val

    
#@pytest.mark.skip(reason="Skipping this test for now")
def test_components_part2(session_setup, per_test_setup):
    # Set up the app
    conn = session_setup 
    app = per_test_setup

    a = oj.AC.A(key="a", text="Click me!", href="https://example.com")
    br = oj.PC.Hr()
    label = oj.PC.Label(text="Enter your name:")
    span = oj.PC.Span(text="This is a span")
    input = oj.AC.TextInput(key="input", placeholder="Another input")
    img = oj.AC.Img(key="img", src="https://via.placeholder.com/150", alt="Example image")
    textarea = oj.AC.Textarea(key="textarea", placeholder="Write your message here")


    all_items  = oj.PC.Div(childs=[a, br, label,  span, input, img, textarea])
    wp_components_part2 = oj.create_endpoint(oj.Mutable.WebPage(key="wp_components_part2",
                                                                childs = [all_items
                                                                          ]
                                                                )
                                             )
    app.add_jproute("/component_part2", wp_components_part2)
    
    # Load the webpage
    page_source = conn.root.load_page("http://127.0.0.1:8000/component_part2", "wp_component_part2")

    # Check if the components are rendered correctly
    res_val = conn.root.check_if_tag_text_pair_exists("a", "Click me!")
    assert res_val

    res_val = conn.root.check_if_tag_text_pair_exists("label", "Enter your name:")
    assert res_val

    res_val = conn.root.check_if_tag_text_pair_exists("span", "This is a span")
    assert res_val

    input_change_only_placeholder = conn.root.get_element_attr_value("/input", "placeholder")
    assert "Another input" == input_change_only_placeholder

    img_src = conn.root.get_element_attr_value("/img", "src")
    assert "https://via.placeholder.com/150" == img_src

    textarea_placeholder = conn.root.get_element_attr_value("/textarea", "placeholder")
    assert "Write your message here" == textarea_placeholder

#@pytest.mark.skip(reason="Skipping this test for now")
def test_labeled_input(session_setup, per_test_setup):
    # define an app
    conn = session_setup
    app = per_test_setup

    label1 = oj.PC.LabelDiv(childs=[oj.PC.Span(text="Enter a value"),
                           oj.AC.TextInput(key="input1",
                                           placeholder="a dummy value"
                                           )
                           
                           ]
                            )
    label2 = oj.PC.LabelDiv(childs = [oj.PC.Span(text="Enter a value"),
                                      oj.AC.TextInput(key="input2",
                                             placeholder="a dummy value"
                                           ),
                                      ]
                            )
    comps = oj.PC.StackV(childs = [label1, label2])
    wp = oj.create_endpoint(oj.Mutable.WebPage(key="wp_labeled_input",
                                               childs = [comps
                                                         ]
                                               )
                            )
    app.add_jproute("/labeled_input", wp)
    # use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/labeled_input", "oa")
    res_val = conn.root.check_if_tag_text_pair_exists("span", "Enter a value")
    assert res_val

    input_placeholder = conn.root.get_element_attr_value("/input1", "placeholder")
    assert "a dummy value" == input_placeholder

    input_placeholder = conn.root.get_element_attr_value("/input2", "placeholder")
    assert "a dummy value" == input_placeholder


    

#@pytest.mark.skip(reason="Skipping this test for now")    
def test_labeled_checkbox_view(session_setup, per_test_setup):
    # define an app
    conn = session_setup
    app = per_test_setup

    def on_input_change(dbref, msg, target_of):
        pass
    
    label = oj.PC.LabelDiv(childs=[oj.PC.Span(text="Got Milk?"),
                                oj.AC.CheckboxInput(key="cbox",
                                                    checked = True,
                                                    on_change = on_input_change)
                        ]
                )
    wp_endpoint = oj.create_endpoint(oj.Mutable.WebPage(key="wp_labeled_input",
                                               childs = [label
                                                         ]
                                               )
                            )
    app.add_jproute("/labeled_checkbox_view", wp_endpoint)

    # use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/labeled_checkbox_view", "labeled_checkbox_view")

    # Check the label text
    # res_val = conn.root.check_if_tag_text_pair_exists("span", "Got Milk?")
    # assert res_val

    # Check the checkbox state
    checkbox_checked = conn.root.is_selected("/cbox")
    assert checkbox_checked == True

    conn.root.submit_element("/cbox")
    checkbox_checked = conn.root.is_selected("/cbox")
    assert checkbox_checked == False
    
    


    

global_webpage = None

def store_webpage_in_global(func):
    def wrapper(*args, **kwargs):
        global global_webpage
        wp = func(*args, **kwargs)
        global_webpage = wp
        return wp

    return wrapper


# Turning off for now; unable to trigger submit on_change from browser

# def test_checkbox_input_view(session_setup, per_test_setup):
#     # Define an app
#     conn = session_setup
#     app = per_test_setup


    
#     cbox = oj.AC.CheckboxInput(key="myci",
#                                              checked=False)

#     input_value = None
#     def on_input_change(dbref, msg, target_of):
#         print("on inpput  change called ")
#         nonlocal input_value
#         input_value = msg.value
#         pass
#     ibox = oj.AC.TextInput(key="myti", placeholder="Enter text",
#                            on_change = on_input_change
#                            )
            
#     wp_endpoint = oj.create_endpoint(oj.Mutable.WebPage(key="wp_cbox",
#                                                     childs = [cbox, ibox
#                                                               ]
#                                                         )
#                                      )
         
#     app.add_jproute("/checkbox_input_view", store_webpage_in_global(wp_endpoint))

#     # Use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/checkbox_input_view", "checkbox_input_view")


#     # Check the input placeholder text
#     placeholder_text = conn.root.get_element_attr_value("/myti", "placeholder")
#     assert placeholder_text == "Enter text"

#     # Edit the input field
#     input_text = "New text"
#     conn.root.set_element_text("/myti",  input_text)
#     conn.root.submit_element("/myti")

#     assert input_value == input_text



#@pytest.mark.skip(reason="increamentally building test")
def test_subheading_banner_view(session_setup, per_test_setup):
    conn = session_setup
    app = per_test_setup
    subheading_banner = oj.PC.SubheadingBanner("Sample Subheading")
    wp_endpoint = oj.create_endpoint(oj.Mutable.WebPage(key="wp_labeled_input",
                                               childs = [subheading_banner
                                                         ]
                                               )
                            )
    app.add_jproute("/subheading_banner_view", wp_endpoint)

    # Use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/subheading_banner_view", "subheading_page")


    # Check the heading text
    res_val = conn.root.check_if_tag_text_pair_exists("span", "Sample Subheading")
    assert res_val

    



# #@pytest.mark.skip(reason="increamentally building test")
# def test_subsubsection_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/subsubsection_view", views.subsubsection_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/subsubsection_view", "oa")
#     # Check the heading text
#     heading_text = conn.root.get_element_attr_value("/___heading_sss/headingL", "textContent")
#     # don't know from where but getting white spaces
#     assert heading_text.rstrip() == "Sample Subsubsection"


# #@pytest.mark.skip(reason="increamentally building test")    
# def test_prose_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/prose_view", views.prose_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/prose_view", "oa")

#     # Check if the Prose component is rendered
#     prose_element_id = "/my_prose"
#     assert conn.root.element_exists(prose_element_id)

#     # Check the prose text
#     prose_text = conn.root.get_element_text(prose_element_id)
#     assert prose_text == "Sample text for prose"

#     # Check the class attribute of the prose element
#     prose_element_class = conn.root.get_element_attr_value(prose_element_id, "class")

#     # Get the server-side class value
#     server_prose_element = views.global_webpage.session_manager.stubStore.my_prose

#     # Compare the client-side and server-side class values
#     assert prose_element_class == server_prose_element.target.classes




# #@pytest.mark.skip(reason="increamentally building test")    
# def test_key_value_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/key_value_view", views.key_value_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/key_value_view", "oa")

#     # Check if the KeyValue component is rendered
#     key_value_element_id = "/my_kv"
#     assert conn.root.element_exists(key_value_element_id)

#     # Check the key and value text
#     key_text = conn.root.get_element_text("/___my_kv/keyt")
#     assert key_text == "Key"

#     value_text = conn.root.get_element_text("/___my_kv/valuet")
#     assert value_text == "Value"

#     # Check the classes for key, equals, and value elements
#     key_element_classes = conn.root.get_element_attr_value("/___my_kv/keyt", "class")
#     eq_element_classes = conn.root.get_element_attr_value("/___my_kv/eqt", "class")
#     value_element_classes = conn.root.get_element_attr_value("/___my_kv/valuet", "class")

#     # Get the server-side elements from the global_webpage
#     server_key_element = views.global_webpage.session_manager.stubStore.___my_kv.keyt
#     server_eq_element = views.global_webpage.session_manager.stubStore.___my_kv.eqt
#     server_value_element = views.global_webpage.session_manager.stubStore.___my_kv.valuet

#     # Compare the classes
#     assert key_element_classes == server_key_element.target.classes
#     assert eq_element_classes == server_eq_element.target.classes
#     assert value_element_classes == server_value_element.target.classes

#     # Additional checks can be added for event handling, state change, etc.

    
# #@pytest.mark.skip(reason="increamentally building test")    
# def test_subtitle_title_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/subtitle_title_view", views.subtitle_title_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/subtitle_title_view", "oa")

#     # Check if the SubTitle and Title components are rendered
#     subtitle_element_id = "/my_subtitle"
#     title_element_id = "/my_title"

#     assert conn.root.element_exists(subtitle_element_id)
#     assert conn.root.element_exists(title_element_id)

#     # Check the subtitle and title text
#     subtitle_text = conn.root.get_element_text(subtitle_element_id)
#     title_text = conn.root.get_element_text(title_element_id)

#     assert subtitle_text == "Subtitle Example"
#     assert title_text == "Title Example"

#     # Additional checks can be added for event handling, state change, etc.

# #@pytest.mark.skip(reason="increamentally building test")        
# def test_slider_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/slider_view", views.slider_view)

#     # load the page and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/slider_view", "oa")

#     # Check if the Slider component is rendered
#     slider_element_id = "/my_slider"
#     assert conn.root.element_exists(slider_element_id)

#     # Check the server-side Slider component
#     server_slider_element = views.global_webpage.session_manager.stubStore.my_slider
#     assert server_slider_element is not None

#     # Simulate clicks on the circles and check server component class
#     for i in range(1, 6):
#         circle_element_id = f"/___my_slider/c{i}"
#         assert conn.root.element_exists(circle_element_id)

#         # Simulate the click on the circle element
#         conn.root.submit_element(circle_element_id)

#         # Wait for a moment to let the server-side code process the click event
#         time.sleep(0.5)

#         # Check if the server component class matches with that on the browser side
#         browser_circle_class = conn.root.get_element_attr_value(circle_element_id, "class")
#         server_circle_class = views.global_webpage.session_manager.stubStore.___my_slider[f"c{i}"].target.classes
#         assert browser_circle_class == server_circle_class
    


# # In test_views.py
# #@pytest.mark.skip(reason="increamentally building test")        
# def test_color_selector_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/color_selector_view", views.color_selector_view)

#     # load the page and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/color_selector_view", "oa")

#     # Check if the ColorSelector component is rendered
#     color_selector_element_id = "/my_color_selector"
#     assert conn.root.element_exists(color_selector_element_id)

#     # Check the server-side ColorSelector component
#     server_color_selector = views.global_webpage.session_manager.stubStore.my_color_selector.target
#     assert server_color_selector is not None

#     # Simulate clicks on the mainColorSelector options and the slider circles
#     for main_color in twcc2hex.keys():
#         main_color_option_element_id = f"/___my_color_selector/opt_{main_color}"
#         assert conn.root.element_exists(main_color_option_element_id)

#         # Simulate the click on the mainColorSelector option element
#         conn.root.submit_element(main_color_option_element_id)

#         # Wait for a moment to let the server-side code process the click event
#         time.sleep(0.5)

#         for i in range(1, 10):
#             circle_element_id = f"/___my_color_selector/___shades/c{i}"
#             assert conn.root.element_exists(circle_element_id)

#             # Simulate the click on the slider circle element
#             conn.root.submit_element(circle_element_id)

#             # Wait for a moment to let the server-side code process the click event
#             time.sleep(0.5)

#             # Check if the server-side component's main color and slider value match the clicked elements
#             assert server_color_selector.maincolor_value == main_color
#             assert server_color_selector.slider_value == i

#             # Check if the selected color value is correct
#             selected_color_value = twcc2hex[main_color][onetonine[i]]
#             assert views.selected_color_value == selected_color_value


# def test_stackg_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/stackg_view", views.stackg_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/stackg_view", "oa")

#     # Check if the StackG component is rendered
#     stackg_element_id = "/my_stackg"
#     assert conn.root.element_exists(stackg_element_id)

#     # Check the class attribute of the StackG element
#     stackg_element_class = conn.root.get_element_attr_value(stackg_element_id, "class")

#     # Check if the required Tailwind CSS grid tags are present
#     required_tags = ["grid", "grid-cols-2", "grid-rows-2"]
#     for tag in required_tags:
#         assert tag in stackg_element_class

#     # TODO: Add any additional checks if needed

# #@pytest.mark.skip(reason="increamentally building test")        
# def test_stackd_view(session_setup, per_test_setup):
#     # define an app
#     conn = session_setup
#     app = per_test_setup
#     app.add_jproute("/stackd_view", views.stackd_view)

#     # use browser to load page, query, and perform checks
#     page_source = conn.root.load_page("http://127.0.0.1:8000/stackd_view",
#                                       "stackd_vew")

#     # Check if the StackD component is rendered
#     stackd_element_id = "/mydeck"
#     assert conn.root.element_exists(stackd_element_id)

#     # Check if the buttons are rendered
#     btn1_id = "/mybtn1"
#     btn2_id = "/mybtn2"
#     assert conn.root.element_exists(btn1_id)
#     assert conn.root.element_exists(btn2_id)

#     # Click on the first button and check if the second button is visible
#     conn.root.submit_element(btn1_id)
#     btn2_class = conn.root.get_element_attr_value(btn2_id, "class")
#     assert "hidden" not in btn2_class

#     # Click on the second button and check if the first button is visible
#     conn.root.submit_element(btn2_id)
#     btn1_class = conn.root.get_element_attr_value(btn1_id, "class")
#     assert "hidden" not in btn1_class
    
            
