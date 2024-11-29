import ofjustpy as oj

app = oj.load_app()
dummy_btn  = oj.AD.Button(key="abtn",
                          text="Dummy Button"
                          )


def request_handler(request, path_param_1=None, path_param_2=None):
    itemtype = request.query_params._dict.get('itemtype', "itemtype_nonexists")
    contenttype = request.query_params._dict.get('contenttype', None)
    print ("path params = ", path_param_1, " ", path_param_2)
    print ("query params = ", itemtype, " ", contenttype)
    

    pass


endpoint = oj.create_endpoint("demo_query_path_params",
                   childs = [dummy_btn],
                   request_handler = request_handler,
                   title="Demo query and path params"
                   )


oj.add_jproute("/{path_param_1}/{path_param_2}", endpoint)

query= "itemtype=default&contenttype=text"
from starlette.testclient import TestClient
client = TestClient(app)

response = client.get(f'/Home/menu?{query}')

