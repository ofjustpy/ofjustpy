from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj

oj.set_style("un")

from ofjustpy_plugins import format_code
code = """
with Article(classes="overflow-hidden rounded-lg shadow transition hover:shadow-lg") as comp_box:
    with Img(src=image_url, alt="Office", classes="h-56 w-full object-cover"):
        pass

    with Div(classes="bg-white p-4 sm:p-6"):
        with Time(classes="block text-xs text-gray-500", datetime=date, text=date):
            pass

        with A(href=link):
            with H3(classes="mt-0.5 text-lg text-gray-900", text=title):
                pass

        with P(classes="mt-2 line-clamp-3 text-sm/relaxed text-gray-500", text=content):
            pass
"""
fct = format_code(code)


def on_btn_click(dbref, msg, to_ms):
    print("btn clicked")
    pass


with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as top_box:

        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):

                with H2(classes="font-medium", text="📌 Effortless HTML: No-Templates, No-Boilerplate, Just Clean Pythonic Code"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass



        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="text-center"):
                with H2(text="Author HTML inline within Python code", classes="font-bold tracking-tight text-2xl"):
                    pass

            with Div(classes="flex justify-center mt-8"):
                with Ul(classes="space-y-2 text-balance text-lg text-slate-700",
                        extra_classes="tracking-tight") as desc_box:
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Eliminates need for templates ", classes=""):
                            pass
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight",  classes="w-5 h-5"):
                            pass
                        with Span(text="Low boilerplate crud", classes=""):
                            pass

                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Easy to read and maintain", classes=""):
                            pass               

            with Div(classes="mt-8 space-y-2"):            
                with Div(classes="text-center"):
                    with H2(text="Code Demo: A sample html using ofjustpy", classes="text-xl ", extra_classes="tracking-tight"):
                        pass
                with Div(classes="flex justify-center mt-2 font-bold text-sm tracking-tight overflow-auto") as code_block_container:
                    pass                        

                
code_block_container.components.append(fct)
#overview_box.components.append(feature_inline_html_infobox)                
app = oj.load_app()    

   
wp_endpoint = oj.create_endpoint(key="ssr_demo",
                                 childs = [top_box],
                                 title="Demo SSR",
                                 rendering_type="SSR")

    

oj.add_jproute("/", wp_endpoint)
# class WP:
#     def add_component(self, x):
#         pass
#     pass
# from addict import Dict
# request = Dict()
# request.session_id = "abc"
# sm = oj.get_session_manager(request)
# wp = WP()

# html_text  = "".join(top_box.to_html_iter())
# print(html_text)
#print (top_box.htmlRender_body)
