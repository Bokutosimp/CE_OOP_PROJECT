from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def item_page(id):
   try:
      item = main_system.get_item_by_id(id)
      
      render_review = Div(
               H4(f'review from other users',style='color:black;'),
               P(f'average score {round(main_system.get_average_score(item.get_id),2)}'),
               Div(*[
                  Div(
                     Div(f'score: {'⭐'*review.get_score}',style='border-bottom:solid 1px var(--lavender-web-2);'),
                     Div(f'{review.get_comment}'),
                     Div(f'from {review.get_reviewer.get_name}'),
                     style='padding:10px; background-color:#bfbfbf; border-radius:10px; width:100%;color:white; box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;'
                  ) 
                 for review in item.get_review],
                   style='display:flex; flex-direction:column; gap:10px; align-items:center;'),
               style='padding:20px clamp(50px,15vw,500px);'
            ) if len(item.get_review) != 0 else None
      return Div(Div(
            Div(Img(src=item.get_image),style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Form(
               Div(H2(item.get_name,style="color:black; font-weight:600;"),style="width:100%; border-bottom:1px solid gray;"),
               Div(Span(item.get_description),style="margin:20px auto; width:100%;"),
               Div(P(f"US ${item.get_price}/ea",style="color:black; font-size:30px; font-weight:bold;"),style="width:100%; border-top:1px solid gray;"),
               Div(
                  Span('Quantity:',style="color:black; font-size:15px;"),
                  Input(type='number',value=1,min=1,max=item.get_amount,style="width:70px; margin:0;",id='amount',),
                   style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center;"),
               A(
                  Button('But It Now',
                         style="width:100%; border-radius:50px; margin:0;",
                         type='button',
                         onclick=f"""
                           event.preventDefault();
                           const input = document.getElementById("amount")
                           window.location.href=`/purchase/{item.get_id}/${{input.value}}`
                         """),
                 href='#',style='width:100%;'),
               Button('Add to Cart',style="width:100%;border-radius:50px;",type='submit'),
               style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;",
               method='post',
               action=f'/cart/{item.get_id}'
               ),
            Style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;",),
            #review
            render_review,
            style='max-width:1400px; margin:0 auto;'
            )
   except Exception as e:
      return Script(f"alert(\"{str(e)}\"); window.location.href='/'")
   