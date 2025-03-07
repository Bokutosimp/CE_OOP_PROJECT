from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def login_form():
   return Form(
         Div('Sign in to your account',style='color:black; font-size:24px; font-weight:700;'),
         Span('New to ebay? ',A('Create account',href='/register',style='text-decoration:underline',)),
         Input(type='text',id='username',placeholder='Username',style='width:500px;'),
         Input(type='text',id='password',placeholder='Password',style='width:500px;'),
         Input(type='submit',value='Login',style='width:500px;'),
         action='/login',
         method='POST',
         style='''display:flex; flex-direction:column; justify-content:center; align-items:center; padding: 50px; gap:15px;''')

def login_method(session,username:str,password:str):
   result = main_system.login(username,password)
   if result == None:
      return Script("alert('Invalid username or password'); window.location.href = '/login';")
   else:
      session['auth'] = result
      return Redirect('/')