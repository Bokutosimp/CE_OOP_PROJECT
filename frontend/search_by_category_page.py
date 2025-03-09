from fasthtml.common import *
# from mock.items import items
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def search_by_category_page(category):
   filtered_items = main_system.get_items_by_category(category)
   print(filtered_items)
   if filtered_items:
      return Div(
         H2(main_system.get_category_by_id(category).get_name,style="color:black;"),
         Div(*[A(Div(
               Img(src=item.get_image,style="width:200px; height:auto; object-fit:contain;",alt='item image'),
               style="display:grid; place-items:center; width:200px; height: 200px; background:rgb(200, 200, 200); border-radius:15px;",
            ),Div(
               Div(item.get_name,style="font-size:20px; font-weight:400;"),
               Div('⭐⭐⭐⭐⭐ (24)',style="color:gray;"),
               Div(f'US ${item.get_price}',style="font-size:20px;"),
               style="padding:10px;"
            ),
            style="",
            href=f"{'/item/'+str(item.get_id) if item.__class__.__name__ == 'Item' else '/bid/'+str(item.get_id)}",
            ) 
            for item in filtered_items],
             style="display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:20px; width:100%;",),
         style="padding:20px; max-width:1024px; margin: 0 auto;"
      )
   else:
      return Div('not found')