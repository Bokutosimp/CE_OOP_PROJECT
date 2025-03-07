from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def sum_price(items_in_cart):
   return sum(round(item.get_item.get_price*item.get_amount_in_cart,3) for item in items_in_cart) 

def cart(session):
   user_id = session['auth'][0]
   items_in_cart = main_system.get_cart(user_id)
   if len(items_in_cart.get_list_item_in_cart) == 0:
      return Div('No Item in cart yet ',A('home',href='/'))
   delivery = 10
   return Div((
      H2('Shopping cart',style="color:black;"),
      Div(
         #Cart items
         Div(*[Div(Div(
            Div(style=f"width:100%; aspect-ratio:1/1; overflow:hidden; background-image:url({item.get_item.get_image}); background-size:contain; background-position:center; background-repeat:no-repeat;"),
            A(item.get_item.get_name,style="",href=f'/item/{item.get_item.get_id}'),
            Div(Label(f"Qty"),Input(type="number",value=item.get_amount_in_cart,min=1,id='amount',
               style="width:70px; background-color:white; color:black;",
               hx_post=f'/cart/{item.get_item.get_id}',hx_swap='innerHTML'),
            style="justify-self:end; display:flex; align-items:center; gap:10px;"),
            Div(f"US ${item.get_item.get_price}",style="justify-self:end;"),
            style="padding:10px; display:grid; gap:30px; grid-template-columns:1fr 3fr 1fr 2fr;"),
            Div(
               A("But it now",style="text-decoration:underline; cursor:pointer;",href=''),
               Span("|"),
               Span("Remove",style="text-decoration:underline; color:black;cursor:pointer;",
               hx_delete=f'/cart/{item.get_item.get_id}',hx_swap='outerHTML',hx_confirm='Are you sure?',),
               style="width:100%; display:flex; flex-direction:row; justify-content:end; gap:10px; padding:10px;"),
            style="border-bottom:1px solid gray;"
         ) for item in items_in_cart.get_list_item_in_cart],
         style="display:flex; flex-direction:column; gap:10px; border:1px solid gray; padding:10px; border-radius:15px;",),
         #Cart summary
         Div(Div(Span(f"Items ({len(items_in_cart.get_list_item_in_cart)})"),Span(f'US ${sum_price(items_in_cart.get_list_item_in_cart)}'),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; color:black;"),
             Div(
                Span('Shipping to ?'),
                Span(f'US ${delivery}'),
                style=f"{'display:none;' if delivery == 0 else 'display:flex;'}width:100%; display:flex; flex-direction:row; justify-content:space-between; border-bottom:1px solid black; color:black; padding-bottom:10px;"),
             Div(Span("Subtotal"),Span(f"US ${sum_price(items_in_cart.get_list_item_in_cart) + delivery}"),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; font-size:25px; color:black; "),
             Button("Go to checkout"),
             Span("Purchase protected by",A(" eBay Money Back Guarantee",href="#"),style="font-size:15px;"),
             style="background:rgb(232, 232, 232); border-radius:15px; padding:15px; display:flex; flex-direction:column; gap:15px; width:100%; max-height: 320px;"),
         style="width:100%; display:grid; grid-template-columns:2fr 1fr; gap:20px;"
         ),
      ),
      style="padding:20px; max-width:1024px; margin: 0 auto;"
   )
   
def add_to_cart(id:str,amount:str,session):
   try:
        result = main_system.add_to_cart(id,session['auth'][0],int(amount))
        if not result['success']: raise Exception(result['error'])
   except Exception as e:
        print(str(e))
        return Script(f'window.location.href = "/cart";alert("/item/{id}?error={str(e)}");')
   return Script(f'window.location.href = "/cart";alert("cart has been updated");')

def remove_from_cart(item_id:str,session):
   print(item_id)
   result = main_system.remove_from_cart(item_id,session['auth'][0])
   if not result['success']: return Script(f'alert("{result['error']}"); window.location.href = "/cart"')
   return Script(f'alert("item has been removed"); window.location.href = "/cart"')
   