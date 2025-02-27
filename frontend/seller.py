from fasthtml.common import *
import add_product

app, rt = fast_app()

@rt('/')
def get():
    return Main(
        Div(
            H1("Product Management", style="text-align: center; margin-bottom: 20px; color: #222;"),  
            style="background: #f7f7f7; padding: 20px; border-bottom: 2px solid #ddd;"
        ),

        # Profile Section
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
                            "มาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                            style='margin: 0; font-size: 14px; color: gray;'
                        ),  
                        style='display: flex; flex-direction: column; margin-left: 10px; max-width: 150px;'  
                    ),
                    style='display: flex; align-items: center;'  
                ),
                Button("Add Product", onclick="window.location.href='/add';", style="background: #0074bd; color: white; border-radius: 5px; padding: 10px 15px; border: none; margin-top: 10px;"),
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

        # Product Section
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
                        Button("Stock", style="background: #0074bd; color: white; border-radius: 5px; padding: 8px 12px; border: none;"),
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

        style="background: #fff; min-height: 100vh; font-family: Arial, sans-serif;"
    )

@rt('/add')
def add():
    return add_product.add_product_page()

serve()
