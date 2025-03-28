from .category import Category
from typing import Literal
from datetime import datetime
from .order import Order,OrderHistory,ShippingStatus
from datetime import datetime,timedelta

class Item:
   def __init__(self,id:str,name :str , price:float,amount:int, owner:object,image:str,category:list[Category],description:str):
      self.__id = id
      self.__name = name
      self.__price = price
      self.__amount = amount
      self.__image = image
      if not isinstance(owner,Seller): raise Exception('owner should be seller')
      self.__owner = owner
      self.__category = category
      self.__review = []
      self.__description = description
   
   def __str__(self):
      return f"ID: {self.__id}\nName: {self.__name}\nPrice: {self.__price}\nAmount: {self.__amount}\nOwner: {self.__owner}\nCategory: {self.__category} \n description: {self.__description}"
      
   @property
   def get_id(self) -> str:
      return self.__id
   @property 
   def get_name(self)-> str:
      return self.__name
   @property
   def get_category(self) -> list[Category]:
      return self.__category
   @property
   def get_price(self) -> float:
      return self.__price
   @property
   def get_amount(self) -> int:
      return self.__amount
   @get_amount.setter
   def set_amount(self,amount:int): self.__amount = amount
   @property
   def get_image(self) -> str:
      return self.__image
   @property
   def get_owner(self) -> object :
      return self.__owner
   @property
   def get_review(self) -> list:
      return self.__review
   @property
   def get_description(self) -> str:
      return self.__description
   
   def show_review(self) -> str:
      for review in self.__review:
         print(review)
      print(len(self.__review))
   
   def add_amount(self , amount) :
      self.__amount += amount 

   def edit_item(self, name:str , category:list[Category] ,desciption:str , price:float , img:str ) :
      self.__name = name 
      self.__price = price
      self.__category = category
      self.__image = img
      self.__description = desciption
      
   def edit_item_name(self , new_name) :
      self.__name = new_name

   def edit_item_price(self, new_price):
      self.__price = new_price

   def edit_category(self, new_category):
      self.__category = new_category

   def edit_describtion(self, new_describtion):
      self.__description = new_describtion

   def check_availability(self,quantity:int) -> bool:
      return quantity <= self.__amount
   
   def add_review(self, rating:int,review:str,user:object):
      self.__review.append(Review(rating,review,user))
      
   @property
   def get_average_score(self):
      if len(self.__review) == 0: return None
      return sum(review.get_score for review in self.__review)/len(self.__review)
      
class ItemInCart:
   def __init__(self,item:Item,amount_in_cart:int,is_selected:bool):
      self.__item = item
      self.__amount_in_cart = amount_in_cart
      self.__is_selected = is_selected
      
   def __str__(self):
      return f"item:{self.__item}, amount:{self.__amount_in_cart}, isSelected:{self.__is_selected}"
   
   @property
   def get_item(self) -> Item: return self.__item
   
   @property
   def get_amount_in_cart(self) -> int: return self.__amount_in_cart
   @get_amount_in_cart.setter
   def set_amount_int_cart(self,quantity:int): self.__amount_in_cart = quantity
   @property
   def get_is_selected(self) -> bool: return self.__is_selected
   @get_is_selected.setter
   def set_is_selected(self,select:bool): self.__is_selected = select
   

class Cart:
   def __init__(self):
      self.__list_item_in_cart:list[ItemInCart] = []

   def __str__(self):
      return f'{[cart for cart in self.__list_item_in_cart]}'  
   
   @property
   def get_list_item_in_cart(self): return self.__list_item_in_cart
   @get_list_item_in_cart.setter
   def set_list_item_in_cart(self,list): self.__list_item_in_cart = list
    
   def add_cart(self,itemInCart:ItemInCart):
      self.__list_item_in_cart.append(itemInCart)
   
   def remove_from_cart(self,index:int):
      self.__list_item_in_cart.pop(index)
      
   def set_select_item(self,index:int,select:bool):
      self.__list_item_in_cart[index].set_is_selected = select
   
