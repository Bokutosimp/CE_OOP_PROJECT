from .item import *
from .discount_code import Code
from .item import User
class order:
    def __init__(self,total_amount,shipping_fee,item_price,list_item:ItemInCart):
        self.__total_amount = total_amount
        self.__shipping_fee = shipping_fee
        self.__item_price = item_price
        self.__list_items = list_item
        
    def item_price(self):
        return self.__item_price
    
    def check_amount(self):
        pass
        
    def apply_code(self,input_code):
        discount = 0
        for i in Code:
            if input_code == i.item.itemincart.name:
                discount = i.item.itemincart.Discount
            else :
                return f"This code doesn't exist"

        return self.__item_price - discount
                
    def buy(self):
        return User.item.itemincart.Seatung(self.__item_price)
    