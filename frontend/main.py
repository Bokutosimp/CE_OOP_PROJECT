from fasthtml.common import *
import os
import dotenv

#import page
from layout import layout
from cart import *
from main_page import *
from stylesheet import stylesheet
from seller import *
from add_product import *
from add_bid_product import *
from add_discount import *
from item_page import item_page
from bid_page import *
from review_page import *
from search_page import search_page
from search_by_category_page import search_by_category_page
from create_category import *
from history_item import *
from buy import buy,buy_post,buy_one_item
from login import *
from register import *
from decorators.auth import auth
from decorators.redirect_path import redirect_path
from admin import admin_page
from shipping_status import check_status
from edit_item import edit_item,edit_bid_item
from profile_page import profile_page
from bid_history_page import *

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
def get(session,keyword:str=''):
    return layout(search_page(keyword),session)

@rt('/item/{id}')
def get(session,id:str):
    return (layout(item_page(id),session))
    
@rt('/bid/{id}')
def get(id:str,session):
    return (layout(bid_page(id, session),session))

@rt('/bid/submit',methods=["post"])
def post(bid_input:float,item_id:str,session):
    return submit_bid_page(bid_input,item_id,session)

@rt('/bid_status/{item_id}')
def get(item_id: str):
    try:
        bid_item = main_system.get_bid_item_by_id(item_id)
        return bid_item.get_status  # Returns "Not Started", "Started", "Ended", or "Sold"
    except Exception:
        return "Error"

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

@rt('/edit_item/{item_id}')
def get(session,item_id:str):
    return edit_item(session,item_id)

@rt('/edit_bid_item/{item_id}')
def get(session,item_id:str):
    return edit_bid_item(session,item_id)

@rt('/seller/add/submit', methods=["post"])
async def post(session ,product:Product ):
    return submit_product_page(product,session)

@rt('/seller/discount_code')
async def get(session):
    return layout(add_discount_page(session),session)

@rt('/seller/discount_code/submit', methods=["post"])
async def post(session , discount_code : Discount_code ):
    return submit_discount_page(discount_code ,session)

@rt('/seller/add_bid')
def get(session):
    return layout(add_bid_product_page(session),session)

@rt('/seller/add_bid/submit',  methods=["post"])
def get(session , product : Bid_Product):
    return layout(submit_bid_product_page(product , session ),session)

@rt("/update_bid_stock", methods=["post"])
def post(session , add_bid_stock : Stock_bid_product):
    result =  update_bid_stock(add_bid_stock, session)
    return layout(result , session)

@rt("/update_stock", methods=["post"])
def post(session , add_stock : Stock_product):
    result =  update_stock(add_stock, session)
    return layout(result , session)

@rt("/edit_product", methods=["patch"])
def patch(session ,edit_item_id:str,new_name:str, new_price:float ,new_category:str,new_detail:str,new_image:str):
    print(f"item {edit_item_id},new name = {new_name}")
    return edit_product(session,edit_item_id,new_name,new_price,new_category,new_detail,new_image)

@rt("/edit_bid_product", methods=["patch"])
def patch(session ,edit_bid_item_id:str,new_name:str,new_start_price:float,new_category:str,new_detail:str,new_image:str , new_start_time : str , new_end_time : str):
    print(f"bid item {edit_bid_item_id},new name = {new_name}")
    return edit_bid_product(session,edit_bid_item_id,new_name,new_start_price,new_category,new_detail,new_image , new_start_time , new_end_time)



@rt('/admin/create_category')
@auth(['Admin'])
def get(session):
    return create_category()

@rt('/admin/create_category')
@auth(['Admin'])
def post(session,category_name:str,category_description:str):
    return post_create_category(category_name,category_description,session)

@rt('/admin')
@auth(['Admin'])
def get(session):
    return layout(admin_page(),session)

@rt('/history')
def get(session):
    return layout(order_history_page(session),session)

@rt('/bid_history')
def get(session):
    return layout(bid_history_page(session),session)

@rt('/purchase')
def get(session):
    return layout(buy(session),session)

@rt('/purchase/{item_id}/{amount}')
def get(session,item_id:str,amount:str):
    return layout(buy(session,item_id,amount),session)

@rt('/purchase')
def post(session,coupon:str=''):
    return buy_post(session,coupon)

@rt('/purchase/{item_id}/{amount}')
def post(session,item_id:str,amount:str,coupon:str=''):
    return buy_one_item(session,item_id,amount,coupon)

@rt('/ship/{id}')
def get(id:str,session):
    return check_status(id)

@rt('/profile')
def get(session):
    return layout(profile_page(session),session)

serve(port=int(os.getenv("PORT")))