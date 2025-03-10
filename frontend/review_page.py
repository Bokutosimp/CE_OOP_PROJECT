from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system
from stylesheet import *

def review_page(id, session):
    try:
        review = main_system.get_item_by_id(id)
        print(review)
        print(session['auth'])

        return Div(
            Script(f"<style>{stylesheet}</style>"),

            H1("Leave a Review", style="text-align: center; color: #333; font-size: 36px; font-weight: bold; margin-bottom: 20px;"),

            Div(
                Img(src=review.get_image),
                style="width:100%; max-width:400px; height:auto; border-radius:15px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); object-fit: cover;"
            ),
            
            Form(
                P(review.get_name, style="color:#333; font-size:28px; font-weight:600; text-align:center; margin-top: 1px;"),
                
                Textarea(
                    id='review',
                    name='review',
                    type='text',
                    placeholder='Write your review...',
                    style="width:100%; padding:15px; font-size:16px; border-radius:8px; border:1px solid #ccc; box-sizing:border-box; height:150px; resize:none; margin-bottom:20px;"
                ),
                
                Select(
                    Option('⭐', value=1),
                    Option('⭐⭐', value=2),
                    Option('⭐⭐⭐', value=3),
                    Option('⭐⭐⭐⭐', value=4),
                    Option('⭐⭐⭐⭐⭐', value=5),
                    style="width:100%; padding:12px; font-size:16px; border-radius:8px; border:1px solid #ccc; box-sizing:border-box; margin-bottom:20px;",
                    name='rating',
                    id='rating'
                ),
                
                Input(id="item_id", type='hidden', value=id),
                
                Button(
                    'Submit Review',
                    style=""" background-color :#333 ; class color: white; padding:15px; font-size:18px; font-weight:bold; border-radius:50px; width:100%; border:none; cursor:pointer; transition: background-color 0.3s;""",
                    type='submit'
                ),

                style="display: flex; flex-direction: column; gap: 15px; width:80%; max-width:500px; margin:auto;",
                action=f"/review/submit?item_id={id}",
                method="post"
            ),
            
            style="""display: flex; flex-direction: column; align-items: center; padding: 30px 0; background-color: #ced9f3ff; gap: 40px;
                border-radius: 15px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); border: 1px solid #ddd; padding: 30px; max-width: 650px; margin: auto;"""
        )

    except:
        return Div("Item not found", style="color:red; font-size:24px; font-weight:bold; text-align:center;")

def submit_review_page(review: str, rating: int, item_id: str, session):
    user_id = session['auth'][0]
    user = main_system.get_user_by_id(user_id)
    print(f"Review: {review}, Rating: {rating}, Item ID: {item_id}, User ID: {user}")
    main_system.add_review(item_id, rating, review, user)
    return Redirect(f"/")
