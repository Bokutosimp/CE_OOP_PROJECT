from fasthtml.common import *
from mock.items import items

def review_page(id):
   try:
      item = [items[i] for i in range(len(items)) if items[i]['id'] == int(id)][0]
      return Div(
            Div(Img(src=item['image']),style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Div(
                Div(H2(item['name'],style="color:black; font-weight:600;"),style="width:100%; border-bottom:1px solid gray; margin-bottom:20px;"),
                Br(),
                Div(P("Review",style="color:black; font-size:20px;"),style="width:100%;"),
                Div(
                    Textarea(style="width:100%; height:200px; border-radius:15px;"),
                    style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center;"),
                Div("Rating",style="color:black; font-size:20px;"),
                Div(
                    Select(
                        Option("1",value=1),
                        Option("2",value=2),
                        Option("3",value=3),
                        Option("4",value=4),
                        Option("5",value=5),
                        style="width:100px; border-radius:50px;"),
                    ),
                Button('Submit',style="width:100%; border-radius:50px;"),
                style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;"
                ),
            Style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;",)
   except:
      return Div("Item not found")