class User:
   def __init__(self,name:str,user_id:str,email:str,phone_number:str,username:str,password:str,birth_date:object,gender:Literal['M','F']):
      self.__name = name
      self.__user_id = user_id
      self.__email = email
      self.__phone_number = phone_number
      self.__username = username
      self.__password = password
      self.__birth_date = birth_date
      if gender not in ["M", "F"]:
         raise ValueError("Gender must be 'M' or 'F'")
      self.__gender = gender
      
   def __str__(self):
      return f"Name: {self.__name}\nUser ID: {self.__user_id}\nEmail: {self.__email}\nPhone Number: {self.__phone_number}\nUsername: {self.__username}\nPassword: {self.__password}\nBirth Date: {self.__birth_date}\nGender:{self.__gender}"
   
   @property
   def get_name(self) -> str:
      return self.__name
   @property
   def get_user_id(self) -> str:
      return self.__user_id
   @property
   def get_email(self) -> str:
      return self.__email
   @property
   def get_phone_number(self) -> str:
      return self.__phone_number
   @property
   def get_username(self) -> str:
      return self.__username
   @property
   def get_password(self) -> str:
      return self.__password
   @property
   def get_birth_date(self) -> object:
      return self.__birth_date
   @property
   def get_gender(self) -> str:
      return self.__gender

      
class Admin(User):
   def __init__(self, name, user_id, email, phone_number, username, password, birth_date, gender):
      super().__init__(name, user_id, email, phone_number, username, password, birth_date, gender)
      
   def __str__(self):
      return f"Role:Admin Username:{self.get_username}"
   
      
class Customer(User):
   def __init__(self, name, user_id, email, phone_number, username, password, birth_date, gender,address:str,e_bux:float=0,cart:Cart=Cart()):
      super().__init__(name, user_id, email, phone_number, username, password,birth_date,gender)
      self.__address = address
      self.__e_bux = e_bux
      self.__cart = cart
      self.__order_history = []
      self.__bid_history = []
      
   def __str__(self): return f"Role:customer Username:{self.get_username}"
   @property
   def get_address(self) -> str: return self.__address
   @property
   def get_e_bux(self) -> float: return self.__e_bux
   @get_e_bux.setter
   def set_e_bux(self,e_bux): self.__e_bux = e_bux
   @property
   def get_cart(self) -> Cart: return self.__cart
   @property
   def get_order_history(self) -> list[OrderHistory]: return self.__order_history
   @property
   def get_bid_history(self): return self.__bid_history
   
   def add_history(self,order_history):
      not_selected_items = [item for item in self.__cart.get_list_item_in_cart if not item.get_is_selected]
      self.__cart.set_list_item_in_cart = not_selected_items
      self.__order_history.append(order_history)
      
   def add_bid_history(self,item, ship_time, get_date):
      self.__bid_history.append(BidHistory(item, ShippingStatus(ship_time, get_date)))
   
   def add_to_cart(self,item:Item,quantity:int):
      if quantity < 0: raise Exception('quantity can not be less than or equal to zero')
      if not item.check_availability(quantity): raise Exception('Item out of stock')
      for item_in_cart in self.__cart.get_list_item_in_cart:
         if item_in_cart.get_item == item:
            item_in_cart.set_amount_int_cart = quantity
            return 
      itemInCart = ItemInCart(item,quantity,False)
      self.__cart.add_cart(itemInCart)
   
   def remove_from_cart(self,item:Item):
      for index, item_in_cart in enumerate(self.__cart.get_list_item_in_cart):
         if item_in_cart.get_item == item:
            self.__cart.remove_from_cart(index)
            return
      raise Exception('item not found in cart')
   
   def set_select_item(self,item:Item,select:bool):
      for index,item_in_cart in enumerate(self.__cart.get_list_item_in_cart):
         if item_in_cart.get_item == item:
            self.__cart.set_select_item(index,select)
            return 
      raise Exception('item not found in cart')
   
   def buy_item_in_cart(self):
      buy_list = []
      total_price = 0
      for item in self.__cart.get_list_item_in_cart:
         if item.get_is_selected == True: 
            buy_list.append(item)
            total_price += item.get_item.get_price*item.get_amount_in_cart
      orderClass = Order(10,total_price,buy_list)
      order_history = OrderHistory(orderClass)
      return order_history
   
   def buy_item(self,buy_list:list[ItemInCart],code:object=None,shipping_fee:float=10.0,shipping_date=datetime.now(),get_item_date=datetime.now()+timedelta(seconds=30)):
      total_price = 0
      discount = 0
      if code != None: discount = code.get_discount / 100
      for cart_item in buy_list:
         total_price += round(cart_item.get_item.get_price*cart_item.get_amount_in_cart*(1 - discount),2)
      self.decrease_e_bux(total_price)
      order = Order(10.0, total_price,buy_list)
      shipping_status = ShippingStatus(shipping_date,get_item_date)
      self.add_history(OrderHistory(order,shipping_status))
      for item in buy_list:
         item.get_item.set_amount = item.get_item.get_amount - item.get_amount_in_cart
      return total_price
      
   def decrease_e_bux(self, amount: float):
        if amount > self.__e_bux:
            raise Exception("Insufficient e-bux")
        self.__e_bux -= amount
   
   def is_already_review(self,item:Item):
         for review in item.get_review:
            if review.get_reviewer == self: return True
         return False
   
   def is_buy_item(self,item:Item):
         for history in self.get_order_history:
            for item_usr in history.get_order.get_list_item_select:
               if item_usr.get_item == item: return True
         return False
      
   def add_review(self,item:Item,review:str,rating:int):
         if self.is_already_review(item): raise Exception('user already reviewed')
         if not self.is_buy_item(item): raise Exception('User not buy this item yet')
         item.add_review(rating,review,self)
   # def SeaTung(self,amount):
   #    if amount > self.__e_bux :
   #       return "Nah bro, you're broke af"
   #    else :
   #       self.__e_bux -= amount
   #       return "Buying successfully"
      
