import macropy.activate
from svelte_safelist_builder import get_svelte_safelist
twtags, fontawesome_icons = get_svelte_safelist("fontawesome_icons_server_side_rendering")

print ('fontawesome_icons  = ', fontawesome_icons)

# which font families to include
font_families = []

from  svelte_bundler import ssr_bundle_builder

ssr_bundle_builder(twtags,
                   font_families=font_families,
                   ui_library="ssr",
                   output_dir="./static/ssr",
                                    )
