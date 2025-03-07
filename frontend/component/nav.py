from fasthtml.common import *
from stylesheet import *
from fasthtml.svg import *

svg_cart = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16"><path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5M3.14 5l1.25 5h8.22l1.25-5zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0m9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0"/></svg>"""

def nav(session):
    guess_nav = Div(
        Div(
            A('Sign in', href='/login', style='text-decoration:underline;'),
            Span(' or '),
            A('register', href='/register', style='text-decoration:underline;')
        ),
        A(Svg(Path(d='M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5M3.14 5l1.25 5h8.22l1.25-5zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0m9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0'),
            viewBox='0 0 16 16', h='16', w='16', xmlns='http://www.w3.org/2000/sv', fill='currentColor'),
        href='/login'
    ),
    style='height:25px; display:flex; justify-content:space-between; padding:0 40px;'
    )
    try:
        if 'auth' in session and session['auth']:
            login_nav = Div(
                Div(A('logout', href='logout'), 
                    A('product management', href=f'/seller?user_id={session['auth'][0]}') if session['auth'][1] == 'Seller' else None,
                    A('History', href=f'/history?user_id={session['auth'][0]}') ,
                    style="display:flex; gap:10px;"),
                A(Svg(Path(d='M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5M3.14 5l1.25 5h8.22l1.25-5zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0m9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0'),
                viewBox='0 0 16 16', h='16', w='16', xmlns='http://www.w3.org/2000/sv', fill='currentColor'),
                href='/cart'
            ),
            style='height:25px; display:flex; justify-content:space-between; padding:0 40px;'
            )
            render_nav = login_nav 
        else:
            render_nav = guess_nav

    except KeyError:
        render_nav = guess_nav
      
    return Nav(
      render_nav,
      Div(
        A(Span('e',style="color:red"),Span('b',style="color:blue"),Span('a',style="color:yellow"),Span('y',style="color:green;"),href='/',style="""text-decoration:none; font-size:30px;"""),
        Div(P('Shop by',style="margin:0;"),P('category',style="margin:0;"),style=""),
        Form(
          Input(type='text',placeholder='Search',id="keyword",
          style="""border-radius:50px; color:black; width:80%; border:solid 3px black; height:45px; margin-bottom:0px; background:white;""",),
          Button('Search', className = "button",style="""background:rgb(12, 18, 176); border-radius:50px; color:white; height:45px; padding:0; width:20%; margin-bottom:0px;""",type="submit"),
          method="GET",
          action="/search",
          style="width:100%; display:flex; flex-direction:row; gap:10px; margin-bottom:0px;",
        ),
         Span('Advanced' ),
         style="""display:flex; flex-direction:row; justify-content:space-between; align-items:center; padding:20px 40px 20px 40px; gap:10px; border-bottom:1px solid black; border-top:1px solid black; """
      ),style="""width:100%; display:flex; flex-direction:column;"""
    )