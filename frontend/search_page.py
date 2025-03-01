from fasthtml.common import *
from mock.items import items

def search_page(keyword):
   
   filtered_items = [item for item in items if keyword in item["name"].lower()]
   if filtered_items:
      return Div(
         H4(f"result for {keyword}"),
         Div(*[A(
               Div(Img(src=item["image"],style="width:256px; height:auto; object-fit:contain;"),style="display:grid; place-items:center; width:256px; height: 256px; background:rgb(200, 200, 200); border-radius:15px;"),
               Div(
                  Div(item["name"],style="font-size:20px;"),
                  Div('New-Open box',style="font-size:15px; color:gray;"),
                  Div(
                     Div(f"US ${item["price"]}",style="font-weight:bold; font-size:25px; width:50%;"),
                     Div("Save up to 15% when you buy more ginosurplus713 (282) 100%",style="justify-self:end; font-size:15px; width:50%;"),
                     style="display:flex; flex-direction:row; width:100%; margin-top:20px;"),
                  style="display:flex; flex-direction:column; width:100%; margin:10px 20px;"),
               style="display:flex; flex-direction:row; gap:20px; text-decoration:none; color:black; width:100%; background:rgb(232, 232, 232); border-radius:15px; padding:0; overflow:hidden;",
               href=f"/item/{item['id']}"               
            ) 
            for item in filtered_items],
             style="display:flex; flex-direction:column; gap:10px; width:100%;",
             ),
         style="padding:20px; max-width:1024px; margin: 0 auto;")
   else:
      return Div('not found')   