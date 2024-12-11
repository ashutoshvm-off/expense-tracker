import csv
import os
from datetime import datetime
from tabulate import tabulate

# File name for storing expenses
CSV_FILE = "expenses.csv"

# Ensure the CSV file exists and has a header
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Expense"])

# Add a new expense entry
def add_expense(description, expense):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, expense])

# Display all expenses in a tabular format
def display_expenses():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
        if len(data) > 1:  # If there are entries
            print(tabulate(data, headers="firstrow", tablefmt="grid"))
        else:
            print("No expenses recorded yet.")

# Main program loop
def main():
    initialize_csv()
    print("Expense Tracker")
    print("===================")
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Enter expense description: ").strip()
            expense = input("Enter expense amount: ").strip()
            if expense.isdigit() or expense.replace('.', '', 1).isdigit():  # Valid number
                add_expense(description, float(expense))
                print("\nExpense added successfully!")
            else:
                print("\nInvalid amount. Please enter a valid number.")
        elif choice == "2":
            print("\nCurrent Expenses:")
            display_expenses()
        elif choice == "3":
            print("\nExiting Expense Tracker. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
