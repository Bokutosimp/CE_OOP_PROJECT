class Category:
   def __init__(self,ID:str,name:str,description:str):
      self.__ID = ID
      self.__name = name
      self.__description = description
   def __str__(self):
      return f"ID: {self.__ID}\nName: {self.__name}\nDescription: {self.__description}"
   
   @property
   def get_id(self):
      return self.__ID
   @property
   def get_name(self):
      return self.__name