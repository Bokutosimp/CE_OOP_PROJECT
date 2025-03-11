from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def auction_end():
    return Div(
                P("Auction Ended", style="color: red; font-size: 24px; font-weight: bold;"),
                A(Button("Back", type='button', style="font-size: 16px; padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 25px; cursor: pointer;"),href="/"
                )
            )

def bid_page(id, session):
    try:
        bid_item = main_system.get_bid_item_by_id(id)
        status = main_system.bid_status(bid_item)
        if status == "Sold":
            return auction_end()
        if status == "Ended":
            main_system.end_bid(bid_item)
            return auction_end()
        user_id = session['auth'][0]
        user = main_system.get_user_by_id(user_id)
        print(f"{bid_item.get_name}\n{bid_item.get_status}\n{bid_item.get_start_time}\n{bid_item.get_end_time}")
        return Div(
    Meta(http_equiv="refresh", content="5"), 
    Div(
        Div(
            Img(src=bid_item.get_image), 
            style="width: 450px; height: 450px; border-radius: 15px; overflow: hidden; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); margin-right: 50px;"
        ),
        
        Div(
            Form(
                Div(
                    H2(bid_item.get_name, style="color: #3498DB; font-weight: bold; font-size:40px; text-align:left; margin-bottom: 15px;"),
                    style="border-bottom: 3px solid #85C1E9; padding-bottom:10px; margin-bottom:5px;"
                ),
                
                Div(
                    P("Description:", style="color:#1C1C1C; font-size:24px; font-weight:bold;"),
                    P(f"{bid_item.get_description}", style="color:#1C1C1C; font-size:20px;"),
                    style="width:100%; border-bottom: 3px solid #85C1E9; padding-bottom:15px; margin-bottom:5px;"
                ),
                
                Div(
                    P(f"Status : {bid_item.get_status}", style="color:#1C1C1C; font-size:24px; font-weight:bold;"),
                    style="width:100%; text-align:left; margin-bottom:5px;"
                ),
                
                Div(
                    P(f"Current bid price: ${bid_item.get_price}", style="color:#1C1C1C; font-size:24px; font-weight:bold;"),
                    style="width:100%; text-align:left; margin-bottom:5px;"
                ),
                Div(
                    P(f"Start-time: {bid_item.get_start_time.strftime('%Y-%m-%d %H:%M:%S')}", style="color:#1C1C1C; font-size:24px; font-weight:bold;"),
                    style="width:100%; text-align:left; margin-bottom:5px;"
                ),
                Div(
                    P(f"End-time: {bid_item.get_end_time.strftime('%Y-%m-%d %H:%M:%S')}", style="color:#1C1C1C; font-size:24px; font-weight:bold;"),
                    style="width:100%; text-align:left;"
                ),
                
                Div(
                    Div(
                        Input(
                            id="bid_input",
                            type='number',
                            min=round(bid_item.get_price + 0.1, 1),
                            max=round(user.get_e_bux, 2),
                            step=0.01,
                            required=True,
                            style="width:100%; max-width:300px; text-align:center; border-radius:50px; font-size:20px; padding:15px; border: 2px solid #ccc; transition: border 0.3s ease; margin-bottom: 15px;",
                            placeholder='Enter your bid',
                            onfocus="this.style.border='2px solid #3498DB';",  
                            onblur="this.style.border='2px solid #ccc';"
                        ),
                        Button(
                            'Place Bid', 
                            style="""border-radius:50px; font-size:20px; width:250px; background-color: #3498DB; 
                                     color: white; border: none; padding: 15px 30px; cursor: pointer;
                                     transition: background-color 0.3s ease, transform 0.2s ease;
                                     box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);""", 
                            type='submit',
                            onmouseover="this.style.backgroundColor='#1E88E5'; this.style.transform='scale(1.05)';",
                            onmouseout="this.style.backgroundColor='#3498DB'; this.style.transform='scale(1)';"
                        ),
                        style="display:flex; flex-direction:row; align-items:center; justify-content:flex-start; gap:20px; margin-top:20px; width:100%;"
                    ),
                    style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px; width: 100%; max-width: 700px; margin: auto;"
                ),
                
                style="display:flex; flex-direction:column; gap:25px; width:100%; max-width:700px; align-items:left;",
                action=f"/bid/submit?item_id={id}",
                method="post"
            )
        ),
        
        style="""display: flex; flex-direction: row; justify-content: center; align-items: center; 
                 background-color: #ffffff; border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); 
                 width: 100%; max-width: 1200px; margin: auto; padding: 25px; gap: 50px;"""
    ),
    
    style="background-color: #D6EAF8; display: flex; justify-content: center; padding: 70px 0; gap: 60px;"
)

    except Exception as e:
        return Div(f"Item not found. Error: {e}", style="text-align:center; color:red; font-size:24px; font-weight:bold;")

def submit_bid_page(bid_input: float, item_id: str, session):
    item = main_system.get_bid_item_by_id(item_id)
    user_id = session['auth'][0]
    user = main_system.get_user_by_id(user_id)
    
    if item.get_status in ["Ended", "Sold"]:
        return Script(f"alert(\"Bidding has ended\"); window.location.href='/bid/{item_id}'")
    
    if bid_input <= item.get_price:
        return Script(f"alert(\"Bid must be higher than current price\"); window.location.href='/bid/{item_id}'")
    
    if user != item.top_bidder:
        main_system.set_top_bidder(item_id, bid_input, user)
        return Redirect(f"/bid/{item_id}")
    else:
        return Script(f"alert(\"You are already the highest bidder\"); window.location.href='/bid/{item_id}'")
