from datetime import datetime,timedelta

class Order:
    def __init__(self,shipping_fee:float,total_price:float,list_item:list[object]):
        # self.__total_amount = total_amount
        self.__shipping_fee = shipping_fee
        self.__total_price = total_price
        if len(list_item) == 0: raise Exception('you should select atleast one item')
        self.__list_items = list_item
        self.__apply_code = None
    
    def __str__(self):
        return f'total price is {self.__total_price}\n item is:{self.__list_items}'
        
    def check_cart_with_stock(self,user:object):
        select_stock = [item for item in user.get_cart.get_list_item_in_cart if item.get_is_selected]
        for item in select_stock:
            if not item.get_item.check_availability(item.get_amount_in_cart):
                return "Payment denied"
    @property
    def get_total_price(self):
        return self.__total_price
    
    @property
    def get_list_item_select(self) : return self.__list_items
    
    @property
    def get_apply_code(self): return self.__apply_code
    @get_apply_code.setter
    def set_apply_code(self,code:object): self.__apply_code = code
    


    
class ShippingStatus:
    def __init__(self,shipping_date:datetime,get_item_date=datetime):
      self.__shipping_date = shipping_date
      self.__get_item_date = get_item_date
      
    def __str__(self):
        return f'shipping date :{self.__shipping_date.strftime("%y-%m-%d")} {self.__shipping_date.strftime("%H:%M:%S")} \n get item date : {self.__get_item_date.strftime("%y-%m-%d")} {self.__get_item_date.strftime("%H:%M:%S")}'
      
    def get_info(self):
      return f"Status: {self.__status}, Shipping Date: {self.__shipping_date}, Get Item Date: {self.__get_item_date}"
  
    @property
    def get_shipping_date(self) -> datetime: return self.__shipping_date
    @property
    def get_get_item_date(self) -> datetime: return self.__get_item_date

class OrderHistory :
    def __init__(self , order : Order,shipping_status:ShippingStatus ):
        self.__order = order
        self.__shipping_status =  shipping_status
        
    @property
    def get_shipping_status(self) -> ShippingStatus: return self.__shipping_status
    
    @property
    def get_order(self) -> Order: return self.__order
    def set_status(self , status : ShippingStatus) :
        self.__shipping_status = status
        