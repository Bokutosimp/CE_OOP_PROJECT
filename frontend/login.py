from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def login_form():
   return Form(
      Input(type='text',id='username',placeholder='Username'),
      Input(type='text',id='password',placeholder='Password'),
      Input(type='submit',value='Login'),
      action='/login',
      method='POST',
   )

def login_method(session,username:str,password:str):
   result = main_system.login(username,password)
   print(result)
   if result == None:
      return Script("alert('Invalid username or password'); window.location.href = '/login';")
   else:
      session.setdefault('user_id',result[0])
      session.setdefault('user_role',result[1])
      return Div(f'hello wolrd, {session['user_id']},{session['user_role']}')
      