import functools

from py_tailwind_utils import *

default_tags = [
    f"'{_}'"
    for _ in [
        "flex",
        "h-6",
        "hover:bg-gray-100",
        "hover:border",
        "hover:border-double",
        "hover:border-gray-200",
        "items-center",
        "m-1",
        "m-2",
        "p-1",
        "rounded-full",
        "text-pink-200",
        "text-sm",
        "w-6",
        "outline-offset-2",
        "outline-black",
        "outline-2",
        "outline-double",
        "flex",
        "flex-col",
        "font-bold",
        "form-checkbox",
        "gap-1",
        "grid",
        "grid-cols-2",
        "grid-flow-row",
        "grid-rows-2",
        "h-6",
        "hidden",
        "hover:border",
        "hover:border-double",
        "hover:border-gray-200",
        "invisible",
        "items-center",
        "justify-around",
        "justify-center",
        "leading-normal",
        "m-1",
        "m-2",
        "mb-1",
        "mt-0",
        "opacity-80",
        "p-1",
        "rounded-full",
        "shadow-md",
        "text-pink-200",
        "text-sm",
        "text-xl",
        "w-6",
    ]
]


def get_svelte_safelist(stubStore):
    all_twsty = set()
    for spath, stub in dictWalker(stubStore):
        for atag in stub.kwargs.get("twsty_tags"):
            all_twsty.add(tstr(atag))

    with open("svelte_safelist.txt", "w") as fh:
        all_tags = sorted(set([*[f"'{_}'" for _ in all_twsty], *default_tags]))
        all_tags = [_ for _ in all_tags if "bg-" not in _]
        fh.write(",\n".join(all_tags))



def traverse_component_hierarchy(rdbref):
    """
    recursively traverse html components contained with a
    component
    """
    if hasattr(rdbref, "components"):
        for cbref in rdbref.components:
            yield (cbref, rdbref)
            yield from traverse_component_hierarchy(cbref)


def csrfprotect(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wp = func(*args, **kwargs)
        # TBD: get SECRET_KEY from whereever  secret key should be picked.
        SECRET_KEY = "Pls use a good professional secret key"
        csrf_cookie_name = "csrftoken"
        csrf_secret = "shhshh2"
        wp.cookies[csrf_cookie_name] = "shhshh2"

        return wp

    return wrapper
