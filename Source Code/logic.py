from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import re
import json
import common


#---------------------------------------------------------------------------------------------#

#This function validates the money that is being deposited.
def validate_deposit(username, entry_amount, update_balance, print_activity, deposit_window):

    global operation_type, amount_deposit

    input_value = entry_amount.get()

    if not input_value.replace('.', '', 1).isdigit():
        messagebox.showerror("Invalid Input", "Enter a valid numerical value.")

    elif float(input_value) <= 0:
        messagebox.showerror("Invalid Input", "The deposit must be a positive amount and exceed zero.")

    elif username not in common.accounts:
        messagebox.showerror("Error", "The user could not be found!")

    else:
        amount_deposit = float(input_value)
        common.accounts[username] += amount_deposit
        common.save_data()
        messagebox.showinfo("Deposit", f"Deposit of {amount_deposit:.2f} kr completed successfully.")

        operation_type = "Deposit"
        print_activity(username)
        update_balance()
        deposit_window.destroy()
    
        

#---------------------------------------------------------------------------------------------#

#This function validates the money that is being withdrawn.
def validate_withdraw(username, entry_amount, update_balance, withdraw_window, print_activity):
     
    global operation_type, amount_withdraw

    input_value = entry_amount.get()
    if not common.valid_amount(input_value):
        messagebox.showerror("Invalid Input", "Enter a valid positive numerical value.")
        return
    if username not in common.accounts:
        messagebox.showerror("Error", "The user could not be found!")
        return

    amount_withdraw = float(input_value)
    common.accounts[username] -= amount_withdraw
    common.save_data()
    messagebox.showinfo("Withdraw", f"Withdraw of {amount_withdraw:.2f} kr completed successfully.")

    operation_type = "Withdraw"
    print_activity(username)
    update_balance()
    withdraw_window.destroy()

#---------------------------------------------------------------------------------------------#

# This function checks the balance to transfer money and updates the balance
def check_balance_transfer(print_activity, username, update_balance, transfer_window):

    global operation_type

    balance = common.accounts.get(username,0)

    if amount_transfer <= balance:
        common.accounts[username] -= amount_transfer
        messagebox.showinfo("Transfer Successfull", f"Transferred {amount_transfer:.2f} kr to {recipient_transfer}. Account Number: {account_number_transfer}.")

        update_balance()
        operation_type = "Transfer"
        print_activity(username)
        transfer_window.destroy()

    else:
        messagebox.showerror("Insufficient Balance", f"Transfering failed. Your current balance is {balance:.2f} kr.")

#---------------------------------------------------------------------------------------------#

#This function checks if there is enough balance in the account to do the transaction and updates the balance.
def check_balance_transaction(username, transaction_window, update_balance, authenticate_window, print_activity):

    global operation_type

    if amount_transaction < 0:
        messagebox.showerror("Invalid amount! Amount must be greater than 0.")

    current_balance = common.accounts.get(username, 0)

    if current_balance >= amount_transaction:
        common.accounts[username] -= amount_transaction
        messagebox.showinfo("Transaction Successfull", f"Transferred {amount_transaction:.2f} kr to {recipient_transaction}. OCR: {ocr}.")
        
        update_balance()
        operation_type = "Transaction"
        print_activity(username)
        transaction_window.destroy()
        authenticate_window.destroy()
   
    else:
        messagebox.showerror("Insufficient Balance", f"Transaction failed. Your current balance is {current_balance:.2f} kr.")

#---------------------------------------------------------------------------------------------#

# This function displays the window to enter the recipients information
def transfering_money(username, update_balance, transfer_window, print_activity):
    
    global amount_transfer, recipient_transfer, account_number_transfer, date_transfer, operation_type

    recipient_transfer = recipient_input.get()
    account_number_transfer = account_number_input.get()
    date_transfer = date_transfer.get()
    amount_transfer = float(amount_to_transfer.get())

    operation_type = "Transfer"

    check_balance_transfer(print_activity, username, update_balance, transfer_window)

#---------------------------------------------------------------------------------------------#

