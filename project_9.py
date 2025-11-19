import os
from library import functions
from library.classes_9 import Budget

name_of_user = input ("Enter your name: ")


os.system('cls' if os.name == 'nt' else 'clear' )
print (f"Hey {name_of_user},This is BudgetBuddy, Your personal assistant") 
income = float(input("Enter your total income: "))

total_expenses = []

grocery = Budget("Grocery")
car = Budget("Car")

grocery.add_expenses()
car.add_expenses()


total_expenses.append(grocery.get_expenses())
total_expenses.append(car.get_expenses())

bal = functions.calc_balance(income, sum(total_expenses))
functions.financial_status(bal)

grocery.get_expenses_list()