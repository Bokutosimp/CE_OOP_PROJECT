from fasthtml.common import *
from backend.system import main_system

app, rt = fast_app()

@dataclass
class Stock_product:
    stock: int
    stock_item_id: str

@dataclass
class Stock_bid_product:
    stock: int
    stock_bid_item_id: str

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
    user_id = session['auth'][0]
    seller = main_system.get_user_by_id(user_id)
    list_item = main_system.get_items()
    products = []
    bid_products = []

    #check bid item
    for i in list_item :
         if main_system.is_bid_item(i):
              bid_products.append(i)
         else: products.append(i)

    def create_product_card(item, is_bid=False):
            # กำหนด ID ของ input และ URL ให้แตกต่างกัน
            stock_input_id = "stock_bid_item_id" if is_bid else "stock_item_id"
            stock_action_url = "/update_bid_stock" if is_bid else "/update_stock"

            return Card(
                Div(
                    H3(item.get_name, style="color: #0074bd;"),
                    Img(src=item.get_image, style="width: 100px; height: 100px; object-fit: cover;"),
                    P(f"Stock: {item.get_amount}", style="color: black; font-weight: bold;"),
                    P(f"Price: {item.get_price} $", style="color: green; font-weight: bold;"), 
                    style="display: flex; flex-direction: column; align-items: center; text-align: center;"
                ),
                Div(
                    # ปุ่ม "Stock" ของ Item และ Bid Item แยกกัน
                    Button(
                        "Stock", 
                        onclick=f"""
                            document.getElementById('{stock_input_id}').value = '{item.get_id}';
                            document.getElementById('popup-stock').dataset.action = '{stock_action_url}';
                            document.getElementById('popup-stock').style.display='flex';
                        """, 
                        className="button"
                    ),
                    A(Button(
                        "Edit", 
                        className="button",  
                        style="background-color: green;"
                    ),href=f'{ '/edit_bid_item/'+str(item.get_id) if is_bid else '/edit_item/'+str(item.get_id) }'),
                    style="display: flex; gap: 10px; justify-content: center;"
                ),
                style=f"width: 250px; padding: 15px; background: {'#e5ffca' if is_bid else 'white'}; box-shadow: 0 2px 5px rgba(0,0,0,0.1);"
            )

# { '/edit_bid_item/'+str(item.get_id) if is_bid else '/edit_item/'+str(item.get_id) }

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
                    H3("Stock Item", style="text-align: center; color: #333;"),
                    Input(type="hidden", id="stock_item_id", name="stock_item_id"),  
                    Input(type="hidden", id="stock_bid_item_id", name="stock_bid_item_id"),  
                    Input(
                        type="number", name="stock", id="stock", placeholder="Enter amount",
                        style="""
                            padding: 10px; border-radius: 8px; border: 1px solid #ccc;
                            width: 100%; font-size: 16px; margin-top: 5px; text-align: center;
                        """,
                        required="true"
                    ),

                    Button(
                        "Submit", type="submit",
                        style="""
                            background: #0074bd; color: white; padding: 12px; border-radius: 8px;
                            border: none; cursor: pointer; font-size: 16px; font-weight: bold;
                            margin-top: 15px; width: 100%; transition: background 0.3s;
                        """,
                        onmouseover="this.style.background='#005fa3'",
                        onmouseout="this.style.background='#0074bd'"
                    ),

                    action="/update_stock", method="post", id="stock-form",
                    style="""
                        display: flex; flex-direction: column; gap: 15px;
                        background: white; padding: 25px; border-radius: 12px;
                        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
                        width: 350px;
                    """
                ),

                id="popup-stock",
                style="""
                    display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                    background: rgba(0,0,0,0.4); backdrop-filter: blur(5px);
                    justify-content: center; align-items: center; z-index: 999;
                """,
                onsubmit="""
                    event.preventDefault();
                    const form = document.getElementById('stock-form');
                    form.action = document.getElementById('popup-stock').dataset.action;  
                    form.submit();
                """
            )  ,

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
        )

    )

@rt("/update_stock", methods=["post"])
def update_stock(add_stock: Stock_product, session):
    # try:
        user_id = session['auth'][0]
        amount = add_stock.stock
        item_id = add_stock.stock_item_id

        main_system.add_stock(user_id, item_id, amount) 
    
        return Script(""" alert('Add stock successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")
    # except Exception as e:
    #     print(f"Error: {str(e)}")
    #     return Script(""" alert('Invalid stock update'); setTimeout(function(){ window.location.href = '/seller ';  });""")

@rt("/update_bid_stock", methods=["post"])
def update_bid_stock(add_bid_stock: Stock_bid_product, session):
    # try:
        user_id = session['auth'][0]
        amount = add_bid_stock.stock
        item_id = add_bid_stock.stock_bid_item_id
        print(amount)
        print(item_id)
        
        result = main_system.add_bid_stock(user_id, item_id, amount) 
        return Script(""" alert('Add stock successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")

    # except Exception as e:
    #     print(f"Error: {str(e)}")
    #     return Script(""" alert('Invalid stock update'); setTimeout(function(){ window.location.href = '/seller ';  });""")



def edit_product(session ,edit_item_id:str,new_name:str,new_price:float,new_category:str,new_detail:str,new_image:str):
    user_id = session['auth'][0]
    print('trying in seller.py editing id = ',edit_item_id+"cat = "+str(type(new_category))+f"({new_category.split(',')})")
    main_system.edit_item(edit_item_id ,new_name , new_category.split(',') , new_detail ,new_price , new_image)  

def edit_bid_product(session ,edit_bid_item_id:str,new_name:str,new_price:float,new_category:str,new_detail:str,new_image:str , new_start_time : str , new_end_time : str):
    user_id = session['auth'][0]
    print(f'{new_category} , {new_price}')
    print(f"{new_image}")
    print('trying in seller.py editing id = ',edit_bid_item_id+"cat = "+str(type(new_category))+f"({new_category.split(',')})")
    main_system.edit_bid_item(edit_bid_item_id ,new_name , new_category.split(',') , new_detail ,new_price , new_image , new_start_time , new_end_time)  


