from app.utils.sessioin_decorator import with_session
from sqlmodel import select
from app.models.models import User
from app.utils.auth import get_password_hash, verify_password, create_access_token
from app.schemas.schemas import Token

@with_session
def register_new_user(user_data, *, session):
    if session.exec(select(User).where(User.username == user_data.username)).first():
        return None  
    user = User(
        username=user_data.username,
        hashed_password=get_password_hash(user_data.password),
        role=user_data.role,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@with_session
def login_user(user_credentials, *, session):
    user = session.exec(
        select(User).where(User.username == user_credentials.username)
    ).first()
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        return None
    access_token = create_access_token({"sub": str(user.id), "role": user.role})
    return Token(access_token=access_token, token_type="bearer")

@with_session
def get_all_users_logic(*, session):
    return session.exec(select(User)).all()