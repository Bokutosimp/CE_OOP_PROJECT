from fasthtml.common import *
import os
import dotenv
import json
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
from shipping_status import check_status

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

dotenv.load_dotenv()

    
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
@auth(['Customer','Seller'])
def get(session):
    return layout(cart(session),session)

@rt('/cart/{id}')
@auth(['Seller', 'Customer'])
def post(session,amount:str,id:str):
    return add_to_cart(id,amount,session)

@rt('/cart/{item_id}')
@auth(['Seller', 'Customer'])
def delete(session,item_id:str):
    return remove_from_cart(item_id,session)

@rt('/cart/{item_id}')
@auth(['Seller', 'Customer'])
def patch(session,item_id:str,select:bool):
    return set_selected(item_id,select,session)

@rt('/category/{category}')
def get(category:str,session):
    return (layout(search_by_category_page(category),session))

@rt('/search/')
def get(keyword:str,session):
    return layout(search_page(keyword),session)

@rt('/item/{id}')
def get(session,id:str):
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
def get(session):
    return layout(product_management(session), session)

@rt('/seller/add')
def get(session):
    return layout(add_product_page(session),session)

@rt('/seller/add/submit', methods=["post"])
async def post(session ,product:Product ):
    return layout(submit_product_page(product,session), session)

@rt('/seller/add_bid')
def get(session):
    return layout(add_bid_product_page(session),session)

@rt('/seller/add_bid/submit',  methods=["post"])
def get(session , product : Bid_Product):
    return layout(submit_bid_product_page(product , session ),session)

@rt("/update_stock", methods=["post"])
async def post(session , add_stock : Stock_product):
    result = await update_stock(add_stock, session)
    return layout(result , session)

@rt("/edit_product", methods=["post"])
async def post(session , edit : Edit_product, ):
    result = await edit_product(edit , session)
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
    return layout(buy(session),session)

@rt('/ship/{id}')
def get(id:str,session):
    return check_status(id)

serve(port=int(os.getenv("PORT")))