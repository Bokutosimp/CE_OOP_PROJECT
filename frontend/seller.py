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
    list_codes = main_system.get_codes()
    products = []
    bid_products = []
    load_discount_code = []

    #check bid item
    for i in list_item :
         if main_system.is_bid_item(i):
              bid_products.append(i)
         else: products.append(i)

    for j in list_codes :
         if main_system.is_discount_code(j): load_discount_code.append(j)

    print(load_discount_code)

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
    H1("Product Management", style="text-align: center ; color : black;"),

    Card(
        H3("Profile", style="color: #0074bd;"),
        H5(seller.get_store_name, style="font-size: 16px; color: #333;"),
        Div(
            Button("Add Product", onclick=f"window.location.href='/seller/add';", className="button"),
            Button("Add Bid Product", onclick=f"window.location.href='/seller/add_bid';", className="button"),
            Button("Create Discount Code", onclick=f"window.location.href='/seller/discount_code';", className="button"),
            style="display: flex; gap: 10px; justify-content: center; margin-top: 10px;"
        ),
        style="max-width: 700px; margin: auto; text-align: center; background-color: white !important; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);"
    ),

        Div(
    Button("Products", 
        onclick="showProducts()", 
        style="""background: #3498DB; color: white; padding: 10px 24px; border-radius: 20px; 
                 border: 2px solid #3498DB; cursor: pointer; font-size: 16px; font-weight: bold; transition: all 0.3s;""",
        onmouseover="this.style.background='#1E88E5'; this.style.borderColor='#1E88E5';",
        onmouseout="this.style.background='#3498DB'; this.style.borderColor='#3498DB';"
    ),
    Button("Bid Products", 
        onclick="showBidProducts()", 
        style="""background: #2A7FB8; color: white; padding: 10px 24px; border-radius: 20px; 
                 border: 2px solid #2A7FB8; cursor: pointer; font-size: 16px; font-weight: bold; transition: all 0.3s; margin-left: 12px;""",
        onmouseover="this.style.background='#1E5FA5'; this.style.borderColor='#1E5FA5';",
        onmouseout="this.style.background='#2A7FB8'; this.style.borderColor='#2A7FB8';"
    ),
    Button("Discount Code", 
        onclick="showCode()", 
        style="""background: #85C1E9; color: white; padding: 10px 24px; border-radius: 20px; 
                 border: 2px solid #85C1E9; cursor: pointer; font-size: 16px; font-weight: bold; transition: all 0.3s; margin-left: 12px;""",
        onmouseover="this.style.background='#5DADE2'; this.style.borderColor='#5DADE2';",
        onmouseout="this.style.background='#85C1E9'; this.style.borderColor='#85C1E9';"
    ),
    style="display: flex; justify-content: center; gap: 15px; margin: 20px;"
)

                ,

                Div(
                    Grid(*[create_product_card(p) for p in products if p.get_owner.get_user_id == user_id],
                        id="products-section",  
                        style="display: none; flex-wrap: wrap; gap: 20px; justify-content: center;"
                    )
                ),

                Div(
                    Grid(*[create_product_card(p, is_bid=True) for p in bid_products if p.get_owner.get_user_id == user_id],
                        id="bid-products-section",  
                        style="display: none; flex-wrap: wrap; gap: 20px; justify-content: center;"  
                    )
                ),
                 Div(
                  Div(
                    *[
                        Card(
                            H4(d.get_name, style="color: #333; font-weight: bold; text-align: center;"),
                            P(f"Discount: {d.get_discount}%", style="color: green; font-size: 16px; text-align: center;"),
                            Button("Copy Code", 
                                onclick=f"copyToClipboard('{d.get_name}')", 
                                style="""background: #ff8c00; color: white; padding: 6px 12px; border-radius: 5px; border: none; cursor: pointer; font-size: 14px; font-weight: bold; display: block; margin: 10px auto; transition: background 0.3s;""",
                                onmouseover="this.style.background='#e07a00'",
                                onmouseout="this.style.background='#ff8c00'"
                            ),
                            style="""width: 200px; padding: 15px; background: white; border-radius: 8px;box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center;"""
                        )  for d in load_discount_code
                    ],
                    id="discount-code-section", style="display: none; flex-wrap: wrap; gap: 20px; justify-content: center; margin-top: 15px;"
                ),
                    Script("""
                    function copyToClipboard(text) {
                    navigator.clipboard.writeText(text).then(() => {
                    alert("Copied: " + text);
                    }).catch(err => {
                    alert("Failed to copy: " + err);
                    });
                    }
                        """)
            )
