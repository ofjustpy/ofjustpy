
import ofjustpy as oj

aspan = oj.PC.Span(text="abc")
print (list(aspan.to_html_iter()))

adiv = oj.PC.Div(childs=[aspan])
print (list(adiv.to_html_iter()))

