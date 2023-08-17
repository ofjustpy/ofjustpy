import ofjustpy as oj
with oj.MountCtx("example_001"):
    from . import example_001


with oj.MountCtx("example_002"):
    from . import example_002

with oj.MountCtx("example_003"):
    from . import example_003

with oj.MountCtx("example_004"):    
    from . import example_004

