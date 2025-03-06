from .discount_code import Code
from .category import Category
from .item import *
import uuid

class System:
   def __init__(self):
      self.__list_items:list[Item] = []
      self.__list_bid_items:list[BidItem] = []
      self.__list_users:list[User] = []
      self.__list_codes:list[Code] = []
      self.__list_categories:list[Category] = []
      
   def login(self,username:str,password:str) :
      for user in self.__list_users:
         if user.get_username == username and user.get_password == password:
            return [user.get_user_id,type(user).__name__]
      return None
   
   #function for validation duplicate name in list of instances
   def __validate_name(self,name:str,instance:list[object]) -> bool:
      for item in instance:
         if item.get_name  == name:
            return False
      return True
      
   #function to get list of instace
   def get_categories(self,query:str = '') -> list[Category]:
      if(query == ''): return self.__list_categories
      else: return [category for category in self.__list_categories if query in category.get_name]
      
   def get_category_by_id(self,id:str):
      for cat in self.__list_categories:
         if cat.get_id == id:
            return cat
      return 'Not found'
   
   def get_items(self,query:str = ''):
      if(query == ''):
         return self.__list_items
      else:
         return [item for item in self.__list_items if query.lower() in item.get_name.lower()]
      
   def get_bid_items(self,query:str = ''):
      if(query == ''):
         return self.__list_bid_items
      else:
         return [item for item in self.__list_bid_items if query.lower() in item.get_name.lower()]   
      
   def get_item_by_id(self,id:str):
      for item in self.__list_items: 
         if item.get_id == id: return item
      return None
   
   def get_bid_item_by_id(self,id:str):
      for item in self.__list_bid_items: 
         if item.get_id == id: return item
      return None
      
   def get_users(self,query:str = ''):
      if(query == ''):
         return self.__list_users
      else:
         return [user for user in self.__list_users if query in user.get_name]
      
   def get_items_by_category(self,category_id:str) -> list[Item]:
      filtered_items:list[Item] = []
      for item in self.__list_items:
         for category in item.get_category:
            print(category.get_id,category_id)
            if category.get_id.lower() == category_id.lower():
               filtered_items.append(item)
      return filtered_items
   
   def get_user_by_id(self,id:str):
      for user in self.__list_users:
         if user.get_user_id == id:
            return user
      return None
   
   #function to create instace
   def create_category(self, id:str,name:str, description:str):
      if not self.__validate_name(name,self.__list_categories): raise Exception('Name already exist')
      self.__list_categories.append(Category(id,name,description))
      return 'Category created'
   
   def create_admin(self,name, user_id, email, phone_number, username, password, birth_date, gender):
      if not self.__validate_name(username,self.__list_users): raise Exception('Name already exist') 
      self.__list_users.append(Admin(name, user_id, email, phone_number, username, password, birth_date,gender))
      return 'Admin created'
   
   def create_customer(self,name:str, user_id:str, email:str, phone_number:int, username:str, password:str, birth_date,gender,address:str,e_bux:float=0):
      if not self.__validate_name(email,self.__list_users): raise Exception('Email already exist')
      if not self.__validate_name(username,self.__list_users): raise Exception('username already exist')
      cart = Cart()
      self.__list_users.append(Customer(name, user_id, email, phone_number, username, password, birth_date,gender,address,e_bux,cart))
      return 'Customer created'
   
   def create_seller(self,customer:Customer,store_name:str,store_address:str):
      for i in range(len(self.__list_users)):
         if self.__list_users[i].get_user_id == customer.get_user_id and isinstance(self.__list_users[i],Customer):
            self.__list_users[i] = Seller(customer,store_name,store_address)
            return 'Seller created'  
      
   def create_discount_code(self, name:str, discount_percent:float):
      self.__list_codes.append(Code(name,discount_percent))
      return 'Code created'
      
   def create_item(self,current_user_id:str,id:str,name:str, price:float, amount:int,category_id:list[str],img=''):
      if not self.__validate_name(name,self.__list_items): raise Exception('Item already exist')
      current_user = self.get_user_by_id(current_user_id)
      if current_user == None: raise Exception('User not found')
      if not isinstance(current_user,Seller): raise Exception('User is not a seller')
      category_list:list[Category] = []
      for id in category_id:
         for category in self.__list_categories:
            if category.get_id == id:
               category_list.append(category)
      if len(category_list) == 0: raise Exception('Category not found')
      self.__list_items.append(Item(id,name,price,amount,current_user,img,category_list))
      return 'Item created'
   
   def view_item(self,itemId:str):
      for item in self.__list_items :
         if item.get_id == itemId  :
           return item 
      return "Item not found"
   
   
   def save_item(self, user_id, name: str, price: float, amount: int, category_id: str, img=''):
    try:
        item_id = str(uuid.uuid4())
        self.create_item(user_id, item_id, name, price, amount, [category_id], img)
        return 'Item saved successfully'
    except Exception as e:
        return 'Error'

   def save_stock(self ,name : str , amount):
      pass

   def save_bid_item(self, name:str , start_price , amount : int , category : str):
      pass

   def save_discount_code(self,ID, discount_percent):
      pass
   
   def get_top_bidder(self, item_id:str):
      for item in self.__list_bid_items:
         if item.get_id == item_id:
            return item.get_top_bidder
         
   def start_bid(self, item_id:str):
      for item in self.__list_bid_items:
         if item.get_id == item_id:
            item.start_bid()
            return 'Bid started'
         
   def end_bid(self, item_id:str):
      for item in self.__list_bid_items:
         if item.get_id == item_id:
            item.end_bid()
            return 'Bid ended'
         
   def is_bid_started(self, item_id:str):
      for item in self.__list_bid_items:
         if item.get_id == item_id:
            return item.is_started
         
   def is_bid_ended(self, item_id:str):
      for item in self.__list_bid_items:
         if item.get_id == item_id:
            return item.is_ended


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


def createInstance():
   from .mock.items import items
   from .mock.bid_items import bid_items
   from .mock.category import categories
   from .mock.users import users
   main_system = System()
   #create category
   [main_system.create_category(category['id'],category['name'],category['description']) for category in categories]
   categories_instane = main_system.get_categories()
   [print(category) for category in categories_instane]
   #create user
   for user in users:
      if user['role'] == 'admin':
         main_system.create_admin(user['name'],user['user_id'],user['email'],user['phone_number'],user['username'],user['password'],user['birth_date'],user['gender'])
      elif user['role'] == 'customer' or user['role'] == 'seller':
         main_system.create_customer(user['name'],user['user_id'],user['email'],user['phone_number'],user['username'],user['password'],user['birth_date'],user['gender'],user['address'],user['e_bux'])
         if user['role'] == 'seller':
            main_system.create_seller(main_system.get_user_by_id(user['user_id']),user['store_name'],user['store_address'])
   users_instance = main_system.get_users()
   [print(user) for user in users_instance]
   #create item
   for item in items:
      main_system.create_item('sell001',item['id'],item['name'],item['price'],item['amount'],['1','2'],item['image'])
   items_instance = main_system.get_items()
   [print(item) for item in items_instance]
   print('result of search by category',main_system.get_items_by_category(main_system.get_categories()[0].get_id))
   print('result of search item by id',main_system.get_item_by_id(items_instance[0].get_id))
   #create bid item
   for bid_item in bid_items:
      main_system.create_item('sell001', bid_item['id'], bid_item['name'], bid_item['start_price'], bid_item['amount'], ['1', '2'], bid_item['image'])
   bid_items_instance = main_system.get_bid_items()
   [print(bid_item) for bid_item in bid_items_instance]
   return main_system

main_system = createInstance()