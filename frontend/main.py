from fasthtml.common import *
from layout import layout
from cart import cart
from main_page import main_page
from stylesheet import stylesheet

css = stylesheet
app,rt = fast_app(live=True,hdrs=(picolink,Style(css)))


@rt('/')
def get():
    return (
        layout(content=main_page()))
    

@rt('/cart')
def get():
    return (
        layout(content=cart())
    )

serve(port=1111)