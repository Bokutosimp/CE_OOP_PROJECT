from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def login_form():
   return Form(
         Input(type='text',id='username',placeholder='Username'),
         Input(type='text',id='password',placeholder='Password'),
         Input(type='submit',value='Login'),
         action='/login',
         method='POST',)

def login_method(session,username:str,password:str):
   result = main_system.login(username,password)
   if result == None:
      return Script("alert('Invalid username or password'); window.location.href = '/login';")
   else:
      session['auth'] = result
      return Redirect('/')