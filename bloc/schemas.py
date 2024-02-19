from typing import Optional
import uuid
from pydantic import BaseModel, Field, UUID4
from fastapi_users import schemas as s


class Response(BaseModel):
    detail: str
