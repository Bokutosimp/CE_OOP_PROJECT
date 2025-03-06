from fasthtml.common import *
from component.nav import nav

def layout(content,session):
   return Body(
      nav(session),
      content(),
      style=""""""
   )