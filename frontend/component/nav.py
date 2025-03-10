from fasthtml.common import *
from stylesheet import *
from fasthtml.svg import *

svg_cart = """<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16"><path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5M3.14 5l1.25 5h8.22l1.25-5zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0m9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0"/></svg>"""

def nav(session):
    guess_nav = Div(
        Div(
            A('Sign in', href='/login', style='text-decoration: none; color: #3498db; font-weight: bold; transition: color 0.3s;'),
            Span(' or '),
            A('register', href='/register', style='text-decoration: none; color: #3498db; font-weight: bold; transition: color 0.3s;')
        ),
        style='display: flex; justify-content: center; align-items: center; gap: 15px; padding: 15px 30px; background-color: #ecf0f1; border-radius: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);'
    )

    try:
        if 'auth' in session and session['auth']:
            if session['auth'][1] == 'Admin':
                login_nav = Div(
                    Div(A('logout', href='/logout', style="color: #e74c3c; text-decoration: none; font-weight: bold;"),
                        A('Product Management', href=f'/seller', style="color: #2ecc71; text-decoration: none; font-weight: bold;") if session['auth'][1] == 'Seller' else None,
                        A('History', href=f'/history', style="color: #2ecc71; text-decoration: none; font-weight: bold;"),
                        style="display: flex; gap: 20px; align-items: center;"),
                    A('Admin Panel', href='/admin', style="color: #3498db; text-decoration: none; font-weight: bold;"),
                    style='height: 25px; display: flex; justify-content: space-between; padding: 0 40px; align-items: center;'
                )
            else:
                login_nav = Div(
                    Div(A('logout', href='/logout', style="color: #e74c3c; text-decoration: none; font-weight: bold;"),
                        A('Product Management', href=f'/seller', cls='verticle_nav', style="color: #2ecc71; text-decoration: none; font-weight: bold;") if session['auth'][1] == 'Seller' else None,
                        A('History', href=f'/history', cls='verticle_nav', style="color: #2ecc71; text-decoration: none; font-weight: bold;"),
                        A('Profile', Svg(Path(d='M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0'),
                            Path(fill_rule='evenodd',d='M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1'),
                            xmlns="http://www.w3.org/2000/svg", width="16", height="16", fill="currentColor", cls="bi bi-person-circle", viewBox="0 0 16 16"), href='/profile', style="color: #3498db; text-decoration: none; font-weight: bold;"),
                        style="display: flex; gap: 20px; align-items: center;"),
                    A(Svg(Path(d='M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5M3.14 5l1.25 5h8.22l1.25-5zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0m9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0'),
                    viewBox='0 0 16 16', h='16', w='16', xmlns='http://www.w3.org/2000/svg', fill='currentColor'),
                    href='/cart', style="color: #3498db; text-decoration: none; font-weight: bold;"
                ),
                style='height: 25px; display: flex; justify-content: space-between; padding: 0 40px; align-items: center;'
            )
            render_nav = login_nav
        else:
            render_nav = guess_nav

    except KeyError:
        render_nav = guess_nav
    
    return Nav(
        render_nav,
        Div(
            A(Span('e', style="color: #e74c3c;"), Span('b', style="color: #3498db;"), Span('a', style="color: #f39c12;"), Span('y', style="color: #2ecc71;"), href='/', style="""text-decoration: none; font-size: 32px; font-weight: bold;"""),
            Div(P('Shop by', style="margin:0; color: #34495e;"), P('category', style="margin:0; color: #34495e;"), style=""),
            Form(
                Input(type='text', placeholder='Search', id="keyword",
                style="""border-radius: 30px; color: #34495e; width: 80%; border: solid 2px #3498db; height: 45px; margin-bottom: 0px; background: #fff; padding: 0 15px; font-size: 16px;""",),
                Button('Search', className="button", 
                    style="""background: #3498db; border-radius: 30px; color: white; height: 45px; padding: 0; width: 20%; margin-bottom: 0px; font-size: 16px; transition: background 0.3s;""",
                    type="submit"),
                method="GET",
                action="/search",
                style="width: 100%; display: flex; flex-direction: row; gap: 10px; margin-bottom: 0px;",
            ),
            Span('Advanced', style="font-size: 14px; font-weight: bold; color: #3498db;"),
            style="""display: flex; flex-direction: row; justify-content: space-between; align-items: center; padding: 20px 40px 20px 40px; gap: 10px; border-bottom: 1px solid #ddd; border-top: 1px solid #ddd;"""
        ),
        style="""width: 100%; display: flex; flex-direction: column; background-color: #f8f9fa;"""
    )
