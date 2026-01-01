import csv
import os
from expense import Expense

#To give the path to the python directly
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "expenses.csv")


def ensure_data_file():
    data_dir = os.path.dirname(DATA_FILE)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
#if no such files it will create one
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def load_expenses():
    ensure_data_file()
    #To keep the previous expenses in the list
    expenses = []

    with open(DATA_FILE, "r") as f:
        reader = csv.reader(f)

        try:
            next(reader)  # skipping the header
        except StopIteration:
            return []

        for row in reader:
            if row:
                expenses.append(Expense.from_row(row))

    return expenses



def save_expenses(expenses):
    ensure_data_file()

    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])

        for expense in expenses:
            writer.writerow(expense.to_row())
