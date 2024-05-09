from py_tailwind_utils import *
import ofjustpy as oj
from addict import Dict
from html_writer.macro_module import macros, writer_ctx



app = oj.load_app()

with writer_ctx:
    with Container() as root_box:
        with Title(title_text="Title of this page", twsty_tags=[fc/slate/700]):
            pass

        with SubTitle(title_text="A subtitle description", twsty_tags=[fc/slate/600]):
            pass
        
        with Subsection(heading_text = "Sample Subheading",
                        content = oj.PD.Prose(text="""
Donec et mollis sem. Quisque est arcu, molestie eu pretium gravida, cursus in urna. Sed ut rutrum libero. Fusce placerat, justo in scelerisque pulvinar, ipsum diam egestas mi, sed accumsan lacus libero sit amet nisi. Pellentesque vitae nisl vestibulum, lobortis libero ac, pulvinar diam. Cras luctus dignissim orci, in vehicula turpis faucibus ac. Fusce sed faucibus eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque nunc nunc, pretium et sodales in, placerat id ligula.
Nunc et vulputate ligula, in viverra risus. Vestibulum ornare scelerisque odio ac laoreet. Donec gravida blandit ipsum sit amet congue. Maecenas dapibus urna tortor, ultricies finibus purus molestie at. Phasellus at nisl ut erat tempus volutpat. Aliquam condimentum gravida tellus at fringilla. Ut odio dolor, iaculis ac enim in, semper molestie diam. Proin fringilla velit nec leo placerat lacinia. Phasellus fermentum vitae lorem eu aliquet. """),
                        twsty_tags = [mr/st/1, pd/2]
                              ):

            with Subsubsection(heading_text="Subsubheading",
                               content = oj.PD.Prose(text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis tempus massa. Fusce imperdiet ac lectus quis porttitor. Vestibulum quis varius odio. Curabitur auctor ante at leo lobortis vulputate nec ac orci. Duis tempus euismod orci tempor tempor. Aenean pulvinar turpis quis molestie bibendum. Phasellus varius mi eu iaculis euismod. Duis dignissim in justo a eleifend. """)

                               ):
                with TitledPara(heading_text="Para title",
                                content = oj.PD.Prose(text=""" Fusce sed faucibus eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque nunc nunc, pretium et sodales in, placerat id ligula."""),
                                fix_sty_section_nesting=True
                                ):
                    pass
                pass
            pass


        pass
            

wp_endpoint = oj.create_endpoint("SubheadingBanner", childs = [root_box]
                   )


app.add_jproute("/", wp_endpoint)
