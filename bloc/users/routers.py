from .auth import fastapi_users
from bloc.users.auth import get_user_manager, auth_backend
from bloc.users.schemas import UserCreate, UserRead

# роуты fastapi_users
auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)
password_reset_router = fastapi_users.get_reset_password_router()
