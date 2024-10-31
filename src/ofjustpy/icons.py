from .parse_svg_component import parse as parse_svg_component
from .HC_TF import gen_HC_type
from ofjustpy_engine.HCType import HCType
from ofjustpy_engine import HC_Div_type_mixins as TR
from . import ui_styles

class fontawesomeBaseComponentMixin:
    def __init__(self, *args, **kwargs):
        """

        """
        self.domDict.vue_type = "fontawesome_component"

        self.domDict.events = []
        self.domDict.show = kwargs.get("show", True)
        self.domDict.debug = kwargs.get("debug", False)
        pass



class updateFAClasses:
    """
    post process to apply fontawesome classes to self.domDict.classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        """
        self.update_extra_classes("svg-inline--fa fa-user fa-fw fa-2x")

        pass
        
    
    
FontAwesomeIcon = gen_HC_type(HCType.passive,
                              "FontAwesomeIcon",
                              TR.FontAwesomeIconMixin,
                              stytags_getter_func=lambda m=ui_styles: m.sty.fontawesome,
                              baseComponentMixinType = fontawesomeBaseComponentMixin,
                              static_addon_mixins = [updateFAClasses]
                              )
# Icon_Cog = lambda **kwargs: parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
#   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
#   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
# </svg>""")


# Icon_Teams = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5 opacity-75"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#         stroke-width="2"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
#         />
#       </svg>
# """)


# Icon_Billing = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5 opacity-75"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#         stroke-width="2"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
#         />
#       </svg>
# """)

# Icon_Invoices = lambda **kwargs: parse_svg_component("""
# <svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5 opacity-75"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#         stroke-width="2"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"
#         />
#       </svg>

# """)

# Icon_Account = lambda **kwargs: parse_svg_component(""" <svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5 opacity-75"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#         stroke-width="2"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
#         />
#       </svg>

# """)
# Icon_Menu = lambda **kwargs: parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
#   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
# </svg>""")



# Icon_Chevronright = lambda **kwargs: parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
#   <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
# </svg>""")

# Icon_Chevronleft = lambda **kwargs: parse_svg_component("""
#       <svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5 rtl:rotate-180"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
#           clip-rule="evenodd"
#         />
#       </svg>
# """)
      
# Icon_Chevrondown = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-4 w-4"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
#           clip-rule="evenodd"
#         />
#       </svg>""")

# Icon_ChartUp = lambda **kwargs: parse_svg_component("""<svg
#       xmlns="http://www.w3.org/2000/svg"
#       class="h-4 w-4"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke="currentColor"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         stroke-width="2"
#         d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
#       />
#     </svg>
# """)

# Icon_ChartDown = lambda **kwargs: parse_svg_component("""<svg
#       xmlns="http://www.w3.org/2000/svg"
#       class="h-4 w-4"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke="currentColor"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         stroke-width="2"
#         d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"
#       />
#     </svg>
# """)

# Icon_PaperMoney = lambda **kwargs: parse_svg_component("""
#       <svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-6 w-6"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#         stroke-width="2"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"
#         />
#       </svg>

# """
#     )

# Icon_IdCard = lambda **kwargs: parse_svg_component("""
#         <svg
#           class="h-6 w-6 sm:h-5 sm:w-5"
#           xmlns="http://www.w3.org/2000/svg"
#           fill="none"
#           viewBox="0 0 24 24"
#           stroke="currentColor"
#           stroke-width="2"
#         >
#           <path
#             stroke-linecap="round"
#             stroke-linejoin="round"
#             d="M10 6H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V8a2 2 0 00-2-2h-5m-4 0V5a2 2 0 114 0v1m-4 0a2 2 0 104 0m-5 8a2 2 0 100-4 2 2 0 000 4zm0 0c1.306 0 2.417.835 2.83 2M9 14a3.001 3.001 0 00-2.83 2M15 11h3m-3 4h2"
#           />
#         </svg>

# """)

# Icon_AddressPin = lambda **kwargs: parse_svg_component("""
# <svg
#           class="h-6 w-6 sm:h-5 sm:w-5"
#           xmlns="http://www.w3.org/2000/svg"
#           fill="none"
#           viewBox="0 0 24 24"
#           stroke="currentColor"
#           stroke-width="2"
#         >
#           <path
#             stroke-linecap="round"
#             stroke-linejoin="round"
#             d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
#           />
#           <path
#             stroke-linecap="round"
#             stroke-linejoin="round"
#             d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
#           />
#         </svg>

# """)

