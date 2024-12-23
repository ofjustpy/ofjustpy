from py_tailwind_utils import *

h1 = []

h2 = []  # "prose", "prose-2xl"

h3 = []  # "prose", "prose-2xl"

h4 = []  # "prose", "prose-2xl"

h5 = []  # "prose", "prose-2xl"

h6 = []  # "prose", "prose-2xl"

para = []

ul = []
ol = []
img = []
li = []
button = []

title_text = []
subtitle_text = []

heading_box = [db.f, jc.around]
heading_text = []
subheading_box = [db.f, jc.around]
subheading_text = []

subsubheading_text = []

spacing = []
centering_div = [db.f, jc.center]
span = []

form = []
theme = []
P = []
A = []

stackv = [db.f, flxdir.col]
stackh = [db.f]
stackw = [db.f, flxw.w, jc.center]
stackd = [db.f]
_ = dbr = Dict()
_.banner = []
_.result = [hidden / ""]

border_style = []

icon_button = []

theme = []

heading = heading_box
heading2 = subheading_box
heading_span = heading_text
heading2_span = subheading_text

prose = []

divbutton = []

expansion_item = []

inputJbutton = []
select = []
selectwbanner = []

infocard = []

barpanel = []

slider = [H / 6, db.f, ai.center, space/x/4]
circle = [W / 6, H / 6, bdr.full, bg/gray/400, *hover(bds.double, noop/bd)]

expansion_item = []

textarea = []

textinput = [db.f, jc.center]
input = []

cell = []

left_cell = [*cell, ta.end, W / "5/12"]
right_cell = [*cell, ta.start, W / "5/12"]
eq_cell = [*cell, ta.center, op.c]

option = []
label = [db.f, jc.center]

wp = []

nav = [top / 0]
footer = []
div = []

hr = []


def stackG(num_cols, num_rows):
    return [db.g, G / cols / f"{num_cols}", G / rows / f"{num_rows}", gf.row]


def get_color_tag(colorname):
    return globals()[colorname]


def build_classes(*args):
    return tstr(*args)


td = []
tr = []

tbl = [fz.sm, tbl.auto, W / full, overflow.auto, overflowx.auto]

expansion_container = [fz.lg]

togglebtn = []

checkbox = []


def halign(align="center"):
    """
    align the contents : options are start, end, center, between, evenly, around
    """
    return [db.f, getattr(jc, align)]


def valign(align="center"):
    """
    align the contents : options are start, end, center, between, evenly, around
    """
    return [db.f, getattr(ai, align)]


def align(halign="center", valign="center"):
    """
    vertical and horizonal align
    """
    return [db.f, getattr(ai, valign), getattr(jc, halign)]


container = [noop/container]

default_border = [bd / 2, bdr.lg]
dockbar = [*stackh, jc.center, W / full, H / 16]
undock_button = []
code = []
pre = []
collapsible = []
chartjs = []
dt = []
dd = []
dl = []
header = []
p = []
section = []
aside = []
main = []

fieldset = []
legend = []
optgroup = []
datalist = []
titledPara = []

fontawesome = []

accordion = []

accordionitem = []
tabgroup = []

tab = []
listboxitem = []
listbox = []

details = []
summary = []
article = []
small  = []
thead = []
th = []
tbody = []
table = []
br = []
time = []

address = []
script = []
blockquote = []
fontawesome = []

shadcnui_accordionitem  = []

shadcnui_alert  = []
shadcnui_alert_title  = []
shadcnui_alert_description  = []

shadcnui_alertdialog  = []

shadcnui_alertdialog_trigger  = []
shadcnui_alertdialog_content  = []
shadcnui_alertdialog_header  = []
shadcnui_alertdialog_footer  = []
shadcnui_alertdialog_cancel  = []
shadcnui_alertdialog_action  = []
shadcnui_alertdialog_title  = []
shadcnui_alertdialog_description  = []

shadcnui_calendar  = []

shadcnui_checkbox  = []

shadcnui_label  = []

shadcnui_button  = []

shadcnui_select = []
shadcnui_select_root = []
shadcnui_select_trigger = []
shadcnui_select_value = []
shadcnui_select_content = []
shadcnui_select_item = []
shadcnui_select_label = []

shadcnui_card= []

shadcnui_card_header = []
shadcnui_card_title = []
shadcnui_card_description = []
shadcnui_card_content = []
shadcnui_card_footer = []


shadcnui_input  = []
shadcnui_carousel_item = []
shadcnui_carousel_content = []
shadcnui_carousel_previous = []
shadcnui_carousel_next = []
shadcnui_carousel = []

shadcnui_collapsible = []

shadcnui_breadcrumb = []

shadcnui_breadcrumb_list = []

shadcnui_avatar = []

shadcnui_avatar_image = []

shadcnui_avatar_fallback = []

shadcnui_breadcrumb = []
shadcnui_breadcrumb_list = []
shadcnui_breadcrumb_item = []
shadcnui_breadcrumb_link = []
shadcnui_breadcrumb_separator = []
shadcnui_breadcrumb_page = []

