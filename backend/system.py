from .category import Category
from datetime import datetime
from .item import Item,BidItem,User,Code,Customer,Seller,Admin,Cart,Review
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
      raise Exception('user not found')
   
   #function for validation duplicate name in list of instances
   def __validate_name(self,name:str,instance:list[object]) -> bool:
      for item in instance:
         if item.get_name == name:
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
      raise Exception('Not found')
   
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
      raise Exception('item not found')
   
   def get_bid_item_by_id(self,id:str):
      for item in self.__list_items:
         if str(item.get_id) == str(id) and isinstance(item, BidItem): return item
      raise Exception('bid item not found')
      
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
      raise Exception('user not found')
   
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
      try:
         result = self.__validate_name(name,self.__list_items)
         if not result: raise Exception('item already exist')
         current_user = self.get_user_by_id(current_user_id)
         if not isinstance(current_user,Seller): raise Exception('User is not a seller')
         category_list:list[Category] = []
         for cat_id in category_id:
            for category in self.__list_categories:
               if category.get_id == cat_id:
                  category_list.append(category)
         if len(category_list) == 0: raise Exception('Category not found')
         self.__list_items.append(Item(id,name,price,amount,current_user,img,category_list))
         return {'success':True}
      except Exception as e:
         raise Exception((str(e)))
   
   def create_bid_item(self,id:str,name:str, price:float, amount:int,category_id:list[str],img:str,owner_id:str,start_time:str,end_time:str,status:str,top_bidder:str):
      try:
         if not self.__validate_name(name,self.__list_bid_items): raise Exception('Item already exist')
         current_user = self.get_user_by_id(owner_id)
         if not isinstance(current_user,Seller): raise Exception('User is not a seller')
         category_list:list[Category] = []
         for cat_id in category_id:
            for category in self.__list_categories:
               if category.get_id == cat_id:
                  category_list.append(category)
         if len(category_list) == 0: raise Exception('Category not found')
         self.__list_items.append(BidItem(id,name,price,amount, current_user ,img , category_list ,start_time,end_time,status,top_bidder)) 
         return 'Bid item created'
      except Exception as e:
         raise Exception((str(e)))
   
   # def view_item(self,itemId:str):
   #    for item in self.__list_items :
   #       if item.get_id == itemId  :
   #         return item 
   #    raise Exception('item not ')
   
   def save_item(self, user_id, name: str, price: float, amount: int, category_id: str, img: str):
      if (user_id == '' or name == '' or price == '' or amount == '' or category_id == ''):
         return Exception((str(e)))
      try:
         item_id = str(uuid.uuid4())
         self.create_item(user_id, item_id, name, price, amount, category_id, img)
         return 'Item saved successfully'
      except Exception as e:
         raise Exception(str(e))

   def add_stock(self, user_id, id, amount):
      try:
         if amount <= 0:
               raise ValueError('Amount should be positive')

         item_current = main_system.get_item_by_id(id)
         if not item_current:
               return "Item not found"

         item_current.add_amount(amount)
         return 'Success'
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))

   def edit_item(self, id, name: str, category : str ,description: str, price: int , img : str):
      try:
         if price <= 0:
               raise ValueError('Price should be positive')
         item_current = main_system.get_item_by_id(id)
         if not item_current:
               return "Item not found"

         item_current.edit_item(name , category , description ,price , img)
         return "Item updated successfully"
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))

   def save_bid_item(self, user_id, name: str, price: float, amount: int, category_id: str, img: str, start_time: str, end_time: str):
      try:
         item_id = str(uuid.uuid4())
         main_system.create_bid_item(item_id, name, price, amount, category_id, img, user_id, start_time, end_time, status=None, top_bidder=None)
         return "Save Bid item success"
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))
      
   # def edit_item(self,user_id, name, price, amount, category, image, start_time, end_time) :
   #    try :
      
   #    except:
   #       pass
      

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
   
   #cart and item in cart
   def add_to_cart(self,item_id:str,user_id:str,quantity:int):
      try:
         user = self.get_user_by_id(user_id)
         item = self.get_item_by_id(item_id)
         user.add_to_cart(item,quantity)
         return {"success":True}
      except Exception as e:
         raise Exception(str(e))
      
   def remove_from_cart(self,item_id:str,user_id:str):
      try:
         user = self.get_user_by_id(user_id)
         item = self.get_item_by_id(item_id)
         user.remove_from_cart(item)
         return {'success':True}
      except Exception as e:
         raise Exception(str(e))
      
   def set_select_item(self,item_id:str,user_id:str,select:bool):
      try:
         user = self.get_user_by_id(user_id)
         item = self.get_item_by_id(item_id)
         user.set_select_item(item,select)
         return {'success':True}
      except Exception as e:
         raise Exception(str(e))

   def get_cart(self,user_id:str):
      try:
         user = self.get_user_by_id(user_id)
         return user.get_cart
      except Exception as e:
         raise Exception(str(e))
   
   def add_review(self,item_id:str,rating:int,review:str,user_id:str):
      try:
         user = self.get_user_by_id(user_id)
         if not isinstance(user,Customer): raise Exception('User is not a customer')
         item = self.get_item_by_id(item_id)
         item.add_review(Review(rating,review,user))
         item.show_review()
      except Exception as e:
         raise Exception(str(e))
   
   #buy item in cart
   def buy_item_in_cart(self,user_id:str):
      try:
         user = self.get_user_by_id(user_id)
         order = user.buy_item_in_cart()
         user.add_history(order)
      except Exception as e:
         raise Exception(str(e))
   
