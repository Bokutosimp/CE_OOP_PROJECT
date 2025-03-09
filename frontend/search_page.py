from fasthtml.common import *
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from backend.system import main_system

def search_page(keyword):

   filtered_items = main_system.get_items(keyword)
   if filtered_items:
      return Div(
         H4(f"{'result for '+keyword if keyword != '' else ''}"),
         Div(*[A(
               Div(style=f"width:256px; height: 256px; background:rgb(200, 200, 200); background-image:url({item.get_image});  background-position:center; background-size:contain; background-repeat: no-repeat; border-radius:15px;"),
               Div(
                  Div(item.get_name,style="font-size:20px;"),
                  Div('New-Open box',style="font-size:15px; color:gray;"),
                  Div(
                     Div(f"US ${item.get_price}",style="font-weight:bold; font-size:25px; width:50%;"),
                     Div("Save up to 15% when you buy more ginosurplus713 (282) 100%",style="justify-self:end; font-size:15px; width:50%;"),
                     style="display:flex; flex-direction:row; width:100%; margin-top:20px;"),
                  style="display:flex; flex-direction:column; width:100%; margin:10px 20px;"),
               style="display:flex; flex-direction:row; gap:20px; text-decoration:none; color:black; width:100%; background:var(--lavender-web-2); border-radius:15px; padding:0; overflow:hidden;",
               href=f"{'/item/'+str(item.get_id) if item.__class__.__name__ == 'Item' else '/bid/'+str(item.get_id)}"               
            ) 
            for item in filtered_items],
             style="display:flex; flex-direction:column; gap:10px; width:100%;",
             ),
         style="padding:20px; max-width:1024px; margin: 0 auto;")
   else:
      return Div('not found')   