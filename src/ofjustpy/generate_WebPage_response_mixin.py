import json
from urllib.parse import urlparse
from ofjustpy_engine.jpcore import justpy_app
from ofjustpy_engine.jpcore import jpconfig
from starlette.responses import HTMLResponse
# updates justpy_app.component_file_list
justpy_app.create_component_file_list()

frontend_engine_type = jpconfig.FRONTEND_ENGINE_TYPE
frontend_engine_libs = jpconfig.FRONTEND_ENGINE_LIBS
    
class ResponsiveStatic_SSR_ResponseMixin:


        
    def get_html_response_string(page_id,
                             title,
                             use_websockets,
                             redirect,
                             display_url,
                             page_ready,
                             result_ready,
                             reload_interval_ms,
                             events,
                             static_resources_url,
                             debug, 
                             base_url,
                             comps_html_render_iter,
                             head_html="",
                             body_style="",
                             body_classes="",
                             body_html = "",
                             components_link_srcs = "",
                                 csr_bundle_dir = ""

                             ):
        """
        components_link_srcs: reference custom javascript components within /static/ directory

        """
        if body_style:
            body_style = f"""style="{body_style}"
            """

        if body_classes:
            body_classes = f"""class="{body_classes}"
            """


        # not sure if really required
        #<script src="/static/{csr_bundle_dir}bundle.iife.js"></script>

        html_response_string = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <base href={base_url}>

        
        <link href="/static/{csr_bundle_dir}style.css" rel="stylesheet"
          type="text/css">
        <script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js" async></script>

        {head_html}
        </head>
        <body {body_style} {body_classes}>
        {body_html}
        <div id="components">
        {"".join(comps_html_render_iter)}
        </div>
        <!-- main stuff -->
        {components_link_srcs}
        <script src='/templates/js/comm_channel.js'></script>


        <script>
        var page_id = '{page_id}';
        var use_websockets = {use_websockets};
        let justpy_core=new CommChannelHandler(
                this, // window
                '{page_id}', // page_id
                '{title}', // title
                '{use_websockets}', // use_websockets
                '{redirect}', // redirect
                '{display_url}', // display_url
                {page_ready}, // page_ready
                {result_ready}, // result_ready     
                {reload_interval_ms}, // reload_interval
                {events},  // events
                '{static_resources_url}',  // static_resources_url
                {debug}   // debug
        );
        </script>
        <script src='/templates/js/event_handler_ssr.js'></script>

        <script>
        console.log("setting up justpy_core");
        justpy_core.setup()
        </script>
        
         </body>
        </html>
        </html>
        """
        return html_response_string


    def __init__(self, *args, **kwargs):
        print("calling SSR-WEBPAGE: kwargs", kwargs)
        self.csr_bundle_dir = kwargs.get("csr_bundle_dir", "") + "/"
        pass

    def get_response_for_load_page(self, request):
        """
        get the response for the given webpage

        Args:
            request(Request): the request to handle
            return as a full HtmlResponse

        Returns:
            Reponse: the response for the given load_page
        """

        components_link_srcs = "\n".join([f"""<script src={request.url_for(jpconfig.STATIC_NAME, path=file_name)}</script>""" for file_name in justpy_app.component_file_list
        ])

        page_ready = "page_ready" in self.events #???
        result_ready = "result_ready" in self.events #???
        reload_interval = self.reload_interval
        if reload_interval:
            reload_interval_ms = round(reload_interval * 1000)
        else:
            reload_interval_ms = 0
            

        static_resources_url = request.url_for("static",
                                               path="/") 
        response_string = ResponsiveStatic_SSR_ResponseMixin.get_html_response_string(self.page_id,
                                                                         self.title,
                                                                         json.dumps(
                                                                             self.use_websockets),
                                                   self.redirect,
                                                   self.display_url,
                                                   json.dumps(page_ready),
                                                   json.dumps(result_ready),
                                                   reload_interval_ms,
                                                   self.events,
                                                   static_resources_url,
                                                   json.dumps(self.debug),
                                                   jpconfig.BASE_URL,
                                                self.to_html_iter(),

                                                                                      head_html = self.head_html,
                                                   body_style=self.body_style,
                                                   body_classes= self.body_classes,
                                                   body_html=self.body_html,
                                                                                      components_link_srcs=components_link_srcs,
                                                                                      csr_bundle_dir = self.csr_bundle_dir
                                                   )
        return HTMLResponse(content=response_string)
    


class ResponsiveStatic_CSR_ResponseMixin:
    """
    ResponsiveStatic: implies that the webpage is responsive, it recieves events from clients
    and responds to them. Implies client will make websocket connection with the server.
    CSR: client side rendering: we pass a json, that is rendered by svelte runtime.
    """

               
    def get_html_response_string(page_id,
                             title,
                             use_websockets,
                             redirect,
                             display_url,
                             page_ready,
                             result_ready,
                             reload_interval_ms,
                             events,
                             static_resources_url,
                             debug, 
                             base_url,
                             justpyComponentsJson,
                             head_html="",
                             body_style="",
                             body_classes="",
                             body_html = "",
                                 components_link_srcs = "",
                                 setup_skeleton_script_src = "",
                                 skeleton_data_theme="modern",
                                 csr_bundle_dir = ""
                             ):
        """
        components_link_srcs: reference custom javascript components within /static/ directory

        """
        if body_style:
            body_style = f"""style="{body_style}"
            """

        if body_classes:
            body_classes = f"""class="{body_classes}"
            """
        # this was used in the old justpy to load supported javascript libraries like Quasar etc.
        # won't work now since we have no external libs as of now
        # and client side framework js are moved to the svelte directory
        
        # frontend_engine_srcs = "\n".join([f"<script src='/templates/js/{frontend_engine_type}/{file_name}.js'></script>" for file_name in frontend_engine_libs])

        # get domain name from base_url

        html_response_string = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <base href={base_url}>
        <script src="https://cdn.jsdelivr.net/npm/js-cookie@3.0.1/dist/js.cookie.min.js" async></script>
        <script src="/static/{csr_bundle_dir}bundle.iife.js"></script>
        <link href="/static/{csr_bundle_dir}style.css" rel="stylesheet"
          type="text/css">
        <link href="/templates/js/svelte/skeleton-ui-token-style.css" rel="stylesheet"
          type="text/css">
        {head_html}
        </head >
        <body {body_style} {body_classes} data-theme="{skeleton_data_theme}">
        {body_html}
        <div id="components">
        </div>
        <!-- main stuff -->
        {components_link_srcs}
        <script src='/templates/js/justpy_core.js'></script>


        <script>
        var page_id = '{page_id}';
        var use_websockets = {use_websockets};
        var justpyComponents = {justpyComponentsJson};
        let justpy_core=new JustpyCore(
                this, // window
                '{page_id}', // page_id
                '{title}', // title
                '{use_websockets}', // use_websockets
                '{redirect}', // redirect
                '{display_url}', // display_url
                {page_ready}, // page_ready
                {result_ready}, // result_ready     
                {reload_interval_ms}, // reload_interval
                {events},  // events
                '{static_resources_url}',  // static_resources_url
                {debug}   // debug
        );
        </script>
        <script src='/templates/js/event_handler.js'></script>
        <script src='/templates/js/svelte/component_generator.js'></script>
        {setup_skeleton_script_src}
        <script>
        console.log("setting up justpy_core");
        justpy_core.setup()
        </script>

        </body>
        </html>
        </html>
        """
        return html_response_string


    def __init__(self, *args, **kwargs):
        self.csr_bundle_dir = kwargs.get("csr_bundle_dir", "")

        if self.csr_bundle_dir:
            self.csr_bundle_dir = self.csr_bundle_dir  + "/"

        pass

    def get_response_for_load_page(self, request):
        """
        get the response for the given webpage

        Args:
            request(Request): the request to handle
            return as a full HtmlResponse

        Returns:
            Reponse: the response for the given load_page
        """

      
        components_link_srcs = "\n".join([f"""<script src={request.url_for(jpconfig.STATIC_NAME, path=file_name)}</script>""" for file_name in justpy_app.component_file_list
        ])


        page_ready = "page_ready" in self.events #???
        result_ready = "result_ready" in self.events #???
        reload_interval = self.reload_interval
        if reload_interval:
            reload_interval_ms = round(reload_interval * 1000)
        else:
            reload_interval_ms = 0
            

        static_resources_url = request.url_for("static",
                                               path="/")
        assert hasattr(self, "to_json_optimized")
        page_json = self.build_json()

        setup_skeleton_script_src = ""
        if jpconfig.USE_SVELTE_SKELETON:
            setup_skeleton_script_src = "<script src='/templates/js/svelte/skeleton_setup.js'></script>"
        response_string = ResponsiveStatic_CSR_ResponseMixin.get_html_response_string(self.page_id,
                                                                         self.title,
                                                                         json.dumps(
                                                                             self.use_websockets),
                                                   self.redirect,
                                                   self.display_url,
                                                   json.dumps(page_ready),
                                                   json.dumps(result_ready),
                                                   reload_interval_ms,
                                                   self.events,
                                                   static_resources_url,
                                                   json.dumps(self.debug),
                                                   jpconfig.BASE_URL,
                                                                                      
                                                                                      page_json,
                                                                                      head_html = self.head_html,
                                                   body_style=self.body_style,
                                                   body_classes= self.body_classes,
                                                   body_html=self.body_html,
                                                                                      components_link_srcs=components_link_srcs,
                                                                                      setup_skeleton_script_src = setup_skeleton_script_src,
                                                                                      skeleton_data_theme = self.skeleton_data_theme,
                                                                                      csr_bundle_dir = self.csr_bundle_dir
                                                   )
        return HTMLResponse(content=response_string)
    
    
