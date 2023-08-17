# https://www.creative-tim.com/learning-lab/tailwind-starter-kit/documentation/css/typography/headings
from py_tailwind_utils import *

h1 = [xl3, lh.normal, lh.normal, mr / st / 0, mr / sb / 2, text / gray / 6]

h2 = [fz.lg, lh.normal, fw.semibold, mr / sl / 2, mr / sb / 2]  # "prose", "prose-2xl"

h3 = [fz.lg, fw.semibold, lh.normal, mr / sl / 2, mr / sb / 2]  # "prose", "prose-2xl"

h4 = [fz._, lh.normal, fw.semibold, mr / sl / 2, mr / sb / 2]  # "prose", "prose-2xl"

h5 = [fz._, lh.normal, fw.semibold, mr / sl / 2, mr / sb / 2]  # "prose", "prose-2xl"

h6 = [fz._, lh.normal, fw.semibold, mr / sl / 2, mr / sb / 2]  # "prose", "prose-2xl"

para = [
    base,
    fw.light,
    relaxed,
    mr / st / 0,
    mr / sb / 4,
]

ul = [mr / 2, pd / 2, li.disc]
ol = [mr / 2, pd / 2, W / "1/2", li.disc]
img = [mr / 2, pd / 2]
# li is also tailwind constructs
# name collision can be confusing
li = []
button = [
    bg / gray / 1,
    fc / gray / 6,
    mr / sr / 1,
    mr / sb / 1,
    pd / x / 4,
    pd / y / 2,
    bold,
    outline._,
    shadow._,
    shadow.sm,
    tt.u,
    *hover(shadow.md, bg / gray / 2, outline / 4, bdr.md),
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
    *h2,
    fw.bold,  # shadow.sm, #shadows no good
    # sw/slate/"500/50"
]  # "prose", "prose-2xl"

subsubheading_text = [
    *h3,
    fw.medium,
    W / 96  # shadow.lg,
    # sw/slate/"500/80"
]  # "prose", "prose-2xl"

spacing = []
centering_div = [db.f, jc.center]
# span = [base, fw.light, relaxed, *spacing, ]
span = [pd / 1]

form = [db.f, jc.center]
theme = []  # default background, font, border, etc stuff
P = [pd / x / 2, pd / y / 1]  # W/"11/12" <-- this should be done optionally
A = [
    fc / gray / 6,
    pd / 1,
    pd / x / 1,
    *hover(fc / gray / 9),
]  # pd/x/4 : again optionally
stackv = [db.f, flx.col]
stackh = [db.f, *spacing]
stackw = [
    db.f,
    flx.wrap,
    jc.center,
]
stackd = [db.f, *spacing]
# ================ copied from fancy str--using empty ================
_ = dbr = Dict()
_.banner = []
_.result = [hidden / ""]

border_style = []

icon_button = [
    bg / gray / 1,
    ta.center,
    pd / 1,
    shadow.md,
    pd / 1,
    *hover(bg / gray / 2),
]


theme = []

heading = heading_box
heading2 = subheading_box
heading_span = heading_text
heading2_span = subheading_text

# span = [*theme, *spacing, db.f, ai.center]
prose = [
    fc / gray / 6,
    prose.lg,
    max / W / "prose",
]  # TODO:use some other name than prose
# prose = [fc/gray/6, "prose", "prose-2xl"]

divbutton = [db.f, jc.center]
# button = [fz.xl, bg/gray/2,  fc/gray/6, ta.center, bt.bd,
#           bdr.md,   pd/1, shadow.md, mr/2, op.c, hover(bg/gray/4)]

expansion_item = [mr / st / 0, bg / gray / 2, shadow.sm]

inputJbutton = [pd / 4, bg / gray / 1, flex, jc.center, *border_style]
select = [fz.sm, mr / "2", bg / "inherit"]
selectwbanner = [bt.bd, bdr.md, bd / gray / 1, pd / 1, mr / x / 2]

infocard = [mr / 4]
# [db.f, flx.col, bg/pink/1]

barpanel = [mr / 1]

slider = [
    H / 6,
    bg / gray / 9,
    bg / opacity / 5,
    db.f,
    ai.center,
    mr / 1,
]
circle = [
    W / 6,
    H / 6,
    bg / gray / 7,
    fc / pink / 2,
    bdr.full,
    mr / 2,
    noop / bt.bd,
    bd / gray / 1,
    *hover(noop / bds.double, noop / bt.bd, bg / gray / 1, bd / gray / 2),
]  # bg/gray/5

expansion_item = [mr / 1, bg / gray / 2]

textarea = [
    fz.sm,
    fw.bold,
    fc / gray / 6,
    bg / gray / 1,
    opacity / 80,
    fw.light,
    ta.center,
    pd / 1,
    W / "full",
    H / "full",
]

textinput = [db.f, jc.center, bt.bd, bdr.md, bd / gray / 1]
input = [bg / gray / 1, opacity / 80]


cell = [fc / gray / 6, fz.xl, pd / 1, bg / gray / 2]

left_cell = [*cell, ta.end, W / "5/12"]
right_cell = [*cell, ta.start, W / "5/12"]
eq_cell = [*cell, ta.center, op.c]

option = []
label = [pd / 1]
wp = [bg / gray / 2, bg / opacity / "25"]

# TODO:z-10
# W/full or max or screen is not working at all
# nav  = [container, ppos.fixed, top/0, bg/green/6]
nav = [top / 0]
footer = [mr / st / 4, shadow._]
div = []
hr = [
    mr / st / 4,
    mr / sb / 4,
    bt.bd,
    bd / gray / "400/20",
    bg / gray / "400/20",
    container,
]


def stackG(num_cols, num_rows):
    return [db.g, gap / 1, G / cols / f"{num_cols}", G / rows / f"{num_rows}", gf.row]


def get_color_tag(colorname):
    return globals()[colorname]


def build_classes(*args):
    return tstr(*args)


td = [bt.bd, pd / 2, ta.center]
tr = [
    [bg / gray / 2, fc / gray / 6],
    [bg / pink / 1, fc / gray / 6],
]  # for odd/even row  # 'text-gray-600'

tbl = [
    fz.sm,
    tbl.auto,
    W / full,
    ovf / auto,
    ovf / x / auto,
]  # TODO: incorporate into twtags

expansion_container = [mr / st / 8, bg / gray / 1, shadow.sm, fz.lg]

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
container = [mr / x / auto, container]

default_border = [bd / 2, bd / gray / 4, bdr.lg]
dockbar = [
    *stackh,
    bg / pink / 1,
    *default_border,
    jc.center,
    space / x / 2,
    W / full,
    H / 16,
]
code = [bg / gray / 1]
pre = [bg / gray / 1]
collapsible = []
chartjs = []
