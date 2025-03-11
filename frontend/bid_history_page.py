from fasthtml.common import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def generate_bid_order_card(order):
    return Div(
        P(f"{order.get_name}"),
        P(f"{order.get_price}")
    )

def bid_history_page(session):
    user_id = session['auth'][0]
    order_list = main_system.get_history_bids(user_id)

    if not order_list:
        return Div("No purchase history available.")

    return Div(
        H1("Order History", style="text-align: center; margin-bottom: 20px; color: #222;"),
        *[generate_bid_order_card(order) for order in order_list],
        style="display:flex; flex-direction:column; gap:30px; padding:20px;"
    )
