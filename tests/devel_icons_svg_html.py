from ofjustpy.icons import FontAwesomeIcon

fa_icon = FontAwesomeIcon(label="faCross")
html_text  = "".join(fa_icon.to_html_iter())
print(html_text)
