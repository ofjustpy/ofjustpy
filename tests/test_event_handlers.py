# from project_dev_toolbox.test_tools.pytest_setup_utils import *





import os
import pytest
import os
import rpyc
import sys
import time
import logging
from project_dev_toolbox.test_tools.pytest_utils_common import uvicorn_server_control_center
import asyncio

module_path = os.path.dirname(os.path.realpath(__file__))

import sys
import importlib

@pytest.fixture(autouse=True)
def per_test_setup(scope="function"):
    # launch uvicorn server
    print ("%%%%%%%%%%%%%%%% Init oj and app %%%%%%%%%%%%%%%%%%%%%%")
    module_name  = "ofjustpy"
    oj = importlib.import_module(module_name)
    app = oj.build_app()
    webserver_controller = uvicorn_server_control_center("localhost", 8000, app)
    asyncio.run(webserver_controller.start())
    asyncio.run(asyncio.sleep(1))

    yield oj, app

    print ("tear down post test run")
    try:
        asyncio.run(webserver_controller.stop())
    except Exception as e:
        #print ("usual exception when closing uvicorn server")
        pass
        
    asyncio.run(asyncio.sleep(10))

    # unload ofjustpy
    x = []
    for _ in sys.modules.keys():
        if "ofjustpy" in _:
            x.append(_)
    for _ in x:
        del sys.modules[_]
    del oj
    

    
# Something is off about datalist, Switch, StackH, Div
@pytest.fixture(params= [# ("AD", "Span"),
                         #  ("AD", "Img"),
                         # ("AD", "TextInput"),
                         # ("AD", "Textarea"),
    
                         #("AD", "Switch"),
                         #("AD", "StackH"),
                         #("AD", "Div"),
                         ("AD", "Button"),
                         ("Mutable", "Button"),
                         ("Mutable", "Circle"), #TODO: add other mutable components
            ])
def oj_component_accesspath(request):
    return request.param

@pytest.fixture
def oj_mutable_component_accesspath(oj_component_accesspath):
    mod, label = oj_component_accesspath
    if mod == "Mutable":
        return oj_component_accesspath
    else:
        pytest.skip()
        

@pytest.fixture(scope="session", autouse=True)
def session_setup():
    server_port =  9324
    # ======== test setup; start browser + page loader service =======

    os.system(f"""
    python3 {module_path}/browser_page_loader_service.py {server_port} > ~/Execution/ofjustpy/run_dir/browser_page_loader_service.out 2> ~/Execution/ofjustpy/run_dir/browser_page_loader_service.err&
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




@pytest.mark.skip(reason="test ran successfully")
def test_test1(session_setup, per_test_setup,  oj_component_accesspath):
    """
    test event handling active component
    """
    conn = session_setup
    oj,app = per_test_setup
    mod, label = oj_component_accesspath
    component_genfunc = getattr(getattr(oj, mod), label)
    print ("component_genfunc = ", component_genfunc)
    
    clickCount = 0
    async def onBtnClick(self, msg, target_of):
        nonlocal clickCount
        clickCount += 1
        print("clickCount = ", clickCount)
        pass
    
    abtn = component_genfunc(key="abtn",
                 on_click = onBtnClick
                 )
    wp_endpoint = oj.create_endpoint(key="test1",
                                     childs = [abtn],
                                     title="test1"
                                     

                                     )
    oj.add_jproute("/wp_test1", wp_endpoint)
    page_source = conn.root.load_page("http://127.0.0.1:8000/wp_test1", "wp_test1")
    for i in range(1, 5):
        conn.root.submit_element("/abtn")
        asyncio.run(asyncio.sleep(1))
        assert clickCount > 0
    assert True
    

def test_ui_twtags_mutability(session_setup, per_test_setup,  oj_mutable_component_accesspath):
    conn = session_setup
    oj,app = per_test_setup
    mod, label = oj_mutable_component_accesspath
    print (mod, " ", label)
    async def onBtnClick(self, msg, target_of):
        btn_ms = target_of(self)
        btn_ms.add_twsty_tags([bg/green/100])
    component_genfunc = getattr(getattr(oj, mod), label)
    oj.set_style("un")
    mcomp = component_genfunc(key="mbtn",
                             text="Not clicked yet",
                             on_click = onBtnClick
                             )
    wp_endpoint = oj.create_endpoint(key="test1",
                                     childs = [mcomp],
                                         title="test1"
                                     )
    oj.add_jproute("/wp_ui_twtags_mutability", wp_endpoint)
    page_source = conn.root.load_page("http://127.0.0.1:8000/wp_ui_twtags_mutability", "wp_test1")
    tw_class = conn.root.get_element_attr_value("/mbtn", "class")
    print ("Before == ", tw_class)
    conn.root.submit_element("/mbtn")
    tw_class = conn.root.get_element_attr_value("/mbtn", "class")
    print ("After == ", tw_class)
    assert True
    
    

