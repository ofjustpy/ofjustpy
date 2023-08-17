"""
Enables creation of hierarchal context within
which components can be placed. Provides a way to id
the components which can later be useful to perform build uiedits.
"""
import functools

from addict import Dict

# There is only one core tracker globally
# If you need different core tracker for each page
# simply put them in different uictx

hierarchy_tracker = Dict()
curr_hierarchy_tracker = hierarchy_tracker


class uictx:
    _currSpath = "/"

    def __init__(self, ctx):
        self.ctx = ctx
        pass

    def __enter__(self):
        global curr_hierarchy_tracker
        if self.ctx not in curr_hierarchy_tracker:
            curr_hierarchy_tracker[self.ctx] = Dict()
        self.pctx = curr_hierarchy_tracker
        self.pspath = uictx._currSpath
        curr_hierarchy_tracker = curr_hierarchy_tracker[self.ctx]
        uictx._currSpath = uictx._currSpath + f"{self.ctx}/"
        return curr_hierarchy_tracker

    def __exit__(self, type, value, traceback):
        global curr_hierarchy_tracker
        curr_hierarchy_tracker = self.pctx
        uictx._currSpath = self.pspath


def id_assigner(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        the_comp = func(*args, **kwargs)
        id = uictx._currSpath + the_comp.key
        the_comp.id = id
        curr_hierarchy_tracker[the_comp.key] = the_comp
        return the_comp

    return wrapper
