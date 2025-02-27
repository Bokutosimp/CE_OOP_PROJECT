from fasthtml.common import *

app, rt = fast_app()

@rt('/add') 
def get():
    return Container(
        Grid(
            H1("Add Item Management", style="text-align: center; margin-bottom: 20px; color: #F8F0FB;"),  
        ),
        Form(
            Label("Product Name:", Input(type="text", id="name", placeholder="Enter your product name", style="padding: 8px; border-radius: 5px; border: 1px solid #CAD5CA; width: 100%;")),
            Label("Price:", Input(type="number", id="price", placeholder="Enter your price", style="padding: 8px; border-radius: 5px; border: 1px solid #CAD5CA; width: 100%;")),
            Label("Description:", Textarea(id="description", rows=5, placeholder="...", style="padding: 8px; border-radius: 5px; border: 1px solid #CAD5CA; width: 100%;")),
            Label("Image:", Input(type="file", id="image", accept="image/*", style="padding: 8px; border-radius: 5px; border: 1px solid #CAD5CA; width: 100%;")), 
           
            Button("Submit", type="submit", 
                   style="background: #8075FF; color: white; border-radius: 5px; padding: 10px; border: none; cursor: pointer; width: 100%; font-weight: bold; transition: 0.3s;"),
            method="post",
            action="/submit",
            enctype="multipart/form-data",
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: #6320EE; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);"
        ),
        style="background-color: #211A1D; min-height: 100vh; padding: 20px; color: #F8F0FB;"
    )

@rt('/submit')
def post():
    return Main(
        H1("✅ เรียบร้อย! พวกเราชาวนิ่มได้เพิ่มสินค้าให้พวกคุณเรียบร้อยแล้ว", 
           style="text-align: center; color: #F8F0FB; background: #6320EE; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);"),
           style="background-color: #211A1D; min-height: 100vh; padding: 20px; display: flex; justify-content: center; align-items: center; color: #F8F0FB;"
    )
