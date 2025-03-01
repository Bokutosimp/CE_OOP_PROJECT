from fasthtml.common import *
from add_product import add_product_page

app, rt = fast_app()

def product_management():
    return Main(
        Div(
            H1("Product Management", style="text-align: center; margin-bottom: 20px; color: #222;"),  
            style="background: #f7f7f7; padding: 20px; border-bottom: 2px solid #ddd;"
        ),

        Div(
            Card(
                H3("Profile", style="color: #0074bd;"),
                Div(
                    Img(
                        src='https://i.pinimg.com/564x/f5/9f/5e/f59f5ece0a7984f20413a4e32a4f25a2.jpg',
                        style='width: 50px; height: 50px; object-fit: cover; border-radius: 50%;' 
                    ),
                    Div(
                        H5('Gojo Satoru', style='font-size: 16px; margin: 0; color: #333;'), 
                        P(
                            "อิมาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                            style='margin: 0; font-size: 14px; color: gray;'
                        ),  
                        style='display: flex; flex-direction: column; margin-left: 10px; max-width: 150px;'  
                    ),
                    style='display: flex; align-items: center;'  
                ),
                Button("Add Product", onclick="window.location.href='/seller/add';", style="background: #0074bd; color: white; border-radius: 5px; padding: 10px 15px; border: none; margin-top: 10px;"),
                Button("Add Bid Product", onclick="window.location.href='/seller/add_bid';", style="background: #0074bd; margin-left : 10px ;color: white; border-radius: 5px; padding: 10px 15px; border: none; margin-top: 10px;"),
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
                    H3(f"PRODUCT #{i}", style="color: #0074bd;"),
                    Div(
                        Img(
                            src=img_url,
                            style='width: 120px; height: 120px; object-fit: cover; border-radius: 8px; margin-right: 15px; border: 1px solid #ddd;' 
                        ),
                        P(
                            "คำอธิบายสินค้าตัวอย่างที่นี่...",
                            style='font-size: 14px; color: #555; max-width: 200px;'
                        ),
                        style='display: flex; align-items: center; padding: 10px;'
                    ),
                    Div(
                        Button("Stock", onclick="document.getElementById('popup').style.display='flex'" ,style="background: #0074bd; color: white; border-radius: 5px; padding: 8px 12px; border: none;"),
                        Button("Ship", style="background: #ff9900; color: white; border-radius: 5px; padding: 8px 12px; border: none; margin-left: 10px;"),
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
                ) for i, img_url in enumerate([
                    'https://leagueofitems.com/images/items/256/3078.webp',
                    'https://s.isanook.com/ga/0/ud/221/1106953/frost-cape.png?ip/resize/w728/q80/png',
                    'https://tkcdn.tekedia.com/wp-content/uploads/2022/05/23204855/coke-768x432.jpg'
                ], start=1)
            ],
            style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; background: #f7f7f7;"
        ),
        Div(
            Div(
                 Label(Input(type="number", id="amount", placeholder="Amount", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
                
              
                Button("Submit", onclick="document.getElementById('popup').style.display='none'; document.getElementById('amount').value = '';",
                       style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),

                style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center;"
            ),
            id="popup",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center;"
        ),

        style="background: #fff; min-height: 100vh; font-family: Arial, sans-serif;"
    )
