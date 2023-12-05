
Stub.add_register_childs
.........................

- all stubs call register_childs
- HC Passive/active/mutable register_childs are noops
- Div Passive/active stub
  - register_childrens calls add_register_childs which invokes stub()
    for all the childs

Recursion loop: webpage init calls add_register_childs
  which calls  c= stub() (as in gen_stub) and then
  the c.__call__ (which now has the target) calls
  its childs and the recursion continues.
  
  
    
gen_stub()
..........

1. tracker calls gen_stub with session_manager kwargs
   
now tracking gen_stub for
- HCPassive
- HCActive
- DivPassive
   

is_static
.........
is_static is used in two places

1. mutable components do not register static components in their spath
2. Same thing with WebPage.
   
   
  
Design Gotcha
..............
- For passive/active components
add_register_childs is called by stub
- For mutable components
add_register_childs is called by
init of the mutable objects
This is done because we want to create
mapping from id to the object.


