"""
display python code as formatted text
"""

from ofjustpy_plugins import format_code
import ofjustpy as oj
app = oj.load_app()

textarea_read_fc = format_code("""textarea_input_ = oj.Textarea_("myTextarea",
                           rows=10,
                           cols=30,
                           disabled=False,
                           wrap="hard",
                           maxlength=200,
                           minlength=50,
                           debug=True,
                           twsty_tags=[bg/green/100, W/"1/3"],
disable_tracking=True,
                                   immutable=True
                           )"""
                               
                               )


wp_endpoint = oj.create_endpoint(key="example_006",
                                 childs = [textarea_read_fc],
                                 title="example_006"
                                 )

oj.add_jproute("/", wp_endpoint)

