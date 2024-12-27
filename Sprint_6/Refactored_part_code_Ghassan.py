def deposit_screen(username, update_balance):
    global menu_screen, operation_type

    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Deposit")

    tk.Label(menu_screen, image=img_5, anchor="n", bg="#253568").pack(pady=5, padx=20)
    tk.Label(menu_screen, text="Make a Deposit", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)
    tk.Label(menu_screen, text="Enter Amount (kr):", font=("Abhaya Libre", 18), bg="#253568", fg="white").pack(pady=10)

    entry_amount = tk.Entry(menu_screen, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(menu_screen, text="Confirm", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=lambda: validate_deposit(username, entry_amount, update_balance)).pack(pady=10, ipadx=20, ipady=10)

    tk.Button(menu_screen, text="Close", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=menu_screen.destroy).pack(pady=10, ipadx=20, ipady=10)


def validate_deposit(username, entry_amount, update_balance):
    global menu_screen, operation_type

    input_value = entry_amount.get()

    if not input_value.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid Input", "Enter a valid numerical value.")
    elif float(input_value) <= 0:
        messagebox.showerror("Invalid Input", "The deposit must be a positive amount and exceed zero.")
    elif username not in accounts:
        messagebox.showerror("Error", "The user could not be found!")
    else:
        amount = float(input_value)
        accounts[username] += amount
        save_data()
        messagebox.showinfo("Deposit", f"Deposit of {amount:.2f} kr completed successfully.")
        operation_type = "Deposit"
        display_history(username, amount)
        update_balance()
        menu_screen.destroy()


def withdraw_screen(username, update_balance):
    global menu_screen, operation_type

    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Withdraw")

    tk.Label(menu_screen, image=img_5, anchor="n", bg="#253568").pack(pady=5, padx=20)
    tk.Label(menu_screen, text="Make a Withdraw", font=("Abhaya Libre", 30, "bold"), bg="#253568", fg="white").pack(pady=20)
    tk.Label(menu_screen, text="Enter Amount (kr):", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    entry_amount = tk.Entry(menu_screen, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(menu_screen, text="Confirm", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=lambda: validate_withdraw(username, entry_amount, update_balance)).pack(pady=10, ipadx=20, ipady=10)

    tk.Button(menu_screen, text="Close", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20, command=menu_screen.destroy).pack(pady=10, ipadx=20, ipady=10)

    return menu_screen

def validate_withdraw(username, entry_amount, update_balance):
    global menu_screen, operation_type

    input_value = entry_amount.get()

    if not input_value.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid numerical value.")
    elif float(input_value) <= 0:
        messagebox.showerror("Invalid Input", "Amount should be positive and greater than zero.")
    else:
        amount = float(input_value)
        current_balance = accounts.get(username, 0)

        if amount > current_balance:
            messagebox.showerror("Invalid Withdraw", f"You do not have enough funds. Your current balance is {current_balance:.2f} kr.")
        else:
            accounts[username] -= amount
            message = f"Withdrawal of {amount:.2f} kr completed successfully."
            messagebox.showinfo("Withdraw", message)

            operation_type = "Withdraw"
            display_history(username, amount)
            update_balance()
            menu_screen.destroy()