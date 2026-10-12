from fastapi import APIRouter, Depends
from app.services.charts_service import income_vs_expense_chart, category_expenses_chart, monthly_balance_chart
from app.schemas import MonthlyBalance, MonthlyIncomeExpenses, CategoryExpense, SavingsData
from app.auth.dependency import get_current_user 


router = APIRouter(prefix="/charts", tags=["Charts"])


@router.get("/income-expense", response_model=list[MonthlyIncomeExpenses])
def income_expense_api(user_id: int = Depends(get_current_user)):

    balance = income_vs_expense_chart(user_id)
    return balance


@router.get("/category_expenses", response_model=list(CategoryExpense))
def category_expenses_api(user_id: int = Depends(get_current_user)):

    categories_balance = category_expenses_chart(user_id)
    return categories_balance


@router.get("/monthly_balance", response_model=list[MonthlyBalance])
def monthly_balance_api(user_id: int = Depends(get_current_user)):

    monthly_balances = monthly_balance_chart(user_id)
    return monthly_balances
