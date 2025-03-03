from .itemInCart import ItemInCart

class Cart:
   def __init__(self):
      self.__list_item_in_cart:list[ItemInCart] = []
      