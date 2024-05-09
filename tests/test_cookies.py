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


def test_cookies_and_sessions(session_setup, per_test_setup):
    conn = session_setup
    oj,app = per_test_setup
    
    wp_endpoint = oj.create_endpoint(key="test1",
                                     childs = [oj.PD.Span(text="hello")],
                                     title="test1"
                                     
                                     )
    oj.add_jproute("/wp1", wp_endpoint)
    page_source = conn.root.load_page("http://127.0.0.1:8000/wp_test1", "wp_test1")
    pass
