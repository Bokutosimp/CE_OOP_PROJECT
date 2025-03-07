from fasthtml.common import *
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system
from mock.users import *

def buy(session):
    user_id = session['auth'][0]
    user = main_system.get_user_by_id(user_id)
    if not user :
        return Body(H4("User not found", style="color: red;"))
    
    total_amount = sum((item.get_item.get_price * item.get_amount_in_cart for item in user.get_cart.get_list_item_in_cart))
    shipping_amount = 10
    grand_total = total_amount + shipping_amount

    return Body(
        Card(
            H4(Label("Buy with E-bux only for now!", style="color: #000000; text-align: left;"), style="background-color: #B5E2FF; padding: 20px; border-radius: 5px; height: 20%;"),
            style="background-color: #EEEEEE; margin: 0;",
        ),
        
        Div(
            Div(
                H2("Pay with", style="color: #000000;"),
                Div(
                    Label(Input(type="radio", name="payment", value="E-bux"), "E-bux", style="color: #000000;"),
                    Label(Input(type="radio", name="payment", value="NULL"), "NULL", style="color: #000000;"),
                    Label(Input(type="radio", name="payment", value="null"), "null", style="color: #000000;"),
                    style="text-align: left; margin-bottom: 20px;",
                ),
                style="background-color: #EEEEEE; flex: 1; padding: 10px; height: 30%;",
            ),
            
            Card(
                Div(
                    H2("Order Summary", style="color: #000000;"),
                    Label(f"Total: {total_amount} E", style="color: #000000;"),
                    Label(f"Shipping: {shipping_amount} E", style="color: #000000;"),
                    Label(B(f"Grand Total: {grand_total} E"), style="color: #000000;"),
                    style="text-align: left;",
                ),
                Div(style="border-bottom: 2px solid #000000; width: 100%; margin-top: 10px;"),
                Div(
                    Button("confirm purchases", type="button", onclick="openDialog()", style="background-color: #6fc276; color: white; padding: 10px 15px; border: none; border-radius: 20px; cursor: pointer; width: auto;"),
                    style="text-align: middle; margin-top: 10px;",
                ),
                style="background-color: #dddddd; flex: 1; padding: 10px; height: 30%; margin-top: 27px; weight: 50%;",
            ),
            style="display: flex; justify-content: space-between; gap: 20px; background-color: #EEEEEE; min-height: 100vh; padding: 20px;",
        ),
        
        # Dialog Element
        Div(
            Div(
                H2("Enter code or coupon", style="color: #000000;"),
                Form(
                    Input(type="text", id="coupon", placeholder="Enter code or coupon here!", style="padding: 10px; border-radius: 5px; border: 1px solid #000000;"),
                    Div(
                        Button("Submit", type="submit", style="background-color: #28a745; color: white; padding: 10px 15px; border: none; border-radius: 20px; cursor: pointer; width: auto;"),
                        Button("Close", type="button", onclick="closeDialog()", style="background-color: #C30F16; color: white; padding: 10px 15px; border: none; border-radius: 20px; cursor: pointer; width: auto;"),
                        style="display: flex; gap: 10px; margin-top: 10px;",  # Ensure buttons are on the same line
                    ),
                    method="post",
                    action="/submit"
                ),
                style="background-color: #FFFFFF; padding: 20px; border-radius: 10px; width: 600px; text-align: center;",
            ),
            id="dialog",
            style="display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: rgba(0, 0, 0, 0.5); width: 100%; height: 100%; justify-content: center; align-items: center;",
        ),
        
        # JavaScript for Dialog
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
        
        style="background-color: #EEEEEE; min-height: 100vh; margin: 0;",
    )