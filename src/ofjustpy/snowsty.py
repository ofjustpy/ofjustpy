# https://www.creative-tim.com/learning-lab/tailwind-starter-kit/documentation/css/typography/headings
from py_tailwind_utils import *

h1 = [xl3, fw.bold,  mr/sl/2, fc/slate/700]

h2 = [fz.lg, fw.semibold, mr / sl / 2,  fc/slate/700]  # "prose", "prose-2xl"

h3 = [fz.lg, fw.normal,  mr / sl / 2, fc/slate/600]  # "prose", "prose-2xl"

h4 = [fz._,  fw.normal, mr / sl / 2, fc/slate/600]  # "prose", "prose-2xl"

h5 = [fz._,  fw.light, mr / sl / 2, fc/slate/500]  # "prose", "prose-2xl"

h6 = [fz.sm,  fw.light, mr / sl / 2, fc/slate/500]  # "prose", "prose-2xl"


para = [ base, fw.light, relaxed, mr / st / 0, mr / sb / 4, ]

ul = [mr / 2, pd / 2, lst.disc]
ol = [mr / 2, pd / 2, W / "1/2", lst.disc]
img = [mr / 2, pd / 2]
# li is also tailwind constructs
# name collision can be confusing
li = []
button = [ bg / gray / 100, fc / gray / 600, mr / sr / 1, mr / sb / 1, pd / x / 4, pd / y / 2, bold, boxtopo.outline, shadow._, shadow.sm, tt.u, *hover(shadow.md, bg / gray / 200, outline / 4, bdr.md),
]


# title_box = [db.f, jc.center]
title_text = [xl6, fw.bold, mr / st / 0, mr / sb / 2, text / gray / 8]
subtitle_text = [xl4, fw.medium, mr / st / 1, mr / sb / 2, text / gray / 8]

# title_banner = [
#     db.f, jc.center, *spacing]

# title_span = [bdr.md, fc/gray/6, fz.xl, pd/2]

heading_box = [db.f, jc.around]
heading_text = [*h1, fw.bold]
subheading_box = [db.f, jc.around]
subheading_text = [
    fw.bold,
    fc/slate/"700/50",
    # shadow.sm, #shadows no good
    # sw/slate/"500/50"
]  # "prose", "prose-2xl"

# subsubheading_text = [
#     fw.medium,
#     fc/slate/"500/50"
#     #W / 96  # shadow.lg,
#     # sw/slate/"500/80"
# ]  # "prose", "prose-2xl"

# no difference between medium and normal for mono - changing to light, extralight
# light extralight also not working
# switch to thin

section_title_sty = [    (fz.xl4, fw.bold, ff.mono),(fz.xl4, fw.semibold, ff.mono),(fz.xl4, fw.medium, ff.mono),(fz.xl4, fw.light, ff.mono),(fz.xl4, fw.thin, ff.mono),
    (fz.xl3, fw.bold, ff.mono),(fz.xl3, fw.semibold, ff.mono),(fz.xl3, fw.medium, ff.mono),(fz.xl3, fw.light, ff.mono),(fz.xl3, fw.thin, ff.mono),
    (fz.xl2, fw.bold, ff.mono),(fz.xl2, fw.semibold, ff.mono),(fz.xl2, fw.medium, ff.mono),(fz.xl2, fw.light, ff.mono),(fz.xl2, fw.thin, ff.mono),
    (fz.xl, fw.bold, ff.mono),(fz.xl, fw.semibold, ff.mono),(fz.xl, fw.medium, ff.mono),(fz.xl, fw.light, ff.mono),(fz.xl, fw.thin, ff.mono),
    (fz.lg, fw.bold, ff.mono),(fz.lg, fw.semibold, ff.mono),(fz.lg, fw.medium, ff.mono),(fz.lg, fw.light, ff.mono),(fz.lg, fw.thin, ff.mono),
    (fz._, fw.bold, ff.mono),(fz._, fw.semibold, ff.mono),(fz._, fw.medium, ff.mono),(fz._, fw.light, ff.mono),(fz._, fw.thin , ff.mono)

    ]

