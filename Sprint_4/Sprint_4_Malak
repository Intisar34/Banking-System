def display_loan():
    loan_screen = Toplevel(main_window)
    loan_screen.geometry("800x600")
    loan_screen.title("Loan")
    loan_screen.config(bg="#253568")

    Label(loan_screen, image=img_4, anchor="center", bg="#253568").pack(pady=15, padx=50)

    full_name_entry = Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    account_number_entry = Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    income_entry = Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    amount_entry = Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    purpose_entry = Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))

    full_name = Label(loan_screen, text="Full Name:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white")
    full_name.pack(pady=10)
    full_name_entry.pack()

    account_number = Label(loan_screen, text="Account Number:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white")
    account_number.pack(pady=10)
    account_number_entry.pack()

    income = Label(loan_screen, text="Income:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white")
    income.pack(pady=10)
    income_entry.pack()

    amount = Label(loan_screen, text="Amount:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white")
    amount.pack(pady=10)
    amount_entry.pack()

    purpose = Label(loan_screen, text="Purpose:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white")
    purpose.pack(pady=10)
    purpose_entry.pack()
    
    Button(loan_screen, text="Submit", font=("Abhaya Libre", 18, "bold"),
       bg="#253568", cursor="hand2", width=20).pack(pady=20, ipadx=20, ipady=10)