# Icon_PaymentCard = lambda **kwargs: parse_svg_component("""
# <svg
#           class="h-6 w-6 sm:h-5 sm:w-5"
#           xmlns="http://www.w3.org/2000/svg"
#           fill="none"
#           viewBox="0 0 24 24"
#           stroke="currentColor"
#           stroke-width="2"
#         >
#           <path
#             stroke-linecap="round"
#             stroke-linejoin="round"
#             d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
#           />
#         </svg>
# """)
# Icon_PaginationLeft = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-3 w-3"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
#           clip-rule="evenodd"
#         />
#       </svg>

# """)

# Icon_PaginationRight = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-3 w-3"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
#           clip-rule="evenodd"
#         />
#       </svg>""")

      
# Icon_Minus =  lambda **kwargs: parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" class="h-2 w-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
#   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
# </svg>""")


# Icon_EncircledCheckmark = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-6 w-6"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
#         />
#       </svg>""")

# Icon_Cross = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-6 w-6"
#       >
#         <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
#       </svg>""")


# Icon_Preview = lambda **kwargs: parse_svg_component("""<svg
#             xmlns="http://www.w3.org/2000/svg"
#             fill="none"
#             viewBox="0 0 24 24"
#             stroke-width="1.5"
#             stroke="currentColor"
#             class="h-4 w-4"
#           >
#             <path
#               stroke-linecap="round"
#               stroke-linejoin="round"
#               d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"
#             />
#           </svg>""")

# Icon_Warning = lambda **kwargs: parse_svg_component("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="h-5 w-5">
#       <path
#         fill-rule="evenodd"
#         d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z"
#         clip-rule="evenodd"
#       />
#     </svg>""")

# Icon_EuroCurrency = lambda **kwargs: parse_svg_component("""<svg
#     xmlns="http://www.w3.org/2000/svg"
#     fill="none"
#     viewBox="0 0 24 24"
#     stroke-width="1.5"
#     stroke="currentColor"
#     class="-ms-1 me-1.5 h-4 w-4"
#   >
#     <path
#       stroke-linecap="round"
#       stroke-linejoin="round"
#       d="M14.25 7.756a4.5 4.5 0 100 8.488M7.5 10.5h5.25m-5.25 3h5.25M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
#     />
#   </svg>""")

# Icon_BreadcrumbSepArrow = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-4 w-4"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
#           clip-rule="evenodd"
#         />
#       </svg>""")


# Icon_RightArrow = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         class="h-5 w-5"
#         viewBox="0 0 20 20"
#         fill="currentColor"
#       >
#         <path
#           fill-rule="evenodd"
#           d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
#           clip-rule="evenodd"
#         />
#       </svg>""")



# Icon_Home = lambda **kwargs: parse_svg_component("""<svg
#           xmlns="http://www.w3.org/2000/svg"
#           class="h-4 w-4"
#           fill="none"
#           viewBox="0 0 24 24"
#           stroke="currentColor"
#         >
#           <path
#             stroke-linecap="round"
#             stroke-linejoin="round"
#             stroke-width="2"
#             d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
#           />
#         </svg>""")

# Icon_Edit = lambda **kwargs: parse_svg_component("""<svg
#       xmlns="http://www.w3.org/2000/svg"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke-width="1.5"
#       stroke="currentColor"
#       class="h-4 w-4"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10"
#       />
#     </svg>""")

# Icon_Openlink = lambda **kwargs: parse_svg_component("""
# <svg
#             xmlns="http://www.w3.org/2000/svg"
#             class="h-4 w-4"
#             fill="none"
#             viewBox="0 0 24 24"
#             stroke="currentColor"
#             stroke-width="2"
#           >
#             <path
#               stroke-linecap="round"
#               stroke-linejoin="round"
#               d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
#             />
#           </svg>
# """)
# Icon_View = lambda **kwargs: parse_svg_component("""<svg
#       xmlns="http://www.w3.org/2000/svg"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke-width="1.5"
#       stroke="currentColor"
#       class="h-4 w-4"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"
#       />
#       <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
#     </svg>

# """)

# Icon_Delete = lambda **kwargs: parse_svg_component("""    <svg
#       xmlns="http://www.w3.org/2000/svg"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke-width="1.5"
#       stroke="currentColor"
#       class="h-4 w-4"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
#       />
#     </svg>
# """)

# Icon_Emailat = lambda **kwargs: parse_svg_component("""
# <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-4 w-4">
#       <path
#         fill-rule="evenodd"
#         d="M5.404 14.596A6.5 6.5 0 1116.5 10a1.25 1.25 0 01-2.5 0 4 4 0 10-.571 2.06A2.75 2.75 0 0018 10a8 8 0 10-2.343 5.657.75.75 0 00-1.06-1.06 6.5 6.5 0 01-9.193 0zM10 7.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5z"
#         clip-rule="evenodd"
#       />
#     </svg>
# """)