# section_title_sty = [
#     (fz.xl4, fw.bold, ff.mono), (fz.xl3, fw.bold, ff.mono), (fz.xl2, fw.bold, ff.mono), 
#     (fz.xl, fw.bold, ff.mono), (fz.lg, fw.bold, ff.mono), (fz._, fw.bold, ff.mono), 
#     (fz.xl4, fw.semibold, ff.mono), (fz.xl3, fw.semibold, ff.mono), (fz.xl2, fw.semibold, ff.mono), 
#     (fz.xl, fw.semibold, ff.mono), (fz.lg, fw.semibold, ff.mono), (fz._, fw.semibold, ff.mono), 
#     (fz.xl4, fw.medium, ff.mono), (fz.xl3, fw.medium, ff.mono), (fz.xl2, fw.medium, ff.mono), 
#     (fz.xl, fw.medium, ff.mono), (fz.lg, fw.medium, ff.mono), (fz._, fw.medium, ff.mono), 
#     (fz.xl4, fw.normal, ff.mono), (fz.xl3, fw.normal, ff.mono), (fz.xl2, fw.normal, ff.mono), 
#     (fz.xl, fw.normal, ff.mono), (fz.lg, fw.normal, ff.mono), (fz._, fw.normal, ff.mono), 
#     (fz.xl4, fw.light, ff.mono), (fz.xl3, fw.light, ff.mono), (fz.xl2, fw.light, ff.mono), 
#     (fz.xl, fw.light, ff.mono), (fz.lg, fw.light, ff.mono), (fz._, fw.light, ff.mono)
# ]


spacing = []
centering_div = [db.f, jc.center]
# span = [base, fw.light, relaxed, *spacing, ]
span = [pd / 1]

form = [db.f, jc.center]
theme = []  # default background, font, border, etc stuff
P = [pd / x / 2, pd / y / 1]  # W/"11/12" <-- this should be done optionally
A = [
    fc / gray / 600,
    pd / 1,
    pd / x / 1,
    *hover(fc / gray / 9),
]  # pd/x/4 : again optionally
stackv = [db.f, flxdir.col]
stackh = [db.f, *spacing]
stackw = [
    db.f,
    flxw.w,
    jc.center,
]
stackd = [db.f, *spacing]
# ================ copied from fancy str--using empty ================
_ = dbr = Dict()
_.banner = []
_.result = [hidden / ""]

border_style = []

icon_button = [
    bg / gray / 100,
    ta.center,
    pd / 1,
    shadow.md,
    pd / 1,
    *hover(bg / gray / 200),
]


theme = []

heading = heading_box
heading2 = subheading_box
heading_span = heading_text
heading2_span = subheading_text

# span = [*theme, *spacing, db.f, ai.center]
prose = [
    fc / gray / 800,
    ta.justify,
    prose.lg,
    #max / W / "prose",
]  # TODO:use some other name than prose
# prose = [fc/gray/6, "prose", "prose-2xl"]

divbutton = [db.f, jc.center]
# button = [fz.xl, bg/gray/2,  fc/gray/6, ta.center, bt.bd,
#           bdr.md,   pd/1, shadow.md, mr/2, op.c, hover(bg/gray/4)]

expansion_item = [mr / st / 0, bg / gray / 200, shadow.sm]

inputJbutton = [pd / 4, bg / gray / 100, flex, jc.center, *border_style]
select = [fz.sm, mr / "2", bg / "inherit"]
selectwbanner = [boxtopo.bd, bdr.md, bd / gray / 100, pd / 1, mr / x / 2]

infocard = [mr / 4]


barpanel = [mr / 1]

slider = [
    bg / slate / 500,
    bg / opacity / 500,
    db.f,
    ai.center,
    mr / 1,
    pd/2, # need some space for ring to show up
    bdr.full,
    space/x/4,
    jc.center # place the items (circles) right in the center
    
    
]
circle = [
    W/5,
    H/5,
    db.bi,
    bdr.full,
    boxtopo.bd,
    bd/slate/600,
    bg/slate/600,
    fc/white,
    *hover(bg/transparent, fc/slate/600),
    #*focus(outline.none, boxtopo.ring),
    #*active(fc/slate/5),
    fz.sm
    # W / 6,
    # H / 6,
    # bg / gray / 7,
    # fc / pink / 2,
    # bdr.full,
    # mr / 2,
    # noop / bd,
    # bd / gray / 1,
    # *hover(noop / bds.double, noop / bd, bg / gray / 1, bd / gray / 2),
]  # bg/gray/5

