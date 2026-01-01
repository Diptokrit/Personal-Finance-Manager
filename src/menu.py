from expense import Expense
from file_manager import load_expenses, save_expenses


def show_menu():
    print("\n========= Personal Finance Manager =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


def add_expense():
    print("\n--- Add New Expense ---")

    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    expense = Expense(amount, category, date, description)

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print(" Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for exp in expenses:
        print(exp)


def menu_loop():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice. Please try again.")


# TEMPORARY (for testing only)
#menu_loop()
