import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from library.classes_9 import Budget
from library import functions

class BudgetBuddyGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("diva")
        self.window.geometry("550x650")
        self.window.configure(bg="#ffb6c1")  # light pink bg

        # Load Hello Kitty Image
        try:
            img = Image.open("Hello_Kitty.webp")     # <--- CHANGE IF NEEDED
            img = img.resize((150, 150))
            self.hk_img = ImageTk.PhotoImage(img)
            self.img_label = tk.Label(window, image=self.hk_img, bg="#ffb6c1")
            self.img_label.pack(pady=5)
        except:
            pass

        # Title
        self.title_label = tk.Label(
            window, 
            text="Diva Budget Collector",
            font=("Comic Sans MS", 26, "bold"),
            bg="#ffb6c1",
            fg="#ff1493"
        )
        self.title_label.pack(pady=5)

        # ------- Inputs Section -------

        self.name_label = tk.Label(window, text="Enter your name:", bg="#ffb6c1", font=("Comic Sans MS", 14))
        self.name_label.pack()
        self.name_entry = tk.Entry(window, font=("Comic Sans MS", 12), bg="#e70e6f")
        self.name_entry.pack()

        self.income_label = tk.Label(window, text="Enter total income:", bg="#ffb6c1", font=("Comic Sans MS", 14))
        self.income_label.pack()
        self.income_entry = tk.Entry(window, font=("Comic Sans MS", 12), bg="#e70e6f")
        self.income_entry.pack()

        self.expense_type_label = tk.Label(window, text="Expense Type (e.g., Grocery):", bg="#ffb6c1", font=("Comic Sans MS", 14))
        self.expense_type_label.pack()
        self.expense_type_entry = tk.Entry(window, font=("Comic Sans MS", 12), bg="#e70e6f")
        self.expense_type_entry.pack()

        self.expense_label = tk.Label(window, text="Enter expenses (Type Cost):", bg="#ffb6c1", font=("Comic Sans MS", 14))
        self.expense_label.pack()
        self.expense_entry = tk.Entry(window, font=("Comic Sans MS", 12), bg="#e70e6f")
        self.expense_entry.pack()

        # ------- Buttons -------

        self.add_button = tk.Button(
            window,
            text="Add Expense",
            command=self.add_expense,
            font=("Comic Sans MS", 14, "bold"),
            bg="#ff69b4",
            fg="white",
            activebackground="#ff85c2",
            relief="ridge",
            borderwidth=5
        )
        self.add_button.pack(pady=10)

        self.show_button = tk.Button(
            window,
            text="Calculate Balance",
            command=self.calculate_balance,
            font=("Comic Sans MS", 14, "bold"),
            bg="#ff69b4",
            fg="white",
            activebackground="#ff85c2",
            relief="ridge",
            borderwidth=5
        )
        self.show_button.pack(pady=10)

        # Display Box
        self.output_box = tk.Text(
            window, 
            height=12, 
            width=50,
            font=("Comic Sans MS", 12),
            bg="#e70e6f"
        )
        self.output_box.pack(pady=10)

        # Storage
        self.budgets = {}

    
    def save_to_file(self, name, expense_type, category, cost):
        with open("user_expenses.txt", "a") as file:
            file.write(f"{name} | {expense_type} | {category} | ${cost}\n")

  

    def add_expense(self):
        exp_type = self.expense_type_entry.get().strip()
        exp_input = self.expense_entry.get().strip()
        name = self.name_entry.get().strip()

        if exp_type == "" or exp_input == "" or name == "":
            messagebox.showerror("ERROR", "Please fill all fields including your name.")
            return

        try:
            category, cost = exp_input.split()
            cost = float(cost)
        except:
            messagebox.showerror("ERROR", "Use Proper Format e.g. Milk 10")
            return

        if exp_type not in self.budgets:
            self.budgets[exp_type] = Budget(exp_type)

        # Add to budget object
        self.budgets[exp_type].expenses.append(cost)
        self.budgets[exp_type].categories.append(category)

        # Save to text file
        self.save_to_file(name, exp_type, category, cost)

        # Output to GUI
        self.output_box.insert(tk.END, f"Added {category} - ${cost} from {exp_type}\n")
        self.expense_entry.delete(0, tk.END)

    def calculate_balance(self):
        name = self.name_entry.get()
        income = self.income_entry.get()

        if name == "" or income == "":
            messagebox.showerror("ERROR", "Enter your name and income.")
            return

        try:
            income = float(income)
        except:
            messagebox.showerror("ERROR", "Income must be a number.")
            return

        total = 0
        self.output_box.insert(tk.END, "\n----- SUMMARY -----\n")
        for key, budget in self.budgets.items():
            t = budget.get_expenses()
            total += t
            self.output_box.insert(tk.END, f"{key} Total: ${t}\n")

        balance = functions.calc_balance(income, total)
        status = functions.financial_status(balance)

        self.output_box.insert(tk.END, f"\nTotal Expenses: ${total}\n")
        self.output_box.insert(tk.END, f"Balance: ${balance}\n")
        self.output_box.insert(tk.END, f"{status}\n")


# MAIN LOOP
window = tk.Tk()
app = BudgetBuddyGUI(window)
window.mainloop()
#skibidi toilet 677 LOLLL