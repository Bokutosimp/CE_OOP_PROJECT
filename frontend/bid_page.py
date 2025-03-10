from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def bid_page(id):
   try:
      bid_item = main_system.get_bid_item_by_id(id)
      print(bid_item)
      return Div(
         Div(Img(src=bid_item.get_image), style="width: 500px; height: 500px; border-radius: 15px; overflow: hidden;"),
         Form(
            Div(H2(bid_item.get_name, style="color:black; font-weight:1000;"), style="width:100%; border-bottom: 2px solid black; padding-bottom:10px; margin-bottom:10px;"), 
            Div(
               P("Description:", style="color:black; font-size:30px; font-weight:bold;"),
               P(f"{bid_item.get_description}", style="color:black; font-size:20px;"), style="width:100%; border-bottom: 2px solid black; padding-bottom:10px; margin-bottom:10px;"),
            Div(P(f"Status : {bid_item.get_status}", style="color:black; font-size:30px; font-weight:bold;"), style="width:100%; text-align:center;"),
            Div(P(f"Current bid price: ${bid_item.get_price}", style="color:black; font-size:30px; font-weight:bold;"), style="width:100%; text-align:center;"),
            Div(
               P('Your Bid:', style="color:black; font-size:30px; font-weight:bold; text-align:center;"),
               Input(id="bid_input",
                     type='number',
                     min=round(bid_item.get_price + 0.1, 1),
                     step=0.1,
                     required=True,
                     style="width:500px; text-align:center; border-radius:50px; padding:10px; font-size:18px;", 
                     placeholder='Enter your bid'),
               Button('Place Bid', style="border-radius:50px; padding:12px 25px; font-size:18px; width:150px", type='submit'),
               style="display:flex; flex-direction:row; align-items:center; justify-content:center; gap:15px;"
            ),
            style="display:flex; flex-direction:column; gap:20px; width:50%; align-items:center;",
            action=f"/bid/submit?item_id={id}",
            method="post"
         ),
         style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;"
      )
   except:
      return Div("Item not found")


   
def submit_bid_page(bid_input: float, item_id: str, session):
   user_id, user_role = session['auth']
   print(f"Bid: {bid_input}, Item ID: {item_id}, User ID: {user_id}")
   main_system.set_top_bidder(item_id, bid_input, user_id)
   return Redirect(f"/bid/{item_id}")