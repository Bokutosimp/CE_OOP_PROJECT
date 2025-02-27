from fasthtml.common import *

mock_item = [{
   'id': 1,
      'name': 'Item1',
      'price': 100,
      'quantity': 1,
      'amount':1,
      },
      {
         'id': 2,
      'name': 'Item2',     
      'price': 200,
      'quantity': 1,
      'amount':1
      }
]

def cart():
   return Div((
      H2('Shopping cart',style="color:black;"),
      Div(
         Div(*[Div(
            Div(style="border:2px solid black; width:100%; aspect-ratio:1/1;"),
            A(item["name"],style="",href=f'/item/{item['id']}'),
            Div(f"qty {item["amount"]}"),
            Div(f"US ${item['price']}",style="justify-self:end;"),
            style="border:1px solid black; border-radius:15px; padding:10px; display:grid; gap:30px; grid-template-columns:1fr 3fr 1fr 2fr;"
         ) for item in mock_item],
         style="display:flex; flex-direction:column; gap:10px; width:70%;")
         ),
      ),
      style="padding:20px;"
   )