from fasthtml.common import *
from mock.items import items

def search_by_category_page(category):
   filtered_items = [item for item in items if category.lower() in [cat.lower() for cat in item["category"]]]
   if filtered_items:
      return Div(
         H2(category,style="color:black;"),
         Div(*[A(Div(
               Img(src=item["image"],style="width:200px; height:auto; object-fit:contain;"),
               style="display:grid; place-items:center; width:200px; height: 200px; background:rgb(200, 200, 200); border-radius:15px;",
            ),Div(
               Div(item["name"],style="font-size:20px; font-weight:400;"),
               Div('⭐⭐⭐⭐⭐ (24)',style="color:gray;"),
               Div(f'US ${item["price"]}',style="font-size:20px;"),
               style="padding:10px;"
            ),
            style="",
            href=f"/item/{item['id']}"
            ) 
            for item in filtered_items],
             style="display:grid; grid-template-columns:repeat(auto-fill, minmax(200px, 1fr)); gap:20px; width:100%;",),
         style="padding:20px; max-width:1024px; margin: 0 auto;"
      )
   else:
      return Div('not found')