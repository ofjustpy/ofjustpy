
FAQs
====


- Which attributes belong to selfdomDict vs. self.attrs?

   
- Passive/Active/Mutable containment calculus:

 Passive containers can only have passive/active components
 Mutable containers can have either

- HCCMutable classes don't have assign_id

  Because the container itself is not mutable.

- Which is the template html file
svelte.html

- What happens if mutable content is placed under static
  Static components like to call 'kwargs[a].add_component'
  at initialization time which is not available.

..
  329.     def __init__(self, *args, **kwargs):

  330.         if "a" in kwargs:

  331.             if kwargs["a"] is not None:

  332.                 kwargs["a"].add_component(self)

  333.

  334.

  335. class EventMixinBase


- Margins and spacing
  good to make rule of thumbs: mr/y/2 for within div,
  mr/y/4 for across div within section
  mr/y/8 for across div across sections

- When is build_json called
called by stub after the childs are registered
