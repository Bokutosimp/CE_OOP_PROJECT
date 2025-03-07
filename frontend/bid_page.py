from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def bid_page(id):
   try:
      bid_item = main_system.get_bid_item_by_id(id)
      return Div(
            Div(Img(src=bid_item.get_image), style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Div(
               Div(H2(bid_item.get_name, style="color:black; font-weight:600;"), style="width:100%; border-bottom:1px solid gray; margin-bottom:20px;"),
               Div(style="height:40px; width:100%; border-bottom:1px solid gray;"),
               Div(P(f"Current bids price ${bid_item.get_price}", style="color:black; font-size:30px; font-weight:bold;"), style="width:100%;"),
               Div(
                  Input(id="bid_input", style="width:flex; margin:0; text-align:center; border-radius:50px;", placeholder='Enter your bid'),
                   style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center;"),
               Button('Bid', style="width:100%; border-radius:50px;"),
               style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;"
               ),
            style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;")
   except:
      return Div("Item not found")