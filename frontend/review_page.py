from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def review_page(id):
    try:
        review = main_system.get_item_by_id(id)
        print(review)
        return Div(
            Div(Img(src=review.get_image),style="width:50%; height:auto; border-radius:15px; overflow:hidden;"),
            Form(
                P(review.get_name,style="color:black; font-weight:600;"),
                Textarea(name = 'review',type='text',placeholder='Enter your review',style="width:100%; margin:0;"),
                Select(
                        Option('⭐',value='1'),
                        Option('⭐⭐',value='2'),
                        Option('⭐⭐⭐',value='3'),
                        Option('⭐⭐⭐⭐',value='4'),
                        Option('⭐⭐⭐⭐⭐',value='5'),
                    style="width:100%; margin:0;",
                    name='rating'
                ),
                Button('Submit',style="width:100%; border-radius:50px;",type='submit'),
                style="display:flex; flex-direction:column; gap:10px; width:50%; align-items:center;",
            )
            ,style="display:flex; flex-direction:row; width:100%; padding:30px; gap:20px;"
        )
    except:
        return Div("Item not found")