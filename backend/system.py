from .category import Category
from datetime import datetime
from .order import Order,ShippingStatus,OrderHistory
from datetime import datetime,timedelta
from .item import Item,BidItem,User,Code,Customer,Seller,Admin,Cart,Review , Discount , FreeDelivery
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
      raise Exception('user or password incorrect')
   
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
         if str(cat.get_id) == str(id):
            return cat
      raise Exception('Not found')
   
   def get_codes(self, query: str = '') -> list[Code]:
      if query == '':
         return self.__list_codes
      else:
         return [code for code in self.__list_codes if query.lower() in code.get_name.lower()]
   
   def get_code_by_id(self, id: str) -> Code:
      for code in self.__list_codes:
         if str(code.get_id) == str(id):
            return code
      raise Exception('Code not found')

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
            if str(category.get_id) == str(category_id):
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
      for item in self.__list_users:
         if item.get_email == email:
            raise Exception('email already exist')
      for item in self.__list_users:
         if item.get_username == username:
            raise Exception('username already exist')
      print('test creat user')
      cart = Cart()
      self.__list_users.append(Customer(name, user_id, email, phone_number, username, password, birth_date,gender,address,e_bux,cart))
      return 'Customer created'
   
   def create_seller(self,customer:Customer,store_name:str,store_address:str):
      for i in range(len(self.__list_users)):
         if self.__list_users[i].get_user_id == customer.get_user_id and isinstance(self.__list_users[i],Customer):
            self.__list_users[i] = Seller(customer,store_name,store_address)
            return 'Seller created'  
      
   def create_discount_code(self,ID:str, name:str, discount_percent:float,seller:Seller):
      if not self.__validate_name(name,self.__list_codes): raise Exception('Name already exist')
      self.__list_codes.append(Discount(ID,name,discount_percent,seller))
      return 'Code created'
   def apply_code(self, code: str):
      for Dcode in self.__list_codes:
         print(f"Checking code: {Dcode.get_name} against provided code: {code}")
         if Dcode.get_name == code:
            discount = Dcode.get_discount / 100
            return discount
      raise Exception('Invalid discount code')
   def create_item(self,current_user_id:str,id:str,name:str, price:float, amount:int,category_id:list[str],img='',description:str=''):
      try:
         result = self.__validate_name(name,self.__list_items)
         if not result: raise Exception('item already exist')
         current_user = self.get_user_by_id(current_user_id)
         if not isinstance(current_user,Seller): raise Exception('User is not a seller')
         category_list:list[Category] = []
         for cat_id in category_id:
            for category in self.__list_categories:

               print(f"{category.get_id} and {cat_id}" , str(category.get_id) == str(cat_id))
               if str(category.get_id) == str(cat_id):
                  category_list.append(category)
         
         if len(category_list) == 0: raise Exception('Category not found')
         self.__list_items.append(Item(id,name,price,amount,current_user,img,category_list,description))
         return {'success':True}
      except Exception as e:
         raise Exception((str(e)))
   
   def create_bid_item(self,id:str,name:str, price:float, amount:int,category_id:list[str],img:str,owner_id:str,start_time:str,end_time:str,status:str,top_bidder:str,description:str=''):
      try:
         if not self.__validate_name(name,self.__list_bid_items): raise Exception('Item already exist')
         current_user = self.get_user_by_id(owner_id)
         if not isinstance(current_user,Seller): raise Exception('User is not a seller')
         category_list:list[Category] = []
         for cat_id in category_id:
            for category in self.__list_categories:
               print(f"{category.get_id} and {cat_id}" , str(category.get_id) == str(cat_id))
               if str(category.get_id) == str(cat_id):
                  category_list.append(category)
         if len(category_list) == 0: raise Exception('Category not found')
         self.__list_items.append(BidItem(id,name,price,amount, current_user ,img , category_list ,description,start_time,end_time,status,top_bidder)) 
         return 'Bid item created'
      except Exception as e:
         raise Exception((str(e)))
   
   # def view_item(self,itemId:str):
   #    for item in self.__list_items :
   #       if item.get_id == itemId  :
   #         return item 
   #    raise Exception('item not ')
   
   def save_item(self, user_id, name: str, price: float, amount: int, category_id: str, description : str, img: str):
      if (user_id == '' or name == '' or price == '' or amount == '' or category_id == ''):
         return Exception((str(e)))
      try:
         item_id = str(uuid.uuid4())
         self.create_item(user_id, item_id, name, price, amount, category_id, img , description )
         return 'Item saved successfully'
      except Exception as e:
         raise Exception(str(e))

   def add_stock(self, user_id, id, amount):
      try:
         if amount <= 0:
               raise ValueError('Amount should be positive')
         

         item_current = main_system.get_item_by_id(id)
         
         print(f"wow : {user_id}")
         print(f"wow : {id}")
         print(f"wow : {amount}")
         if not item_current:
               return "Item not found"

         item_current.add_amount(amount)
         return 'Success'
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))
      
   def add_bid_stock(self, user_id, id, amount):
      try:
         if amount <= 0:
               raise ValueError('Amount should be positive')
         item_current = main_system.get_bid_item_by_id(id)
         print(item_current)

         print(f"bid : {user_id}")
         print(f"bid : {id}")
         print(f"bid : {amount}")
         if not item_current:
               return "Item not found"

         item_current.add_amount(amount)
         return 'Success'
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))
      
   

   def edit_item(self, id:str, name: str, category : list[str] ,description: str, price: int , img : str):
      try:
         if price <= 0:
               raise ValueError('Price should be positive')
         item_current = main_system.get_item_by_id(id)
         cat_instaces  = []
         for cat in self.__list_categories:
            for cat_id in category:
               if str(cat_id) == str(cat.get_id): cat_instaces.append(cat)
         item_current.edit_item(name , cat_instaces , description ,price , img)
         return "Item updated successfully"
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))

   def save_bid_item(self, user_id, name: str, price: float, amount: int, category_id: str, img: str, start_time: str, end_time: str , new_description : str):
      try:
         item_id = str(uuid.uuid4())
         
         main_system.create_bid_item(item_id, name, price, amount, category_id, img, user_id, start_time, end_time, status=None, top_bidder=None , description=new_description )
         print(main_system.get_bid_item_by_id(item_id)) 
         return "Save Bid item success"
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))
      
   def edit_bid_item(self, id:str, name: str, category : list[str] ,description: str, price: int , img : str, start_time : str , end_time : str):
         try:
            if price <= 0:
                  raise ValueError('Price should be positive')
            item_current = main_system.get_bid_item_by_id(id)
            cat_instaces  = []
            for cat in self.__list_categories:
               for cat_id in category:
                  if str(cat_id) == str(cat.get_id): cat_instaces.append(cat)
            item_current.edit_bid_item(name , price , cat_instaces , description , img , start_time ,end_time )
            return "Item updated successfully"
         except Exception as e:
            raise Exception(str(e))
         except ValueError as e:
            raise ValueError(str(e))

      

   def save_discount_code(self,name , discount_percent,description):
      try:
            ID = str(uuid.uuid1)
            if not isinstance(discount_percent, (int, float)) or discount_percent <= 0 or discount_percent > 100:
                raise ValueError("Discount percent must be a number between 1 and 100")
            new_discount_code = Discount(ID, name, discount_percent, description)
            self.__list_codes.append(new_discount_code)
            return "Discount code saved successfully"
      except Exception as e:
         raise Exception(str(e))
      except ValueError as e:
         raise ValueError(str(e))

   def get_top_bidder(self, item_id:str):
      for item in self.__list_items:
         if item.get_id == item_id:
            return item.get_top_bidder
         
   def set_top_bidder(self, item_id:str,bid_input:float, user:User):
      now = datetime.now()
      now = now.replace(microsecond=0)
      for item in self.__list_items:
         if str(item.get_id) == str(item_id):
            item.set_new_top_bidder(user, bid_input, now)
            item.show_history()
            return 'Top bidder set'
         
   def start_bid(self, item_id:str):
      for item in self.__list_items:
         if item.get_id == item_id:
            item.start_bid()
            return 'Bid started'
         
   def end_bid(self, item_id:str):
      for item in self.__list_items:
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
         
   def is_bid_item(self, item) -> bool:
       return isinstance(item, BidItem)


   def is_discount_code(self, code) -> bool:
      return isinstance(code, Discount)

      


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
   
   def add_review(self,item_id:str,rating:int,review:str,user:User):
      try:
         if not isinstance(user,Customer): raise Exception('User is not a customer')
         item = self.get_item_by_id(item_id)
         item.add_review(rating,review,user)
         item.show_review()
      except Exception as e:
         raise Exception(str(e))
      
   def buy_cart_check_stock(self,user_id:str): # return price of selected product
      try:
         user = self.get_user_by_id(user_id)
         # check_stock = Order.check_cart_with_stock(self,user)
         total_price = sum((round(item.get_item.get_price * item.get_amount_in_cart, 3) if item.get_is_selected else 0) for item in user.get_cart.get_list_item_in_cart)
         # Order(10.0, total_price, [item for item in user.get_cart.get_list_item_in_cart if item.get_is_selected])
         return total_price
      except Exception as e:
         raise Exception(str(e))
      
   def buy_item_with_code(self, user_id: str, code: str,shipping_date=datetime.now(),get_item_date=datetime.now()+timedelta(minutes=5)):
    try:
      user = self.get_user_by_id(user_id)
      discount = self.apply_code(code)
      total_price = self.buy_cart_check_stock(user_id)
      discounted_price = total_price * (1 - discount)
      order = Order(10.0, discounted_price, [item for item in user.get_cart.get_list_item_in_cart if item.get_is_selected])
      shipping_status = ShippingStatus(shipping_date,get_item_date)
      for Dcode in self.__list_codes:
         if Dcode.get_name == code:
            order.set_apply_code = Dcode
            break
      user.add_history(OrderHistory(order,shipping_status))
      user.decrease_e_bux(discounted_price)
      return discounted_price
    except Exception as e:
        raise Exception(str(e))
   
   #buy item in cart
   def buy_item_in_cart(self,user_id:str,code:str=None,shipping_date=datetime.now(),get_item_date=datetime.now()+timedelta(minutes=5)):
      try:
         if code != None and code != '':
            return self.buy_item_with_code(user_id,code,shipping_date,get_item_date)
         user = self.get_user_by_id(user_id)
         total_price = self.buy_cart_check_stock(user_id)
         order = Order(10.0, total_price, [item for item in user.get_cart.get_list_item_in_cart if item.get_is_selected])
         shipping_status = ShippingStatus(shipping_date,get_item_date)
         user.add_history(OrderHistory(order,shipping_status))
         user.decrease_e_bux(total_price)
         return total_price
      except Exception as e:
         raise Exception(str(e))
      
   #get history for user 
   #get status as shipping (check from get_date_time in Shippinstatus)
   def get_shipping_items(self,user_id:str) -> list[OrderHistory]:
      user = self.get_user_by_id(user_id)
      history = user.get_order_history
      history_list:list[OrderHistory] = []
      now = datetime.now()
      for his in history:
         if his.get_shipping_status.get_get_item_date > now:
            history_list.append(his) 
      return history_list
      
   def get_history_items(self,user_id:str) -> list[OrderHistory]:
      user = self.get_user_by_id(user_id)
      history = user.get_order_history
      history_list:list[OrderHistory] = []
      now = datetime.now()
      for his in history:
         if his.get_shipping_status.get_get_item_date < now:
            history_list.append(his) 
      return history_list
   
