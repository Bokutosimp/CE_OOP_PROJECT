from fasthtml.common import *
from backend.system import main_system

app, rt = fast_app()

@dataclass
class Discount_code :
    name : str
    discount_percentage : float
    detail : str

def add_discount_page(session):
    load_category = main_system.get_categories()  
    return Container(
        Grid(H1("Create Discount Code", style="text-align: center; margin-bottom: 20px; color: #0074bd;")),
         Form(
            Label("Code", Input(id="name", name="name", type="text", placeholder="Enter your product name" , required='true')),
            Label("Discount percentage", Input(id="discount_percentage", name="discount_percentage", type="number", min ='0' , max ='100',placeholder="Enter your Discount percentage" , step="0.01",  required='true')),
            Label("Description", Textarea(id="detail", name="detail", type="text", rows=5 , placeholder="Enter Description")),
            Button("Submit",type='submit'),
            style="display: flex; flex-direction: column; gap: 15px; width: 50%; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); color: #222;",
            onsubmit=f"""
                    event.preventDefault();
                    const form = new FormData();
                    form.append('name',document.getElementById("name").value) 
                    form.append('discount_percentage',document.getElementById("discount_percentage").value) 
                    form.append('detail',document.getElementById("detail").value) 
                    fetch('/seller/discount_code/submit', {{method: "POST", body: form}})
                    .then(response => console.log(response.text()))
                    .then(data => {{
                    alert("Discount code has been created");  
                    window.location.href = '/seller';  
                    }})
                    .catch(error => alert("Error: " + error));""",
        )
    )

def submit_discount_page( discount_code : Discount_code , session):
    try:
        user_id = session['auth'][0]
        print(f"User ID: {user_id}")
        print(f'{discount_code.name} , {discount_code.discount_percentage}')

        main_system.save_discount_code(discount_code.name , discount_code.discount_percentage , discount_code.detail )
        
        return Script(""" 
                alert('Discount code has been created');  
                window.location.href='/seller';""")
    except (Exception,ValueError, KeyError) as e:
        return Script(f""" alert('{str(e)}'); window.location.href='/seller/discount_code';""")