def createInstance():
   from .mock.items import items , items_2
   from .mock.bid_items import bid_items
   from .mock.category import categories
   from .mock.users import users
   main_system = System()
   #create category
   [main_system.create_category(category['id'],category['name'],category['description']) for category in categories]
   categories_instane = main_system.get_categories()
   # [print(category) for category in categories_instane]
   #create user
   for user in users:
      if user['role'] == 'admin':
         main_system.create_admin(user['name'],user['user_id'],user['email'],user['phone_number'],user['username'],user['password'],user['birth_date'],user['gender'])
      elif user['role'] == 'customer' or user['role'] == 'seller':
         main_system.create_customer(user['name'],user['user_id'],user['email'],user['phone_number'],user['username'],user['password'],user['birth_date'],user['gender'],user['address'],user['e_bux'])
         if user['role'] == 'seller':
            main_system.create_seller(main_system.get_user_by_id(user['user_id']),user['store_name'],user['store_address'])
   [print(user) for user in main_system.get_users()]
   #create item
   print("---############### create item ############---")
   for item in items:
      print(f"id item is {item['id']} ")
      main_system.create_item('sell001', item['id'],item['name'],item['price'],item['amount'],['1','2'],item['image'])
   for item in items_2:
      print(f"id item is {item['id']} ")
      main_system.create_item('sell002', item['id'],item['name'],item['price'],item['amount'],['1','2'],item['image'])     
      
   items_instance = main_system.get_items()
   [print(f'item is {item}') for item in items_instance]
   # print('result of search by category',main_system.get_items_by_category(main_system.get_categories()[0].get_id))
   print('result of search item by id',main_system.get_item_by_id(items_instance[0].get_id))
   #create item in cart
   print("---############ item in cart #############---")
   # add item
   print(main_system.add_to_cart('2','cust001',2))
   try:
      print(main_system.add_to_cart('2','cust001',100))
   except Exception as e: print(str(e))
   print(main_system.add_to_cart('3','cust001',2))
   print(main_system.add_to_cart('4','cust001',2))
   print("item added",[cart.get_item.get_name for cart in main_system.get_cart('cust001').get_list_item_in_cart])
   #remove item
   print(main_system.remove_from_cart('3','cust001'))
   print("remove item(3)",[cart.get_item.get_name for cart in main_system.get_cart('cust001').get_list_item_in_cart])
   # set item selected
   print(main_system.set_select_item('2','cust001',True))
   print("set item(2) select to true",[f'{cart.get_item.get_id} is {cart.get_is_selected}' for cart in main_system.get_cart('cust001').get_list_item_in_cart])
   #create bid item
   print("---############ bid item #############---")
   for bid_item in bid_items:
      main_system.create_bid_item(bid_item['id'], bid_item['name'], bid_item['price'], bid_item['amount'], ['10'], bid_item['image'] ,'sell001', bid_item['start_time'], bid_item['end_time'], bid_item['status'], bid_item['top_bidder'])
   bid_items_instance = main_system.get_bid_items()
   [print(bid_item) for bid_item in bid_items_instance]
   #test buy item in cart
   print("---###### buy item in cart of user cust001 #####---")
   main_system.buy_item_in_cart('cust001')
   print(main_system.get_user_by_id('cust001').get_order_history[0].get_order)
   
   return main_system

main_system = createInstance()