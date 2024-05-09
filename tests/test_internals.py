import pytest
import ofjustpy as oj
from lxml import html
from py_tailwind_utils import *
from pytest_cases import fixture_union, pytest_fixture_plus

oj.set_style('un')
@pytest_fixture_plus(name= "static_component_with_details",
                params = [({'tag': 'span', 'text' : "hello", 'classes':"p-1"}, oj.PD.Span(text="hello", twsty_tags=[pd/1])),
                          ({'tag': 'div', 'classes':"bg-green-100", 'childs': [{'tag': 'span', 'text' : "hello", 'classes':"p-1"}]}, oj.PD.Div(childs = [oj.PC.Span(text="hello", twsty_tags=[pd/1])], twsty_tags=[bg/green/1])),
                          
                          ({'tag': 'button', 'text' : "hello", 'id': '/a',  'classes':"p-1"}, oj.AD.Button(key="a", text="hello", twsty_tags=[pd/1])),
                          ({'tag': 'button', 'text' : "hello", 'id': '/a',  'classes':"p-1", 'childs' :[{'tag': 'span', 'text' : "hello", 'classes':"p-1"}]}, oj.AD.Button(key="a", text="hello", twsty_tags=[pd/1], childs = [oj.PC.Span(text="hello", twsty_tags=[pd/1])])),
                          
                          ]
                )
def _static_component_with_details(request):
    return request.param

# ================ contraption for mutable components ================
class WP:
    def add_component(self, x):
        pass
    pass
from addict import Dict
request = Dict()
request.session_id = "abc"
sm = oj.get_session_manager(request)
# ================================ end ===============================

@pytest_fixture_plus(name= "mutable_component_with_details",
                params = [
                          ({'tag': 'button', 'text' : "hello", 'id': '/a',  'classes':"p-1"}, oj.Mutable.Button(key="a", text="hello", twsty_tags=[pd/1])),
                    ({'tag': 'div', 'id': '/a',  'classes':"p-1"}, oj.HCCStatic.Div(key="a",  twsty_tags=[pd/1])),
                    ({'tag': 'div',  'classes':"p-1"}, oj.HCCMutable.Div(twsty_tags=[pd/1])),
                    ({'tag': 'div',  'classes':"p-1", 'childs':[{'tag': 'button', 'text' : "Submit", 'classes':"bg-green-100", "id":"/abtn"}]}, oj.HCCMutable.Div(childs = [oj.Mutable.Button(key="abtn", twsty_tags=[bg/green/100], text="Submit")], twsty_tags=[pd/1])),
                    
                          ]
                     
                )
def _mutable_component_with_details(request):
    details, static_core = request.param
    wp = WP()
    with  oj.sessionctx(sm):
        m_shell = static_core.stub()(wp)
    return (details, m_shell)


fixture_union('component_with_details', ['static_component_with_details', 'mutable_component_with_details'])

def test_to_html_iter(component_with_details):
    details, component = component_with_details
    html_text  = "".join(component.to_html_iter())
    try:
        root = html.fromstring(html_text)
        
        assert root.tag == details['tag']
        assert details['classes'] in root.attrib['class']
        if 'text' in details:
            assert root.text == details['text']
        if 'id' in details:
            assert details['id'] in root.attrib['id']
        if 'childs' in details:
            # assume there is only one child single child
            child = root.getchildren()[0]
            child_detail = details['childs'][0]
            assert child_detail['classes'] in child.attrib['class']
            assert child_detail['tag'] == child.tag
            if 'text' in child_detail:
                assert child_detail['text'] == child.text
            
            print ("test for childs")
            pass
    except:
        assert False

# Do get_changed_diff_patch tests : for sure
# But A object and do url_for, and url_path_for tests
# some tests around cookies
# some form validation tests
# Test out the with mount_ctx business
# we should test oj.uictx()
