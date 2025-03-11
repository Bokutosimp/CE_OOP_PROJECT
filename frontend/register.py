from fasthtml.common import *
from typing import Literal
import uuid
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def register_form():
   return Div(
    Form(
        Input(type='text', id='name', placeholder='Full Name', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='email', id='email', placeholder='Email', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='text', id='phone_number', placeholder='Phone Number', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='text', id='username', placeholder='Username', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='password', id='password', placeholder='Password', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='date', id='birth_date', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Input(type='text', id='address', placeholder='Address', required=True, 
              style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'),

        Select(
            Option('Select Gender', value=''),
            Option('Female', value='F'),
            Option('Male', value='M'),
            id='gender', required=True, 
            style='height: 45px; width: 100%; outline: none; font-size: 16px; border-radius: 5px; padding-left: 15px; border: 1px solid #3498DB; transition: all 0.3s ease;'
        ),

        Button('Register', type='submit', 
               style='height: 45px; width: 100%; border-radius: 5px; border: none; background: #3498DB; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: all 0.3s ease, transform 0.2s ease-in-out;', 
               onmouseover="this.style.backgroundColor='#1E88E5'; this.style.transform='scale(1.05)';", 
               onmouseout="this.style.backgroundColor='#3498DB'; this.style.transform='scale(1)';"),

        Span('Already have an account? ', A('Log in', style='text-decoration:underline; color: #3498DB;', href='/login')),

        method='POST',
        action='/register',
        style='display:flex; flex-direction:column; justify-content:center; align-items:center; padding:20px; gap:10px; background-color: #fff; max-width: 700px; width: 100%; border-radius: 5px; box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);'
    ),
    style='display:flex; justify-content:center; align-items:center; height:100vh; background-color: #D6EAF8;'
)


def register_post(name:str,email:str,phone_number:str,username:str,password:str,birth_date:str,gender:Literal['M','F'],address,session):
   try:
      d,m,y= birth_date.split('-')[2],birth_date.split('-')[1],birth_date.split('-')[0]
      date = datetime.datetime(int(y),int(m),int(d))
   except:
      return Script('alert("Date format is incorrect"); window.location.href="/register"')
   try:
      result = main_system.create_customer(name,str(uuid.uuid4()),email,phone_number,username,password,date,gender,address)
      user = main_system.login(username,password)
      session['auth'] = user
      return Redirect('/')
   except (Exception,ValueError,KeyError) as e:
      return Script(f'alert("{str(e)}"); window.location.href="/register"')