from fasthtml.common import *
from component.nav import nav

def layout(content):
   return Body(
      nav(),
      content,
      style=""""""
   )