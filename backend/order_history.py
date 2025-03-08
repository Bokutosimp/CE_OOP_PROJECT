from .itemInCart import ItemInCart
from .discount_code import Code
from .item import User
from .order import order
from .shippingStatus import ShippingStatus

class order_history :
    def __init__(self , order : order ):
        self.__order = order
        self._shipping_status =  None 

    def set_status(self , status : ShippingStatus) :
        self._shipping_status = status

    