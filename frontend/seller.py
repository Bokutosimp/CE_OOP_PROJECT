from fasthtml.common import *
from backend.system import main_system

app, rt = fast_app()

@dataclass
class Stock_product:
    stock: int
    stock_item_id: str

@dataclass
class Edit_product:
    new_name: str
    new_detail: str
    new_price: float

def product_management(request: Request):
    user_id = request.query_params.get("user_id", "NO DATA")
    seller = main_system.get_user_by_id(user_id)
    products = main_system.get_items()
    bid_products = main_system.get_bid_items()

    def create_product_card(item, is_bid=False):
        return Card(
            H3(item.get_name, style="color: #0074bd;"),
            Img(src=item.get_image, style="width: 100px; height: 100px; object-fit: cover;"),
            P(f"Stock: {item.get_amount}", style="color: black; font-weight: bold;"),
            Div(
                Button(
                    "Stock", 
                    onclick=f"document.getElementById('stock_item_id').value = '{item.get_id}'; document.getElementById('popup-stock').style.display='flex'", 
                    className="button"
                ),
                Button(
                    "Edit", 
                    onclick=f"document.getElementById('edit-item-id').value = '{item.get_id}'; document.getElementById('popup-edit').style.display='flex'", 
                    className="button", 
                    style="background-color: green;"
                ),
                Button("Ship", className="button", style="background-color: orange;"),
                style="display: flex; gap: 10px; justify-content: center;"
            ),
            style=f"width: 250px; padding: 15px; background: {'#e5ffca' if is_bid else 'white'}; box-shadow: 0 2px 5px rgba(0,0,0,0.1);"
        )

    return Main(
        H1("Product Management", style="text-align: center;"),
        Card(
            H3("Profile", style="color: #0074bd;"),
            H5(seller.get_store_name, style="font-size: 16px; color: #333;"),
            Div(
                Button("Add Product", onclick=f"window.location.href='/seller/add?user_id={user_id}';", className="button"),
                Button("Add Bid Product", onclick=f"window.location.href='/seller/add_bid?user_id={user_id}';", className="button"),
                Button("Create Discount Code", onclick=f"window.location.href='/discount_code?user_id={user_id}';", className="button"),
                style="display: flex; gap: 10px; justify-content: center; margin-top: 10px;"
            ),
            style="max-width: 700px; margin: auto; text-align: center; background-color: white !important; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);"
        ),
        H4("Products", style="text-align: center; margin-top: 20px;"),
        Grid(*[create_product_card(p) for p in products if p.get_owner.get_user_id == user_id],
             style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;"),
        H4("Bid Products", style="text-align: center; margin-top: 20px;"),
        Grid(*[create_product_card(p, is_bid=True) for p in bid_products if p.get_owner.get_user_id == user_id],
             style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;"),
        Div(
            Form(
                H3("Stock Item"),
                Input(type="hidden", id="stock_item_id", name="stock_item_id"),  
                Input(type="number", name="stock", placeholder="Amount",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Button("Submit", type="submit",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                action=f"/update_stock?user_id={user_id}", method="post",
            ),
            id="popup-stock",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
        Div(
            Form(
                H3("Edit Product"),
                Input(type="hidden", id="edit-item-id", name="stock_item_id"),  # ✅ ชื่อตรงกับ dataclass
                Input(type="text", name="new_name", placeholder="New Product Name",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Input(type="text", name="new_detail", placeholder="New Detail",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Input(type="number", name="new_price", placeholder="New Price",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Button("Submit", type="submit",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                action=f"/edit_product?user_id={user_id}", method="post",
            ),
            id="popup-edit",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        )
    )

@rt("/update_stock", methods=["post"])
async def update_stock(add_stock: Stock_product, request: Request):
    user_id = request.query_params.get("user_id", "none")
    amount = add_stock.stock
    item_id = add_stock.stock_item_id
    try:
        if main_system.add_stock(user_id, item_id, amount) == 'Success' :
            return Main(
        H1("✅ Added Stock Successfully!", style="text-align: center; color: #222;"),
        Script(f"setTimeout(function(){{ window.location.href = '/seller?user_id={user_id}'; }}, 2000);"),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )
    except Exception as e:
        print(f"Error: {e}")
        return Main(
        H1("❌ Added Stock Failed!", style="text-align: center; color: #222;"),
        Script(f"setTimeout(function(){{ window.location.href = '/seller?user_id={user_id}'; }}, 2000);"),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

@rt("/edit_product", methods=["post"])
async def edit_product(edit: Edit_product, request: Request):
    user_id = request.query_params.get("user_id", "none")

    try:
        main_system.update_product(user_id, edit.stock_item_id, edit.new_name, edit.new_detail, edit.new_price)  # ✅ ใช้ค่าจาก dataclass
    except Exception as e:
        print(f"Error: {e}")

    return Main(
        H1("✅ Edit Product Successfully!", style="text-align: center; color: #222;"),
        Script(f"setTimeout(function(){{ window.location.href = '/seller?user_id={user_id}'; }}, 2000);"),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )
