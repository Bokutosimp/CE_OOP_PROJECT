from item import Item
from datetime import datetime
from biddingHistory import BiddingHistory
from user_class import User

class BitItem:
    def __init__(self, item : Item):
        self.__item = item
        self.__top_bidder = None
        self.__current_price = 0
        self.__bids_history = []
        self.__status = "Not Started"
        self.__end_time = None
        self.__start_time = None
        
    def start(self):
        self.__start_time = datetime.now()
        self.__status = "Started"
        
    def end(self):
        self.__end_time = datetime.now()
        self.__status = "Ended"
        
    @property
    def item(self):
        return self.__item
    
    @property
    def top_bidder(self):
        return self.__top_bidder
    
    @property
    def current_price(self):
        return self.__current_price
    
    @property
    def bids_history(self):
        return self.__bids_history
    
    def set_top_bidder(self, user : User):
        self.__top_bidder = user
        
    def set_current_price(self, price : float):
        self.__current_price = price
    
    def add_history(self, bid_history : BiddingHistory):
        self.__bids_history.append(bid_history)
        
    def is_started(self):
        return self.__status == "Started"
    
    def is_ended(self):
        return self.__status == "Ended"