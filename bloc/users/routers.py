import uuid

from fastapi_users import FastAPIUsers

from bloc.users.auth import get_user_manager, auth_backend
from bloc.users.schemas import UserCreate, UserRead

from .models import User

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
password_reset_router = fastapi_users.get_reset_password_router()
