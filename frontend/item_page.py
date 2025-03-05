from fasthtml.common import *
from mock.items import items

def item_page(id):
   try:
      item = [items[i] for i in range(len(items)) if items[i]['id'] == int(id)][0]
      return Div(
            Div(Img(src=item['image']),style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Div(
               Div(H2(item['name'],style="color:black; font-weight:600;"),style="width:100%; border-bottom:1px solid gray; margin-bottom:20px;"),
               Div(style="height:40px; width:100%; border-bottom:1px solid gray;"),
               Div(P(f"US ${item['price']}/ea",style="color:black; font-size:30px; font-weight:bold;"),style="width:100%;"),
               Div(
                  Span('Quantity:',style="color:black; font-size:15px;"),
                  Input(type='number',value=1,min=1,max=item['amount'],style="width:70px; margin:0;"),
                   style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center;"),
               Button('But It Now',style="width:100%; border-radius:50px;"),
               Button('Add to Cart',style="width:100%;border-radius:50px;"),
               style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;"
               ),
            Style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;",)
   except:
      return Div("Item not found")