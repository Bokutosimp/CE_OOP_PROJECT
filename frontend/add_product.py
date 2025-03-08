from fasthtml.common import *
from backend.system import main_system

app, rt = fast_app()

@dataclass
class Product:
    name: str
    price: float
    amount: int
    category: list
    description: str
    image: str 

@rt("/seller/add")
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
                        Input(type="checkbox", id=f"cat-{cat.get_id}", value=cat.get_id, name="category"),
                        cat.get_name
                    ) for cat in load_category],
                    style="display: flex; flex-direction: column; padding: 10px;"
                ),
                style="border: 1px solid #ccc; padding: 5px; width: 100%;"
            ),
            Label("Description:", Textarea(id="description", name="description", rows=5, placeholder="Product description...")),
            Label("Image:", Input(id="image", name="image", type="text", placeholder="Enter your image url")),
            Button("Submit", type="submit"),
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            action=f"/seller/add/submit",
            method="post"
        ) , Script("""
            document.querySelector("form").addEventListener("submit", function(event) {
                event.preventDefault();  // ป้องกันการ submit แบบปกติ

                // สร้าง Array สำหรับเก็บ ID ของหมวดหมู่ที่เลือก
                let selectedCategories = [];

                // ตรวจสอบทุก checkbox ว่าถูกเลือกหรือไม่
                document.querySelectorAll('input[name="category"]:checked').forEach(function(checkbox) {
                    selectedCategories.push(checkbox.value);  // เพิ่ม ID ของหมวดหมู่ที่เลือก
                });

                // ถ้าไม่ได้เลือกหมวดหมู่
                if (selectedCategories.length === 0) {
                    alert('Please select at least one category');
                    return;
                }

                // ส่งค่าหมวดหมู่ที่เลือกไปที่ backend ด้วย AJAX
                fetch('/seller/add/submit', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',  // ระบุ Content-Type เป็น JSON
                    },
                    body: JSON.stringify({
                        categories: selectedCategories  // ส่งค่าหมวดหมู่ที่เลือก
                    })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Product added successfully');
                        window.location.href = '/seller';
                    } else {
                        alert('Error adding product');
                    }
                })
                .catch(error => {
                    alert('An error occurred');
                    console.error(error);
                });
            });
        """)
    )

@rt("/seller/add/submit", methods=["post"])
async def submit_product_page( request : Request , product: Product, session):
    user_id = session['auth'][0]
    print(f"User ID: {user_id}")

    data = await request.json()  
    categories = data.get('categories') 
    print(categories)
    
    # ตรวจสอบว่าได้รับค่าหมวดหมู่หรือไม่
    if not product.category:
        return Script(""" alert('Please select at least one category'); setTimeout(function(){ window.location.href = '/seller ';  });""")
    
    print(f"📦 Product Name: {product.name}")
    print(f"💰 Price: {product.price}")
    print(f"🏷️ Category: {product.category}")    
    print(f"🖼️ Image: {product.image}")    

    # บันทึกสินค้าที่เลือกหมวดหมู่
    main_system.save_item(user_id, product.name, product.price, product.amount, product.category, product.image)
    
    return Script(""" alert('Add Product Successfully'); setTimeout(function(){ window.location.href = '/seller ';  });""")