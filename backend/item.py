from .category import Category
from typing import Literal

class Item:
   def __init__(self,id:str,name :str , price:float,amount:int, owner:object,image:str,category:list[Category]):
      self.__id = id
      self.__name = name
      self.__price = price
      self.__amount = amount
      self.__image = image
      if not isinstance(owner,Seller): return "Owner must be a seller"
      self.__owner = owner
      self.__category = category
   
   def __str__(self):
      return f"ID: {self.__id}\nName: {self.__name}\nPrice: {self.__price}\nAmount: {self.__amount}\nOwner: {self.__owner}\nCategory: {self.__category}"
      
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
   @property
   def get_image(self) -> str:
      return self.__image
   def check_availlability(self,quantity:int) -> bool:
      return quantity <= self.__amount


class ItemInCart:
   def __init__(self,item:Item,amount_in_cart:int,isSelected:bool):
      self.__item = item
      self.__amount_in_cart = amount_in_cart
      self.__isSelected = isSelected
      
   def __str__(self):
      return f"item:{self.__item}, amount:{self.__amount_in_cart}, isSelected:{self.__isSelected}"
   
   @property
   def get_item(self) -> Item: return self.__item
   @property
   def get_amount_in_cart(self) -> int: return self.__amount_in_cart
   @get_amount_in_cart.setter
   def set_amount_int_cart(self,quantity:int): self.__amount_in_cart = quantity
   @property
   def get_isSelected(self) -> bool: return self.__isSelected
   
   

class Cart:
   def __init__(self):
      self.__list_item_in_cart:list[ItemInCart] = []

   def __str__(self):
      return f'{[cart for cart in self.__list_item_in_cart]}'  
   
   @property
   def get_list_item_in_cart(self): return self.__list_item_in_cart
    
   def add_cart(self,itemInCart:ItemInCart):
      self.__list_item_in_cart.append(itemInCart)
   
   def remove_from_cart(self,index:int):
      self.__list_item_in_cart.pop(index)
   
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
      return f"Name: {self.__name}\nUser ID: {self.__user_id}\nEmail: {self.__email}\nPhone Number: {self.__phone_number}\nUsername: {self.__username}\nPassword: {self.__password}\nBirth Date: {self.__birth_date}\nGender:"
   
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
      
   def __str__(self): return f"Role:customer Username:{self.get_username}"
   @property
   def get_address(self) -> str: return self.__address
   @property
   def get_e_bux(self) -> float: return self.__e_bux
   @property
   def get_cart(self) -> Cart: return self.__cart
   
   
   def add_to_cart(self,item:Item,quantity:int):
      if quantity < 0: raise Exception('quantity can not be less than or equal to zero')
      if not item.check_availlability(quantity): raise Exception('Item out of stock')
      for item_in_cart in self.__cart.get_list_item_in_cart:
         if item_in_cart.get_item.get_id == item.get_id:
            item_in_cart.set_amount_int_cart = quantity
            return 
      itemInCart = ItemInCart(item,quantity,False)
      self.__cart.add_cart(itemInCart)
   
   def remove_from_cart(self,item:Item):
      for index, item_in_cart in enumerate(self.__cart.get_list_item_in_cart):
         if item_in_cart.get_item.get_id == item.get_id:
            self.__cart.remove_from_cart(index)
            return
      raise Exception('item not found in cart')
   
   def SeaTung(self,amount):
      if amount > self.__e_bux :
         return "Nah bro, you're broke af"
      else :
         self.__e_bux -= amount
         return "Buying successfully"
      
class Seller(Customer):
   def __init__(self,customer:Customer,store_name:str,store_address:str):
      super().__init__(customer.get_name, customer.get_user_id, customer.get_email, customer.get_phone_number, customer.get_username, customer.get_password,customer.get_birth_date,customer.get_gender,customer.get_address,customer.get_e_bux,customer.get_cart)
      self.__store_name = store_name
      self.__store_address = store_address

   def __str__(self):
      return f"Role:seller Username:{self.get_username}"

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