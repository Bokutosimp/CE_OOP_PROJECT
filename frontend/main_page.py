from fasthtml.common import *

def main_page():
   return Container(
        Div(Div(P('ELECTRONICS',style="""color:rgb(0, 0, 0);"""),
            H2('Everything you want and more',style="""color:rgb(0, 0, 0);"""),
            P('Choose from a vast selection of new tech.',style="""color:rgb(0, 0, 0);"""),
            Button('Shop now electronics',style="""background:rgb(0,0,0); border-radius:50px;"""),
            style=""""""),
            Div(style="""border:solid black 1px; width:400px; height: 250px;"""),
            style="""background-color:#CAD5CA; border-radius: 10px;padding:40px; display:flex; flex-direction:row; justify-content:space-between;"""),
        Div(H4('Trending on eBay',style="""color:black;"""),Div(Div(Div(style="""border:solid 1px black; border-radius:50%; width:75px; height: 75px;"""),Span("Item1"),style="""display:flex; flex-direction:column; justify-content:center; align-items:center;"""),
        style="""display:flex; flex-direction:row;"""),style="""margin:20px; """),
        Div(Div(P('REFURBISHED',style="""color:rgb(0, 0, 0);"""),
            H2('Save on your every day ally',style="""color:rgb(0, 0, 0);"""),
            P('Choose from a vast selection of new tech.',style="""color:rgb(0, 0, 0);"""),
            Button('Shop smartphones',style="""background:rgb(0,0,0); border-radius:50px;""")),
            Div(style="""border:solid black 1px; width:400px; height: 250px;"""),style="""background-color:#CAD5CA; border-radius: 10px;padding:40px; display:flex; flex-direction:row; justify-content:space-between;"""),
        Div(Div(H2('Shopping made easy',style="""color:rgb(0, 0, 0);"""),
                      P('Enjoy reliable, secure deliveries and hassle-free returns.',style="""color:rgb(0, 0, 0);""")),
                  Button('Start now',style="""background:black; height:60px; border-radius:40px;"""),
                  style="""background-color:#CAD5CA; border-radius:10px; margin-top:20px; padding:20px 40px 20px 40px; display:flex; flex-direction:row; justify-content:space-between; align-items:center;"""),
    )