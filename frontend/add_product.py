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

def add_product_page(session):
    load_category = main_system.get_categories()
    # แสดงค่า ID ของแต่ละหมวดหมู่ที่โหลดมา
    for cate in load_category:
        print(cate.get_id)  
    return Container(
        Grid(H1("Add Item Management", style="text-align: center; margin-bottom: 20px; color: #0074bd;")),
         Form(
            Label("Product Name:", Input(id="name", name="name", type="text", placeholder="Enter your product name")),
            Label("Price:", Input(id="price", name="price", type="number", placeholder="Enter your price")),
            Label("Amount:", Input(id="amount", name="amount", type="number", placeholder="Enter your amount")),
            Details(
                Summary("เลือกหมวดหมู่"), 
                Div(
                    *[Label(
                        Input(type="checkbox", id=f"cat-{cat.get_id}", value=cat.get_id, name="category",cls="checkbox"),
                        cat.get_name
                    ) for cat in load_category],
                    style="display: flex; flex-direction: column; padding: 10px;"
                ),
                style="border: 1px solid #ccc; padding: 5px; width: 100%;"
            ),
            Label("Description:", Textarea(id="description", name="description", rows=5, placeholder="Product description...")),
            Label("Image:", Input(id="image", name="image", type="text", placeholder="Enter your image url")),
            Button("Submit",type='submit'),
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
                    form.append('description',document.getElementById("description").value | '')
                    form.append('image',document.getElementById("image").value | '')
                    fetch('/seller/add/submit', {{method: "POST", body: form}})
                    .then(data => {{
                    alert("Product added successfully!");  
                    window.location.href = '/seller';  
                    }})
                    .catch(error => alert("Error: " + error));""",
        )
    )

def submit_product_page( product: Product, session):
    try:
        user_id = session['auth'][0]
        print(f"User ID: {user_id}")
        print(f"📦 Product Name: {product.name}")
        print(f"💰 Price: {product.price}")
        print(f"🏷️ Category: {product.category.split(',')}")    
        print(f"🖼️ Image: {product.image}")    
        result = main_system.save_item(user_id, product.name, product.price, product.amount, product.category.split(','), product.image)
    
    except (Exception,ValueError, KeyError) as e:
        return Script(f""" alert('{str(e)}'); window.location.href='/seller/add';""")