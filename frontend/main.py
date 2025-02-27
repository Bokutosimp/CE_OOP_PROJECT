from fasthtml.common import *
from layout import layout
from cart import cart
from main_page import main_page
from stylesheet import stylesheet
from seller import product_management
from add_product import *
from add_bid_product import *


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
@rt('/seller')
def get():
    return(
        layout(content=product_management())
    )

@rt('/seller/add')
def get():
    return layout(content=add_product_page())

@rt('/seller/add/submit')
def get():
    return layout(content=post())

@rt('/seller/add_bid')
def get():
    return layout(content=add_bid_product_page())

@rt('/seller/add_bid/submit')
def get():
    return layout(content=post_bid())


serve(port=1111)