,
                 Script("""
                        function showProducts() {
                            document.getElementById("products-section").style.display = "flex";
                            document.getElementById("bid-products-section").style.display = "none";
                            document.getElementById("discount-code-section").style.display = "none";
                        }
                        function showBidProducts() {
                            document.getElementById("products-section").style.display = "none";
                            document.getElementById("bid-products-section").style.display = "flex";
                            document.getElementById("discount-code-section").style.display = "none";
                        }
                        function showCode() {
                            document.getElementById("products-section").style.display = "none";
                            document.getElementById("bid-products-section").style.display = "none";
                            document.getElementById("discount-code-section").style.display = "flex";
                        }
                    """)
                    ,

                Div(
                Form(
    Div(
        H3("Stock Item", style="margin-left : 10 px ; text-align: center; color: #3498DB; flex-grow: 1;"),
        Button(
            "❌", type="button", 
            style="""background: none; border: none; font-size: 24px; color: #E74C3C; cursor: pointer;""",
            onclick="document.getElementById('popup-stock').style.display='none';"
        ),
        style="display: flex; justify-content: space-between; align-items: center; width: 100%;"
    ),

    Input(type="hidden", id="stock_item_id", name="stock_item_id"),  
    Input(type="hidden", id="stock_bid_item_id", name="stock_bid_item_id"),  

    Input(
        type="number", name="stock", id="stock", placeholder="Enter amount",
        style="""padding: 10px; border-radius: 8px; border: 1px solid #3498DB;
                 width: 100%; font-size: 16px; margin-top: 5px; text-align: center;""",
        required=True
    ),

    Button(
        "Submit", type="submit",
        style="""background: #3498DB; color: white; padding: 12px; border-radius: 8px;
                 border: none; cursor: pointer; font-size: 16px; font-weight: bold;
                 margin-top: 15px; width: 100%; transition: background 0.3s;""",
        onmouseover="this.style.background='#1E88E5'",
        onmouseout="this.style.background='#3498DB'"
    ),

    action="/update_stock", method="post", id="stock-form",
    style="""display: flex; flex-direction: column; gap: 15px; background: white;
             padding: 25px; border-radius: 12px; box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
             width: 350px; position: relative;"""
)
,

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


    )

@rt("/update_stock", methods=["post"])
def update_stock(add_stock: Stock_product, session):
    try:
        user_id = session['auth'][0]
        amount = add_stock.stock
        item_id = add_stock.stock_item_id

        main_system.add_stock(user_id, item_id, amount) 
    
        return Script(""" alert('Add stock successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")
    except Exception as e:
        return Script(""" alert('Invalid stock update'); setTimeout(function(){ window.location.href = '/seller ';  });""")

@rt("/update_bid_stock", methods=["post"])
def update_bid_stock(add_bid_stock: Stock_bid_product, session):
    try:
        user_id = session['auth'][0]
        amount = add_bid_stock.stock
        item_id = add_bid_stock.stock_bid_item_id
        print(amount)
        print(item_id)
        
        main_system.add_bid_stock(user_id, item_id, amount) 
        return Script(""" alert('Add stock successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")

    except:
        return Script(""" alert('Invalid stock update'); setTimeout(function(){ window.location.href = '/seller ';  });""")



def edit_product(session ,edit_item_id:str,new_name:str,new_price:float,new_category:str,new_detail:str,new_image:str):
    user_id = session['auth'][0]
    main_system.edit_item(edit_item_id ,new_name , new_category.split(',') , new_detail ,new_price , new_image)  

def edit_bid_product(session ,edit_bid_item_id:str,new_name:str,new_price:float,new_category:str,new_detail:str,new_image:str , new_start_time : str , new_end_time : str):
    user_id = session['auth'][0]
    main_system.edit_bid_item(edit_bid_item_id ,new_name , new_category.split(',') , new_detail ,new_price , new_image , new_start_time , new_end_time)  


