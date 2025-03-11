from fasthtml.common import *
from stylesheet import *
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def main_page():
    category_list = main_system.get_categories()
    return Container(
        Div(
            Div(
                P(f'{category_list[0].get_name}', style="color:#3498DB; font-weight:bold;"),
                H2('Everything you want and more', style="color:#3498DB;"),
                P('Choose from a vast selection of new fresh fruits.', style="color:#1C1C1C;"),
                A('Shop now fruits', className='button', href=f'/category/{category_list[0].get_id}',
                  style='background:#3498DB; color: white; border-radius: 50px; padding: 8px 12px; font-weight:bold;'),
                style="max-width:50%;"
            ),
            Div(style="width:400px; height:250px; background-image:url(https://img.freepik.com/free-photo/colorful-fruits-tasty-fresh-ripe-juicy-white-desk_179666-169.jpg); background-position:center; background-size:cover; border-radius:10px;"),
            style="background-color:#D6EAF8; border-radius:10px; padding:40px; display:flex; flex-direction:row; justify-content:space-between; align-items:center;"
        ),

        Div(
            H4('Trending on eBay', style="color:#3498DB; font-weight:bold;"),
            Div(
                *[
                    A(
                        Div(
                            Img(src='https://cdn.pixabay.com/photo/2016/07/07/16/46/dice-1502706_640.jpg', style='width:auto; height:75px; object-fit:cover;'),
                            style="border:solid 2px #3498DB; border-radius:50%; width:75px; height:75px; overflow:hidden; display:grid; place-items:center;"
                        ),
                        Div(f"{cat.get_name[:12] + '...' if len(cat.get_name) > 12 else cat.get_name}", style="color:#1C1C1C; font-size:14px; text-align:center; font-weight:bold;"),
                        style="display:flex; flex-direction:column; justify-content:center; align-items:center; min-width:110px; text-decoration:none;",
                        href=f'/category/{cat.get_id}'
                    )
                    for cat in category_list
                ],
                style="display:grid; grid-template-columns:repeat(10,1fr); gap:5px; overflow-x:scroll; scrollbar-color:#3498DB #D6EAF8; scroll-width:thin;"
            ),
            style="margin:20px; background:#D6EAF8; padding:20px; border-radius:10px;"
        ),

        Div(
            Div(
                P('REFURBISHED', style="color:#3498DB; font-weight:bold;"),
                H2('Save on your everyday ally', style="color:#3498DB;"),
                P('Choose from a vast selection of new tech.', style="color:#1C1C1C;"),
                Button('Shop smartphones', style="background:#3498DB; color:white; border-radius:50px; padding:10px 20px; font-weight:bold; cursor:pointer; border:none;")
            ),
            Div(style="width:400px; height:250px; background-image:url(https://www.go-globe.com/wp-content/uploads/2024/07/athletic-woman-using-her-smartphone.webp); background-position:center; background-size:cover; border-radius:10px;"),
            style="background-color:#D6EAF8; border-radius:10px; padding:40px; display:flex; flex-direction:row; justify-content:space-between; align-items:center;"
        ),

        Div(
            Div(
                H2('Shopping made easy', style="color:#3498DB;"),
                P('Enjoy reliable, secure deliveries and hassle-free returns.', style="color:#1C1C1C;")
            ),
            Form(
                Button('Start now', className="button", style="background:#3498DB; color:white; height:60px; border-radius:50px; padding:10px 20px; font-weight:bold; cursor:pointer; border:none;"),
                Input(type='hidden', value='', id='keyword'),
                method='get', action="/search"
            ),
            style="background-color:#D6EAF8; border-radius:10px; margin-top:20px; padding:20px 40px; display:flex; flex-direction:row; justify-content:space-between; align-items:center;"
        ),
    )
