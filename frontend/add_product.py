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
    # image: UploadFile 

@rt("/seller/add")
def add_product_page(request : Request):
    user_id = request.query_params.get('user_id',"no user_id")
    return Container(
        Grid(H1("Add Item Management", style="text-align: center; margin-bottom: 20px; color: #222;")),
        Form(
            Label("Product Name:", Input(id="name", name="name", type="text", placeholder="Enter your product name")),
            Label("Price:", Input(id="price", name="price", type="number", placeholder="Enter your price")),
            Label("Amount:", Input(id="amount", name="amount", type="number", placeholder="Enter your amount")),
            Label("Category:", Input(id="category", name="category", type="text", placeholder="Enter category")),
            Label("Description:", Textarea(id="description", name="description", rows=5, placeholder="Product description...")),
            Label("Image:", Input(id="image", name="image", type="file", accept="image/*")),
            Button("Submit", type="submit"),
            enctype="multipart/form-data",
            action=f"/seller/add/submit?user_id={user_id}",
            method="post"
        )
    )

@rt("/seller/add/submit", methods=["post"])
async def submit_product_page(product: Product , request : Request):
    user_id = request.query_params.get('user_id','no user_id')
    print(user_id)
    # image_data = product.image.read() 
    print(f"📦 Product Name: {product.name}")
    print(f"💰 Price: {product.price}")
    print(f"🏷️ Category: {product.category}")    
    if (product.name != None and product.price != None and product.category != None and product.description != None):
        main_system.save_item(user_id,product.name,product.price , product.amount , product.category , img = '' )
    else : return Script("alert('Invalid")

    return Main(
        H1("✅ Product Added Successfully!", style="text-align: center; color: #222;"),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

serve()
