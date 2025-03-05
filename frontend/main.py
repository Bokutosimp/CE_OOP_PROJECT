from fasthtml.common import *
from layout import layout
from cart import cart
from main_page import main_page
from stylesheet import stylesheet
from seller import product_management
from add_product import *
from add_bid_product import *
from item_page import item_page
from bid_page import bid_page
from review_page import review_page
from search_page import search_page
from search_by_category_page import search_by_category_page
from create_category import *
from history_item import *
from buy import buy
from login import *

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

css = stylesheet
app,rt = fast_app(live=True,hdrs=(picolink,Style(css)))

@rt('/')
def get():
    return (
        layout(content=main_page()))

@rt('/login')
def get():
    return login_form()

@rt('/login')
def post(session,username:str,password:str):
    print(username,password)
    return login_method(session,username,password)

@rt('/cart')
def get():
    return (layout(content=cart()))

@rt('/category/{category}')
def get(category:str):
    return (layout(content=search_by_category_page(category)))

@rt('/search/')
def get(keyword:str):
    return layout(search_page(keyword))

@rt('/item/{id}')
def get(id:str):
    return (layout(content=item_page(id)))
    
@rt('/bid/{id}')
def get(id:str):
    return (layout(content=bid_page(id)))

@rt('/review/{id}')
def get(id:str):
    return (layout(content=review_page(id)))

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

@rt('/admin/create_category')
def get():
    return create_category()

@rt('/admin/create_category')
def post(category_name:str,category_description:str):
    return post_create_category(category_name,category_description)

@rt('/history')
def get():
    return  layout(content=order_history_page())

@rt('/purchase')
def get():
    return layout(content=buy())
serve(port=1111)