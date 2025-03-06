from datetime import datetime
from .item import User

class BiddingHistory:
    def __init__(self, user : User, bidAmount : float, bidTime : datetime):
        self.user = user
        self.bidAmount = bidAmount
        self.bidTime = bidTime