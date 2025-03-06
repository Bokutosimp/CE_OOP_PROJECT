from functools import wraps
from fasthtml.common import Response
def auth(roles):
    def decorator(f):
        @wraps(f)
        def wrapper(session,*args,**kwargs):
            try:
                user_role =session['auth'][1]
            except KeyError:
                return Response('not authorized',status_code=401)
            for role in roles:
               if role == user_role:
                  return f(session,*args,**kwargs)
            return Response('forbidden',status_code=403)
        return wrapper
    return decorator