from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


# ==========================================================
# USER SCHEMAS
# ==========================================================

class UserCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    ) 
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=64,
        description="User password",
        examples=["MyPassword123"]
    )


class UserResponse(BaseModel):
    id: int
    name: str = Field(
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    )
    email: EmailStr


class PasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="User full name",
        examples=["Richard"]
    )

    email: EmailStr | None = Field(
        default=None,
        description="User email",
        examples=["richard@example.com"]
    )


# class RefreshToken(BaseModel):
#     refresh_token: str


# ==========================================================
# TRANSACTION SCHEMAS
# ==========================================================

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class TransactionCreate(BaseModel):
    user_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str = Field(
        min_length=1,
        max_length=200
    )
    category_id: int = Field(gt=0)
    account: str = Field(
        min_length=1,
        max_length=50
    )


class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    transaction_type: TransactionType
    description: str
    created_at: datetime
    category_id: int
    account: str


# ==========================================================
# CATEGORY SCHEMAS
# ==========================================================

class CreateCategory(BaseModel):
    name: str = Field(
            min_length=2,
            max_length=50,
            description="User full name",
            examples=["Income"]
        )

    user_id: int
    
class UpdateCategory(BaseModel):
    name: str = Field(
            min_length=2,
            max_length=50,
            description="User full name",
            examples=["Income"]
        )
    
class ResponseCategory(BaseModel):
    id: int
    name: str


# ==========================================================
# GOAL SCHEMAS
# ==========================================================




# GoalCreate
# GoalResponse