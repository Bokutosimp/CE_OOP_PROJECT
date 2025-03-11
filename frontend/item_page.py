from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from backend.system import main_system

def item_page(id):
    try:
        item = main_system.get_item_by_id(id)

        render_review = reviews_section = (
            Div(
                H4("Reviews from Other Users", style="color:#3498DB; text-align:center; margin-bottom:10px;"),
                P(f'Average Score: {round(main_system.get_average_score(item.get_id),2)}', 
                  style="font-size:18px; font-weight:bold; color:#3498DB; text-align:center;"),
                Div(
                    *[
                        Div(
                            Div(f"Score: {'⭐' * review.get_score}", 
                                style="border-bottom:solid 1px #85C1E9; font-weight:bold; padding-bottom:5px;"),
                            Div(review.get_comment, style="margin-top:5px; font-size:14px;"),
                            Div(f"From: {review.get_reviewer.get_name}", 
                                style="font-size:12px; color:#555; margin-top:5px;"),
                            style=(
                                "padding:15px; background-color:#ECF0F1; border-radius:8px; width:90%;"
                                "color:#333; box-shadow:0px 2px 5px rgba(0, 0, 0, 0.1); border-left:5px solid #3498DB;"
                            )
                        )
                        for review in item.get_review
                    ],
                    style="display:flex; flex-direction:column; gap:15px; align-items:center;",
                    cls="reviews-list"
                ),
                style="max-width:600px; background:white; padding:20px; border-radius:12px; "
                      "box-shadow:0px 4px 10px rgba(0, 0, 0, 0.1); text-align:center; margin:auto;"
            )
            if item.get_review
            else None
        )

        return Div(
            Div(
                Div(
                    Img(src=item.get_image, style="width:100%; height:auto; border-radius:15px; overflow:hidden;"),
                    style="flex:1; max-width:45%;"
                ),

                Form(
                    Div(H2(item.get_name, style="color:#3498DB; font-weight:600;"), 
                        style="width:100%; border-bottom:1px solid #85C1E9; padding-bottom:10px;"),

                    Div(Span(item.get_description), style="margin:20px auto; width:100%; font-size:16px; color:#333;"),

                    Div(
                        P(f"US ${item.get_price}/ea", style="color:#3498DB; font-size:30px; font-weight:bold;"),
                        style="width:100%; border-top:1px solid #85C1E9; padding-top:10px;"
                    ),

                    Div(
                        Span('Quantity:', style="color:#3498DB; font-size:15px;"),
                        Input(type='number', value=1, min=1, max=item.get_amount, id='amount',
                              style="width:70px; padding:5px; text-align:center; border:1px solid #ccc; border-radius:5px;"),
                        style="display:flex; flex-direction:row; gap:10px; width:100%; align-items:center; margin-bottom:10px;"
                    ),

                    A(
                        Button('Buy It Now', type='button',
                               style="width:100%; padding:12px; border-radius:50px; background-color:#3498DB; color:white; border:none; font-size:16px; cursor:pointer;",
                               onclick=f"""
                                    event.preventDefault();
                                    const input = document.getElementById("amount");
                                    window.location.href=`/purchase/{item.get_id}/${{input.value}}`;
                               """
                        ),
                        href='#',
                        style="width:100%; text-decoration:none;"
                    ),

                    Button('Add to Cart',
                           style="width:100%; padding:12px; border-radius:50px; background-color:#21618C; color:white; border:none; font-size:16px; cursor:pointer;",
                           type='submit'
                    ),

                    method='post',
                    action=f'/cart/{item.get_id}',
                    style="display:flex; flex-direction:column; gap:15px; width:50%; align-items:center;"
                ),

                style=(
                    "display:flex; flex-direction:row; width:100%; padding:30px; gap:20px; align-items:center; "
                    "justify-content:space-between; flex-wrap:wrap; max-width:1200px; margin:auto;"
                ),
            ), 
            reviews_section,
            style="max-width:1400px; margin:0 auto;"
        )

    except Exception as e:
        return Script(f"alert(\"{str(e)}\"); window.location.href='/'")