# This fucntion validates the loan and updates the current balance with the new loan.
def validate_loan(loan_screen, income_entry, username, update_balance):

    global loan_income
    loan_income = float(income_entry.get())
    loan_message, loan_amount = loan_approval()
    common.accounts[username] += loan_amount

    messagebox.showinfo("Loan approved", f"{loan_message}")
    update_balance()

    loan_screen.destroy()
    confirmation_window.destroy()

#---------------------------------------------------------------------------------------------#

# This function checks and compares the income and accordingly assign the new loan.
def loan_approval():
    global loan_message, loan_amount

    loan_amount = 0
    loan_message = ""
    if loan_income < 10000 :
       loan_message = "Your income is very low. You can't take a loan"
       loan_amount  = 0
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
    

#---------------------------------------------------------------------------------------------#

# This function updates the username in the json file for all user's accounts
def update_username(username,username_change, enter_username):

    updated_username = enter_username.get()

    common.users[updated_username] = common.users.pop(username)
    common.accounts[updated_username] = common.accounts.pop(username)
    common.account_numbers[updated_username] = common.account_numbers.pop(username)
    common.savings_account[updated_username] = common.savings_account.pop(username) 
    common.save_data()
    messagebox.showinfo(f"New username",f"Your new username is {updated_username}")

    username_change.destroy() 

#---------------------------------------------------------------------------------------------#

# This function updates the user's email in the json file
def update_email(username, email_change, enter_email):

    updated_email = enter_email.get()
    if "@" not in updated_email or "." not in updated_email:
            messagebox.showerror("Error", "Invalid email address.")
            return
    
    common.users[username]['email']= updated_email
    common.save_data()
    messagebox.showinfo(f"New email", f"Your new email is {updated_email}")

    email_change.destroy()

#---------------------------------------------------------------------------------------------#

#Updates the phone number in the json file.
def update_phonenumber(username, change_phone_number, enter_phonenumber):

    new_phonenumber = enter_phonenumber.get()

    if re.findall(r"[a-zA-Z@.]", new_phonenumber):
        messagebox.showerror("Error", "Please type in a valid phone number")

    else:
        common.users[username]["Mobile Number"] = new_phonenumber
        common.save_data()
        messagebox.showinfo(f"New phone number",f"Phone number updated successfully to {new_phonenumber}")

    change_phone_number.destroy()

#---------------------------------------------------------------------------------------------#

#Updates the adress in the json file.
def update_address(username,adress_window, enter_address):

    new_address = enter_address.get()

    if re.findall(r"\d", new_address):
        messagebox.showerror("Error", "Please type in a valid address")

    else:
        common.users[username]["address"] = new_address
        common.save_data()
        messagebox.showinfo(f"New adress", f"Address updated successfully to {new_address}")

    adress_window.destroy()

#---------------------------------------------------------------------------------------------#

#Checks if the registering user already exists, if not registers them and adds it to the json file.
def register_user(username, password, full_name, mobile_number, email, address, dob):
    if username in common.users:
        return "User already exists!"

    account_number = common.generate_account_number()
    common.users[username] = {
        "password": password,
        "full_name": full_name,
        "Mobile Number": mobile_number,
        "email": email,
        "address": address,
        "dob": dob,
    }
    common.account_numbers[username] = account_number
    common.accounts[username] = 0

    common.save_data()
    return f"User registered successfully! Your account number is {account_number}."

#---------------------------------------------------------------------------------------------#

#This function ensures that the username and password exists in the json file.
def login_user(username, password):
    if username in common.users and common.users[username]["password"] == password:
        return True
    return False

#---------------------------------------------------------------------------------------------#

#Deposit ensures account balances are updated correctly and checks that deposits are valid.
def deposit(username, amount):
    if amount <= 0:
       return "The deposit must be a positive amount and exceed zero."
    if username not in common.accounts:
        return "The user could not be found!"
    common.accounts[username] += amount
    common.save_data()
    return f"Deposit of {amount:.2f} kr completed successfully."

#---------------------------------------------------------------------------------------------#


# Functions for opening new windows
def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    elif not re.search(r"[A-Z]", password):
        return "Password must include at least one uppercase letter."
    elif not re.search(r"[a-z]", password):
        return "Password must include at least one lowercase letter."
    elif not re.search(r"\d", password):
        return "Password must include at least one digit."
    else:
        return None
    

