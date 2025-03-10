from fasthtml.common import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def generate_order_card(order):
    return Div(
        Span(f'get item date {order.get_shipping_status.get_shipping_date.strftime("%y-%m-%d")}',style='color: #666;'),
        P(f"Total Price: ${order.get_order.get_total_price}", style="font-size: 16px; color: #666;"),
        Div(
            *[
                Grid(
                    Div(
                        Div(
                            Img(
                                src=item.get_item.get_image,
                                style="width: 120px; height: 120px; object-fit: cover; border-radius: 8px; border: 1px solid #ddd;"
                            ),
                            Div(
                                H4(item.get_item.get_name, style="font-size: 18px; font-weight: bold; color: #333;"),
                                P(f"Amount {item.get_amount_in_cart}", style="font-size: 16px; color: #666;"),
                                P(f"Price {item.get_item.get_price}/ea", style="font-size: 16px; color: #666;"),
                                style="display: flex; flex-direction: column; gap: 5px; padding: 10px;"
                            ),
                            style="display: flex; align-items: center; gap: 15px;"
                        ),
                        style="display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);"
                    )
                ) for item in order.get_order.get_list_item_select
            ],
            style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: var(--azure-web);"
        )
    )

def order_history_page(session):
    user_id = session['auth'][0]
    order_list = main_system.get_history_items(user_id)

    if not order_list:
        return Div("No purchase history available.")

    return Div(
        H1("Order History", style="text-align: center; margin-bottom: 20px; color: #222;"),
        *[generate_order_card(order) for order in order_list],
        style="display:flex; flex-direction:column; gap:30px; padding:20px;"
    )
