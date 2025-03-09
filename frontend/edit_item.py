from fasthtml.common import *
from backend.system import main_system

load_category = main_system.get_categories()

def is_check(item_cat_list,cat_id):
   for cat in item_cat_list:
      if cat.get_id == cat_id:return True
   return False 

def edit_item(session,item_id:str):
   current_item = main_system.get_item_by_id(str(item_id))
   return Div(
            Form(
                H3("Edit Product"),
                Input(type="hidden", id="edit_item_id", name="edit_item_id",value=(current_item.get_id) , required='true'),  
                Input(type="text", id= "new_name" , name="new_name", placeholder="New Product Name",value=current_item.get_name,
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true'),
                 Details(
                        Summary("เลือกหมวดหมู่"), 
                            Div(
                                *[Label(
                                    Input(type="checkbox", id=f"cat-{cat.get_id}", value=cat.get_id,
                                          checked=f'{True if is_check(current_item.get_category,cat.get_id) else ''}', name="new_category",cls="checkbox"),
                                    cat.get_name
                                ) for cat in load_category],
                                style="display: flex; flex-direction: column; padding: 10px;", required='true'
                            ),
                            style="border: 1px solid #ccc; padding: 5px; width: 100%;"
                        ),
                Input(type="text", id = "new_detail" , name="new_detail", placeholder="New Detail",value='',
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"  ),
                Input(type="number", id= "new_price" , name="new_price", placeholder="New Price",value=current_item.get_price,
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true'),
                Input(type="text", id = "new_image", name="new_image", placeholder="New image",value=current_item.get_image,
                      style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" ),
                Button("Submit", type="submit", style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
                    style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
                    onsubmit="""
                        event.preventDefault();
                        const checkboxes = document.querySelectorAll('.checkbox');
                        const selected = Array.from(checkboxes).filter(checkbox => checkbox.checked);
                        console.log('Selected categories:', selected);
                        const cat_id_selected = selected.map(checkbox => checkbox.value);
                        const form = new FormData();
                        form.append('edit_item_id',document.getElementById("edit_item_id").value);
                        form.append('new_name',document.getElementById("new_name").value);
                        form.append('new_price',document.getElementById("new_price").value);
                        form.append('new_category', cat_id_selected);
                        form.append('new_detail', document.getElementById("new_detail").value || '');
                        form.append('new_image', document.getElementById("new_image").value || '');
                        console.log('Form data:', form);
                        form.forEach((value, key) => {
                                        console.log(`  ${key}:`, value);
                                    });

                        fetch('/edit_product', {method: "PATCH", body: form})
                        .then(data => {
                            alert("Product edited successfully!");
                            window.location.href = '/seller';
                        })
                        .catch(error => alert("Error: " + error));
                """,
            ),
            id="popup-edit",
            style="display: flex; justify-content: center; align-items: center;"
        )

def edit_bid_item(session, item_id: str):
    current_item = main_system.get_bid_item_by_id(item_id)
    print(f"{(current_item.get_end_time)} ,,,, {current_item.get_start_time}")
    return Div(
        Form(
            H3("Edit Bid Product"),
            Input(type="hidden", id="edit_bid_item_id", name="edit_bid_item_id", value=current_item.get_id),  
            Input(type="text", id="new_name", name="new_name", placeholder="New Product Name", value=current_item.get_name,
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;"),
            Details(
                Summary("เลือกหมวดหมู่"), 
                Div(
                    *[Label(
                        Input(type="checkbox", id=f"cat-{cat.get_id}", value=cat.get_id,
                              checked='checked' if is_check(current_item.get_category, cat.get_id) else '', 
                              name="new_category", cls="checkbox"),
                        cat.get_name
                    ) for cat in load_category],
                    style="display: flex; flex-direction: column; padding: 10px;"
                ),
                style="border: 1px solid #ccc; padding: 5px; width: 100%;"
            ),
            Input(type="text", id="new_detail", name="new_detail", placeholder="New Detail",
                  value='', 
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" ,),
            Input(type="number", id="new_start_price", name="new_start_price", placeholder="New Start Price",
                  value=current_item.get_price,
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true' ),
            Input(type="datetime-local", id="new_start_time", name="new_start_time", placeholder="Start time",
                  value=current_item.get_start_time,
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true' ),
            Input(type="datetime-local", id="new_end_time", name="new_end_time", placeholder="End time",
                  value=current_item.get_end_time,
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" , required='true' ),
            Input(type="text", id="new_image", name="new_image", placeholder="New Image",
                  value=current_item.get_image,
                  style="padding: 8px; border-radius: 5px; border: 1px solid #ccc; width: 100%;" ),
            Button("Submit", type="submit", 
                   style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            onsubmit="""
                event.preventDefault();
                const checkboxes = document.querySelectorAll('.checkbox');
                const selected = Array.from(checkboxes).filter(checkbox => checkbox.checked);
                const cat_id_selected = selected.map(checkbox => checkbox.value);
                const form = new FormData();
                form.append('edit_bid_item_id', document.getElementById("edit_bid_item_id").value);
                form.append('new_name', document.getElementById("new_name").value);
                form.append('new_start_price', document.getElementById("new_start_price").value);
                form.append('new_category', cat_id_selected);
                form.append('new_detail', document.getElementById("new_detail").value || '');
                form.append('new_start_time', document.getElementById("new_start_time").value);
                form.append('new_end_time', document.getElementById("new_end_time").value);
                form.append('new_image', document.getElementById("new_image").value || '');
                console.log('Form data:', form);
                console.log("🔹 Form Data (Detailed View):");
                form.forEach((value, key) => {
                    console.log(`  ${key}:`, value);
                });



                fetch('/edit_bid_product', { method: "PATCH", body: form })
                .then(response => {
                    console.log("🔹 Server Response Status:", response.status);  // ดู status code
                    return response.text();
                })
                .then(data => {
                    console.log("🔹 Server Response Data:", data);  // ดูข้อมูลที่เซิร์ฟเวอร์ส่งกลับมา
                    alert("Bid Product edited successfully!");
                    window.location.href = '/seller';
                })
                .catch(error => {
                    console.error("❌ Fetch Error:", error);  // ดู error ถ้ามีปัญหา
                    alert("Error: " + error);
                });
            """,
        ),
        id="popup-edit",
        style="display: flex; justify-content: center; align-items: center;"
    )
