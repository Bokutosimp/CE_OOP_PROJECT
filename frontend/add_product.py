from fasthtml.common import *
from backend.system import main_system

app, rt = fast_app()

@dataclass
class Product:
    name: str
    price: float
    amount: int
    category: str
    description: str
    image: str 

@rt("/seller/add")
def add_product_page(session):
    user_id = session['auth'][0]
    return Container(
        Grid(H1("Add Item Management", style="text-align: center; margin-bottom: 20px; color: #0074bd;")),
        Form(
            Label("Product Name:", Input(id="name", name="name", type="text", placeholder="Enter your product name")),
            Label("Price:", Input(id="price", name="price", type="number", placeholder="Enter your price")),
            Label("Amount:", Input(id="amount", name="amount", type="number", placeholder="Enter your amount")),
            Label("Category:", Input(id="category", name="category", type="text", placeholder="Enter category")),
            Label("Description:", Textarea(id="description", name="description", rows=5, placeholder="Product description...")),
            Label("Image:", Input(id="image", name="image", type="text" , placeholder="Enter your image url" )),
            Button("Submit", type="submit"),
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            action=f"/seller/add/submit",
            method="post"
        )
    )

@rt("/seller/add/submit", methods=["post"])
async def submit_product_page(product: Product , session):
    user_id = session['auth'][0]
    print(user_id)
    # image_data = product.image.read() 
    print(f"📦 Product Name: {product.name}")
    print(f"💰 Price: {product.price}")
    print(f"🏷️ Category: {product.category}")    
    print(f"🏷️ Category: {product.category}")    
    print(f"🏷️ Category: {product.image}")    

    if (product.name != None and product.price != None and product.category != None and product.description != None):
        main_system.save_item(user_id,product.name,product.price , product.amount , product.category , product.image )
    else : 
        return Script("alert('Invalid")

    return Main(
        H1("✅ Product Added Successfully!", style="text-align: center; color: #222;"),
        Script(
            """ 
            setTimeout(function(){
                window.location.href = '/seller ';  }, 2000);
            """
        ),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

serve()
