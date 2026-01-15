from datetime import datetime
import csv
from src.utils import load_expenses, save_expenses, get_current_month

def add_transaction(amount, category, transaction_type):
    expenses = load_expenses()

    transaction = {
        "amount": amount,
        "category": category,
        "type": transaction_type,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(transaction)
    save_expenses(expenses)

def monthly_summary():
    expenses = load_expenses()
    month = get_current_month()

    income = 0
    expense = 0

    for item in expenses:
        if item["date"].startswith(month):
            if item["type"] == "income":
                income += item["amount"]
            else:
                expense += item["amount"]

    return income, expense, income - expense

def export_to_csv():
    expenses = load_expenses()
    with open("exports/expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "type", "category", "amount"]
        )
        writer.writeheader()
        writer.writerows(expenses)