expansion_item = [mr / 1, bg / gray / 200]

textarea = [
    fz.sm,
    fw.bold,
    fc / gray / 600,
    bg / gray / 100,
    opacity / 80,
    fw.light,
    ta.center,
    pd / 1,
    W / "full",
    H / "full",
]

textinput = [db.f, jc.center, boxtopo.bd, bdr.md, bd / gray / 100]
input = [bg / gray / 100, opacity / 80]


cell = [fc / gray / 600, fz.xl, pd / 1, bg / gray / 200]

left_cell = [*cell, ta.end, W / "5/12"]
right_cell = [*cell, ta.start, W / "5/12"]
eq_cell = [*cell, ta.center, op.c]

option = []
label = [pd / 1]
wp = [bg / gray / 200, bg / opacity / "25"]

# TODO:z-10
# W/full or max or screen is not working at all
# nav  = [container, ppos.fixed, top/0, bg/green/6]
nav = [top / 0]
footer = [mr / st / 4, shadow._]
div = []
hr = [
    mr / st / 4,
    mr / sb / 4,
    boxtopo.bd,
    bd / gray / "400/20",
    bg / gray / "400/20",
    noop/container,
]


def stackG(num_cols, num_rows):
    return [db.g, gap / 1, G / cols / f"{num_cols}", G / rows / f"{num_rows}", gf.row]


def get_color_tag(colorname):
    return globals()[colorname]


def build_classes(*args):
    return tstr(*args)


td = [boxtopo.bd, pd / 2, ta.center]
tr = [
    [bg / gray / 200, fc / gray / 600],
    [bg / pink / 100, fc / gray / 600],
]  # for odd/even row  # 'text-gray-600'

tbl = [
    fz.sm,
    tbl.auto,
    W / full,
    overflow.auto,
    overflowx.auto,
]  # TODO: incorporate into twtags

expansion_container = [mr / st / 8, bg / gray / 100, shadow.sm, fz.lg]

togglebtn = ["q-ma-md"]

# TODO: use https://github.com/tailwindlabs/tailwindcss-forms
#'form-checkbox'
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


# Caution keep this at the last
# otherwise will override use of container at the top
container = [mr / x / auto, noop/container]

default_border = [bd / 2, bd / gray / 400, bdr.lg]
dockbar = [
    *stackh,
    bg / pink / 100,
    *default_border,
    jc.center,
    space / x / 2,
    W / full,
    H / 16,
]
code = [bg / gray / 100]
pre = [bg / gray / 100]
collapsible = []
chartjs = []

undock_button = [bd/blue/300, boxtopo.bd, bdr.full,  bg/gray/800, pd/x/3, pd/y/2, *hover(bd/blue/500)]
table = []
tr = [*variant(bg/gray/300, rv="odd"), *variant(bg/gray/200,  rv="even")]

td = [pd/x/4, pd/y/2, noop/bd]
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
details = []
summary = []
article = []
small  = []

thead = []
th = []
tbody = []
table = []
br  = []

time = []
address = []

script = []
blockquote = []

datalist = []

titledPara = []

fontawesome = []

accordion = []

accordionitem = []
tabgroup = []

tab = []
listboxitem = []
listbox = []
meltui_slider=[]

meltui_avatar=[]


meltui_calendar = []
meltui_checkbox = []

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

shadcnui_select  = []

shadcnui_select_item  = []

shadcnui_select_group  = []
shadcnui_select_content  = []

shadcnui_input  = []
shadcnui_carouselitem = []
shadcnui_carousel = []

shadcnui_collapsible = []
shadcnui_collapsible_trigger = []
shadcnui_collapsible_content = []

shadcnui_breadcrumb = []

shadcnui_breadcrumb_list = []

shadcnui_carousel = []
shadcnui_carousel_content = []
shadcnui_carousel_item = []
shadcnui_carousel_previous = []
shadcnui_carousel_next = []
shadcnui_progress = []

iframe = []

# ======================== ofjustpy_components =======================
varlistdiv = [] # ofjustpy_components.variable_length_list_TF