def createInstance():
   from .mock.items import items , items_2
   from .mock.bid_items import bid_items
   from .mock.category import categories
   from .mock.users import users
   from .mock.discount_codes import discount_codes
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
      main_system.create_item('sell001', item['id'],item['name'],item['price'],item['amount'],['1','2'],item['image'],item['description'])
   for item in items_2:
      print(f"id item is {item['id']} ")
      main_system.create_item('sell002', item['id'],item['name'],item['price'],item['amount'],['1','2'],item['image'],item['description'])     
   print("---############### create discount codes ############---")
   seller = main_system.get_user_by_id('sell001')
   for discount_code in discount_codes:
      main_system.create_discount_code(discount_code['id'],discount_code['name'], discount_code['discount_percent'],seller)
      print(f"Discount code {discount_code['name']} created")
   
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
   start_bid_time = datetime.now()
   start_bid_time = start_bid_time.replace(microsecond=0)
   increase_time = 5  # Initial increment in minutes
   for bid_item in bid_items:
      end_bid_time = start_bid_time + timedelta(minutes=increase_time)  
      main_system.create_bid_item(
         bid_item['id'], bid_item['name'], bid_item['price'], bid_item['amount'], 
         ['10'], bid_item['image'], 'sell001', start_bid_time, end_bid_time, 
         bid_item['top_bidder'], bid_item['status']
      )
    # Update start time for the next bid
      increase_time += 5
      # main_system.create_bid_item(bid_item['id'], bid_item['name'], bid_item['price'], bid_item['amount'], ['10'], bid_item['image'] ,'sell001', datetime.strptime(bid_item['start_time'], "%Y-%m-%d %H:%M:%S"), datetime.strptime(bid_item['end_time'], "%Y-%m-%d %H:%M:%S"), bid_item['status'], bid_item['top_bidder'])
   bid_items_instance = main_system.get_items()
   for item in bid_items_instance:
      if isinstance(item,BidItem): print(item)
   
   #test buy item in cart
   print("---###### buy item in cart of user cust001 #####---")
   user = main_system.get_user_by_id('cust001')
   print(f"User money before purchase: {user.get_e_bux}")
   check_stock = main_system.buy_cart_check_stock('cust001')
   print("return price :", check_stock, "E")
   confirm_purchase = main_system.buy_item_with_code('cust001', 'SUMMER_SALE')
   print("Discounted price:", confirm_purchase)
   print(f"User money after purchase: {user.get_e_bux}")
   now = datetime.now()
   main_system.add_to_cart('5','cust001',2)
   main_system.set_select_item('5','cust001',True)
   print(f"try create history by buy item in past {main_system.buy_item_in_cart('cust001','SUMMER_SALE',now-timedelta(minutes=10),now-timedelta(minutes=5))}")
   print(f"update user cart {[item.get_item.get_name for item in user.get_cart.get_list_item_in_cart]}")
   print(f"get shipping item \n {main_system.get_shipping_items('cust001')[0].get_shipping_status}")
   print(f"get history of item \n {main_system.get_history_items('cust001')[0].get_shipping_status}")
   print(f"get order in history\n {main_system.get_history_items('cust001')[0].get_order.get_list_item_select}")
   
   return main_system

main_system = createInstance()