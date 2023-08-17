
import pytest
import ofjustpy as oj
import sys
from addict import Dict
app = oj.load_app()
# The repo is structured as
# <root>/examples
# <root>/tests/test_examples/

sys.path.append("../../")
import importlib

@pytest.fixture(name="comp_type", params=("input", "static", "mutable"))
def _comp_type(request):
    return request.param


@pytest.fixture(name="idx", params=(f"00{idx}" for idx in range(1, 9)))
def _idx(request):
    return request.param

# @pytest.fixture(name="comp_type", params=("input", ))
# def _comp_type(request):
#     return request.param


# @pytest.fixture(name="idx", params=(f"00{idx}" for idx in range(1, 2)))
# def _idx(request):
#     return request.param

# A mock request object
@pytest.fixture
def reqobj():
    req = Dict()
    req.session_id = "abc"
    return req





@pytest.fixture
def example_mod(comp_type, idx):
    assert comp_type in ("input", "static", "mutable")
    example_module = importlib.import_module(f"examples.{comp_type}_webpages")
    try:
        ex_mod = getattr(example_module, f"example_{idx}")
        return (idx, ex_mod)
    except Exception as e:
        print(f"mod not found {comp_type}:{idx}")
        pytest.skip(f"Fixture setup failed: {e}")

        pass

from starlette.testclient import TestClient            

@pytest.fixture
def testclient():
    client = TestClient(app)
    return client

def test_example_mod(example_mod, reqobj):
    (idx, ex_mod) = example_mod
    endpoint_func = getattr(ex_mod, 'wp_endpoint')
    wp_obj = endpoint_func(reqobj)



    assert True

def test_example_response(example_mod, testclient):
    (idx, ex_mod) = example_mod
    response = testclient.get(f'/example_{idx}')
    assert response.status_code == 200

