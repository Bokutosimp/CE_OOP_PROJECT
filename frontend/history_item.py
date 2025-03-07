from fasthtml.common import *
from mock.items import items
from backend.mock.users import users
from backend.system import *

def order_history_page(request: Request):
    history_cards = []
    user_id = request.query_params.get('user_id', 'no data')
    user_order_history = main_system.get_user_by_id(user_id)
    
    for order in user_order_history.get_order_history:
        history_cards.append(
            Grid(
                *[
                    Div(
                        Div(
                            Img(
                                src='https://cdn.pixabay.com/photo/2016/07/07/16/46/dice-1502706_640.jpg',
                                style="width: 120px; height: 120px; object-fit: cover; border-radius: 8px; border: 1px solid #ddd;",
                            ),
                            Div(
                                A(order['order_id'], style="font-size: 18px; font-weight: bold; color: #333;", 
                                  onclick="document.getElementById('popup').style.display='flex'; document.getElementById('order_id').innerText = '{}';".format(order['order_id'])),
                                P(f"Total Price: $ {order['total_price']}", style="font-size: 16px; color: #666;"),
                                 P(f"Total Price: $ {order['items']}", style="font-size: 16px; color: #666;"),
                                P(f"Status: {order['status']}", style="font-size: 16px; color: #666;"),
                                P(f"Order Date: {order['order_date']}", style="font-size: 16px; color: #666;"),
                                style="display: flex; flex-direction: column; gap: 5px; padding: 10px;"
                            ),
                            style="display: flex; align-items: center; gap: 15px;"
                        ),
                        style="display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);"
                    ),
                ],
                style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: #f7f7f7;"
            ),
        )

    if not history_cards:
        return Div("No purchase history available.", style="display: flex; flex-direction: column; gap: 30px; padding: 20px; background: #f7f7f7;")

    return Div(
        H1("Order History", style="text-align: center; margin-bottom: 20px; color: #222;"),
        *history_cards,
        Div(
            Div(
                Label(H3('')),
                Label(Input(type="number", id="amount", placeholder="Amount", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                Button("Submit", onclick="document.getElementById('popup').style.display='none'; document.getElementById('amount').value = '';",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);"
            ),
            id="popup",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
        Div(
            Script(
                '''
                function closePopup() {
                    document.getElementById('popup').style.display = 'none';
                }
                '''
            ),
            style="display: none;"
        ),
        style="display: flex; flex-direction: column; gap: 30px; padding: 20px; background: #f7f7f7;"
    )
