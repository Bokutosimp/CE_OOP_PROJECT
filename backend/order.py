class Order:
    def __init__(self,shipping_fee:float,total_price:float,list_item:list[object]):
        # self.__total_amount = total_amount
        self.__shipping_fee = shipping_fee
        self.__total_price = total_price
        self.__list_items = list_item
        self.__isApply = None
    
    def __str__(self):
        return f'total price is {self.__total_price}'
        
    def check_cart_with_stock(self,user:object):
        select_stock = [item for item in user.get_cart.get_list_item_in_cart if item.get_is_selected]
        for item in select_stock:
            if not item.get_item.check_availability(item.get_amount_in_cart):
                return "Payment denied"
        
    def item_price(self):
        return self.__item_price
    
    @property
    def get_list_item_select(self) : return self.__list_items
    
    
class ShippingStatus:
   def __init__(self,status:str,shipping_date:str,get_item_date=None):
      self.__status = status
      self.__shipping_date = shipping_date
      self.__get_item_date = get_item_date
      
   def get_info(self):
      return f"Status: {self.__status}, Shipping Date: {self.__shipping_date}, Get Item Date: {self.__get_item_date}"

class OrderHistory :
    def __init__(self , order : Order ):
        self.__order = order
        self._shipping_status =  None 

    @property
    def get_order(self): return self.__order
    def set_status(self , status : ShippingStatus) :
        self._shipping_status = status

    def check_status(self):
        return self._shipping_status.get_info()
    