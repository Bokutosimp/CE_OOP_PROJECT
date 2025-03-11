from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def login_form():
   return Form(
    Div('Sign in to your account', style='color:#3498DB; font-size:24px; font-weight:700; text-align:center;'),
    Span('New to eBay? ', A('Create account', href='/register', style='text-decoration:underline; color:#3498DB;')),
    
    Input(
        type='text', id='username', placeholder='Username',
        style='width:500px; height: 45px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; font-size: 16px; transition: all 0.3s ease;'
    ),
    
    Input(
        type='password', id='password', placeholder='Password',
        style='width:500px; height: 45px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; font-size: 16px; transition: all 0.3s ease;'
    ),
    
    Input(
        type='submit', value='Login',
        style='width:500px; height: 45px; border-radius: 5px; border: none; background: #3498DB; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: all 0.3s ease, transform 0.2s ease-in-out;',
        onmouseover="this.style.backgroundColor='#1E88E5'; this.style.transform='scale(1.05)';",
        onmouseout="this.style.backgroundColor='#3498DB'; this.style.transform='scale(1)';"
    ),

    action='/login',
    method='POST',
    style='display:flex; flex-direction:column; justify-content:center; align-items:center; padding: 50px; gap:15px ; border-radius: 10px; 5px 10px rgba(0, 0, 0, 0.15); max-width: 600px; margin: auto;'
)


def login_method(session,username:str,password:str):
   try:
      result = main_system.login(username,password)
      session['auth'] = result
      return Script(""" 
        alert('Login Successful');  
        window.location.href = '/';  
    """)
   except Exception as e:
      return Script(f""" 
        alert('{str(e)}');  
        window.location.href = '/login';
    """)