shadcnui_collapsible = []
shadcnui_collapsible_trigger = []
shadcnui_collapsible_content = []

shadcnui_command = []
shadcnui_command_input = []
shadcnui_command_list = []
shadcnui_command_empty = []

shadcnui_command_group = []
shadcnui_command_item = []
shadcnui_command_separator = []


shadcnui_dialog = []
shadcnui_dialog_trigger = []
shadcnui_dialog_content = []
shadcnui_dialog_header = []
shadcnui_dialog_title = []
shadcnui_dialog_description = []

shadcnui_drawer = []
shadcnui_drawer_trigger = []
shadcnui_drawer_content = []
shadcnui_drawer_header = []
shadcnui_drawer_title = []
shadcnui_drawer_description = []
shadcnui_drawer_footer = []
shadcnui_drawer_button = []
shadcnui_drawer_close = []

shadcnui_dropdownmenu = []
shadcnui_dropdownmenu_trigger = []
shadcnui_dropdownmenu_content = []
shadcnui_dropdownmenu_group = []
shadcnui_dropdownmenu_label = []
shadcnui_dropdownmenu_separator = []
shadcnui_dropdownmenu_item = []

shadcnui_hovercard = []
shadcnui_hovercard_trigger = []
shadcnui_hovercard_content = []

shadcnui_menubar = []
shadcnui_menubar_menu = []
shadcnui_menubar_trigger = []
shadcnui_menubar_content = []
shadcnui_menubar_item = []
shadcnui_menubar_separator = []
shadcnui_menubar_shortcut = []

shadcnui_pagination = []
shadcnui_pagination_content = []
shadcnui_pagination_item = []
shadcnui_pagination_prevbutton = []
shadcnui_pagination_ellipsis = []
shadcnui_pagination_link = []
shadcnui_pagination_nextbutton = []
shadcnui_progress = []


shadcnui_radiogroup = []
shadcnui_radiogroup_item = []
shadcnui_radiogroup_input = []


shadcnui_resizable = []
shadcnui_resizable_panegroup = []
shadcnui_resizable_pane = []
shadcnui_resizable_handle = []

shadcnui_scrollarea = []

shadcnui_separator = []

shadcnui_sheet = []
shadcnui_sheet_trigger = []
shadcnui_sheet_content = []
shadcnui_sheet_header = []
shadcnui_sheet_title = []
shadcnui_sheet_description = []

shadcnui_skeleton = []

shadcnui_slider = []

shadcnui_switch = []

shadcnui_table = []
shadcnui_table_root = []
shadcnui_table_caption = []
shadcnui_table_header = []
shadcnui_table_body = []
shadcnui_table_row = []
shadcnui_table_head = []
shadcnui_table_cell = []


shadcnui_tabs = []
shadcnui_tabs_root = []
shadcnui_tabs_list = []
shadcnui_tabs_trigger = []
shadcnui_tabs_content = []

shadcnui_textarea = []

shadcnui_tooltip = []
shadcnui_tooltip_root = []
shadcnui_tooltip_trigger = []
shadcnui_tooltip_content = []

shadcnui_accordion = []
shadcnui_accordion_root = []
shadcnui_accordion_item = []
shadcnui_accordion_trigger = []
shadcnui_accordion_content = []

skeletonui_ratings = []

skeletonui_stepper = []
skeletonui_step = []

section_title_sty = [    (fz.xl4, fw.bold, ff.mono),(fz.xl4, fw.semibold, ff.mono),(fz.xl4, fw.medium, ff.mono),(fz.xl4, fw.light, ff.mono),(fz.xl4, fw.thin, ff.mono),
    (fz.xl3, fw.bold, ff.mono),(fz.xl3, fw.semibold, ff.mono),(fz.xl3, fw.medium, ff.mono),(fz.xl3, fw.light, ff.mono),(fz.xl3, fw.thin, ff.mono),
    (fz.xl2, fw.bold, ff.mono),(fz.xl2, fw.semibold, ff.mono),(fz.xl2, fw.medium, ff.mono),(fz.xl2, fw.light, ff.mono),(fz.xl2, fw.thin, ff.mono),
    (fz.xl, fw.bold, ff.mono),(fz.xl, fw.semibold, ff.mono),(fz.xl, fw.medium, ff.mono),(fz.xl, fw.light, ff.mono),(fz.xl, fw.thin, ff.mono),
    (fz.lg, fw.bold, ff.mono),(fz.lg, fw.semibold, ff.mono),(fz.lg, fw.medium, ff.mono),(fz.lg, fw.light, ff.mono),(fz.lg, fw.thin, ff.mono),
    (fz._, fw.bold, ff.mono),(fz._, fw.semibold, ff.mono),(fz._, fw.medium, ff.mono),(fz._, fw.light, ff.mono),(fz._, fw.thin , ff.mono)

    ]
iframe = []
