from fasthtml.common import *

#import page
from layout import layout
from cart import *
from main_page import main_page
from stylesheet import stylesheet
from seller import *
from add_product import *
from add_bid_product import *
from item_page import item_page
from bid_page import bid_page
from review_page import *
from search_page import search_page
from search_by_category_page import search_by_category_page
from create_category import *
from history_item import *
from buy import buy
from login import *
from register import *
from decorators.auth import auth
from decorators.redirect_path import redirect_path
from admin import admin_page

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
@redirect_path
def get(session):
    return login_form()

@rt('/login')
@redirect_path
def post(session,username:str,password:str):
    return login_method(session,username,password)

@rt('/register')
@redirect_path
def get(session):
    return register_form()

@rt('/register')
@redirect_path
def post(name:str,email:str,phone_number:str,username:str,password:str,birth_date:str,gender:str,address:str,session):
    return register_post(name,email,phone_number,username,password,birth_date,gender,address,session)

@rt('/cart')
def get(session):
    return layout(cart(session),session)

@rt('/cart/{id}')
def post(amount:str,id:str,session):
    return add_to_cart(id,amount,session)

@rt('/cart/{item_id}')
def delete(item_id:str,session):
    return remove_from_cart(item_id,session)

@rt('/cart/{item_id}')
def patch(item_id:str,select:bool,session):
    return set_selected(item_id,select,session)

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
    return (layout(review_page(id,session),session))

@rt("/review/submit",methods=["post"])
def post(review:str,rating:int,item_id:str,session):
    return submit_review_page(review,rating,item_id,session)

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
def get(session , request : Request):
    return layout(add_bid_product_page(request),session)

@rt('/seller/add_bid/submit',  methods=["post"])
def get(session , product : Bid_Product , request : Request):
    return layout(submit_bid_product_page(product , request ),session)

@rt("/update_stock", methods=["post"])
async def post(session , add_stock : Stock_product ,request: Request):
    result = await update_stock(add_stock,request)
    return layout(result , session)

@rt("/edit_product", methods=["post"])
async def post(session , edit : Edit_product,request: Request):
    result = await edit_product(edit , request)
    return layout(result,session)

@rt('/admin/create_category')
@auth(['Admin'])
def get(session):
    return create_category()

@rt('/admin/create_category')
@auth(['Admin'])
def post(session,category_name:str,category_description:str):
    return post_create_category(category_name,category_description)

@rt('/admin')
@auth(['Admin'])
def get(session):
    return layout(admin_page(),session)

@rt('/history')
def get(session):
    return layout(order_history_page(),session)

@rt('/purchase')
def get(session):
    return layout(buy(),session)
serve(port=1111)