from fasthtml.common import *
from backend.system import *
from datetime import datetime

app, rt = fast_app()

@dataclass
class Bid_Product:
    name: str
    price: float
    amount: int
    category : str
    start_time : str
    end_time : str
    description: str
    image: str 

def add_bid_product_page(session): 
    load_category = main_system.get_categories()
    return Container(
        Grid(
            H1("Add Bid Item Management", style="text-align: center; margin-bottom: 20px; color: #0074bd;"),  
        ),
        Form( 
            Label("Bid Product Name:", Input(type="text", id="name", placeholder="Enter your product name", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true')),
            Label("Start Price:", Input(type="number", min='0'  , id="price",  step="0.01" ,placeholder="Enter your price", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true')),
            Label("Amount:", Input(id="amount", name="amount", type="number", placeholder="Enter your amount" , required='true')),
            Details(
                Summary("เลือกหมวดหมู่"), 
                Div(
                    *[Label(
                        Input(type="checkbox", id=f"cat-{cat.get_id}", value=cat.get_id, name="category",cls="checkbox") ,
                        cat.get_name
                    ) for cat in load_category],
                    style="display: flex; flex-direction: column; padding: 10px;"
                ),
                style="border: 1px solid #ccc; padding: 5px; width: 100%;"
            ),
            Label("Start Time", Input(type="datetime-local", id="start_time", placeholder="Enter end time", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;") ,),
            Label("End Time", Input(type="datetime-local", id="end_time", placeholder="Enter category", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" ) ,),
            Label("Description:", Textarea(id="description", rows=5, placeholder="Product description...", style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;")),
            Label("Image:", Input(type="text", id="image", placeholder="Enter your image url" , style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;") ), 

            Button("Submit", type="submit"),
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            onsubmit=f"""
                    event.preventDefault();
                    const checkboxes = document.querySelectorAll('.checkbox');
                    const selected = Array.from(checkboxes).filter(checkbox => checkbox.checked);
                    const cat_id_selected = selected.map(checkbox => checkbox.value)
                    const form = new FormData();
                    form.append('name',document.getElementById("name").value) 
                    form.append('price',document.getElementById("price").value) 
                    form.append('amount',document.getElementById("amount").value)
                    form.append('category',cat_id_selected)
                    form.append('start_time',document.getElementById("start_time").value )
                    form.append('end_time',document.getElementById("end_time").value )
                    form.append('description',document.getElementById("description").value | '')
                    form.append('image',document.getElementById("image").value | '')
                    fetch('/seller/add_bid/submit', {{method: "POST", body: form}})
                    .then(response => console.log(response.text()))
                   .then(data => {{
                    alert("Product added successfully!");  
                    window.location.href = '/seller';  
                    }})
                    .catch(error => alert("Error: " + error));""",
        ),
        style="background-color: #f7f7f7; min-height: 100vh; padding: 20px;"
    )

@rt("/seller/add_bid/submit", methods=["post"])
def submit_bid_product_page(product: Bid_Product, session):
        user_id = session['auth'][0] 
        start_time = datetime.strptime(product.start_time, "%Y-%m-%dT%H:%M")
        end_time = datetime.strptime(product.end_time, "%Y-%m-%dT%H:%M")
        
        main_system.save_bid_item(user_id, product.name, product.price, product.amount, product.category.split(','), product.image, start_time, end_time , product.description)

        return Script(""" alert('Add bid Product Successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")


serve()