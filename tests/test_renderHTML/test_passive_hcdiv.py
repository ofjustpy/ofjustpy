
import ofjustpy as oj

aspan = oj.PC.Span(text="abc")
print (aspan.to_html())

adiv = oj.PC.Div(childs=[aspan])
print (adiv.to_html())

