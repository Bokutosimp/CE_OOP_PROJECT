from fasthtml.common import *
from typing import Literal
import uuid
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def register_form():
   return Form(
      Input(type='text',id='name',placeholder='name',required='true'),
      Input(type='email',id='email',placeholder='email',required='true'),
      Input(type='text',id='phone_number',placeholder='phone number',required='true'),
      Input(type='text',id='username',placeholder='username',required='true'),
      Input(type='password',id='password',placeholder='password',required='true'),
      Input(type='date',id='birth_date',required='true'),
      Input(type='text',id='address',placeholder='address',required='true'),
      Select(Option('select gender',value=''),Option('Female',value='F'),Option('Male',value='M'),id='gender',required='true'),
      Button('submit',type='submit'),
      Span('already have an account ',A('log in',style='text-decoration:underline;',href='/login')),
      method='POST',
      action='/register',
      style='''display:flex; flex-direction:column; justify-content:center; align-items:center; padding:20px 20%; gap:5px;''',
   )
   
def register_post(name:str,email:str,phone_number:str,username:str,password:str,birth_date:str,gender:Literal['M','F'],address,session):
   try:
      d,m,y= birth_date.split('-')[2],birth_date.split('-')[1],birth_date.split('-')[0]
      date = datetime.datetime(int(y),int(m),int(d))
   except:
      return Script('alert("date format is incorrect"); window.location.href="/register"')
   try:
      print('test')
      result = main_system.create_customer(name,uuid.uuid4(),email,phone_number,username,password,date,gender,address)
      user = main_system.login(username,password)
      session['auth'] = user
      return Redirect('/')
   except:
      return Script(f'alert({result}); window.location.href="/register"')