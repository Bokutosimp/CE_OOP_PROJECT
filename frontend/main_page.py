from fasthtml.common import *
from stylesheet import *
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def main_page():
    category_list = main_system.get_categories()
    return Container(
        Div(
    Div(
        Div(
            P(f'{category_list[0].get_name}', style="color:rgb(0, 0, 0);"),
            H2('Everything you want and more', style="color:rgb(0, 0, 0);"),
            P('Choose from a vast selection of new fresh fruits.', style="color:rgb(0, 0, 0);"),
            A('Shop now fruits', className='button', href=f'/category/{category_list[0].get_id}', style='background:rgb(0,0,0);color: white; border-radius: 50px; padding: 8px 12px;'),
            style="flex:1;"
        ),
        Div(style="width:400px; height: 250px; background-image:url(https://img.freepik.com/free-photo/colorful-fruits-tasty-fresh-ripe-juicy-white-desk_179666-169.jpg); background-position:center; background-size:cover;"),
        className="slide"
    ),
    Div(
        Div(
            P(f'{category_list[1].get_name}', style="color:rgb(0, 0, 0);"),
            H2('Discover More Freshness', style="color:rgb(0, 0, 0);"),
            P('Find high-quality and exotic fruits.', style="color:rgb(0, 0, 0);"),
            A('Explore More', className='button', href=f'/category/{category_list[1].get_id}', style='background:rgb(0,0,0);color: white; border-radius: 50px; padding: 8px 12px;'),
            style="flex:1;"
        ),
        Div(style="width:400px; height: 250px; background-image:url(https://img.freepik.com/free-photo/fresh-tropical-fruits-wooden-table_1150-18449.jpg); background-position:center; background-size:cover;"),
        className="slide"
    ),
    className="slider-container"
),
Button("❮", id="prev", className="slider-btn"),
Button("❯", id="next", className="slider-btn"),
Script("""
    let index = 0;
    function showSlide(step) {
        let slides = document.querySelectorAll('.slide');
        index = (index + step + slides.length) % slides.length;
        document.querySelector('.slider-container').style.transform = `translateX(${-index * 100}%)`;
    }
    document.getElementById('prev').addEventListener('click', () => showSlide(-1));
    document.getElementById('next').addEventListener('click', () => showSlide(1));
"""),
Style("""
    .slider-container {
        display: flex;
        width: 100%;
        overflow: hidden;
        transition: transform 0.5s ease-in-out;
    }
    .slide {
        min-width: 100%;
        display: flex;
        justify-content: space-between;
        background-color: var(--lavender-web-2);
        border-radius: 10px;
        padding: 40px;
    }
    .slider-btn {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background: rgba(0,0,0,0.5);
        color: white;
        border: none;
        cursor: pointer;
        font-size: 24px;
        padding: 10px;
        border-radius: 50%;
    }
    #prev { left: 10px; }
    #next { right: 10px; }
""")
,
        Div(H4('Trending on eBay',style="""color:black;"""),
            Div(
            *[A(Div(Img(src='https://cdn.pixabay.com/photo/2016/07/07/16/46/dice-1502706_640.jpg',style='width:auto; height:75px; object-fit:cover;'),
                    style="""border:solid 1px black; border-radius:50%; width:75px; height: 75px; overflow:hidden; display:grid; place-items:center;"""),
                Div(f"{cat.get_name [:12] + '...' if len(cat.get_name ) > 12 else cat.get_name }"),
                style="""display:flex; flex-direction:column; justify-content:center; align-items:center; min-width:110px;""",href=f'/category/{cat.get_id}')
              for cat in category_list],style="display:grid; grid-template-columns:repeat(10,1fr); gap:5px; overflow-x:scroll; scrollbar-color:black var(--lavender-web); scroll-width:thin;"
            ),style="""margin:20px; """),
        Div(Div(P('REFURBISHED',style="""color:rgb(0, 0, 0);"""),
            H2('Save on your every day ally',style="""color:rgb(0, 0, 0);"""),
            P('Choose from a vast selection of new tech.',style="""color:rgb(0, 0, 0);"""),
            Button('Shop smartphones',style="""background:rgb(0,0,0); border-radius:50px;""")),
            Div(style="""width:400px; height: 250px; background-image:url(https://www.go-globe.com/wp-content/uploads/2024/07/athletic-woman-using-her-smartphone.webp);background-position:center; background-size:cover;"""),
            style="""background-color:var(--lavender-web-2); border-radius: 10px;padding:40px; display:flex; flex-direction:row; justify-content:space-between;"""),
        Div(Div(H2('Shopping made easy',style="""color:rgb(0, 0, 0);"""),
                      P('Enjoy reliable, secure deliveries and hassle-free returns.',style="""color:rgb(0, 0, 0);""")),
                  Form(Button('Start now',className = "button ",style="height:60px"),
                    Input(type='hidden',value='',id='keyword'),
                    method='get',action="/search"),
                  style="""background-color:var(--lavender-web-2); border-radius:10px; margin-top:20px; padding:20px 40px 20px 40px; display:flex; flex-direction:row; justify-content:space-between; align-items:center;"""),
    )