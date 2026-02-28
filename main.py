# TODO

# add transaction buttons - Done as of 2/25/26
# add colors for each transaction button - Done as of 2/25/26
# make the buttons work - Done as of 2/27/26
# Clean up code make it look more nice - Working on as of 2/28/26

import tkinter as tk
# our list
transactions = []

def get_total(transaction_type):
    total = 0

    for t in transactions:              
        if t[0] == transaction_type:    
            total += t[1]               

    return total



# Add Transaction
def add_transaction(transaction_type):
    amount = float(amount_entry.get())
    transactions.append([transaction_type, amount])
    update_display()



# Update Screen
def update_display():
    income = get_total("Income")
    expense = get_total("Expense")
    balance = income - expense

    income_label.config(text="Total Income: $" + str(income))
    expense_label.config(text="Total Expense: $" + str(expense))
    balance_label.config(text="Balance: $" + str(balance))

    transaction_list.delete(0, tk.END)

    for t in transactions:
        transaction_list.insert(tk.END, t[0] + " $" + str(t[1]))

    amount_entry.delete(0, tk.END)



root = tk.Tk()
root.title("Budget Tracker")
root.geometry("400x500")
root.configure(bg="#f0f8ff")  # set the background

title = tk.Label(root, text="Budget Tracker",
                 font=("Arial", 18, "bold"),
                 bg="#f0f8ff")
title.pack(pady=15)

amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=10)

income_button = tk.Button(root, text="Add Income", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=15, command=lambda: add_transaction("Income"))
income_button.pack(pady=5)

expense_button = tk.Button(root,
                           text="Add Expense",
                           bg="#f44336",
                           fg="white",
                           font=("Arial", 12, "bold"),
                           width=15,
                           command=lambda: add_transaction("Expense"))
expense_button.pack(pady=5)

income_label = tk.Label(root,
                        text="Total Income: $0",
                        font=("Arial", 12),
                        bg="#f0f8ff")
income_label.pack(pady=5)

expense_label = tk.Label(root,
                         text="Total Expense: $0",
                         font=("Arial", 12),
                         bg="#f0f8ff")
expense_label.pack(pady=5)

balance_label = tk.Label(root,
                         text="Balance: $0",
                         font=("Arial", 14, "bold"),
                         bg="#f0f8ff")
balance_label.pack(pady=10)

transaction_list = tk.Listbox(root,
                              width=35,
                              height=8,
                              font=("Arial", 11))
transaction_list.pack(pady=10)

root.mainloop()