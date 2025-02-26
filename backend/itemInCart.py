from .item import Item

class ItemInCart:
   def __init__(self,item:Item,amount:int,isSelected:bool):
      self.__item = item
      self.__amount = amount
      self.__isSelected = isSelected
      
   