from fasthtml.common import *

#import page
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
from register import *
from decorators.auth import auth

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

    
css = stylesheet
app,rt = fast_app(live=True,hdrs=(picolink,Style(css)))

#protect route example (session variable is neccessary)
@rt('/test2')
@auth(['Customer','Admin'])
def test(session):
    return Div('hi')

@app.get('/logout')
def logout(session):
    session.pop('auth',None)
    return Redirect('/')
    
@rt('/')
def get(session):
    return (layout(main_page(),session))

@rt('/login')
def get():
    return login_form()

@rt('/login')
def post(session,username:str,password:str):
    return login_method(session,username,password)

@rt('/register')
def get():
    return register_form()

@rt('/register')
def post(name:str,email:str,phone_number:str,username:str,password:str,birth_date:str,gender:str,address:str,session):
    print(gender)
    return register_post(name,email,phone_number,username,password,birth_date,gender,address,session)

@rt('/cart')
def get(session):
    return layout(cart(),session)

@rt('/category/{category}')
def get(category:str,session):
    return (layout(search_by_category_page(category),session))

@rt('/search/')
def get(keyword:str,session):
    return layout(search_page(keyword),session)

@rt('/item/{id}')
def get(id:str,session):
    return (layout(item_page(id),session))
    
@rt('/bid/{id}')
def get(id:str,session):
    return (layout(bid_page(id),session))

@rt('/review/{id}')
def get(id:str,session):
    return (layout(review_page(id),session))

@rt('/seller')
@auth(['Seller', 'Admin'])
def get(session, request: Request):
    return layout(product_management(request), session)

@rt('/seller/add')
def get(session, request : Request):
    return layout(add_product_page(request),session)

@rt('/seller/add/submit', methods=["post"])
async def get(session, product: Product , request : Request):
    content = await submit_product_page(product , request)  
    return layout(content, session)

@rt('/seller/add_bid')
def get(session):
    return layout(add_bid_product_page(),session)

@rt('/seller/add_bid/submit')
def get(session):
    return layout(submit_bid_product_page(),session)

@rt('/admin/create_category')
def get():
    return create_category()

@rt('/admin/create_category')
def post(category_name:str,category_description:str):
    return post_create_category(category_name,category_description)

@rt('/history')
def get(session):
    return layout(order_history_page(),session)

@rt('/purchase')
def get(session):
    return layout(buy(),session)
serve(port=1111)