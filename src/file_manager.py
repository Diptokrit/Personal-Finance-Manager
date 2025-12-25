import csv
# to read and write csvs
import os
#Used to check whether a file exists or not 
from expense import Expense

DATA_FILE = "data/expenses.csv"
#storing the file path
# here the expenses will be stored

def ensure_data_file():
    #make sure that the csv file exists before opening it 
    if not os.path.exists( DATA_FILE):
        with open(DATA_FILE, "w" , newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])



def load_expenses():

    # load all the expenses from the csv file and return a list of expenses objects.

    ensure_data_file()
    expenses = []

    with open(DATA_FILE , "r") as f:
        reader = csv.reader(f)
        next(reader) #skip header

        for row in reader:
            if row:
                expense = Expense.from_row(row)
                expenses.append(expense)
    return expenses

def save_expenses(expenses):
    """Save a list of expense to the csv file"""

    ensure_data_file()

    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category" , "Amount", "Description"])

        for expense in expenses:
            writer.writerow(expense.to_row())


