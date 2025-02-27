from fasthtml.common import *
import add_product

app, rt = fast_app()

@rt('/')

def get():
   return Main(
      Grid(
         H1("Product Management", style="text-align: center; margin-bottom: 20px; color: #F8F0FB;"),  
      ),
      
      # Profile Section
      Grid(
         Card(
            H3("Profile", style="color: #6320EE;"),
            Div(
               Img(
                  src='https://i.pinimg.com/564x/f5/9f/5e/f59f5ece0a7984f20413a4e32a4f25a2.jpg',
                  style='width: 50px; height: 50px; object-fit: cover; border-radius: 50%;' 
               ),
               Div(
                  H5('Gojo Satoru', style='font-size: 14px; margin: 0; color: #211A1D;'), 
                  P(
                     "มาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                     style='margin: 0; font-size: 12px; color: gray;'
                  ),  
                  style='display: flex; flex-direction: column; margin-left: 10px; max-width: 150px;'  
               ),
               style='display: flex; align-items: center;'  
            ),
            Button("Add Product", method ='add' , action="/add", style="background: #6320EE; color: white; border-radius: 5px; padding: 8px 12px; border: none; margin-top: 10px"),
            style = """
                width: 30%;    
                border-radius: 15px; 
                padding: 15px; 
                margin: auto;
                background: #F8F0FB;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
            """
         )
      ),

      # Product Section
      Grid(
         Card(
            H3("PRODUCT #1", style="color: #6320EE;"),
            Div(
               Img(
                  src='https://leagueofitems.com/images/items/256/3078.webp',
                  style='width: 100px; height: 100px; object-fit: cover; border-radius: 20%; margin-right: 10px;' 
               ),
               P(
                  "มาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                  style='font-size: 12px; color: #211A1D;'
               ),
               style='display: flex; align-items: center;'  
            ),
            Div(
               Button("Stock", style="background: #6320EE; color: white; border-radius: 5px; padding: 8px 12px; border: none;"),
               Button("Ship", style="background: #8075FF; color: white; border-radius: 5px; padding: 8px 12px; border: none; margin-left: 10px;"),
               style="display: flex; justify-content: space-between; margin-top: 15px;"
            ),
            style = """
                width: 50%;    
                border-radius: 15px; 
                padding: 15px; 
                margin: auto;       
                background: #F8F0FB;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
            """
         )
      ),

      Grid(
         Card(
            H3("PRODUCT #2", style="color: #6320EE;"),
            Div(
               Img(
                  src='https://s.isanook.com/ga/0/ud/221/1106953/frost-cape.png?ip/resize/w728/q80/png',
                  style='width: 100px; height: 100px; object-fit: cover; border-radius: 20%; margin-right: 10px;' 
               ),
               P(
                  "มาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                  style='font-size: 12px; color: #211A1D;'
               ),
               style='display: flex; align-items: center;'  
            ),
            Div(
               Button("Stock", style="background: #6320EE; color: white; border-radius: 5px; padding: 8px 12px; border: none;"),
               Button("Ship", style="background: #8075FF; color: white; border-radius: 5px; padding: 8px 12px; border: none; margin-left: 10px;"),
               style="display: flex; justify-content: space-between; margin-top: 15px;"
            ),
            style = """
                width: 50%;    
                border-radius: 15px; 
                padding: 15px; 
                margin: auto;       
                background: #F8F0FB;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
            """
         )
      ),

      Grid(
         Card(
            H3("PRODUCT #3", style="color: #6320EE;"),
            Div(
               Img(
                  src='https://tkcdn.tekedia.com/wp-content/uploads/2022/05/23204855/coke-768x432.jpg',
                  style='width: 100px; height: 100px; object-fit: cover; border-radius: 20%; margin-right: 10px;' 
               ),
               P(
                  "มาเดโม เอากะ ซุนเดรุ อิมาเดโมเอาวะ ซุนเดรุ ดนนาอิโนริโม โคโตบะโม",
                  style='font-size: 12px; color: #211A1D;'
               ),
               style='display: flex; align-items: center;'  
            ),
            Div(
               Button("Stock", style="background: #6320EE; color: white; border-radius: 5px; padding: 8px 12px; border: none;"),
               Button("Ship", style="background: #8075FF; color: white; border-radius: 5px; padding: 8px 12px; border: none; margin-left: 10px;"),
               style="display: flex; justify-content: space-between; margin-top: 15px;"
            ),
            style = """
                width: 50%;    
                border-radius: 15px; 
                padding: 15px; 
                margin: auto;       
                background: #F8F0FB;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
                margin-bottom: 30px;
            """
         )
      ),
            style="background: #211A1D; padding: 20px; min-height: 100vh;",  # เปลี่ยนสีพื้นหลังเว็บ

   )

serve()