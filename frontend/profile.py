from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def profile(session):
   user_id = session['auth'][0]
   user = main_system.get_user_by_id(user_id)
   return Div(
      Div(
      H2(f'{user.get_username}'),
      P(f'address: {user.get_address}'),
      P(f'birth date: {user.get_birth_date}'),
      P(f'email: {user.get_email}'),
      P(f'phone number: {user.get_phone_number}'),
      P(f'username: {user.get_name}'),
      style='display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); width:clamp(600px,100%,700px);'),
      Div(*[Div(
         Div(f'total price {item.get_order.get_total_price}'),
         Div(f'shipping date is {item.get_shipping_status.get_shipping_date}'),
         Div(f'get item date is {item.get_shipping_status.get_get_item_date}'),
         style='border-bottom:solid 1px #bdbcbb; display:flex; flex-direction:column; gap:4px; margin:10px auto; width:100%;'
         ) for item in user.get_order_history],style='display: flex; flex-direction: column; justify-content: space-between; padding: 15px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); width:clamp(500px,100%,700px); margin:15px;'),
      style='display:grid; grid-template-columns:repeat(auto-fill, minmax(500px, 1fr)) gap:20px; padding:20px; place-items:center;',
   )