#---------------------------------------------------------------------------------------------#

#This function creates the page for the transaction where the user inputs the information.
def do_transaction(username, update_balance, print_activity, transaction_window):
  
  global recipient_input, amount_input, date_input, message_input, ocr_input

  Label(master = transaction_window, 
                         text = "Recipient", 
                         font = ("Abhaya Libre", 20, "bold"),
                        fg = "White", 
                        bg = "#253568").pack(pady = 5)
  recipient_input = Entry(master = transaction_window, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  recipient_input.pack(pady=10, ipadx=20, ipady=10)
  
  Label(master = transaction_window,
                      text = "Amount", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568").pack(pady = 5)
  amount_input = Entry(master = transaction_window, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  amount_input.pack(pady=10, ipadx=20, ipady=10)

  Label(master = transaction_window, 
                  text = "Date", 
                  font = ("Abhaya Libre", 20, "bold"), 
                  fg = "White", 
                  bg = "#253568"). pack(pady = 5)
  date_input = Entry(master = transaction_window, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  date_input.pack(pady=10, ipadx=20, ipady=10)

  Label(master = transaction_window, 
                       text = "OCR Number", 
                       font = ("Abhaya Libre", 20, "bold"),
                         fg = "White", 
                         bg = "#253568").pack(pady = 5)
  ocr_input = Entry(master = transaction_window, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  ocr_input.pack(pady=10, ipadx=20, ipady=10)

  Label(master = transaction_window, 
                      text = "Message", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568"). pack(pady = 5)
  message_input = Entry(master = transaction_window, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  message_input.pack(pady=10, ipadx=20, ipady=10)

  submit = Button(master = transaction_window, 
                     text = "Submit", 
                     font = ("Abhaya Libre", 20, "bold"), 
                     bg="#253568",
                     cursor="hand2",
                     width=20,
                     command = lambda : validate_transaction_input(username, update_balance, print_activity, transaction_window))
  submit.pack(pady=20, ipadx=20, ipady=10)

  transaction_window.mainloop()


#---------------------------------------------------------------------------------------------#


#This function validates and saves the inputs from the user when doing a transaction.
def validate_transaction_input(username, update_balance, print_activity, transaction_window):

    global amount_transaction, recipient_transaction, date_transaction, message, ocr, operation_type

    recipient_transaction = recipient_input.get()
    amount_transaction = float(amount_input.get())
    ocr = int(ocr_input.get())
    date_transaction = date_input.get()
    message = message_input.get()

    operation_type = "Transaction"

    authenticate_transaction(username, update_balance, print_activity, transaction_window)

#---------------------------------------------------------------------------------------------#

# This function reconfirm the transacrion process.
def authenticate_transaction(username, update_balance, print_activity, transaction_window):

    global authenticate_window

    authenticate_window = Tk()
    authenticate_window.title("Transaction")
    authenticate_window.geometry("800x600")
    authenticate_window.config(bg="#253568")

    Label(authenticate_window,
                 text="Authentication",
                 anchor="center",
                 font=("Abhaya Libre", 40, "bold"),
                 bg="#253568").pack(pady=10)
    
    Label(authenticate_window,
                 text="Are you sure you want this transaction to go through?",
                 anchor="center",
                 font=("Abhaya Libre", 30, "bold"),
                 bg="#253568").pack(pady=10)
    
    Label(authenticate_window,
                 text=f"""
        Sender: {username}
        Amount: {amount_transaction} kr
        Recipent: {recipient_transaction} 
        Date: {date_transaction} 
        Message: {message}
        OCR: {ocr} """,
                 anchor="center",
                 font=("Abhaya Libre", 20, "bold"),
                 bg="#253568").pack(pady=10)
    
    Button(authenticate_window, text = "Proceed", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,
                         command=lambda :check_balance_transaction(username, transaction_window, update_balance, authenticate_window, print_activity)).pack(pady=10, ipadx=(20), ipady=(10))

    Button(authenticate_window, text = "Cancel", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,
                         command=authenticate_window.destroy).pack(pady=10, ipadx=(20), ipady=(10))
    
    

#---------------------------------------------------------------------------------------------#

# This function creates the page for the loan application
def do_loan(loan_screen, username, update_balance):
    global income_entry, full_name_entry, account_number_entry, purpose_entry

    Label(master= loan_screen, text="Full Name:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    full_name_entry = Entry(master= loan_screen, font=("Abhaya Libre", 20, "bold"))
    full_name_entry.pack(pady=10, ipadx=20, ipady=(10))

    Label(master= loan_screen, text="Account Number", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    account_number_entry = Entry(master = loan_screen, font=("Abhaya Libre", 20, "bold"))
    account_number_entry.pack(pady=10, ipadx=20, ipady=(10))

    Label(loan_screen, text="Income (kr):", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)

    income_entry = Entry(master = loan_screen, font=("Abhaya Libre", 20, "bold"))
    income_entry.pack(pady=10, ipadx=20, ipady=10)

    Label(loan_screen, text="Purpose", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    purpose_entry = Entry(master = loan_screen, font=("Abhaya Libre", 20, "bold"))
    purpose_entry.pack(pady=10, ipadx=20, ipady=(10))

    Button(master = loan_screen, text="Proceed", font=("Abhaya Libre", 18, "bold"),
              bg="#253568",
              cursor="hand2",
              width=20, command=lambda: loan_confirmation(loan_screen, username, update_balance)).pack(pady=10, ipadx=(20),ipady=(10))
    
#---------------------------------------------------------------------------------------------#

#This function displays a confirmation that your loan application has been approved.
def loan_confirmation(loan_screen, username, update_balance):

    global confirmation_window
    confirmation_window = Toplevel(loan_screen)
    confirmation_window.title("Confirm Loan")
    confirmation_window.geometry("800x600")
    confirmation_window.config(bg="#253568")

    Label(confirmation_window, text="LOAN CONFIRMATION", font=("Abhaya Libre", 30, "bold"), bg="#253568",
          fg="white").pack(pady=20)

    frame_details = Frame(confirmation_window, bg="#1F2A44", padx=20, pady=20)
    frame_details.pack(pady=20, padx=20)

    
    details = f"""
    Dear {full_name_entry.get()},

    Thank you for submitting your loan application.
    We have received your application and would like
    to confirm the following details as part of our review process:

    Account Number: {account_number_entry.get()}
    Income: {income_entry.get()} kr
    Purpose: {purpose_entry.get()}

    Please click on Confirm, if everything is correctly filled, 
    Thank you for choosing us for your financial needs.

    Sincerely,
    Financial Forces Bank
    """

    Label(frame_details, text=details, font=("Abhaya Libre", 14, "bold"), bg="#253568", fg="white").pack(pady=10)
    Button(frame_details, text="Confirm", font=("Abhaya Libre", 20, "bold"), bg="#4CAF50", fg="white",
              command=lambda:validate_loan(loan_screen, income_entry, username, update_balance)).pack(pady=10, ipadx=20, ipady=10)


#---------------------------------------------------------------------------------------------#

# This function creates the page for transfer
def do_transfer(transfer_window,username,update_balance, print_activity):
    
    global recipient_input, account_number_input, date_transfer, amount_to_transfer 
    
    Label(transfer_window, text="Recepient Name: ", 
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    recipient_input = Entry(transfer_window,font = ("Abhaya Libre", 20, "bold"))
    recipient_input.pack(pady=10, ipadx=20, ipady=10)

    Label(transfer_window, text="Account Number: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    account_number_input = Entry(transfer_window,font = ("Abhaya Libre", 20, "bold"))
    account_number_input.pack(pady=10, ipadx=20, ipady=10)

    Label(transfer_window, text="Date: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    date_transfer = Entry(transfer_window,font = ("Abhaya Libre", 20, "bold"))
    date_transfer.pack(pady=10, ipadx=20, ipady=10)

    Label(transfer_window, text="Amount: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    amount_to_transfer = Entry(transfer_window,font = ("Abhaya Libre", 20, "bold"))
    amount_to_transfer.pack(pady=10, ipadx=20, ipady=10)

    Button(transfer_window,
           text = "Transfer Amount", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command = lambda:transfering_money(username, update_balance, transfer_window, print_activity)).pack(pady=10, ipadx=(20), ipady=(10))


#---------------------------------------------------------------------------------------------#

#This function deletes the account from the json file.
def confirm_deleting(username):

    common.users.pop(username)
    common.accounts.pop(username)
    common.account_numbers.pop(username)

    common.save_data()
    messagebox.showinfo("Delete Account","Account was successfully deleted.")

#---------------------------------------------------------------------------------------------#

#This function checks if the inputed information in the login entry boxes match the json file.
def attempt_login(username_entry, password_entry, choose_option_menu, login_screen, main_window):
    # Collect input data
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Authenticate user
    if username in common.users and common.users[username]["password"] == password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
        main_window.destroy()
        login_screen.destroy()
        choose_option_menu(username)

    else:
        messagebox.showerror("Error", "Invalid username or password.")




#---------------------------------------------------------------------------------------------#

#This function handles the validty of the inputed information for change of password.
def forget_password_handle(username, new_password, confirm_password,forget_password_window):
    if username not in common.users:
        return "The username provided does not match any existing account."

    elif new_password != confirm_password:
        return "The new password and confirmation password differ."

    # We call validate_password to make sure  that the new password fulfills the complexity criteria.
    elif common.validate_password(new_password):
        password_error = common.validate_password(new_password)
        messagebox.showerror("Error", password_error)

    else:
        common.users[username]["password"] = new_password
        common.save_data()
        messagebox.showinfo("Success", "Password updated successfully!")
        forget_password_window.destroy()

#---------------------------------------------------------------------------------------------#

#This function updates the password in the json file when forgotten.
def update_password_json(username_entry, confirm_password_entry):
    # read the json file first
    with open("bank_users.json", "r") as file:
        data = json.load(file)

    if username_entry not in data["users"]:
        return "The username is not found."

    # we update the password
    data["users"][username_entry]["password"] = confirm_password_entry

    # we overwrite the json file
    with open("bank_users.json", "w") as file:
        json.dump(data, file, indent=4)

    return "The password has been successfully updated in the JSON file."


#---------------------------------------------------------------------------------------------#

#This function checks if the inputs in the entry boxes are valid for the registeration to go through.
def attempt_register(full_name_entry, username_entry, password_entry,
                     mobile_number_entry, email_entry, address_entry,
                     dob_entry, register_screen):
    # Collect input data
    full_name = full_name_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    mobile_number = mobile_number_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    dob = dob_entry.get().strip()

    # Validation
    if not all([full_name, username, password, mobile_number, email, address, dob]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if username in common.users:
        messagebox.showerror("Error", "Username already exists!")
        return

    if not mobile_number.isdigit() or len(mobile_number) < 7:
        messagebox.showerror("Error", "Invalid mobile number.")
        return

    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email address.")
        return

    # Add user to dictionaries
    account_number = common.generate_account_number()
    common.users[username] = {
        "password": password,
        "full_name": full_name,
        "mobile_number": mobile_number,
        "email": email,
        "address": address,
        "dob": dob,
    }
    common.account_numbers[username] = account_number
    common.accounts[username] = 0

    messagebox.showinfo("Registration", f"User registered successfully! Your account number is {account_number}.")
    register_screen.destroy()

#---------------------------------------------------------------------------------------------#
# This function displays the balance in the savings account
def adding_money(enter_money):

    global savings_balance

    savings_balance = 0
    money_saving = float(enter_money.get())
    savings_balance += money_saving
    savings_balance = f"{money_saving:.2f} kr"

#---------------------------------------------------------------------------------------------#

#This function creates the saving account connecting it to the primary account and saves it in the json file.
def create_savings_account(username, add_money, enter_money, saving_window):

    global new_savings_account
    
    new_savings_account = common.generate_account_number()

    common.savings_account[username] = new_savings_account #assigning a key-value pair in the saving_account_number dictionary.
    
    common.save_data()

    messagebox.showinfo(f"Savings account", f"You created a savings account! Your savings account number is {new_savings_account}")

    adding_money(enter_money)
    saving_window.destroy()
    add_money(username)
    


#---------------------------------------------------------------------------------------------#

