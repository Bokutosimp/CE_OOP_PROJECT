from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def admin_page():
    list_categories = main_system.get_categories()
    return Div(
        H2('Admin Panel', style='color: #2c3e50; font-size: 32px; font-weight: 700; margin-bottom: 20px;'),
        H3('Category List', style='color: #34495e; font-size: 24px; font-weight: 600; margin-bottom: 20px;'),
        Div(
            *[
                Div(
               Span(cat.get_name, style='font-size: 18px; font-weight: 500; color: #34495e;'),
                    A(
                        Button('View', style='background-color: #f39c12; color: white; border: none; border-radius: 8px; padding: 8px 20px; cursor: pointer; transition: background-color 0.3s;'),
                        href=f'/category/{cat.get_id}', style='text-decoration: none;'
                    ),
                    style='border: solid 1px #bdc3c7; margin: 10px; display: flex; justify-content: space-between; align-items: center; padding: 10px; background-color: #ecf0f1; border-radius: 8px; transition: background-color 0.3s; width: 230px;',
                ) for cat in list_categories
            ],
            style='display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; margin-bottom: 20px;',
        ),
        A(
            Button('Add Category', style='background-color: #27ae60; color: white; padding: 12px 24px; border: none; border-radius: 8px; cursor: pointer; font-size: 16px; transition: background-color 0.3s; text-decoration: none; margin-top: 20px;'),
            href='/admin/create_category',
            style='text-align: center; display: block;'
        ),
        style='display: flex; flex-direction: column; align-items: center; padding: 30px; background-color: #f5f5f5; border-radius: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);'
    )
