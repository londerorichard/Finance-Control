from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from enum import Enum


# ==========================================================
# USER SCHEMAS
# ==========================================================

class UserCreate(BaseModel):
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
    email: EmailStr


class PasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    email: EmailStr | None = Field(
        default=None,
        description="User email",
        examples=["richard@example.com"]
    )


class Token(BaseModel):
    access_token: str
    token_type: str
    

# class RefreshToken(BaseModel):
#     refresh_token: str


# ==========================================================
# TRANSACTION SCHEMAS
# ==========================================================

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"


class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str | None = None
    category_id: int | None = None
    account: str | None = None


class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str | None
    created_at: datetime
    category_id: int | None
    account: str | None

class TransactionUpdate(BaseModel):
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str | None = None
    category_id: int | None = None
    account: str | None = None


# ==========================================================
# CATEGORY SCHEMAS
# ==========================================================

class CategoryBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        description="Category name",
        examples=["Food"]
    )
    icon: str | None = None
    color: str | None = None

class CreateCategory(CategoryBase):
    parent_id: int | None = None
    
class UpdateCategory(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
        description="Category name",
        examples=["Food"]
    )
    icon: str | None = None
    color: str | None = None
    
class ResponseCategory(BaseModel):
    id: int
    name: str
    user_id: int
    type: str
    icon: str | None = None
    color: str | None = None
    parent_id: int | None = None
    is_default: bool

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# DASHBOARD SCHEMAS
# ==========================================================

class DashboardSummary(BaseModel):
    total_income: float
    total_expenses: float
    balance: float
    transaction_count: int

class CategorySummary(BaseModel):
    category_name: str
    total_spent: float

class RecentTransaction(BaseModel):
    id: int
    amount: float = Field(gt=0)
    transaction_type: TransactionType
    description: str | None
    created_at: datetime
    account: str | None
    category_name: str | None


# ==========================================================
# CHARTS SCHEMAS
# ==========================================================

class MonthlyIncomeExpenses(BaseModel):
    month: date
    monthly_income: float
    monthly_expenses: float

class CategoryExpense(BaseModel):
    category_id: int | None
    category_name: str
    total_expenses: float

class MonthlyBalance(BaseModel):
    month: date
    monthly_income: float
    monthly_expenses: float
    monthly_balance: float

class SavingsData(BaseModel):
    month: date
    monthly_savings: float
    cumulative_savings: float


# ==========================================================
# GOAL SCHEMAS
# ==========================================================

# GoalCreate
# GoalResponse