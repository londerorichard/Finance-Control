from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field
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
    amount: float
    transaction_type: TransactionType
    description: str | None = None
    category_id: int | None = None
    account: str | None = None


class TransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    transaction_type: TransactionType
    description: str | None
    created_at: datetime
    category_id: int | None
    account: str | None

class TransactionUpdate(BaseModel):
    amount: float
    transaction_type: TransactionType
    description: str | None = None
    category_id: int | None = None
    account: str | None = None


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
    amount: float
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