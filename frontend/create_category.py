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
   main_system.create_category(uuid.uuid4(),category_name,category_description)
   return Div(
    P(f"Category '{main_system.get_categories()[-1].get_name}' with the description '{main_system.get_categories()[-1].get_description}' has been successfully created.",
      style="font-size: 18px; font-weight: 600; color: #2c3e50; margin-bottom: 20px; text-align: center;"),
    Div(
        A('Back to Admin Panel', href='/admin', style='color: #3498db; text-decoration: underline; font-size: 16px; margin-right: 20px; font-weight: 500;'),
        A('Back to Home Page', href='/', style='color: #3498db; text-decoration: underline; font-size: 16px; font-weight: 500;'),
        style='display: flex; justify-content: center; gap: 20px; margin-top: 20px;'
    ),
    style='padding: 30px; background-color: #ecf0f1; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); width: 80%; margin: 0 auto; text-align: center;'
   )