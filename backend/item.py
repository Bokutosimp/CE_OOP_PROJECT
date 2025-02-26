from .user_class import Seller

class Item:
   def __init__(self,name :str , price:float,amount:int, owner:Seller) :
      self.__name = name
      self.__aprice = price
      self.__mount = amount
      self.__owner = owner
      
   def check_availlability(self,quantity:int):
      pass
