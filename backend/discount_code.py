from item import Seller

class Code :
   def __init__(self,ID:str,name:str):
      self.__ID = ID
      self.__name = name
      
   def verify_code(self,input):
      pass

class FreeDelivery(Code):
   def __init__(self,ID:str,name:str,minimum:float):
      super().__init__(ID,name)
      self.__minimum = minimum

class Discount(Code):
   def __init__(self,ID:str,name:str,percentage:float,owner:Seller):
      super().__init__(ID,name)
      self.__percentage = percentage
      self.__owner = owner