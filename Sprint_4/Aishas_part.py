def validate_loan(username,update_balance):
    global loan_income
    loan_income = float(income_entry.get())
    loan_message, amountss = loan_approval(loan_income)
    banking_system.accounts[username] += amountss

    messagebox.showinfo("Loan approved", f"{loan_message}")
    update_balance()

    loan_screen.destroy()
    confirmation_window.destroy()