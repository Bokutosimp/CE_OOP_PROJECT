from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def home():
    return Main(
        H1("Product Management", style="text-align: center; color: #222;"),
        
        # ปุ่มเปิด Popup
        Button("Open Pop-up", onclick="document.getElementById('popup').style.display='block';", 
               style="background: #0074bd; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer;"),

        # Popup Modal
        Div(
            Div(
                H2("This is a Pop-up!"),
                P("You clicked the button to open this pop-up."),
                
                # ปุ่มปิด Popup
                Button("Close", onclick="document.getElementById('popup').style.display='none';",
                       style="background: #f44336; color: white; padding: 10px; border-radius: 5px; border: none; cursor: pointer; margin-top: 10px;"),

                style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center;"
            ),
            id="popup",
            style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center;"
        )
    )

serve()
