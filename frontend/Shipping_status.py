from fasthtml.common import *
from mock.items import items
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system


def check_status(id):
    try:
        id = int(id)
        item = main_system.get_item_by_id(id)
        return Div(
            H1("Shipping Status"),
            Div(
                Img(src=item["image"], style="width: 100px; height: 100px; border-radius: 50%;"),
                H2("Order ID: " + str(id), style="color : #000000;"),
                H3("Item: " + item["name"], style="color : #000000;"),
                H3("Status: Shipped", style="color : #000000;"),
                style="background-color: #EEEEEE; padding: 10px; border-radius: 5px; margin: 10px;"
            ),
            style="text-align: center; margin: 0 auto; padding: 10px;"
        )
        return Div("Item not found", style="text-align: center; margin: 0 auto; padding: 10px;")
    except Exception as e:
        return Div(f"Error: {str(e)}", style="text-align: center; margin: 0 auto; padding: 10px;")