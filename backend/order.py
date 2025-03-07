from .item import *
from .discount_code import Code
from .item import *
from .discount_code import *
class order:
    def __init__(self,total_amount,shipping_fee,item_price,list_item:ItemInCart):
        self.__total_amount = 0
        self.__shipping_fee = shipping_fee
        self.__item_price = item_price
        self.__list_items = list_item
        self.__isApply = None
        
    def check_amount(self):
        return Item.checkavaillability(self.__list_items)
        
    def item_price(self):
        return self.__item_price
    
    def sum_item_in_cart(self):
        for i in Cart.get_list_item_in_cart:
            self.__list_items.append(i)
            self.__item_price += i.get_item.get_price * i.get_amount_in_cart
            self.__total_amount += self.__item_price
            return self.__total_amount

        
    def apply_code(self,input_code):
        verify = Code.verify_code(input_code)
        if verify == True:
            self.__total_amount -= self.__total_amount * Code.get_discount
            self.__isApply = True
        else:
            return "Invalid code"
                
    def buy(self):
        return Customer.SeaTung(self.__total_amount)
    