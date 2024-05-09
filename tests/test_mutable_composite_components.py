from views import get_stackd_endpoint

def test_stackd_view(session_setup, per_test_setup):
    conn = session_setup
    oj,app = per_test_setup
    
    # define an app
    wp_endpoint = get_stackd_endpoint(oj)
    app.add_jproute("/stackd_view", wp_endpoint)

    # use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/stackd_view",
                                      "stackd_view")

    # Check if the StackD component is rendered
    stackd_element_id = "/mydeck"
    assert conn.root.element_exists(stackd_element_id)

    # Check if the buttons are rendered
    btn1_id = "/mybtn1"
    btn2_id = "/mybtn2"
    assert conn.root.element_exists(btn1_id)
    assert conn.root.element_exists(btn2_id)

    # Click on the first button and check if the second button is visible
    conn.root.submit_element(btn1_id)
    btn2_class = conn.root.get_element_attr_value(btn2_id, "class")
    assert "hidden" not in btn2_class

    # Click on the second button and check if the first button is visible
    conn.root.submit_element(btn2_id)
    btn1_class = conn.root.get_element_attr_value(btn1_id, "class")
    assert "hidden" not in btn1_class
    
