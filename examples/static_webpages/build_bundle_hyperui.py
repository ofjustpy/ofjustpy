import macropy.activate
from svelte_safelist_builder import get_svelte_safelist
twtags, fontawesome_icons = get_svelte_safelist("example_008")


# which font families to include
font_families = []

from  svelte_bundler import hyperui_bundle_builder

hyperui_bundle_builder(twtags,
                                    font_families=font_families,
                                    fontawesome_icons = fontawesome_icons,
                                    ui_library="hyperui",
                                    output_dir="./static/hyperui"
                                    )
