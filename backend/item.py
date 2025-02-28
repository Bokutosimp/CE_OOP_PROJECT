
class Item:
   def __init__(self,id:str,name :str , price:float,amount:int, owner:object) :
      self.__id = id
      self.__name = name
      self.__aprice = price
      self.__amount = amount
      if not isinstance(owner,Seller): return "Owner must be a seller"
      self.__owner = owner
      self.__category = None
      
   def check_availlability(self,quantity:int):
      pass

class ItemInCart:
   def __init__(self,item:Item,amount_in_cart:int,isSelected:bool):
      self.__item = item
      self.__amount_in_cart = amount_in_cart
      self.__isSelected = isSelected

class Cart:
   def __init__(self):
      self.__list_item_in_cart:list[ItemInCart] = []
   
class User:
   def __init__(self,name:str,user_id:str,email:str,phone_number:str,username:str,password:str,birth_date:object,gender:str):
      self.__name = name
      self.__user_id = user_id
      self.__email = email
      self.__phone_number = phone_number
      self.__username = username
      self.__password = password
      self.__birth_date = birth_date
      self.__gender = gender
      
   def __str__(self):
      return f"Name: {self.__name}\nUser ID: {self.__user_id}\nEmail: {self.__email}\nPhone Number: {self.__phone_number}\nUsername: {self.__username}\nPassword: {self.__password}\nBirth Date: {self.__birth_date}\nGender:"
      
class Admin(User):
   def __init__(self, name, user_id, email, phone_number, username, password, birth_date, gender):
      super().__init__(name, user_id, email, phone_number, username, password, birth_date, gender)
      
class Customer(User):
   def __init__(self, name, user_id, email, phone_number, username, password, birth_date, gender,address:str,e_bux:float,cart:Cart):
      super().__init__(name, user_id, email, phone_number, username, password,birth_date,gender)
      self.__address = address
      self.__e_bux = e_bux
      self.__cart = cart
      
   def SeaTung(self,amount):
      if amount > self.__e_bux :
         return "Nah bro, you're broke af"
      else :
         self.__e_bux -= amount
         return "Buying successfully"
   
   def view_cart(self):
      pass
   
   def add_to_cart(self,item:Item):
      #call check_availlability
      #true --> add to cart
      #false --> item out of stock
      pass
      
class Seller(Customer):
   def __init__(self, name, user_id, email, phone_number, username, password, birth_date,gender,address:str,e_bux:float,store_name:str,store_address:str):
      super().__init__(name, user_id, email, phone_number, username, password,birth_date,gender,address,e_bux)
      self.__store_name = store_name
      self.__store_address = store_address


   def add_item(self,name : str, price : float, amount : int, category : str):
      pass

   def add_stock(self ,name : str , amount):
      pass

   def add_bid_item(self, name:str , start_price , amount : int , category : str):
      pass

   def create_discount_code(self,ID, discount_percent):
      pass
   
   def confirm_bid():
      pass