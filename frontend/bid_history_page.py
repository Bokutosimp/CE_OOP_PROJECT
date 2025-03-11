from fasthtml.common import *
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def generate_bid_order_card(bid):
    return Div(
        Div(
            Span(f'Order Date: {bid.get_shipping_status.get_shipping_date.strftime("%y-%m-%d")}', 
                 style='color: #666; font-size: 14px; font-weight: bold;'),
            P(f"Total Price: ${bid.get_item.get_price:.2f}", 
              style="font-size: 18px; color: #444; font-weight: bold; margin-top: 5px;"),
            style="display: flex; flex-direction: column; align-items: flex-start; padding: 15px; background: #f8f9fa; border-radius: 10px; border-left: 5px solid #007bff; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);"
        ),
        Div(
            Div(
                Div(
                    Img(
                        src=bid.get_item.get_image,
                        style="width: 100px; height: 100px; object-fit: cover; border-radius: 8px; border: 1px solid #ddd;"
                    ),
                    Div(
                        H4(bid.get_item.get_name, style="font-size: 18px; font-weight: bold; color: #333; margin-bottom: 5px;"),
                        P(f"Price: ${bid.get_item.get_price:.2f} each", style="font-size: 16px; color: #777;"),
                        style="display: flex; flex-direction: column; gap: 5px;"
                    ),style="display:flex; align-items:center; gap:15px;"
                ),
                style="display:flex; align-items:center; justify-content:space-between; padding: 10px; background: white; border-radius: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);"
            ),
            style="display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: #fff; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);"
        ),
            )
    
def bid_history_page(session):
    user_id = session['auth'][0]
    bid_list = main_system.get_history_bids(user_id)
    print(bid_list)

    if not bid_list:
        return Div("No purchase history available.")

    return Div(
        H1("Bid History", style="text-align: center; margin-bottom: 20px; color: #222;"),
        *[generate_bid_order_card(bid) for bid in bid_list],
        style="display:flex; flex-direction:column; gap:30px; padding:20px;"
    )
