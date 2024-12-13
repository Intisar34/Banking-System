# Loan message approval
messagebox.showinfo("Loan approved", f"{loan_message}")

# Checking users income to approve loan

def loan_approval():
    global loan_message, loan_amount

    loan_amount = 0
    loan_message = ""
    if loan_income < 10000 :
       loan_message = "Your income is very low. You can't take a loan"
       amountss  = 0
       return loan_message , loan_amount
    elif 10000 <= loan_income < 50000:
        loan_message = "The amount of the loan you can take is 80000."
        loan_amount  = 80000
        return loan_message , loan_amount
    elif 50000 <= loan_income < 100000:
        loan_message = "The amount of the loan you can take is 150000."
        loan_amount = 150000
        return loan_message , loan_amount
    elif 100000 <=  loan_income < 150000:
        loan_message = "The amount of the loan you can take is 200000."
        loan_amount  = 200000
        return loan_message , loan_amount
    else:
        loan_message = loan_income * 2
        loan_amount = loan_income * 2
        return loan_amount, loan_message