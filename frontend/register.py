from fasthtml.common import *
from typing import Literal
import uuid
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def register_form():
   return Form(
      Input(type='text',id='name',placeholder='name'),
      Input(type='email',id='email',placeholder='email'),
      Input(type='text',id='phone_number',placeholder='phone number'),
      Input(type='text',id='username',placeholder='username'),
      Input(type='password',id='password',placeholder='password'),
      Input(type='date',id='birth_date'),
      Input(type='text',id='address',placeholder='address'),
      Select(Option('Female',value='F'),Option('Male',value='M'),id='gender'),
      Button('submit',type='submit'),
      method='POST',
      action='/register',
   )
   
def register_post(name:str,email:str,phone_number:str,username:str,password:str,birth_date:str,gender:Literal['M','F'],address,session):
   try:
      d,m,y= birth_date.split('-')[2],birth_date.split('-')[1],birth_date.split('-')[0]
      date = datetime.datetime(int(y),int(m),int(d))
   except:
      raise Exception('birth date format incorrect')
   try:
      print('test')
      result = main_system.create_customer(name,uuid.uuid4(),email,phone_number,username,password,date,gender,address)
      user = main_system.login(username,password)
      session['auth'] = user
      return Redirect('/')
   except:
      return Script(f'alert({result}); window.location.href="/register"')