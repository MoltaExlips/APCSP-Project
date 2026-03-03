# TODO

# add transaction buttons - Done as of 2/25/26
# add colors for each transaction button - Done as of 2/25/26
# make the buttons work - Done as of 2/27/26
# Clean up code make it look more nice - Working on as of 2/28/26
# Create pie chart - Working on as of 3/1/26
# add labels for each section - Working on as of 2/25/26
# Catch errors that may arise (done for input error as of 3/2/26)(done for value errors for pie chart as of 3/2/26)


import tkinter as tk
import math # for calculating labels
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
    try:
        amount = float(amount_entry.get())
    except ValueError: #show error message if wrong value inputted
        amount_entry.delete(0, tk.END)
        error_label.config(text="Invalid Respose!\nPlease only enter numbers")
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

    for t in transactions[-3:]:
        transaction_list.insert(tk.END, t[0] + " $" + str(t[1]))

    amount_entry.delete(0, tk.END)

#Pie Chart related things
def open_chart_window():
    chart_window = tk.Toplevel(root)
    chart_window.title("Pie Chart")
    chart_window.geometry("400x300")
    canvas = tk.Canvas(chart_window, width=400, height=300)
    canvas.pack(pady=30)
    income = get_total("Income")
    expense = get_total("Expense")
    balance = income - expense
    if balance < 0:
        chart_window.destroy()
        error_label.config(text="Balance cannot be negative")
        return
    if expense == 0:
        chart_window.destroy()
        error_label.config(text="No expenses recorded")
        return
    expense_list = []
    for t in transactions: # creates a list of all expense values
        if t[0] == "Expense":
            expense_list.append(t[1])
    print(expense_list)

    colors = ["Red", "Blue", "Green", "Purple", "Orange", "Brown", "Pink", "Gray"]
    start_angle = 0.0
    col = 0  # changes colors

    cx, cy = 150, 150
    r = 110

    # BALANCE SLICE
    balance_extent = balance * 360 / income
    canvas.create_arc(
        50, 50, 250, 250,
        start=start_angle,
        extent=balance_extent,
        fill=colors[col]
    )

    # Label for balance — mid_angle uses Tkinter's coordinate system
    mid_angle = math.radians(start_angle + balance_extent / 2)
    label_x = cx + r * math.cos(mid_angle)
    label_y = cy - r * math.sin(mid_angle)
    canvas.create_text(label_x, label_y, text="Remainder:" + f"${balance}", font=("Arial", 8, "bold"))

    # update angle
    start_angle += balance_extent
    col += 1

    # Expense slices
    for t in expense_list:
        extent = t * 360 / income  # determines arc length
        canvas.create_arc(
            50, 50, 250, 250,
            start=start_angle,
            extent=extent,
            fill=colors[col]
        )

        # Label for this expense
        mid_angle = math.radians(start_angle + extent / 2)
        label_x = cx + r * math.cos(mid_angle)
        label_y = cy - r * math.sin(mid_angle)
        canvas.create_text(label_x, label_y, text=f"${t}", font=("Arial", 12, "bold"))

        start_angle += extent
        col += 1
        print("ran" + str(col))
        if col == len(colors):
            col = 0


#Building the Window
root = tk.Tk()
root.title("Budget Tracker") # create a title
root.geometry("400x500") # shape of window
root.configure(bg="#f0f8ff")  # set the background
#create title
title = tk.Label(root, text="Budget Tracker",
                 font=("Arial", 18, "bold"),
                 bg="#f0f8ff")
title.pack(pady=15)
#entry box
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=10)
#income button
income_button = tk.Button(root,
                          text="Add Income",
                          bg="#4CAF50",
                          fg="white",
                          font=("Arial", 12, "bold"),
                          width=15,
                          command=lambda: add_transaction("Income"))
income_button.pack(pady=5)
#expense button
expense_button = tk.Button(root,
                           text="Add Expense",
                           bg="#f44336",
                           fg="white",
                           font=("Arial", 12, "bold"),
                           width=15,
                           command=lambda: add_transaction("Expense"))
expense_button.pack(pady=5)
#show current incomes
income_label = tk.Label(root,
                        text="Total Income: $0",
                        font=("Arial", 12),
                        bg="#f0f8ff")
income_label.pack(pady=5)
#show current expenses
expense_label = tk.Label(root,
                         text="Total Expense: $0",
                         font=("Arial", 12),
                         bg="#f0f8ff")
expense_label.pack(pady=5)
#show total (income-expense)
balance_label = tk.Label(root,
                         text="Balance: $0",
                         font=("Arial", 14, "bold"),
                         bg="#f0f8ff")
balance_label.pack(pady=10)
#list of all values added
transaction_list = tk.Listbox(root,
                              width=35,
                              height=3,
                              font=("Arial", 11))
transaction_list.pack(pady=5)
#pie chart button
chart_button = tk.Button(root,
                         text="Show Pie Chart",
                         bg="#2196f3",
                         fg="white",
                         font=("Arial", 12, "bold"),
                         width=15,
                         command=open_chart_window)
chart_button.pack()
#text box for errors
error_label = tk.Label(root,
                         text=" ",
                         font=("Arial", 14, "bold"),
                         bg="#f0f8ff")
error_label.pack(pady=10)


root.mainloop()

