from beanie import Document, Indexed, Link
from typing import Optional
import pymongo
from pydantic import Field, field_validator, ValidationError, ValidationInfo, UUID4
import uuid
from fastapi_users.db import BeanieUserDatabase, BeanieBaseUser
