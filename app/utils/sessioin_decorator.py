from functools import wraps
from app.database.database import get_session

def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Use get_session generator to create a session
        session_gen = get_session()
        session = next(session_gen)
        try:
            result = func(*args, session=session, **kwargs)
            return result
        finally:
            session.close()
    return wrapper