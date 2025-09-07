import json
from addict import Dict
import ofjustpy_engine.HC_Div_type_mixins as TR


class RenderHTMLMixin:
    def __init__(self, *args, **kwargs):

        self.prepare_htmlRender()
        pass

    def build_renderHtml(self):
        pass
    
    def prepare_htmlRender(self):
        # mutable shell's staticCore have
        # prepare_htmlRender which gets
        # updated after update to attrs
        self.htmlRender = f'''{self.text}'''

    def to_html_iter(self):
        yield self.htmlRender

        

class BaseComponentMixin:
    """Attributes related to working with justpy-svelte framework. The json-to-svelte components would need these attributes

    :param show: A Boolean attribute that controls the visibility of the component.
    :type show: bool
    :default show: True

    :param debug: A Boolean attribute that enables or disables debugging for the component.
    :type debug: bool
    :default debug: False

    """

    def __init__(self, **kwargs):

        self.domDict = Dict()

        self.attrs = Dict()
        self.domDict.vue_type = "plaintext_component"
        pass





class StaticJsonMixin:
    """Mixin for static objects that have id/event handler attached to it."""

    def __init__(self, *args, **kwargs):
        self.obj_json = None
        pass

    def get_obj_props_json(self):
        return "[]"

    def get_obj_props_jsondict(self):
        return []

    def build_json(self):
        domDict_json = json.dumps(self.domDict, default=str)[1:-1]
        attrs_json = json.dumps(self.attrs, default=str)[1:-1]
        object_props_json = self.get_obj_props_json()

        self.obj_json = f"""{{ {domDict_json},  "attrs":{{ {attrs_json} }}, "object_props":{object_props_json} }}"""


        
    def convert_object_to_jsondict(self, parent_hidden=False):
        """
        jsondict is a dict representation that would converted to json.
        Currently used for skeleton's slot components
        """
        z = {**self.domDict, "attrs": self.attrs, "object_props": self.get_obj_props_jsondict()}
        return z
    
    def convert_object_to_json(self, parent_hidden=False):
         return self.obj_json

    def get_changed_diff_patch(self, parent_hidden=False):
        return
        yield

    def clear_changed_history(self):
        raise NotImplementedError("Static types don't mutate -- changed diff not applicable")




        
class _PlainText(BaseComponentMixin, TR.SvelteSafelistMixin, TR.HCTextMixin, RenderHTMLMixin, StaticJsonMixin):
    def __init__(self, *args, **kwargs):
        # keep HCTextMixin happy
        self.htmlRender_body = []
        BaseComponentMixin.__init__(self, *args, **kwargs)
        TR.SvelteSafelistMixin.__init__(self, *args, **kwargs)
        TR.HCTextMixin.__init__(self, *args, **kwargs)
        RenderHTMLMixin.__init__(self, *args, **kwargs)
        StaticJsonMixin.__init__(self, *args, **kwargs)
        # build json is called 
        self.build_json()
        pass
    

class PlainText(_PlainText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stub(self):
        return gen_Stub_HCPassive(target=self)



    
    