class Seller(Customer):
   def __init__(self,customer:Customer,store_name:str,store_address:str):
      super().__init__(customer.get_name, customer.get_user_id, customer.get_email, customer.get_phone_number, customer.get_username, customer.get_password,customer.get_birth_date,customer.get_gender,customer.get_address,customer.get_e_bux,customer.get_cart)
      self.__store_name = store_name
      self.__store_address = store_address

   def __str__(self):
      return f"Role:seller Username:{self.get_username}"
   
   @property
   def get_store_name(self) -> str:
      return self.__store_name
   
   @property
   def get_store_address(self) -> str:
      return self.__store_address 

class BiddingHistory:
   def __init__(self, user: User, bidAmount : float, bidTime : datetime):
      self.__user = user
      self.__bidAmount = bidAmount
      self.__bidTime = bidTime
        
   def __str__(self):
      return f"User ID: {self.__user}\nBid Amount: {self.__bidAmount}\nBid Time: {self.__bidTime}"

class BidItem(Item):
   def __init__(self, id: str, name: str, price: float, amount: int, owner: Seller, image: str, category: list[Category], description:str,start_time: datetime, end_time: datetime, top_bidder=None, status="Not Started"):
      # Call Item's constructor
      super().__init__(id, name, price, amount, owner, image, category,description)
      
      # Explicitly re-assign attributes
      self.__owner = owner  # Ensure owner is correctly assigned
      self.__top_bidder = top_bidder
      self.__bids_history = []
      self.__status = status
      self.__start_time = start_time
      self.__end_time = end_time

   def edit_bid_item(self, name : str, price : float , category : list[Category] , description : str , img : str , start_time : str, end_time : str)  :
      self.edit_item_name(name)
      self.edit_item_price(price)
      self.edit_describtion(description)
      self.edit_category(category)
      self.__start_time = str(datetime.strptime(start_time ,"%y%m-%d-%dT%H:%M"))
      self.__end_time = str(datetime.strptime(end_time ,"%y%m-%d-%dT%H:%M"))

   def __str__(self):
      return super().__str__() + f"\nStart Time: {self.__start_time}\nEnd Time: {self.__end_time}\nStatus: {self.__status}\nTop Bidder: {self.__top_bidder}\nBids History: {self.__bids_history}"
              
   def start(self):
      self.__start_time = datetime.now()
      self.__status = "Started"
      
   def end(self):
      self.__end_time = datetime.now()
      self.__status = "Ended"
      
   @property
   def id(self):
      return self.__id
   
   @property
   def top_bidder(self):
      return self.__top_bidder
   
   @property
   def bids_history(self):
      return self.__bids_history
   
   @property
   def get_start_time(self):
      return self.__start_time 
   
   @property
   def get_end_time(self):
      return self.__end_time
   
   @property
   def get_history(self):
      return self.__bids_history
   
   def set_top_bidder(self, user : User):
      self.__top_bidder = user
      
   def set_new_top_bidder(self, user: User, price: float, time: datetime):
      self.set_top_bidder(user)
      self.edit_item_price(price)
      self.add_history(user,price,time)
   
   def add_history(self, user_id : str, bidAmount : float, bidTime : datetime):
      self.__bids_history.append(BiddingHistory(user_id, bidAmount, bidTime))
      
   @property
   def is_ended(self):
      return self.__status == "Ended"
   
   @property
   def get_status(self):
      if self.__status == "Sold":
         return self.__status
      now = datetime.now()
      if now > self.__end_time :
         self.__status = "Ended"
      return self.__status
   
   def is_price_valid(self, price : float):
      return price > self.__price
   
   def sold(self):
      self.__status = "Sold"
   
