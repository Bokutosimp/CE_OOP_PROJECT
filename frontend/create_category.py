from fasthtml.common import *
import os,sys
import uuid
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def create_category():
   return Div(Form(
      H2('Admin Panel',style='color:black;'),
      Input(name='category_name',id='name',placeholder='Category Name',required='true'),
      Textarea(name='category_description',id='description',placeholder='Category Description',required='true'),
      Button('Create Category',type='submit'),
      method='POST',
      action='/admin/create_category',
      style='margin: 0 auto; width: 1024px; padding:20px; border-radius:15px; background-color: #f0f0f0;'
   ),style='padding-top:50px;')
   
def post_create_category(category_name:str,category_description:str):
   if category_name == '' or category_description == '':
      return Script(
         "alert('Category name and description cannot be empty'); window.location.href = '/admin/create_category';"
      )
   main_system.create_category(uuid.uuid4,category_name,category_description)
   return Div(
      P(f"category name is {main_system.get_categories()[-1].get_name} and detail is {main_system.get_categories()[-1].get_description} has been created"),
      A('Back to Admin Panel',href='/admin',style='color:blue;'),
      A('Back to home page',href='/',style='color:blue;'),
   )