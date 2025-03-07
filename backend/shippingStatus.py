class ShippingStatus:
   def __init__(self,status:str,shipping_date:str,get_item_date=None):
      self.__status = status
      self.__shipping_date = shipping_date
      self.__get_item_date = get_item_date