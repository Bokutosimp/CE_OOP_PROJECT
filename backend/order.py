from .discount_code import Code

class Order:
    def __init__(self,shipping_fee:float,total_price:float,list_item:list[object]):
        # self.__total_amount = total_amount
        self.__shipping_fee = shipping_fee
        self.__total_price = total_price
        self.__list_items = list_item
        self.__isApply = None
        
    # def check_amount(self):
    #     return Item.checkavaillability(self.__list_items)
        
    def item_price(self):
        return self.__item_price
    
    # def sum_item_in_cart(self):
    #     for i in Cart.get_list_item_in_cart:
    #         self.__list_items.append(i)
    #         self.__item_price += i.get_item.get_price * i.get_amount_in_cart
    #         self.__total_amount += self.__item_price
    #         return self.__total_amount

        
    def apply_code(self,input_code):
        verify = Code.verify_code(input_code)
        if verify == True:
            self.__total_amount -= self.__total_amount * Code.get_discount
            self.__isApply = True
        else:
            return "Invalid code"
                
    # def buy(self):
    #     return Customer.SeaTung(self.__total_amount)
    
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

    def set_status(self , status : ShippingStatus) :
        self._shipping_status = status

    def check_status(self):
        return self._shipping_status.get_info()
    