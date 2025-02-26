from .item import Item
class BidHistory:
    def __init__(self,item:Item):
        self.__item = item
        self.__status = None
        
    def set_status(self,status:str):
        self.__status = status