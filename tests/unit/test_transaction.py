from app.schemas import TransactionCreate, TransactionType
import pytest
from pydantic import ValidationError


def test_transaction_amount_validation():
    transaction = TransactionCreate(
        amount=31.90,
        transaction_type="income"
    )

    assert transaction.amount == 31.90


def test_transaction_amount_rejects_zero():
    with pytest.raises(ValidationError):
        TransactionCreate(amount=0)


def test_transaction_amount_rejects_negative():
    with pytest.raises(ValidationError):
        TransactionCreate(amount=-10.00)


def test_transaction_amount_rejects_non_numeric():
    with pytest.raises(ValidationError):
        TransactionCreate(amount="invalid")


def test_transaction_type_validation():
    transaction = TransactionCreate(
        amount=31.90,
        transaction_type=TransactionType.income
    )

    assert transaction.transaction_type == TransactionType.income


def test_transaction_type_rejects_invalid_value():
    with pytest.raises(ValidationError):
        TransactionCreate(
            amount=31.90,
            transaction_type="invalid"
        )

