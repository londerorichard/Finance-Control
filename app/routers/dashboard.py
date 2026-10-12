from fastapi import APIRouter, HTTPException 
from app.schemas import DashboardSummary, CategorySummary, RecentTransaction
from app.services.dashboard_service import get_dashboard_summary, get_recent_transactions
from app.services.user_service import get_user_by_id

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/get_summary/{user_id}", response_model=DashboardSummary)
def get_dashboard_summary_endpoint(user_id: int):

    user = get_user_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=404, detail="User not found"
        )

    summary = get_dashboard_summary(user_id)

    balance = summary["total_income"] - summary["total_expenses"]

    return{
        "total_income": summary["total_income"],
        "total_expenses": summary["total_expenses"],
        "balance": balance,
        "transaction_count": summary["transaction_count"]
    }


@router.get("/get_latest_transactions/{user_id}",response_model=list[RecentTransaction])
def get_latest_transactions_endpoint(user_id: int):

    user = get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    latest_transactions = get_recent_transactions(user_id)

    return [dict(transaction) for transaction in latest_transactions]




