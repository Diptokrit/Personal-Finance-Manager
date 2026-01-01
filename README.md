# Personal Finance Manager

A simple Python-based command-line application to track personal expenses, built as a self-learning project.

## Features
- Add expenses through a terminal-based menu
- View total expenses
- View category-wise expense breakdown
- Persistent storage using CSV files
- Clean and modular project structure

## Project Structure
PERSONAL_FINANCE_MANAGER/
├── src/
│ ├── main.py # Application entry point (menu & flow)
│ ├── file_manager.py # File handling (read/write CSV)
│ ├── expense.py # Expense data model
│ ├── reports.py # Reporting & calculations
│ └── utils.py # Helper functions
├── data/
│ └── expenses.csv
└── README.md


## Tech Stack
- Python
- Object-Oriented Programming (OOP)
- CSV file handling

## How to Run
1. Clone the repository
2. Navigate to the project root
3. Run the application:

```bash
python src/main.py
