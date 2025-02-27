from .item import Item

class ItemInCart:
   def __init__(self,item:Item,amount_in_cart:int,isSelected:bool):
      self.__item = item
      self.__amount_in_cart = amount_in_cart
      self.__isSelected = isSelected
      
   