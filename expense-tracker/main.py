from src.tracker import add_transaction, monthly_summary, export_to_csv

def menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Monthly Summary")
    print("4. Export to CSV")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        add_transaction(amount, category, "income")
        print("Income added successfully.")

    elif choice == "2":
        amount = float(input("Amount: "))
        category = input("Category: ")
        add_transaction(amount, category, "expense")
        print("Expense added successfully.")

    elif choice == "3":
        income, expense, balance = monthly_summary()
        print(f"Income: ₹{income}")
        print(f"Expense: ₹{expense}")
        print(f"Balance: ₹{balance}")

    elif choice == "4":
        export_to_csv()
        print("Exported to exports/expenses.csv")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
