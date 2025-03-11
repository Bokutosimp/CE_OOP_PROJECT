from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def bid_page(id, session):
    try:
        bid_item = main_system.get_bid_item_by_id(id)
        user_id = session['auth'][0]
        user = main_system.get_user_by_id(user_id)
        print(bid_item)
        
        return Div(
            # Outer container for the Card layout
            Div(
                # Image section (left side of the card)
                Div(
                    Img(src=bid_item.get_image), 
                    style="width: 450px; height: 450px; border-radius: 15px; overflow: hidden; box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15); margin-right: 50px;"
                ),
                
                # Form and content section (right side of the card)
                Div(
                    Form(
                              Div(
                                 H2(bid_item.get_name, style="color:black; font-weight:1000; font-size:40px; text-align:left; margin-bottom: 15px;"),
                                 style="border-bottom: 3px solid black; padding-bottom:10px; margin-bottom:5px;"),
                              
                              Div(
                                 P("Description:", style="color:black; font-size:24px; font-weight:bold;"),
                                 P(f"{bid_item.get_description}", style="color:black; font-size:20px;"),
                                 style="width:100%; border-bottom: 3px solid black; padding-bottom:15px; margin-bottom:5px;"
                              ),
                              
                              Div(
                                 P(f"Status : {bid_item.get_status}", style="color:black; font-size:24px; font-weight:bold;"),
                                 style="width:100%; text-align:left; margin-bottom:5px;"
                              ),
                              
                              Div(
                                 P(f"Current bid price: ${bid_item.get_price}", style="color:black; font-size:24px; font-weight:bold;"),
                                 style="width:100%; text-align:left; margin-bottom:5px;"
                              ),
                              Div(
                                 P(f"Start-time: ${bid_item.get_start_time}", style="color:black; font-size:24px; font-weight:bold;"),
                                 style="width:100%; text-align:left; margin-bottom:5px;"
                              ),
                              Div(
                                 P(f"End-time: ${bid_item.get_end_time}", style="color:black; font-size:24px; font-weight:bold;"),
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
                                       onfocus="this.style.border='2px solid #4CAF50';",  
                                       onblur="this.style.border='2px solid #ccc';"    
                                 ),
                                 Button(
                                       'Place Bid', 
                                       style="""
                                          border-radius:50px;
                                          font-size:20px;
                                          width:250px;
                                          background-color: #4CAF50;
                                          color: white;
                                          border: none;
                                          padding: 15px 30px;
                                          cursor: pointer;
                                          transition: background-color 0.3s ease, transform 0.2s ease;
                                          box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
                                       """, 
                                       type='submit',
                                       onmouseover="this.style.backgroundColor='#45a049'; this.style.transform='scale(1.05)';",
                                       onmouseout="this.style.backgroundColor='#4CAF50'; this.style.transform='scale(1)';",
                                       onclick="playClickSound();"
                                 ),
                                 style="display:flex; flex-direction:row; align-items:center; justify-content:flex-start; gap:20px; margin-top:20px; width:100%;"
                                 ),
                                 style="display: flex; flex-direction: column; align-items: flex-start; gap: 20px; width: 100%; max-width: 700px; margin: auto;"),
                              style="display:flex; flex-direction:column; gap:25px; width:100%; max-width:700px; align-items:left;",
                              action=f"/bid/submit?item_id={id}",
                              method="post"
                           )

                ),
                
                style="""display: flex; flex-direction: row; justify-content: center; align-items: center; 
                         background-color: #ffffff; border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15); 
                         width: 100%; max-width: 1200px; margin: auto; padding: 25px; gap: 50px;"""
            ),
            
            style="background-color: #eaf4f4; display: flex; justify-content: center; padding: 70px 0; gap: 60px;"
        )
    except Exception as e:
        return Div(f"Item not found. Error: {e}", style="text-align:center; color:red; font-size:24px; font-weight:bold;")

def submit_bid_page(bid_input: float, item_id: str, session):
    bid_item = main_system.get_bid_item_by_id(item_id)
    if bid_item.get_status != "Started":
        return Redirect(f"/bid/{item_id}")
    user_id = session['auth'][0]
    user = main_system.get_user_by_id(user_id)
    print(f"Bid: {bid_input}, Item ID: {item_id}, User ID: {user_id}")
    main_system.set_top_bidder(item_id, bid_input, user)
    return Redirect(f"/bid/{item_id}")
