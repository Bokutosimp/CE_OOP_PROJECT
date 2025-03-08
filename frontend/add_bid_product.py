from fasthtml.common import *
from backend.system import *

app, rt = fast_app()

@dataclass
class Bid_Product:
    name: str
    price: float
    amount: int
    category: str
    start_time : str
    end_time : str
    description: str
    image: str 

def add_bid_product_page(request : Request): 
    user_id = request.query_params.get('user_id','no user_id')
    return Container(
        Grid(
            H1("Add Bid Item Management", style="text-align: center; margin-bottom: 20px; color: #0074bd;"),  
        ),
        Form( 
            Label("Bid Product Name:", Input(type="text", id="name", placeholder="Enter your product name", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Start Price:", Input(type="number", id="price", placeholder="Enter your price", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Amount:", Input(id="amount", name="amount", type="number", placeholder="Enter your amount")),
            Label("Category", Input(type="text", id="category", placeholder="Enter start time", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Start Time", Input(type="date", id="start_time", placeholder="Enter end time", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("End Time", Input(type="date", id="end_time", placeholder="Enter category", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Description:", Textarea(id="description", rows=5, placeholder="Product description...", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Image:", Input(type="text", id="image", placeholder="Enter your image url" , style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")), 

            Button("Submit", type="submit"),
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            action=f"/seller/add_bid/submit?user_id={user_id}",
            method="post"
        ),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

@rt("/seller/add_bid/submit", methods=["post"])
def submit_bid_product_page(product: Bid_Product , request : Request):
    user_id = request.query_params.get('user_id','no user_id')
    print(user_id)
    print(f"📦 Product Name: {product.name}")
    print(f"💰 Price: {product.price}")
    print(f"🏷️ Category: {product.category}")    
    print(f"🏷️ Category: {product.image}")    
    print(f"🏷️ start time: {product.start_time}")    
    print(f"🏷️ end time: {product.end_time}")    
    print("🔥 /submit received a request!")  
    main_system.save_bid_item( user_id, product.name , product.price , product.amount , product.category , product.image , product.start_time  , product.end_time )
    return Main(
        H1("✅ Bid Product Added Successfully!", 
           style="text-align: center; color: #222; background: #0074bd; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1);"),
           Script(
            """ 
            setTimeout(function(){
                window.location.href = '/';  }, 2000);
            """
        ),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px; display: flex; justify-content: center; align-items: center; color: #222;"
    )

serve()