from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def admin_page():
   list_categories = main_system.get_categories()
   return Div(H2('admin panel',style='color:black;'),
              H3('category list'),
              Div(*[A(cat.get_name,style='border-bottom: solid gray 1px; margin-bottom:5px; display:block;',href=f'/category/{cat.get_id}') for cat in list_categories],style='text-align:center; color: black; width:300px;'),
              A('add category',href='/admin/create_category',style='text-decoration:underline;'),style='display:flex; align-items:center; flex-direction:column; padding:20px; margin:40px; background-color:#CAD5CA; border-radius:20px;')