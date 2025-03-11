from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def profile_page(session):
   user_id = session['auth'][0]
   user = main_system.get_user_by_id(user_id)
   
   order_history = main_system.get_shipping_items(user_id)
   order_history_div = None

   if order_history:
       order_history_div = Div(
    H3('Shipping Status', style='color: black;'),
    Div(
        *[
            Div(
          Div(f'Total Price: {order.get_order.get_total_price}', style='color: black;'),
      Div(f'Shipping Date: {order.get_shipping_status.get_shipping_date}', style='color: black;'),
                     Div(f'Item Received Date: {order.get_shipping_status.get_get_item_date}', style='color: black;'),
         Div(
                    *[
             Div(
                 Img(src=item.get_item.get_image, style="width: 100px; height: auto; border-radius: 5px;"),
                            H3(item.get_item.get_name, style="text-align: center; font-size: 1rem; , color : black"),
                            style='display: flex; flex-direction: column; align-items: center; padding: 5px;'
                        )
                   for item in order.get_order.get_list_item_select
                    ],
         style='display: flex; flex-direction: row; gap: 10px; overflow-x: auto; padding: 10px;'
                ),
                style='border-bottom: solid 1px #ddd; padding: 10px 0; display: flex; flex-direction: column; gap: 5px; background: #ffebd6ff;'
            )
            for order in order_history
        ],
        style='display: flex; flex-direction: column; gap: 15px; padding: 15px; background: #ffebd6ff; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); width: clamp(500px, 100%, 700px); margin: 20px auto;'
    ),
    style='display: flex; flex-direction: column; justify-content: center; align-items: center; background: #eaf4f4ff;'
)

   
   return Main(
Div( 
      Div(
          H2(f'Profile', style='color: black; text-shadow: 0 0 10px rgba(0, 0,0, 0.2);') ,
         Div(
            Div(
               Img(src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKsAAACUCAMAAADbGilTAAAAY1BMVEUAAAD////7+/sEBAT39/cICAjz8/Pk5OS9vb3p6emxsbFXV1cfHx+Pj4/ExMSDg4NiYmJAQEC3t7eqqqrPz89tbW13d3eioqJHR0eampotLS3d3d03NzcREREyMjJSUlImJiaVTqGeAAAEiElEQVR4nO2c63KqMBCAczOIXBVEEam+/1OeIG2PimLIhg3nTL5/LZ3pNzsh2Ww2EOLxeDwej8fj8Xg8Ho/HY5n2uo3yfX7ZXlvXKu/gXGlGVVFK+oMsiypq+0cL45SlIX0mTJMv12IDzgcpGXtWVb9h8rAg2xUhx80govfsjre/WgKrJKBMvDUVjAbJIlQ5+SpHg9pTfpEFvGL79xG9G7hU7B17qlDVgg5eqZeysiaOQ5tomfa2iUNPTlY1HU5U71wZrVfOIstJInRNb7YicTcKIjHJVTAZuRFdkS/52e85tCc3i0Kbar9Xv6o0dZN9ZVNNb7aZC9VtYKCqMq8tuiknhZEqpQX2XKD+3eTB2sMo/vJ1MHY9IJuS03APoEtwQnbNdLKr14gKV7XdGauqbQLucrBtAK4N5rTFSQ5QpTRHnAlUggVyxU231oYzVgeja0RTQiDDVQ1YVNfp2eA9ElOVg1QpxRyuMdA19q7eFdG1BbqibrrMs6wOgalKzLPXjhDVNQW5pqi5Sw3KB2o00851D3CldI+aZx1DQFyDI6KpmrTWgLCuketEiXlcBXbNeGs+a2FXicxLRPhFIk5O1GztYvSE7boyXg5SskIvxBuOWAc1TdJV30xAr7zdiAODGnyAmbr+siLH6XMsOzo52+C8WxAmnW9Rlrjr0thMdN048ryV0qeVNnduT4932kuC6FQdwkmsn3CtY+ftDnrnxww9u3oBJ5XOoVxQOQ/q7WXZ7igbaSPoHu22rpsyepTDpRkbB6y5LMP0uwcvSxkdTLa3pYKlGVlYo168LyR90lU/yGLvJAMYoQ9bXgTyd1ZgQgZFfnvo1u0tcZ7Vh6IoDnWWLy2gj/DHJAp/A+Dx/L9wNX/dWOxU9U/SxtfrOcqj8/UaL7Zpn5BTVNXr5u82QTTrQxVhN7docM125WMhpl9rw3KXXV3L/dC9QW1VypH8VZZVSxaRFrR58fmEXha529H7nbgK+qm5uHssnKex+eiG4Mm4yd2Jkn35MaSPwS1dNe4fNwa1tw3uedE3Sagf07vYhsh1AvWGRDoXS15TXnBfsSQAnHEihpZ3tUwYG7RLEVEDOjnult8G6aJBFQJVO9kQpQk2g/W8/SARmvcPw1KQCQzh9Mi0pfyV7cyy9djFwmmImXtJpp27fGLWc5nazlj96zpXZDmkF+Ot7kzt0NWLi8VQVTbHZQOVrcCXgBeyNIxmiKzZFajPBPZ3jbvp2aomdo8TVboJuP/yCZHZzGc5OcMaM0dh4dnqKDDfBehQWjQl1ayqlFqbuNQIgOxYdAjsjQK7acCQLjGw5JrL2V2lrZIMpH9Ul9SO6hFBlVIb7XBczVczv1m0GwWljRF7sZ9evXC1c90fWrfQxcIe4ThXfvWMhY7zDEmVUmDBgM+dCdzTwBJZtbwiTAI9jMIWWuhF2GnUwGkLbwiAU8OznUKbHvIMcp1x6zIE+N0PrIWgB7QcxJjDVQ1Y8y4pTi5Yi1aPWrpMZwKu9x0vewjzS2gccYHtyQAzLOZK0AE4+FpBvuBhwvhXP/4ARPk50MLrd+0AAAAASUVORK5CYII=',
               style='border-radius: 50%; width: 50px; height: 50px; margin-right: 20px;'),
                  H2(f'{user.get_username}', style='color: black;'), style= "display : flex ; align-items : center"
            ),
            P(f'Address: {user.get_address}', style='color: black;'),
            P(f'Birth Date: {user.get_birth_date}', style='color: black;'),
            P(f'Email: {user.get_email}', style='color: black;'),
            P(f'Phone Number: {user.get_phone_number}', style='color: black;'),
            P(f'Username: {user.get_name}', style='color: black;'),
            style='display: flex; flex-direction: column; gap: 10px; padding: 20px; background: #eae4f1ff; border-radius: 10px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); width: clamp(600px, 100%, 700px);'
         ),
         style=' margin: 20px auto; display: flex; flex-direction: column; gap: 20px; justify-content: center; align-items: center;'
         
      ), 
      order_history_div 
   )

   )
