from fasthtml.common import *

def nav():
    return Nav(
        A(Span('e',style="color:red"),Span('b',style="color:blue"),Span('a',style="color:yellow"),Span('y',style="color:green;"),href='/',style="""text-decoration:none; font-size:30px;"""),
        Div(P('Shop by',style="margin:0;"),P('category',style="margin:0;"),style=""),
        Form(
          Input(type='text',placeholder='Search',id="keyword",
          style="""border-radius:50px; color:black; width:80%; border:solid 3px black; height:45px; margin-bottom:0px; background:white;""",),
          Button('Search',style="""background:rgb(12, 18, 176); border-radius:50px; color:white; height:45px; padding:0; width:20%; margin-bottom:0px;""",type="submit"),
          method="GET",
          action="/search",
          style="width:100%; display:flex; flex-direction:row; gap:10px; margin-bottom:0px;",
        ),
         Span('Advanced'),
         style="""display:flex; flex-direction:row; justify-content:space-between; align-items:center; padding:20px 40px 20px 40px; gap:10px; border-bottom:1px solid black;"""
    )