from fasthtml.common import *
from backend import *

app , rt = fast_app()

@rt('/')
def get():
   return Main