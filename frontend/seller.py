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
    new_category : str
    new_detail: str
    new_price: float
    new_image: str
    edit_item_id : str

@dataclass
class EditBidProduct:
    new_name: str
    new_start_price: float
    new_detail: str
    new_amount: int
    new_category: str
    new_start_time: str
    new_end_time: str
    new_description: str
    new_image: str
    edit_bid_item_id: str


def product_management(session):
    print(session['auth'][0])
    user_id = session['auth'][0]
    seller = main_system.get_user_by_id(user_id)
    products = main_system.get_items()
    bid_products = main_system.get_bid_items()
    load_category = main_system.get_categories()

    def create_product_card(item, is_bid=False):
        return Card(
            Div(
                H3(item.get_name, style="color: #0074bd;"),
                Img(src=item.get_image, style="width: 100px; height: 100px; object-fit: cover;"),
                P(f"Stock: {item.get_amount}", style="color: black; font-weight: bold;"),
                P(f"Price: {item.get_price} $", style="color: green; font-weight: bold;"), 
                style="display: flex; flex-direction: column; align-items: center; text-align: center;"

            ),
            Div(
                 Button(
                    "Stock", 
                    onclick=f"document.getElementById('stock_item_id').value = '{item.get_id}'; document.getElementById('popup-stock').style.display='flex'", 
                    className="button"
                ),
                Button(
                    "Edit", 
                    onclick=f"document.getElementById('{ 'edit_bid_item_id' if is_bid else 'edit_item_id' }').value = '{item.get_id}'; document.getElementById('{ 'popup-edit-bid' if is_bid else 'popup-edit' }').style.display='flex'", 
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
                Button("Add Product", onclick=f"window.location.href='/seller/add';", className="button"),
                Button("Add Bid Product", onclick=f"window.location.href='/seller/add_bid';", className="button"),
                Button("Create Discount Code", onclick=f"window.location.href='/discount_code';", className="button"),
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
                Input(type="hidden", id="edit_item_id", name="edit_item_id"),  
                Input(type="text", name="new_name", placeholder="New Product Name",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                 Select(  *[Option(cat.get_name ,value = cat.get_id) for cat in load_category] ,
                    style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;", name='new_category', id='category'
                ),
                Input(type="text", name="new_detail", placeholder="New Detail",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Input(type="number", name="new_price", placeholder="New Price",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Input(type="text", name="new_image", placeholder="New image",
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Button("Submit", type="submit",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                action=f"/edit_product", method="post",
            ),
            id="popup-edit",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
         Div(
            Form(
                H3("Edit Bid Product"),
                Input(type="hidden", id="edit_bid_item_id", name="edit_bid_item_id"), 
                Input(type="text", name="new_name", placeholder="New Bid Product Name", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Input(type="number", name="new_start_price", placeholder="New Start Price", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),  
                Input(type="text", name="new_detail", placeholder="New Detail", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
                Button("Submit", type="submit",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                action=f"/edit_product", method="post",
            ),
            id="popup-edit",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
        # Popup สำหรับแก้ไขสินค้าประมูล
            Div(
                Form(
                    H3("Edit Bid Product"),
                    Input(type="hidden", id="edit_bid_item_id", name="edit_bid_item_id"),
                    Label("Bid Product Name:", Input(type="text", name="new_name", placeholder="Enter your product name",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("Start Price:", Input(type="number", name="new_start_price", placeholder="Enter your start price",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("Amount:", Input(name="new_amount", type="number", placeholder="Enter your amount",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("Category:", 
                        Select(*[Option(cat.get_name, value=cat.get_id) for cat in load_category],
                                style="width:100%; margin:0;", name='new_category')),
                    Label("Start Time:", Input(type="date", name="new_start_time",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("End Time:", Input(type="date", name="new_end_time",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("Description:", Textarea(name="new_description", rows=5, placeholder="Product description...",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Label("Image URL:", Input(type="text", name="new_image", placeholder="Enter your image URL",
                        style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                    Button("Submit", type="submit",
                        style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                    action="/edit_bid_product", method="post",
                ),
                id="popup-edit-bid",
                style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
            )

    )

@rt("/update_stock", methods=["post"])
async def update_stock(add_stock: Stock_product, session):
    try :
        user_id = session['auth'][0]
        amount = add_stock.stock
        item_id = add_stock.stock_item_id
        if main_system.add_stock(user_id, item_id, amount) == 'Success' :
                return Script(""" alert('Add stock successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")
    except :
        return  Script("""Invalid'; setTimeout(function(){ window.location.href = '/seller ';  });""")

@rt("/edit_product", methods=["post"])
async def edit_product(edit: Edit_product, session):
    user_id = session['auth'][0]
    new_name = edit.new_name
    new_detial = edit.new_detail
    new_price = edit.new_price 
    item_id = edit.edit_item_id
    new_image = edit.new_image
    new_category = edit.new_category
    print(item_id)
    try:
        main_system.edit_item(item_id ,new_name , new_category , new_detial ,new_price , new_image)  
    except Exception as e:
        return Script(""" alert('Error'); setTimeout(function(){ window.location.href = '/seller ';  });""")

    return  Script(""" alert('edit Product successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")


@rt("/edit_bid_product", methods=["post"])
async def edit_bid_product(edit: EditBidProduct, session):
    user_id = session['auth'][0]

    return Script(""" alert('Edit Bid Product successfully'); 
                          setTimeout(function(){ window.location.href = '/seller'; });""")
