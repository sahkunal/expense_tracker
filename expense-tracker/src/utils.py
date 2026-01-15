import json
from datetime import datetime

DATA_FILE = "data/expenses.json"

def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def get_current_month():
    return datetime.now().strftime("%Y-%m")
