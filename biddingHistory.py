from datetime import datetime
from user_class import User
class BidHistory:
    def __init__(self, user : User, bidAmount : float, bidTime : datetime):
        self.user = user
        self.bidAmount = bidAmount
        self.bidTime = bidTime