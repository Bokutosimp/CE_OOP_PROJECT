from .item import Customer

class Review:
   def __init__(self,score:int,comment:str,reviewer:Customer):
      self.__score = score
      self.__comment = comment
      self.__reviewer = reviewer
   @property
   def get_score(self)-> int: return self.__score