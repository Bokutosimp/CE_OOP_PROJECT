from fasthtml.common import *

mock_item = [{
   'id': 1,
      'name': 'Item1',
      'price': 100,
      'quantity': 1,
      'amount':1,
      'image':'data:image/png;base64,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'
      },
      {
      'id': 2,
      'name': 'Item2',     
      'price': 200,
      'quantity': 1,
      'amount':1,
      'image':"https://cdn.pixabay.com/photo/2016/07/07/16/46/dice-1502706_640.jpg"
      }
]

def cart():
   sum_price = sum(item['price'] for item in mock_item)
   delivery = 10
   total = sum_price + delivery
   return Div((
      H2('Shopping cart',style="color:black;"),
      Div(
         #Cart items
         Div(*[Div(Div(
            Div(style=f"width:100%; aspect-ratio:1/1; overflow:hidden; background-image:url({item['image']}); background-size:contain; background-position:center; background-repeat:no-repeat;"),
            A(item["name"],style="",href=f'/item/{item['id']}'),
            Div(Label(f"Qty"),Input(type="number",value=item['quantity'],style="width:70px; background-color:white; color:black;"),style="justify-self:end; display:flex; align-items:center; gap:10px;"),
            Div(f"US ${item['price']}",style="justify-self:end;"),
            style="padding:10px; display:grid; gap:30px; grid-template-columns:1fr 3fr 1fr 2fr;"),
            Div(A("But it now",style="text-decoration:underline"),Span("|"),A("Remove",style="text-decoration:underline;"),style="width:100%; display:flex; flex-direction:row; justify-content:end; gap:10px; padding:10px;"),
            style="border-bottom:1px solid gray;"
         ) for item in mock_item],
         style="display:flex; flex-direction:column; gap:10px; border:1px solid gray; padding:10px; border-radius:15px;"),
         #Cart summary
         Div(Div(Span(f"Items ({len(mock_item)})"),Span(f'US ${sum_price}'),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; color:black;"),
             Div(
                Span('Shipping to ?'),
                Span(f'US ${delivery}'),
                style=f"{'display:none;' if delivery == 0 else 'display:flex;'}width:100%; display:flex; flex-direction:row; justify-content:space-between; border-bottom:1px solid black; color:black; padding-bottom:10px;"),
             Div(Span("Subtotal"),Span(f"US ${total}"),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; font-size:25px; color:black; "),
             Button("Go to checkout"),
             Span("Purchase protected by",A(" eBay Money Back Guarantee",href="#"),style="font-size:15px;"),
             style="background:rgb(232, 232, 232); border-radius:15px; padding:15px; display:flex; flex-direction:column; gap:15px; width:100%;"),
         style="width:100%; display:grid; grid-template-columns:2fr 1fr; gap:20px;"
         ),
      ),
      style="padding:20px; max-width:1024px; margin: 0 auto;"
   )