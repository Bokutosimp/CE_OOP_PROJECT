from fasthtml.common import *
from mock.items import items
from mock.order import mock_orders

def order_history_page():
    
    history_cards = []
    
    for order in mock_orders: 
        if not order:
            continue  
        
        history_cards.append(
           Grid(
        *[
            Div(
                Div(
                    Img(
                        src=order["image_url"],
                        style="width: 120px; height: 120px; object-fit: cover; border-radius: 8px; border: 1px solid #ddd;"
                    ),
                    Div(
                        H4(order["product_name"], style="font-size: 18px; font-weight: bold; color: #333;"),
                        P(f"Amount {order['quantity']}", style="font-size: 16px; color: #666;"),
                        P(f"total Price: ${order['total_price']}", style="font-size: 16px; color: #666;"),
                        style="display: flex; flex-direction: column; gap: 5px; padding: 10px;"
                    ),
                    style="display: flex; align-items: center; gap: 15px;"
                ),
                style="display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);"
            )
        ],
        style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: #f7f7f7;"
    )

        )
    
    if not history_cards:
        return Div("No purchase history available.")
    
    return Div( H1("Order History", style="text-align: center; margin-bottom: 20px; color: #222;"),  
               *history_cards,
                style="display:flex; flex-direction:column; gap:30px; padding:20px; background:#f7f7f7;")
