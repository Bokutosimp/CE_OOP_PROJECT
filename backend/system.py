# from .item import Item
# from .user_class import User
from .discount_code import Code
from .category import Category
from .item import *

class System:
   def __init__(self):
      self.__list_items:list[Item] = []
      self.__list_users:list[User] = []
      self.__list_codes:list[Code] = []
      self.__list_categories:list[Category] = []
      
   def search_item(self,query:str = ''):
      #return list of items
      pass
   
   def view_item(self,itemId:str):
      #return item
      pass
   
   
   def save_item(self,name : str, price : float, amount : int, category : str):
      pass

   def save_stock(self ,name : str , amount):
      pass

   def save_bid_item(self, name:str , start_price , amount : int , category : str):
      pass

   def save_discount_code(self,ID, discount_percent):
      pass

   def create_category(self, name:str, description:str):
      self.__list_categories.append(Category(name,description))
      return 'Category created'

   def show_success_message():
      return "So good "
   
   def show_error_message():
      return "There's something wrong" 
   
   def update_top_bidder(self):
      pass

   def retrieve_bid_data() :
      pass

   def retrieve_order_data() :
      pass
print('test gay')