# Icon_Squid = lambda **kwargs: parse_svg_component("""<svg
#             class="h-8 sm:h-10"
#             viewBox="0 0 28 24"
#             fill="none"
#             xmlns="http://www.w3.org/2000/svg"
#           >
#             <path
#               d="M0.41 10.3847C1.14777 7.4194 2.85643 4.7861 5.2639 2.90424C7.6714 1.02234 10.6393 0 13.695 0C16.7507 0 19.7186 1.02234 22.1261 2.90424C24.5336 4.7861 26.2422 7.4194 26.98 10.3847H25.78C23.7557 10.3549 21.7729 10.9599 20.11 12.1147C20.014 12.1842 19.9138 12.2477 19.81 12.3047H19.67C19.5662 12.2477 19.466 12.1842 19.37 12.1147C17.6924 10.9866 15.7166 10.3841 13.695 10.3841C11.6734 10.3841 9.6976 10.9866 8.02 12.1147C7.924 12.1842 7.8238 12.2477 7.72 12.3047H7.58C7.4762 12.2477 7.376 12.1842 7.28 12.1147C5.6171 10.9599 3.6343 10.3549 1.61 10.3847H0.41ZM23.62 16.6547C24.236 16.175 24.9995 15.924 25.78 15.9447H27.39V12.7347H25.78C24.4052 12.7181 23.0619 13.146 21.95 13.9547C21.3243 14.416 20.5674 14.6649 19.79 14.6649C19.0126 14.6649 18.2557 14.416 17.63 13.9547C16.4899 13.1611 15.1341 12.7356 13.745 12.7356C12.3559 12.7356 11.0001 13.1611 9.86 13.9547C9.2343 14.416 8.4774 14.6649 7.7 14.6649C6.9226 14.6649 6.1657 14.416 5.54 13.9547C4.4144 13.1356 3.0518 12.7072 1.66 12.7347H0V15.9447H1.61C2.39051 15.924 3.154 16.175 3.77 16.6547C4.908 17.4489 6.2623 17.8747 7.65 17.8747C9.0377 17.8747 10.392 17.4489 11.53 16.6547C12.1468 16.1765 12.9097 15.9257 13.69 15.9447C14.4708 15.9223 15.2348 16.1735 15.85 16.6547C16.9901 17.4484 18.3459 17.8738 19.735 17.8738C21.1241 17.8738 22.4799 17.4484 23.62 16.6547ZM23.62 22.3947C24.236 21.915 24.9995 21.664 25.78 21.6847H27.39V18.4747H25.78C24.4052 18.4581 23.0619 18.886 21.95 19.6947C21.3243 20.156 20.5674 20.4049 19.79 20.4049C19.0126 20.4049 18.2557 20.156 17.63 19.6947C16.4899 18.9011 15.1341 18.4757 13.745 18.4757C12.3559 18.4757 11.0001 18.9011 9.86 19.6947C9.2343 20.156 8.4774 20.4049 7.7 20.4049C6.9226 20.4049 6.1657 20.156 5.54 19.6947C4.4144 18.8757 3.0518 18.4472 1.66 18.4747H0V21.6847H1.61C2.39051 21.664 3.154 21.915 3.77 22.3947C4.908 23.1889 6.2623 23.6147 7.65 23.6147C9.0377 23.6147 10.392 23.1889 11.53 22.3947C12.1468 21.9165 12.9097 21.6657 13.69 21.6847C14.4708 21.6623 15.2348 21.9135 15.85 22.3947C16.9901 23.1884 18.3459 23.6138 19.735 23.6138C21.1241 23.6138 22.4799 23.1884 23.62 22.3947Z"
#               fill="currentColor"
#             />
#           </svg>""")

# Icon_IncrementDecrement =  lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-5 w-5 text-gray-500"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M8.25 15L12 18.75 15.75 15m-7.5-6L12 5.25 15.75 9"
#         />
#       </svg>
# """)

# Icon_Search = lambda **kwargs: parse_svg_component("""<svg
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke-width="1.5"
#         stroke="currentColor"
#         class="h-4 w-4"
#       >
#         <path
#           stroke-linecap="round"
#           stroke-linejoin="round"
#           d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
#         />
#       </svg>""")

# Icon_Notification = lambda **kwargs: parse_svg_component("""<svg
#             xmlns="http://www.w3.org/2000/svg"
#             class="h-5 w-5"
#             fill="none"
#             viewBox="0 0 24 24"
#             stroke="currentColor"
#             stroke-width="2"
#           >
#             <path
#               stroke-linecap="round"
#               stroke-linejoin="round"
#               d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
#             />
#           </svg>
# """)

