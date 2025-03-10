from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def bid_page(id):
    try:
        bid_item = main_system.get_bid_item_by_id(id)
        print(bid_item)
        return Div(
            Div(Img(src=bid_item.get_image), style="width: 500px; height: 500px; border-radius: 15px; margin-left: 2%; overflow: hidden; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); transition: transform 0.3s;"),
            Form(
                Div(H2(bid_item.get_name, style="color:#333; font-weight:900; font-size: 40px; text-align:center; margin-bottom: 20px; font-family: 'Arial', sans-serif;"), 
                    style="width:100%; border-bottom: 3px solid #ced9f3; padding-bottom:15px; margin-bottom:25px;"), 
                Div(
                    P("Description:", style="color:#333; font-size:26px; font-weight:bold; margin-bottom: 12px;"),
                    P(f"{bid_item.get_description}", style="color:#333; font-size:20px; line-height: 1.8; margin-bottom: 20px;"),
                    style="width:100%; border-bottom: 2px solid #ced9f3; padding-bottom:15px; margin-bottom:20px;"
                ),
                Div(P(f"Status: {bid_item.get_status}", style="color:#333; font-size:26px; font-weight:bold; text-align:center; margin-bottom:20px;"),
                    style="width:100%;"),
                Div(P(f"Current Bid Price: ${bid_item.get_price}", style="color:#333; font-size:26px; font-weight:bold; text-align:center; margin-bottom:25px;"),
                    style="width:100%;"),
                Div(
                    P('Your Bid:', style="color:#333; font-size:26px; font-weight:bold; text-align:center; margin-bottom:20px;"),
                    Input(id="bid_input",
                          type='number',
                          step=0.01,
                          required=True,
                          style="width:500px; padding:12px; font-size:18px; border-radius:30px; border:2px solid #ced9f3; text-align:center; margin-bottom:20px; transition: border-color 0.3s;", 
                          placeholder='Enter your bid',
                          onfocus="this.style.borderColor='#4CAF50';", onblur="this.style.borderColor='#ced9f3';"),
                    Button('Place Bid', style="border-radius:30px; padding:15px 30px; font-size:20px; background-color: #4CAF50; color:white; border:none; width:180px; cursor:pointer; transition: background-color 0.3s;",
                           type='submit', onmouseover="this.style.backgroundColor='#45a049';", onmouseout="this.style.backgroundColor='#4CAF50';"),
                    style="display:flex; flex-direction:column; align-items:center; gap:20px;"
                ),
                style="display:flex; flex-direction:column; align-items:center; gap:40px; width:60%; margin:auto;",
                action=f"/bid/submit?item_id={id}",
                method="post"
            ),
            style="display:flex; flex-direction:row; justify-content:center; padding:50px 0; background-color: #eaf4f4; gap:40px; box-sizing:border-box; transition: background-color 0.3s;"
        )
    except:
        return Div("Item not found", style="text-align:center; color:red; font-size:24px; font-weight:bold;")

def submit_bid_page(bid_input: float, item_id: str, session):
    bid_item = main_system.get_bid_item_by_id(item_id)
    if bid_item.get_status != "Started":
        return Redirect(f"/bid/{item_id}")
    user_id, user_role = session['auth']
    print(f"Bid: {bid_input}, Item ID: {item_id}, User ID: {user_id}")
    main_system.set_top_bidder(item_id, bid_input, user_id)
    return Redirect(f"/bid/{item_id}")
