# budget.py - Student Budget Tracker

import json
import os
from datetime import datetime

FILE = "expensses.json"
MONTHLY_BUDGET = 1700

def load_expenses():
    if not os.path.exists(FILE):
        return[]
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent =2)

def add_expenses():
    name = input("What did you spend on? e.g Food, Taxi, Data: ")
    try:
        amount = float(input("How much ? R"))
    except:
        print("Please enter a number!")
        return
    expense = {
        "name": name,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")

    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print(f" Added: {name} - R{amount}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses yet. Add one !")
        return
    total = 0
    print("\n---YOUR EXPENSES---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['name']} - R{e['amount']} | {e['date']}")
        total += e['amount']
    print(f"\nTOTAL SPENT: R{total}")
    print(f"BUDGET: R{MONTHLY_BUDGET}")
    left = MONTHLY_BUDGET - total
    if left < 0:
        print("OVER BUDGET by R{-left}! Stop spending")
    else:
        print(f"You have R{left} left")

def delete_expense():
    view_expenses()
    try:
        num = int(input("\nWhich number to delete? "))
        expenses = load_expenses()
        removed = expenses.pop(num - 1)
        save_expenses(expenses)
        print(f"Delete: {removed['name']}")
    except: 
        print("Invalid number!")

def main():
    while True:
        print("\n===== STUDENT BUDGET TRACK =====")
        print("1. Add Expense")
        print("2. View Expenses & Budget")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose 1-4: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Bye! Stay on budget")
            break
        else:
            print("Choice 1, 2, 3, or 4")

if __name__== "__main__":
    main()