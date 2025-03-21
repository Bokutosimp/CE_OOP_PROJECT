from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def sum_price(items_in_cart):
   return sum((round(item.get_item.get_price*item.get_amount_in_cart,3) if item.get_is_selected else 0 ) for item in items_in_cart) 

def generate_cart_summary(items_in_cart):
    delivery = 10
    return (Div(Span(f"Items ({len([item for item in items_in_cart.get_list_item_in_cart if item.get_is_selected])})"),Span(f'US ${sum_price(items_in_cart.get_list_item_in_cart)}'),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; color:black;"),
             Div(
                Span('Shipping to ?'),
                Span(f'US ${delivery}'),
                style=f"{'display:none;' if delivery == 0 else 'display:flex;'}width:100%; display:flex; flex-direction:row; justify-content:space-between; border-bottom:1px solid black; color:black; padding-bottom:10px;"),
             Div(Span("Subtotal"),Span(f"US ${sum_price(items_in_cart.get_list_item_in_cart) + delivery}"),style="width:100%; display:flex; flex-direction:row; justify-content:space-between; font-size:25px; color:black; "),
             A(Button("Go to checkout", 
                      style="""
                    background-color: #3498DB; color: white; padding: 12px 20px; border-radius: 25px; 
                    font-size: 16px; cursor: pointer; transition: all 0.3s; width: 100%;
                """,
                onmouseover="this.style.backgroundColor='#1E88E5'; this.style.transform='scale(1.05)';",
                onmouseout="this.style.backgroundColor='#3498DB'; this.style.transform='scale(1)';") 
                ,href='/purchase'),
             Span("Purchase protected by",A(" eBay Money Back Guarantee",href="#"),style="font-size:15px;"),)


def cart(session):
   try:
      user_id = session['auth'][0]
      items_in_cart = main_system.get_cart(user_id)
      if len(items_in_cart.get_list_item_in_cart) == 0:
         return Div('No Item in cart yet ',A('home',href='/'))
      delivery = 10
      return Div(
    H2('Shopping Cart', style="color:#3498DB; font-weight: bold; text-align: center;"),
    
    Div(
        # รายการสินค้าในตะกร้า
        Div(
            *[
                Div(
                    Div(
                        Div(style=f"width:100%; aspect-ratio:1/1; overflow:hidden; background-image:url({item.get_item.get_image}); background-size:contain; background-position:center; background-repeat:no-repeat;"),
                        A(item.get_item.get_name, href=f'/item/{item.get_item.get_id}', style="color:#1C1C1C; font-weight: bold; text-decoration: none;"),
                        Div(
                            Label("Qty"),
                            Input(type="number", value=item.get_amount_in_cart, min=1, id='amount',
                                  cls=f'amount-{item.get_item.get_id}',
                                  style="width:70px; background-color:white; color:#1C1C1C; border: 1px solid #3498DB; border-radius: 5px; padding: 5px;",
                                  hx_post=f'/cart/{item.get_item.get_id}', hx_swap='innerHTML', hx_vals=''
                            ),
                            style="justify-self:end; display:flex; align-items:center; gap:10px;"
                        ),
                        Div(f"US ${item.get_item.get_price}", style="justify-self:end; color:#1C1C1C; font-weight:bold;"),
                        style="padding:10px; display:grid; gap:30px; grid-template-columns:1fr 3fr 1fr 2fr;"
                    ),
                    Div(
                        Input(
                            type='checkbox', id='select', name='id',
                            onchange=f"""
                                fetch('/cart/{item.get_item.get_id}', {{
                                    method: 'PATCH', 
                                    headers: {{'Content-Type': 'application/x-www-form-urlencoded'}}, 
                                    body: 'select='+this.checked
                                }}).then(response => response.text()).then(data => document.getElementById('cart-summary').innerHTML = data);
                            """,
                            checked='true' if item.get_is_selected else '',
                            style='margin:0; justify-self:center; align-self:center; cursor:pointer;'
                        ),
                        Span("|"),
                        A("Buy it now", style="text-decoration:underline; cursor:pointer; color:#3498DB;",
                            onclick=f"""
                                const input = document.querySelector(".amount-{item.get_item.get_id}");
                                window.location.href=`/purchase/{item.get_item.get_id}/${{input.value}}`;
                            """
                        ),
                        Span("|"),
                        Span("Remove", style="text-decoration:underline; color:red; cursor:pointer;",
                             hx_delete=f'/cart/{item.get_item.get_id}', hx_swap='outerHTML', hx_confirm='Are you sure?'
                        ),
                        style="width:100%; display:flex; flex-direction:row; justify-content:end; gap:10px; padding:10px;"
                    ),
                    style="border-bottom:1px solid #85C1E9;"
                )
                for item in items_in_cart.get_list_item_in_cart
            ],
            style="display:flex; flex-direction:column; gap:10px; border:1px solid #3498DB; padding:10px; border-radius:15px;"
        ),
        
        # Cart Summary
        Div(
            Div(
                Span(f"Items ({len([item for item in items_in_cart.get_list_item_in_cart if item.get_is_selected])})"),
                Span(f'US ${sum_price(items_in_cart.get_list_item_in_cart)}'),
                style="width:100%; display:flex; flex-direction:row; justify-content:space-between; color:#1C1C1C;"
            ),
            Div(
                Span("Shipping to ?"),
                Span(f'US ${delivery}'),
                style=f"{'display:none;' if delivery == 0 else 'display:flex;'} width:100%; display:flex; flex-direction:row; justify-content:space-between; border-bottom:1px solid #85C1E9; color:#1C1C1C; padding-bottom:10px;"
            ),
            Div(
                Span("Subtotal"),
                Span(f"US ${sum_price(items_in_cart.get_list_item_in_cart) + delivery}"),
                style="width:100%; display:flex; flex-direction:row; justify-content:space-between; font-size:25px; color:#1C1C1C;"
            ),
            A(
                Button("Go to Checkout", style="""
                    background-color: #3498DB; color: white; padding: 12px 20px; border-radius: 25px; 
                    font-size: 16px; cursor: pointer; transition: all 0.3s; width: 100%;
                """,
                onmouseover="this.style.backgroundColor='#1E88E5'; this.style.transform='scale(1.05)';",
                onmouseout="this.style.backgroundColor='#3498DB'; this.style.transform='scale(1)';"
                ),
                href='/purchase'
            ),
            Span("Purchase protected by", A(" eBay Money Back Guarantee", href="#", style="font-size:15px; color:#3498DB;")),
            style="background:#D6EAF8; border-radius:15px; padding:15px; display:flex; flex-direction:column; gap:15px; width:100%; max-height: 320px;", 
            id='cart-summary'
        ),
        style="width:100%; display:grid; grid-template-columns:2fr 1fr; gap:20px;"
    ),
    
    style="padding:20px; max-width:1024px; margin: 0 auto;"
)

   except Exception as e:
      return Script(f"""alert("{str(e)}"); window.location.href='/'""")
   
def add_to_cart(id:str,amount:str,session):
   try:
      result = main_system.add_to_cart(id,session['auth'][0],int(amount))
      if not result['success']: raise Exception(result['error'])
      return Script(f'window.location.href = "/cart";alert("cart has been updated");')
   except Exception as e:
      return Script(f'window.location.href = "/cart";alert("/item/{id}?error={str(e)}");')

def remove_from_cart(item_id:str,session):
   try:
      result = main_system.remove_from_cart(item_id,session['auth'][0])
      return Script(f'alert("item has been removed"); window.location.href = "/cart"')
   except (Exception,ValueError, KeyError) as e:
      return Script(f'alert("{str(e)}"); window.location.href = "/cart"')

def set_selected(item_id:str, select, session):
   try:
      result = main_system.set_select_item(item_id, session['auth'][0], select)
      # Recalculate the cart summary
      items_in_cart = main_system.get_cart(session['auth'][0])
      summary_html = generate_cart_summary(items_in_cart)
      return summary_html
   except (Exception,ValueError, KeyError) as e:
      return Script(f'alert("{str(e)}"); window.location.href = "/cart"')