class BidHistory:
   def __init__(self,item:BidItem, shipping_status:ShippingStatus):
      self.__item = item
      self.__shipping_status = shipping_status
        
   def __str__(self):
      return f"{self.__item.get_name}\n{self.__shipping_status}"
        
   @property
   def get_shipping_status(self) -> ShippingStatus : return self.__shipping_status
   @property
   def get_order(self) -> Order: return self.__item
   @property
   def get_item(self): return self.__item
   def set_status(self , status : ShippingStatus) :
      self.__shipping_status = status

   # def edit_item(self, name:str , category:list[Category] ,desciption:str , price:float , img:str ) :
   #    self.__name = name 
   #    self.__price = price
   #    self.__category = category
   #    self.__image = img

         
class Review:
   def __init__(self,score:int,comment:str,reviewer:Customer):
      self.__score = score
      self.__comment = comment
      self.__reviewer = reviewer
      
   def __str__(self):
      return f"Score: {self.__score}\nComment: {self.__comment}\nReviewer: {self.__reviewer}"
   @property
   def get_score(self)-> int: return self.__score
   @property
   def get_comment(self) -> str: return self.__comment
   @property
   def get_reviewer(self) -> Customer: return self.__reviewer
      
class Code :
   def __init__(self,ID:str,name:str):
      self.__ID = ID
      self.__name = name
      
   def verify_code(self,input):
      if input == self.__name:
         return True
   
   @property
   def get_id(self):
      return self.__ID
   @property
   def get_name(self):
      return self.__name

   @property
   def get_name(self):
      return self.__name

class Discount(Code):
   def __init__(self,ID:str,name:str,percentage:float,owner:Seller):
      super().__init__(ID,name)
      self.__percentage = percentage
      self.__owner = owner
   
   def __str__(self):
      return f'{self.get_name}'
   
   @property   
   def get_discount(self):
         return self.__percentage
   @property  
   def get_owner(self):
         return self.__owner
   
   @property
   def get_code(self):
      return self.__name