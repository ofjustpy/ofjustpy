"""
Test if component are getting generated properly on the frontend
"""
from views import get_stackg_endpoint
def test_stackg_view(session_setup, per_test_setup):
    conn = session_setup
    oj,app = per_test_setup
    app.add_jproute("/stackg_view", views.stackg_view)

    # use browser to load page, query, and perform checks
    page_source = conn.root.load_page("http://127.0.0.1:8000/stackg_view", "oa")

    # Check if the StackG component is rendered
    stackg_element_id = "/my_stackg"
    assert conn.root.element_exists(stackg_element_id)

    # Check the class attribute of the StackG element
    stackg_element_class = conn.root.get_element_attr_value(stackg_element_id, "class")

    # Check if the required Tailwind CSS grid tags are present
    required_tags = ["grid", "grid-cols-2", "grid-rows-2"]
    for tag in required_tags:
        assert tag in stackg_element_class

    # TODO: Add any additional checks if needed
