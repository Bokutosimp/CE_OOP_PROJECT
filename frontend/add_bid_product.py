from fasthtml.common import *

app, rt = fast_app()

def add_bid_product_page(): 
    return Container(
        Grid(
            H1("Add Bid Item Management", style="text-align: center; margin-bottom: 20px; color: #222;"),  
        ),
        Form(
            Label("Bid Product Name:", Input(type="text", id="name", placeholder="Enter your product name", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Start Price:", Input(type="number", id="price", placeholder="Enter your price", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Description:", Textarea(id="description", rows=5, placeholder="Product description...", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Image:", Input(type="file", id="image", accept="image/*", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")), 
           
            Button("Submit", type="submit", 
                   style="background: #0074bd; color: white; border-radius: 5px; padding: 10px; border: none; cursor: pointer; width: 100%; font-weight: bold; transition: 0.3s;"),
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            action="/seller/add_bid/submit"
        ),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

@rt('/seller/add_bid/submit')
def post_bid():
    print("🔥 /submit received a request!")  
    return Main(
        H1("✅ Bid Product Added Successfully!", 
           style="text-align: center; color: #222; background: #0074bd; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1);"),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px; display: flex; justify-content: center; align-items: center; color: #222;"
    )

serve()