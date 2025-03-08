from functools import wraps
from fasthtml.common import Response

def auth(roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            session = kwargs.get('session')
            if session is None:
                for arg in args:
                    if isinstance(arg, dict) and 'auth' in arg:
                        session = arg
                        break
        
            if session is None or 'auth' not in session:
                return Response('not authorized', status_code=401)
        
            user_role = session['auth'][1]
            if user_role in roles:
                return f(*args, **kwargs)

            return Response('forbidden', status_code=403)

        return wrapper
    return decorator
