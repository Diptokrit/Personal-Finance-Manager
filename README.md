# Personal Finance Manager

A simple Python-based command-line application to track personal expenses, built as a self-learning project.

## Features
- Add expenses through a terminal-based menu
- View total expenses
- View category wise expense breakdown
- Persistent storage using CSV files
- Clean and modular project structure

## Project Structure
The project is organized in a simple and clean way. All the main code is inside the src folder. The main.py file runs the program and shows the menu to the user. The file_manager.py file is used to read and save expense data in a CSV file. Each expense is represented using an Expense class, which is defined in expense.py. The logic for calculating total expenses and category-wise summaries is written in reports.py. Small helper functions are kept in utils.py. The expense data is stored in the data folder inside an expenses.csv file, and the project information is explained in the README.md file.


## Tech Stack
- Python
- Object Oriented Programming (OOP)
- CSV file handling

## How to Run
1. Clone the repository
2. Navigate to the project root
3. Run the application:

```bash
python src/main.py
