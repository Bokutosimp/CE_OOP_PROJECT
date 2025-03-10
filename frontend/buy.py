from fasthtml.common import *
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def buy(session):
    user_id = session['auth'][0]
    if main_system.buy_cart_check_stock(user_id) <= 0:
        return Script("alert('please select atleast one item'); window.location.href='/cart'")
    user = main_system.get_user_by_id(user_id)
    if not user :
        return Body(H4("User not found", style="color: red;"))
    
    total_amount = sum((round(item.get_item.get_price*item.get_amount_in_cart,3) if item.get_is_selected else 0 ) for item in user.get_cart.get_list_item_in_cart)
    shipping_amount = 10
    grand_total = total_amount + shipping_amount

    return Body(
    Card(
        H4(Label("Buy with E-bux only for now!", style="color: #ffffff; text-align: left;"), 
            style="background-color: #6a5acd; padding: 20px; border-radius: 10px; height: 20%;"),
        style="background-color: #eae4f1ff; margin: 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"
    ),
    
    Div(
        Div(
            H2("Pay with", style="color: #333333; font-size: 24px; font-weight: bold;"),
            Div(
                Label(Input(type="radio", name="payment", value="E-bux"), "E-bux", style="color: #333; margin-right: 15px;"),
                Label(Input(type="radio", name="payment", value="NULL"), "NULL", style="color: #333; margin-right: 15px;"),
                Label(Input(type="radio", name="payment", value="null"), "null", style="color: #333;"),
                style="text-align: left; margin-bottom: 20px;",
            ),
            style="background-color: #ffffff; flex: 1; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"
        ),

        Card(
            Div(
                H2("Order Summary", style="color: #333333; font-size: 22px;"),
                Label(f"Total: {total_amount} E", style="color: #333333; font-size: 18px;"),
                Label(f"Shipping: {shipping_amount} E", style="color: #333333; font-size: 18px;"),
                Label(B(f"Grand Total: {grand_total} E"), style="color: #333333; font-size: 20px; font-weight: bold;"),
                style="text-align: left;",
            ),
            Div(style="border-bottom: 2px solid #333333; width: 100%; margin-top: 10px;"),
            Div(
                Button(
                        "Confirm Purchases", 
                        type="button", 
                        onclick="""fetch('/purchase',{method:"POST",body:'bla'}).then(data => {alert('buy successfull'); window.location.href='/cart'})""", 
                        style="""background-color: #6fc276; color: white; padding: 12px 25px; border: none; border-radius: 25px; cursor: pointer; 
                                width: auto; margin: 10px; font-size: 16px; transition: all 0.3s;""",
                        onmouseover="this.style.backgroundColor='#5ba563'; this.style.transform='scale(1.05)';",
                        onmouseout="this.style.backgroundColor='#6fc276'; this.style.transform='scale(1)';"
                    )
                    ,
                Button(
                        "Buy with Code", 
                        type="button", 
                        onclick="""openDialog()""", 
                        style="""background-color: #ff872b; color: white; padding: 12px 25px; border: none; border-radius: 25px; cursor: pointer; 
                                width: auto; font-size: 16px; transition: all 0.3s;""",
                        onmouseover="this.style.backgroundColor='#e37622'; this.style.transform='scale(1.05)';",
                        onmouseout="this.style.backgroundColor='#ff872b'; this.style.transform='scale(1)';"
                    ),

            ),
            style="background-color: #ffffff; flex: 1; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-top: 30px;",
        ),
        style="display: flex; justify-content: space-between; gap: 30px; background-color: #eae4f1ff; min-height: 100vh; padding: 40px;",
    ),

    Div(
        Div(
            H2("Enter Code or Coupon", style="color: #333333; font-size: 24px; font-weight: bold;"),
            Form(
                Input(type="text", id="coupon", placeholder="Enter code or coupon here!", 
                      style="padding: 15px; border-radius: 10px; border: 1px solid #ccc; width: 100%; font-size: 16px; margin-bottom: 20px;"),
                Div(
                    Button("Submit", type="submit", 
                           style="background-color: #28a745; color: white; padding: 12px 25px; border: none; border-radius: 25px; cursor: pointer; width: 100%; font-size: 18px;"),
                    Button("Cancel", type="button", onclick="closeDialog()", 
                           style="background-color: #C30F16; color: white; padding: 12px 25px; border: none; border-radius: 25px; cursor: pointer; width: 100%; font-size: 18px; margin-top: 10px;"),
                    style="display: flex; gap: 15px; margin-top: 20px;",
                ),
                method="post",
                action="/purchase"
            ),
            style="background-color: #ffffff; padding: 30px; border-radius: 12px; width: 600px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);",
        ),
        id="dialog",
        style="display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: rgba(0, 0, 0, 0.5); width: 100%; height: 100%; justify-content: center; align-items: center;",
    ),

    Script(
        """
        function openDialog() {
            const selectedPayment = document.querySelector('input[name="payment"]:checked');
            if (selectedPayment && selectedPayment.value === 'E-bux') {
                document.getElementById('dialog').style.display = 'flex';
            } else {
                alert('Please select E-bux as the payment method to proceed.');
            }
        }
        function closeDialog() {
            document.getElementById('dialog').style.display = 'none';
        }
        """
    ),
    
    style="background-color: #eaf4f4ff; min-height: 100vh; margin: 0;",
)

def buy_post(session,code_name:str):
    try:
        user_id = session['auth'][0]
        if main_system.buy_cart_check_stock(user_id) == 0:
            return Script("alert('please select atleast one item'); window.location.href='/cart'")
        main_system.buy_item_in_cart(user_id,code_name)
        user = main_system.get_user_by_id(user_id)
        print("#### printing user history #####")
        for history in user.get_order_history:
            print(history.get_order)
        return Script("alert('buy successfull'); window.location.href='/cart'")
    except (Exception,ValueError,KeyError) as e:
        return Script(f"alert('{str(e)}'); window.location.href='/purchase'")