# Icon_HeartCircle = lambda **kwargs: parse_svg_component("""
#     <svg
#       xmlns="http://www.w3.org/2000/svg"
#       fill="none"
#       viewBox="0 0 24 24"
#       stroke-width="1.5"
#       stroke="currentColor"
#       class="h-4 w-4"
#     >
#       <path
#         stroke-linecap="round"
#         stroke-linejoin="round"
#         d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
#       />
#     </svg>
# """)

# Icon_Facebook = lambda **kwargs: parse_svg_component("""
# <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
#   <path fill-rule="evenodd" d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z" clip-rule="evenodd"/>
# </svg>
# """)

# Icon_Instagram = lambda **kwargs: parse_svg_component("""
# <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
#   <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.072 4.072 0 002.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" clip-rule="evenodd"/>
# </svg>
# """)

# Icon_Twitter = lambda **kwargs: parse_svg_component("""
# <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
#   <path d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
# </svg>
# """)

# Icon_GitHub = lambda **kwargs: parse_svg_component("""
# <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
#   <path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.65.633.698 1.025 1.595 1.025 2.688 0 3.848-2.34 4.695-4.566 4.943.359.31.678.922.678 1.854 0 1.34-.012 2.417-.012 2.748 0 .267.18.578.688.48C19.136 20.197 22 16.442 22 12.017 22 6.484 17.523 2 12 2z" clip-rule="evenodd"/>
# </svg>
# """)


# Icon_Dribble = lambda **kwargs: parse_svg_component("""
#               <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
#                 <path
#                   fill-rule="evenodd"
#                   d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z"
#                   clip-rule="evenodd"
#                 />
#               </svg>
# """)

# Icon_Degree = lambda **kwargs: parse_svg_component("""<svg
#             class="h-5 w-5"
#             fill="none"
#             stroke="currentColor"
#             viewBox="0 0 24 24"
#             xmlns="http://www.w3.org/2000/svg"
#           >
#             <path d="M12 14l9-5-9-5-9 5 9 5z"></path>
#             <path
#               d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"
#             ></path>
#             <path
#               stroke-linecap="round"
#               stroke-linejoin="round"
#               stroke-width="2"
#               d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"
#             ></path>
#           </svg>""")
          
# Icon_ShoutOut = lambda **kwargs: parse_svg_component("""
#       <svg
#         class="h-4 w-4"
#         fill="currentColor"
#         viewbox="0 0 20 20"
#         xmlns="http://www.w3.org/2000/svg"
#       >
#         <path
#           clip-rule="evenodd"
#           d="M18 3a1 1 0 00-1.447-.894L8.763 6H5a3 3 0 000 6h.28l1.771 5.316A1 1 0 008 18h1a1 1 0 001-1v-4.382l6.553 3.276A1 1 0 0018 15V3z"
#           fill-rule="evenodd"
#         />
#       </svg>
# """)

# Icon_SliderPrev = lambda **kwargs: parse_svg_component("""<svg
#               xmlns="http://www.w3.org/2000/svg"
#               fill="none"
#               viewBox="0 0 24 24"
#               stroke-width="1.5"
#               stroke="currentColor"
#               class="h-5 w-5 rtl:rotate-180"
#             >
#               <path
#                 stroke-linecap="round"
#                 stroke-linejoin="round"
#                 d="M15.75 19.5L8.25 12l7.5-7.5"
#               />
#             </svg>

# """)

# Icon_SliderNext = lambda **kwargs: parse_svg_component("""
# <svg
#               class="h-5 w-5 rtl:rotate-180"
#               fill="none"
#               stroke="currentColor"
#               viewBox="0 0 24 24"
#               xmlns="http://www.w3.org/2000/svg"
#             >
#               <path
#                 d="M9 5l7 7-7 7"
#                 stroke-linecap="round"
#                 stroke-linejoin="round"
#                 stroke-width="2"
#               />
#             </svg>

# """


#     )

# Icon_Rated = lambda **kwargs: parse_svg_component("""
# <svg
#                     class="h-5 w-5"
#                     fill="currentColor"
#                     viewBox="0 0 20 20"
#                     xmlns="http://www.w3.org/2000/svg"
#                   >
#                     <path
#                       d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
#                     />
#                   </svg>

# """)
                                                      
# Icon_Plus = lambda **kwargs: parse_svg_component("""
#       <svg
#         class="h-5 w-5 shrink-0 transition duration-300 group-open:-rotate-180"
#         xmlns="http://www.w3.org/2000/svg"
#         fill="none"
#         viewBox="0 0 24 24"
#         stroke="currentColor"
#       >
#         <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
#       </svg>
# """)
