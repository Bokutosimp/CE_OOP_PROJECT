from fasthtml.common import *
from layout import layout
from component.nav import nav
from cart import cart
from main_page import main_page
from stylesheet import stylesheet
from seller import product_management
from add_product import *
from add_bid_product import *
from item_page import item_page
from search_page import search_page
from category_page import category_page

css = stylesheet
app,rt = fast_app(live=True,hdrs=(picolink,Style(css)))

@rt('/')
def get():
    return (
        layout(content=main_page()))
    

@rt('/cart')
def get():
    return (layout(content=cart()))

@rt('/category/{category}')
def get(category:str):
    return (layout(content=category_page(category)))

@rt('/search/')
def get(keyword:str):
    return layout(search_page(keyword))

@rt('/item/{id}')
def get(id:str):
    return (layout(content=item_page(id)))
    

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