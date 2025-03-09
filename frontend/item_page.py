from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def item_page(id):
   try:
      item = main_system.get_item_by_id(id)
      return Div(
            Div(Img(src=item.get_image),style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Form(
               Div(H2(item.get_name,style="color:black; font-weight:600;"),style="width:100%; border-bottom:1px solid gray; margin-bottom:20px;"),
               Div(style="height:40px; width:100%; border-bottom:1px solid gray;"),
               Div(P(f"US ${item.get_price}/ea",style="color:black; font-size:30px; font-weight:bold;"),style="width:100%;"),
               Div(
                  Span('Quantity:',style="color:black; font-size:15px;"),
                  Input(type='number',value=1,min=1,max=item.get_amount,style="width:70px; margin:0;",id='amount',),
                   style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center;"),
               A(Button('But It Now',style="width:100%; border-radius:50px; margin:0;",type='button'),href='#',style='width:100%;'),
               Button('Add to Cart',style="width:100%;border-radius:50px;",type='submit'),
               style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;",
               method='post',
               action=f'/cart/{item.get_id}'
               ),
            Style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;",)
   except Exception as e:
      return Div(str(e))
   