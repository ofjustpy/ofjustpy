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


# 'bg-amber-500',
# 'bg-blue-500',
# 'bg-cyan-500',
# 'bg-emerald-500',
# 'bg-fuchsia-500',
# 'bg-gray-200',
# 'bg-gray-500',
# 'bg-gray-700',
# 'bg-gray-900',
# 'bg-green-500',
# 'bg-indigo-500',
# 'bg-inherit',
# 'bg-lime-500',
# 'bg-neutral-500',
# 'bg-opacity-25',
# 'bg-opacity-5',
# 'bg-orange-500',
# 'bg-pink-500',
# 'bg-purple-500',
# 'bg-red-500',
# 'bg-rose-500',
# 'bg-sky-500',
# 'bg-slate-500',
# 'bg-stone-500',
# 'bg-teal-500',
# 'bg-violet-500',
# 'bg-yellow-500',


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
