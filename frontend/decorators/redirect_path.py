from fasthtml.common import *
from functools import wraps
def redirect_path(f):
   @wraps(f)
   def wrapper(session,*args,**kwargs):
      try:
         session['auth']
         return Redirect('/')
      except:
         return  f(session,*args,**kwargs)
   return wrapper
