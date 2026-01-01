from file_manager import load_expenses, add_expense
from reports import total_expense, category_summary
from utils import format_currency
from expense import Expense



def show_menu():
    print("\nPersonal Finance Manager")
    print("1. View Expense Report")
    print("2. Add Expense")
    print("3. Exit")


def view_report():
    expenses = load_expenses()
    total = total_expense(expenses)
    summary = category_summary(expenses)

    print("\nExpense Report")
    print("----------------")
    print(f"Total Expense: {format_currency(total)}\n")

    print("Category-wise Breakdown:")
    for category, amount in summary.items():
        print(f"- {category}: {format_currency(amount)}")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            view_report()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
