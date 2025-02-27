from fasthtml.common import *

rt = fast_app()

@rt('/buy')
def get(): return Div('abc')