from fasthtml.common import *
from stylesheet import *
from add_product import add_product_page
from mock.users import users
from backend.system import *
from backend.system import main_system



app, rt = fast_app()



def product_management(request: Request):
    user_id = request.query_params.get("user_id", "์NO DATA!!!!")
    seller  = main_system.get_user_by_id(user_id)
    load_items = main_system.get_items()      
    load_bid_items = main_system.get_bid_items()      
    print(load_bid_items[0].get_owner)
    return Main(
        
        Div(
            H1("Product Management", style="text-align: center; margin-bottom: 20px; color: #222;"),  
            style="background: #f7f7f7; padding: 20px; border-bottom: 2px solid #ddd;"
        ),

        Div(
            Card(
                H3("Profile", style="color: #0074bd;"),
                Div(
                    # Img(
                    #     src='https://i.pinimg.com/564x/f5/9f/5e/f59f5ece0a7984f20413a4e32a4f25a2.jpg',
                    #     style='width: 50px; height: 50px; object-fit: cover; border-radius: 50%;' 
                    # ),
                    Div(
                        H5(seller.get_store_name, style='font-size: 16px; margin: 0; color: #333;'), 
                        P(
                            "อิมาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                            style='margin: 0; font-size: 14px; color: gray;'
                        ),  
                        style='display: flex; flex-direction: column; margin-left: 10px; max-width: 150px;'  
                    ),
                    style='display: flex; align-items: center;'  
                ),
                Button("Add Product", onclick=f"window.location.href='/seller/add?user_id={seller.get_user_id}';", className = "button" , style="margin : 10px"),
                Button("Add Bid Product", onclick=f"window.location.href='/seller/add_bid?user_id={seller.get_user_id}';", className = "button"),
                style = """
                    width: 100%;    
                    border-radius: 8px; 
                    padding: 20px; 
                    background: white;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    margin-bottom: 20px;
                """ 
            ),
            style="display: flex; justify-content: center; padding: 20px;"
        ), 

        Grid(
            *[
                Card(
                    Span(H3(item.get_name, style="color: #0074bd;"), P(item.get_amount, style="color:black ; font-weight: bold;") , style="display: flex; justify-content: space-between; margin-top: 15px;"),
                    Div(
                        Img(
                            src=item.get_image,
                            style='width: 120px; height: 120px; object-fit: cover; border-radius: 8px; margin-right: 15px; border: 1px solid #ddd;' 
                        ),
                        P(
                            "คำอธิบายสินค้าตัวอย่างที่นี่...",
                            style='font-size: 14px; color: #555; max-width: 200px;'
                        ),
                        style='display: flex; align-items: center; padding: 10px;'
                    ),
                    Div(
                        Button("Stock", onclick="document.getElementById('popup').style.display='flex'" , className = "button"),
                        Button("edit", onclick = "document.getElementById('edit-popup').style.display='flex'", className = "button" , style="background-color : green ; margin-left : -35%"),
                        Button("Ship", className = "button" , style="background-color : orange"),
                        style="display: flex; justify-content: space-between; margin-top: 15px;"
                    ),
                    style = """
                        width: 100%;    
                        border-radius: 8px; 
                        padding: 20px; 
                        background: white;
                        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                        margin-bottom: 20px;
                    """
                ) for item in load_items if item.get_owner.get_user_id == user_id 
            ],
            style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: #f7f7f7;"
        ),
        Grid(
            *[
                Card(
                    Span(H3(item.get_name, style="color: #0074bd;"), P(item.get_amount, style="color:black ; font-weight: bold;") , style="display: flex; justify-content: space-between; margin-top: 15px;"),
                    Div(
                        Img(
                            src='https://i.pinimg.com/564x/f5/9f/5e/f59f5ece0a7984f20413a4e32a4f25a2.jpg',
                            style='width: 120px; height: 120px; object-fit: cover; border-radius: 8px; margin-right: 15px; border: 1px solid #ddd;' 
                        ),
                        P(
                            "คำอธิบายสินค้าตัวอย่างที่นี่...",
                            style='font-size: 14px; color: #555; max-width: 200px;'
                        ),
                        style='display: flex; align-items: center; padding: 10px;'
                    ),
                    Div(
                        Button("Stock", onclick="document.getElementById('popup').style.display='flex'" , className = "button"),
                        Button("edit", onclick = "document.getElementById('edit-popup').style.display='flex'", className = "button" , style="background-color : green ; margin-left : -35%"),
                        Button("Ship", className = "button" , style="background-color : orange"),
                        style="display: flex; justify-content: space-between; margin-top: 15px;"
                    ),
                    style = """
                        width: 100%;    
                        border-radius: 8px; 
                        padding: 20px; 
                        background: #f9fec2;
                        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                        margin-bottom: 20px;
                    """
                ) for item in load_bid_items if item.get_owner == user_id 
            ],
            style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: #f7f7f7;"
        ),
        Div(
            Div(
                  Label(H3('Stock Item')),
                 Label(Input(type="number", id="amount", placeholder="Amount", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                Button("Submit", onclick="document.getElementById('popup').style.display='none'; document.getElementById('amount').value = '';",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center;"
            ),
            id="popup",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
         Div(
            Div(
                Label(H3('Edit product')),
                Label(Input(type="string", id="name", placeholder="new product name", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                Label(Input(type="string", id="detial", placeholder="new detail", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                Label(Input(type="number", id="price", placeholder="new price", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                Button("Submit", onclick="document.getElementById('edit-popup').style.display='none'; document.getElementById('amount').value = '';",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center;"
            ),
            id="edit-popup",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),
        style="background: #fff; min-height: 100vh; font-family: Arial, sans-serif;" 
        
    )
