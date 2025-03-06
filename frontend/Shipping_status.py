from fasthtml.common import *
from mock.items import items

def check_status(id):
    try:
        id = int(id)
        for item in items:
            if item["id"] == id:
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