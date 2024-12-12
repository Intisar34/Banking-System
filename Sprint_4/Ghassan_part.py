# Ghassan task
def loan_confirmation(full_name, account_nr, income, amount, purpose):
    confirmation_window = Toplevel()
    confirmation_window.title("Confirm Loan")
    confirmation_window.geometry("800x600")
    confirmation_window.config(bg="#253568")

    tk.Label(confirmation_window, image=img_5, anchor="n", bg="#253568").pack(pady=5, padx=20)

    Label(confirmation_window, text="LOAN CONFIRMATION", font=("Abhaya Libre", 30, "bold"), bg="#253568",
          fg="white").pack(pady=20)

    frame_details = Frame(confirmation_window, bg="#1F2A44", padx=20, pady=20)
    frame_details.pack(pady=20, padx=20)

    details = f"""
    Dear {full_name},

    Thank you for submitting your loan application.
    We have received your application and would like
    to confirm the following details as part of our review process:

    Account Number: {account_nr}
    Income: {income} kr
    Loan Amount: {amount} kr
    Purpose: {purpose}

    Please click on Confirm, if everything is correctly filled, 
    Thank you for choosing us for your financial needs.

    Sincerely,
    Financial Forces Bank
    """

    Label(frame_details, text=details, font=("Abhaya Libre", 14, "bold"), bg="#253568", fg="white").pack(pady=10)
    Button(frame_details, text="Confirm", font=("Abhaya Libre", 20, "bold"), bg="#4CAF50", fg="white",
           command=approval_loan).pack(pady=10, ipadx=20, ipady=10)
