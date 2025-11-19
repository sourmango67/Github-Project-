class Budget():
    def __init__(self, expense_type):

        self.expense_type = expense_type
        self.expenses = []
        self.categories = []

    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"Enter number of {self.expense_type} expenses you want to add (integers only): "))
                break
            except ValueError:
                print("**ERROR**")
                print("Invalid Input. Please enter a whole number.")
                print()
            
        print("Enter expenses in \"Type Cost format\" For e.g., Milk 10 ")
        for i in range(num_expenses):
                while True:
                    try:
                        type, exp = input(f"Enter expense #{i+1}: ").split()
                        self.expenses.append(float(exp))
                        self.categories.append(type)
                        break
                    except:
                        print()
                        print("**ERROR**")
                        print("Invalid Input. Please type expenses in this format. Milk 10")
                        print()

    def get_expenses(self):
        total = sum(self.expenses)
        print(f"Total expenses for {self.expense_type} is {sum(self.expenses)}")
        return sum(self.expenses)
    
    def get_expenses_list(self):
        print(f"Money you spent on {self.expense_type} are:")
        for i in range(len(self.expenses)):

         print(f"{self.categories [i]} {self.expenses[i]}")