import pytest
from app.main import BankAccount

def test_deposit():
    account = BankAccount(100)
    balance = account.deposit(50)
    assert balance == 150, f"Expected balance 150 but got {balance}"
    print(f"✅ test_deposit passed: New Balance = {balance}")

def test_withdraw():
    account = BankAccount(100)
    balance = account.withdraw(30)
    assert balance == 70, f"Expected balance 70 but got {balance}"
    print(f"✅ test_withdraw passed: New Balance = {balance}")

def test_insufficient_funds():
    account = BankAccount(50)
    balance = account.withdraw(100)
    assert balance == 50, f"Expected balance 50 but got {balance}"
    print(f"✅ test_insufficient_funds passed: Balance unchanged at {balance}")

def test_negative_deposit():
    account = BankAccount(100)
    balance = account.deposit(-10)
    assert balance == 100, f"Expected balance 100 but got {balance}"
    print(f"✅ test_negative_deposit passed: Balance unchanged at {balance}")

def test_negative_withdraw():
    account = BankAccount(100)
    balance = account.withdraw(-10)
    assert balance == 100, f"Expected balance 100 but got {balance}"
    print(f"✅ test_negative_withdraw passed: Balance unchanged at {balance}")