from expense import Expense
from file_manager import load_expenses ,  save_expenses

def show_menu():
    print("========= Personal Finance Manager =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expenses():
    print("\n--- Add New Expense ---")

#Taking input from the user
    amount = input("Enter amount: ")
    category = input(" Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
#now to create object out of these data:

    expense = Expense(amount , category , date , description)

    #Load existing expenses
    expenses = load_expenses()

    #Add new expense
    expenses.append(expense)

    #Save back to csv
    save_expenses(expenses)

    print("Expense succesfull !")

def view_expenses():
    #reloading all previous data (csv - obj - list)
    expenses = load_expenses()

    #case : no expense found
    if not expenses:
        print("No expenses found")
    return

    #print every expense
    for exp in expenses:
        print(exp)


def menu_loop():
    #Infinite loop
    while true:
        show_menu()
        choice = input("Enter your choice")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exciting.. Goodbye!")
            break
        else:
            print(" Invalid choise .Please try again")    
    









