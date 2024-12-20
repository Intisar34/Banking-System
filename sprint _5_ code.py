import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import re
import random
import json

# Main window
main_window = Tk()
main_window.title("Banking System")
main_window.geometry("800x600")
main_window.config(bg="#253568")

# Image
img_1 = Image.open('FF_logo.png')
img_1 = img_1.resize((700, 240))
img_1 = ImageTk.PhotoImage(img_1)

img_2 = Image.open('FF_logo.png')
img_2 = img_2.resize((700, 240))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('FF_logo.png')
img_3 = img_3.resize((100, 50))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('FF_logo.png')
img_4 = img_4.resize((1, 1))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('FF_logo.png')
img_5 = img_5.resize((100, 50))
img_5 = ImageTk.PhotoImage(img_5)

img_6 = Image.open('FF_logo.png')
img_6 = img_6.resize((700, 240))
img_6 = ImageTk.PhotoImage(img_6)

img_7 = Image.open('FF_logo.png')
img_7 = img_7.resize((500,180))
img_7 = ImageTk.PhotoImage(img_7)




# Labels, Buttons
img_header = Label(main_window,
                   image=img_1,
                   anchor="center",
                   bg="#253568").pack(pady=15, padx=50)

header_1 = Label(main_window,
                 text="Log in as a private customer:",
                 anchor="center",
                 font=("Abhaya Libre", 20, "bold"),
                 bg="#253568").pack(pady=10)

login_button = Button(main_window,
                      text="LOGIN",
                      font=("Abhaya Libre", 18, "bold"),
                      bg="#253568",
                      cursor="hand2",
                      width=20,
                      command=lambda:login()).pack(pady=10, ipadx=(20), ipady=(10))

header_2 = Label(main_window,
                 text="Register to become a customer:",
                 anchor="center",
                 font=("Abhaya Libre", 20, "bold"),
                 bg="#253568").pack(pady=10)

register_button = Button(main_window,
                         text="REGISTER",
                         font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,
                         command=lambda: register()).pack(pady=10, ipadx=(20), ipady=(10))


# change_hover_color(login_button, register_button, "#92080F", "#FFFFFF")


# This class handles all backend functionalities of the banking system.
class BankingSystem:
    def __init__(self):
        self.users = {}
        
        self.account_numbers = {}
        self.saving_account_number = {}
        self.load_data()

    def generate_account_number(self):
        generate = False
        while not generate:
            account_number = str(random.randint(10 ** 9, 10 ** 10 - 1))
            if account_number not in self.account_numbers.values() or savings_account_number not in self.saving_account_number:
                generate = True
        return account_number or savings_account_number

    def register_user(self, username, password, full_name, mobile_number, email, address, dob):
        if username in self.users:
            return "User already exists!"
        account_number = self.generate_account_number()
        self.users[username] = {
            "password": password,
            "full_name": full_name,
            "Mobile Number": mobile_number,
            "email": email,
            "address": address,
            "dob": dob,
        }
        self.account_numbers[username] = account_number
        self.save_data()
        return f"User registered successfully! Your account number is {account_number}."
    
    def save_data(self):
     data = {
        "users" : self.users,
        "account numbers" : self.account_numbers,
        "savings account": self.saving_account_number
    }
     with open("bank_users.json","w") as file:
        json.dump(data,file,indent=4)

    def load_data(self):
     with open("bank_users.json","r") as file:
      data = json.load(file)
      self.users = data.get("users")
      self.account_numbers = data.get("account numbers")
      self.saving_account_number = data.get("savings account")

    def login_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False


#Deposit ensures account balances are updated correctly and checks that deposits are valid.
    def deposit(self, username, amount):

        if amount <= 0:
            return "The deposit must be a positive amount and exceed zero."
        if username not in self.accounts:
            return "The user could not be found!"
        self.accounts[username] += amount
        return f"Deposit of {amount:.2f} kr completed successfully."

banking_system = BankingSystem()


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


def login():
    login_screen = Toplevel(main_window)
    login_screen.geometry("800x600")
    login_screen.title("Login Form")
    login_screen.config(bg="#253568")

    Label(login_screen, image=img_2, anchor="center", bg="#253568").pack(pady=15, padx=50)
    Label(login_screen, text="Username:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    entry_username = Entry(login_screen, font=("Abhaya Libre", 20, "bold"))
    entry_username.pack()

    Label(login_screen, text="Password:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    entry_password = Entry(login_screen, font=("Abhaya Libre", 20, "bold"), show="*")
    entry_password.pack()

    def attempt_login():
        global username
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        if banking_system.login_user(username, password):
            messagebox.showinfo("Login", f"Welcome, {username}!")
            login_screen.destroy()
            open_buttons(username, )

        else:
            messagebox.showerror("Error", "Invalid username or password.")

    Button(login_screen, text="Login", font=("Abhaya Libre", 18, "bold"),
           bg="#253568", cursor="hand2", width=20, command = lambda : attempt_login()).pack(pady=20, ipadx=20, ipady=10)
    
    Button(login_screen, text="Forget password",
                      font=("Abhaya Libre", 18, "bold"),
                      bg="#253568",
                      cursor="hand2",
                      width=12,
                      command=lambda:forget_password(img_5)).pack(pady=10, ipadx=(10), ipady=(5))
    
    
def forget_password(img_5):
    forget_password_window = Toplevel()
    forget_password_window.geometry("800x600")
    forget_password_window.title("Forget password")
    forget_password_window.config(bg="#253568")

    Label(forget_password_window, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)
    Label(forget_password_window, text="User name:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    username_entry = Entry(forget_password_window, font=("Abhaya Libre", 20, "bold"), width=20)
    username_entry.pack(pady=5, ipadx=10, ipady=5)

    Label(forget_password_window, text="New Password:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    new_password_entry = Entry( forget_password_window, font=("Abhaya Libre", 20, "bold"), show="*", width=20)
    new_password_entry.pack(pady=5, ipadx=10, ipady=5)

    Label(forget_password_window, text="Confirm New Password:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    confirm_password_entry = Entry(forget_password_window, font=("Abhaya Libre", 20, "bold"), show="*", width=20)
    confirm_password_entry.pack(pady=5, ipadx=10, ipady=5)

    Button(forget_password_window, text="Submit", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2",
           command=lambda: forget_password_handle(username_entry.get(), new_password_entry.get(), confirm_password_entry.get(),forget_password_window)).pack(pady=20, ipadx=20, ipady=10)


def forget_password_handle(username, new_password, confirm_password,forget_password_window):
    if username not in banking_system.users:
        return "The username provided does not match any existing account."

    elif new_password != confirm_password:
        return "The new password and confirmation password differ."

    # We call validate_password to make sure  that the new password fulfills the complexity criteria.
    elif validate_password(new_password):
        password_error = validate_password(new_password)
        messagebox.showerror("Error", password_error)

    else:
        banking_system.users[username]["password"] = new_password
        banking_system.save_data()
        messagebox.showinfo("Success", "Password updated successfully!")
        forget_password_window.destroy()


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


# This handles the user registration process
def register():
    register_screen = Toplevel(main_window)
    register_screen.geometry("800x600")
    register_screen.title("Register Form")
    register_screen.config(bg="#253568")

    labels = ["Full Name", "Username", "Password", "Mobile Number", "Email", "Address", "Date of Birth"]
    entries = {}

    Label(register_screen,
          image=img_3,
          anchor="center",
          bg="#253568").pack(pady=15, padx=50)

    for i, label_text in enumerate(labels):
        Label(register_screen, text=label_text + ":", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(
            pady=5)
        if label_text == "Password":
            entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"), show="*")
        else:
            entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
        entry.pack()
        entries[label_text] = entry

    def attempt_register():
        full_name = entries["Full Name"].get().strip()
        username = entries["Username"].get().strip()
        password = entries["Password"].get().strip()
        mobile_number = entries["Mobile Number"].get().strip()
        email = entries["Email"].get().strip()
        address = entries["Address"].get().strip()
        dob = entries["Date of Birth"].get().strip()

        if not all([full_name, username, password, mobile_number, email, address, dob]):
            messagebox.showerror("Error", "All fields are required!")
            return

        password_error = validate_password(password)
        if password_error:
            messagebox.showerror("Error", password_error)
            return

        if not mobile_number.isdigit() or len(mobile_number) < 7:
            messagebox.showerror("Error", "Invalid mobile number.")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address.")
            return

        result = banking_system.register_user(username, password, full_name, mobile_number, email, address, dob)
        messagebox.showinfo("Registration", result)
        if "successfully" in result:
            register_screen.destroy()

    Button(register_screen, text="Register", font=("Abhaya Libre", 18, "bold"),
           bg="#253568", cursor="hand2", width=20, command=attempt_register).pack(pady=20, ipadx=20, ipady=10)

#Userstory 4:Ghassan
#Deposit function validate input, process the deposit, and update the user's account balance.
def deposit_handle (username, update_balance):
    global menu_screen
    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Deposit")

    tk.Label(menu_screen, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)
    tk.Label(menu_screen, text="Make a Deposit", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)
    tk.Label(menu_screen, text="Enter Amount (kr):", font=("Abhaya Libre", 18), bg="#253568", fg="white").pack(pady=10)

    entry_amount = tk.Entry(menu_screen, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    def validate_deposit():

        global operation_type, amount

        amount = float(entry_amount.get())
        if amount <= 0:
            messagebox.showerror("Invalid Input", "The deposit must be a positive amount and exceed zero.")
            return
        message = banking_system.deposit(username, amount)
        messagebox.showinfo("Deposit", message)

        operation_type = "Deposit"

        display_history(username, amount)
        update_balance()
        menu_screen.destroy()

    tk.Button(menu_screen, text="Confirm", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,command=validate_deposit).pack(pady=10, ipadx=(20), ipady=(10))

    tk.Button(menu_screen, text="Close", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,command=menu_screen.destroy).pack(pady=10, ipadx=(20), ipady=(10))
    return menu_screen


def withdraw_handle (username, update_balance):
    
    global amount, operation_type

    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Withdraw")

    tk.Label(menu_screen, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)
    tk.Label(menu_screen, text="Make a Withdraw", font=("Abhaya Libre", 30, "bold"), bg="#253568", fg="white").pack(pady=20)
    tk.Label(menu_screen, text="Enter Amount (kr):", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    entry_amount = tk.Entry(menu_screen, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    

    def validate_withdraw():

        global amount, operation_type

        amount = float(entry_amount.get())
        current_balance = banking_system.accounts.get(username, 0)

        if amount <= 0:
            messagebox.showerror ("Invalid Input", "Amount should be positive and greater than zero.")
            return
        elif amount > current_balance:
            messagebox.showerror ("Invalid Withdraw", f"You do not have enough funds. Your current balance is {current_balance:.2f} kr.")
            return

        banking_system.accounts[username] -= amount
        message = f"Withdrawal of {amount:.2f} kr completed successfully."
        messagebox.showinfo("Withdraw", message)
        
        operation_type = "Withdraw"
        display_history(username, amount)

        update_balance()
        menu_screen.destroy()

    tk.Button(menu_screen, text="Confirm", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20, command=validate_withdraw).pack(pady=10, ipadx=(20), ipady=(10))

    tk.Button(menu_screen, text="Close", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20, command=menu_screen.destroy).pack(pady=10, ipadx=(20), ipady=(10))
    return menu_screen


def display_balance():
    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Main Page")

    tk.Label(menu_screen, image=img_4, anchor="center", bg="#253568").pack(pady=15, padx=50)

    frame_name = tk.Frame(menu_screen, background="#253568")
    frame_name.pack()
    frame_amount = tk.Frame(menu_screen, background="#253568")
    frame_amount.pack()

    amount = "0,00 kr"


    current_balance = tk.Label(master=frame_name, text="Current Amount", background="#253568",
                               foreground="White", font=("Abahya Libre", 30, "bold"))
    display_amount = tk.Label(master=frame_amount, text = amount, font=("Abahya Libre", 20), background="#253568",
                              foreground="White")

    current_balance.pack(anchor="center")
    display_amount.pack()
    return menu_screen, display_amount


def display_balance_info(banking_system, username):

    account_number = banking_system.account_numbers.get(username, "N/A")

    # trans_history = display_history()

    balance_info = tk.Toplevel(main_window)
    balance_info.title("Balance Information")
    balance_info.config(bg="#253568")
    balance_info.geometry("800x600")

    img_3 = Image.open('FF_logo.png')
    img_3 = img_3.resize((300, 100))
    img_3 = ImageTk.PhotoImage(img_3)

    tk.Label(balance_info, image=img_3, anchor="w", bg="#253568").pack(pady=10, padx=20)


    account_name = tk.Frame(balance_info, background="#253568")
    account_name.pack(anchor="center")
    new_account_number = tk.Frame(balance_info, background="#253568")
    new_account_number.pack(anchor="center")

    # transaction = tk.Frame(balance_info, background = "#253568")
    # transaction.pack(anchor = "w", padx = 10, pady = (10,0))

    display_name = tk.Label(master=account_name,
                            text=username,
                            foreground="White",
                            background="#253568",
                            font=("Times New Roman", 30, "bold"))

    display_number = tk.Label(master=new_account_number,
                              text=account_number,
                              foreground="White",
                              background="#253568",
                              font=("Abhaya Libre", 20))
    # display_amount = tk.Label(master = transaction, text = "Transaction History:", foreground = "Black", background = "White",
    # font = ("Abhaya Libre", 20))

    display_name.pack(anchor="center", pady=5)
    display_number.pack(anchor="center", pady=5)

    # From here it displays transaction history: 
    #trans_history = display_history(username, amount)

    history_trans = tk.Label(balance_info, text="Latest activity", font=("Abhaya Libre", 20, "bold"), bg="#253568")
    history_trans.pack(anchor="center", pady=10)

    for transaction in transaction_history:
        transaction_info = tk.Label(balance_info, text=f"{transaction}", font=("Abhaya Libre", 18), bg="#253568")
        transaction_info.pack(anchor="center", padx=40, pady=2)

    balance_info.mainloop()

transaction_history = []

def display_history(username, amount):


    if operation_type == "Deposit":
        output = f" Deposit: {username} ---> Amount: {amount} kr"

    elif operation_type == "Withdraw":
        output = f" Withdraw: {username} ---> Amount: {amount} kr"

    elif  operation_type== "Transaction":
        output = f" Transaction: {username} ---> Amount: {amount} kr ---> Recipent: {recipient} --- Date: {date}"

    elif  operation_type == "Transfer":
        output = f" Transfer: {username} ---> Amount: {amount_to_transfer} kr ---> Recipent: {recepient} --- Date: {date_transfer}"

    
    transaction_history.append(output)

    return transaction_history


    #for i in range(1):
        #transaction_history.append(f"Sender: {username} --- Amount: {amount} kr --- Recipent: {recipient} --- Date: {date}")
    #return transaction_history


def display_transfer(username,update_balance):

    transfer = Toplevel(main_window)
    transfer.title("Transfer")
    transfer.geometry("800x600")
    transfer.config(bg="#253568")

    tk.Label(transfer, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)

    do_transfer(transfer,username,update_balance)


def display_deposit():
    deposit = Toplevel(main_window)
    deposit.title("Deposit")
    deposit.geometry("300x300")
    close_deposit = tk.Button(deposit,
                              text="Close",
                              font=("Abhaya Libre", 18, "bold"),
                              bg="253568",
                              cursor="hand2",
                              width=20,
                              command=deposit.destroy)
    close_deposit.pack(pady=140)


def display_withdraw():
    withdraw = Toplevel(main_window)
    withdraw.title("Withdraw")
    withdraw.geometry("300x300")
    close_withdraw = tk.Button(withdraw,
                               text="Close",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="253568",
                               cursor="hand2",
                               width=20,
                               command=withdraw.destroy)
    close_withdraw.pack(pady=140)


def display_transaction(username, update_balance, ):

    transaction = Toplevel(main_window)
    transaction.title("Transaction")
    transaction.geometry("800x600")
    transaction.config(bg="#253568")
    
    tk.Label(transaction, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)


    do_transaction(transaction, username, update_balance, )

    
def display_loan(username, update_balance):
    global income_entry, full_name_entry, account_number_entry, purpose_entry, loan_screen
    loan_screen = Toplevel(main_window)
    loan_screen.geometry("800x600")
    loan_screen.title("Loan")
    loan_screen.config(bg="#253568")

    tk.Label(loan_screen, image=img_4, anchor="center", bg="#253568").pack(pady=15, padx=50)

    tk.Label(loan_screen, text="Full Name:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    full_name_entry = tk.Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    full_name_entry.pack(pady=10, ipadx=20, ipady=(10))

    tk.Label(loan_screen, text="Account Number", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    account_number_entry = tk.Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    account_number_entry.pack(pady=10, ipadx=20, ipady=(10))

    tk.Label(loan_screen, text="Income (kr):", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)

    income_entry = tk.Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    income_entry.pack(pady=10, ipadx=20, ipady=10)

    tk.Label(loan_screen, text="Purpose", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady = 5)

    purpose_entry = tk.Entry(loan_screen, font=("Abhaya Libre", 20, "bold"))
    purpose_entry.pack(pady=10, ipadx=20, ipady=(10))

    tk.Button(loan_screen, text="Proceed", font=("Abhaya Libre", 18, "bold"),
              bg="#253568",
              cursor="hand2",
              width=20, command=lambda: loan_confirmation(username, update_balance)).pack(pady=10, ipadx=(20),
                                                                                          ipady=(10))

def loan_confirmation(username, update_balance):
    global confirmation_window
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
    tk.Button(frame_details, text="Confirm", font=("Abhaya Libre", 20, "bold"), bg="#4CAF50", fg="white",
              command=lambda: validate_loan(username, update_balance)).pack(pady=10, ipadx=20, ipady=10)



def validate_loan(username,update_balance):
    global loan_income
    loan_income = float(income_entry.get())
    loan_message, loan_amount = loan_approval()
    banking_system.accounts[username] += loan_amount

    messagebox.showinfo("Loan approved", f"{loan_message}")
    update_balance()

    loan_screen.destroy()
    confirmation_window.destroy()


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
    
def display_saving_account():
    
    global enter_name,enter_money
    
    saving_window = Toplevel(main_window)
    saving_window.title("Savings account")
    saving_window.geometry("300x300")
    saving_window.config(bg ="#253568")
    
    Label(saving_window,
     text="creating savings account", 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568", 
     fg="white").pack(pady=10)
    
    Label(saving_window,
     text="Fill in your username here:", 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568",
     fg="white").pack(pady=10)
   
    enter_name = tk.Entry(saving_window,font = ("Abhaya Libre", 20, "bold"))
    enter_name.pack(pady=10, ipadx=20, ipady=10) 
    
    Label(saving_window, 
     text="specify the desired amount you wish to have in your savings account:", 
     font=("Abhaya Libre", 20, "bold"),
     bg="#253568", 
     fg="white").pack(pady=10)

    enter_money = tk.Entry(saving_window,font = ("Abhaya Libre", 20, "bold"))
    enter_money.pack(pady=10, ipadx=20, ipady=10)
    

    generate_saving_account = tk.Button(
        saving_window,
        text="generate",
        font=("Abhaya Libre", 18, "bold"),
        bg="#253568",
        cursor="hand2",
        width=20,
        command = create_savings_account
    )
    generate_saving_account.pack(pady=10, ipadx=(20), ipady=(10))
    
    close_button = tk.Button(
        saving_window,
        text="close",
        font=("Abhaya Libre", 18, "bold"),
        bg="#253568",
        cursor="hand2",
        width=20,
        command = saving_window.destroy
    )
    close_button.pack(pady=10, ipadx=(20), ipady=(10))

def create_savings_account():
    global savings_account_number

    savings_account_number = banking_system.generate_account_number()
    
    banking_system.saving_account_number[username] = savings_account_number
    
    banking_system.save_data()

    messagebox.showinfo(f"savings account", f"You created a savings account! your savings account number is {savings_account_number}")


    
    

def display_settings():

    settings_window = Toplevel(main_window)
    settings_window.title("Settings")
    settings_window.geometry("800x600")
    settings_window.config(bg ="#253568")

    tk.Label(settings_window, image = img_6, anchor="n", bg="#253568").pack(pady = 5, padx = 20)

    delete_account = tk.Button(settings_window, text="Delete Account",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=create_delete_account)
    delete_account.pack(pady=5, ipadx=(20), ipady=(10))

    child_services = tk.Button(settings_window, text="Child Services",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=create_child_account)
    child_services.pack(pady=5, ipadx=(20), ipady=(10))

    update_info = tk.Button(settings_window, 
                            text="Update Information", 
                            font=("Abhaya Libre", 18, "bold"), 
                            bg="#253568", 
                            cursor="hand2", 
                            width=20,
                            command=open_update_info_page)
    update_info.pack(pady=5, ipadx=(20), ipady=(10))
    
    chatbot = tk.Button(settings_window, 
                        text="Chatbot", 
                        font=("Abhaya Libre", 18, "bold"), 
                        bg="#253568", 
                        cursor="hand2",
                        width=20, 
                        command=open_chatbot_page)
    chatbot.pack(pady=5, ipadx=(20), ipady=(10))

    saving_account = tk.Button(
        settings_window,
        text="Saving Account",
        font=("Abhaya Libre", 18, "bold"),
        bg="#253568",
        cursor="hand2",
        width = 20,
        command=display_saving_account,
    )
    saving_account.pack(pady=5, ipadx=(20), ipady=(10))


def open_buttons(username):
    display_button, display_amount = display_balance()

    #User story 4:Ghassan
    #Updates the balance display for a user.
    def update_balance():
        balance = banking_system.accounts.get(username, 0)
        display_amount.config(text=f"{balance:.2f} kr")


    open_balance_info = tk.Button(display_button,
                                  text="Balance Information",
                                  font=("Abhaya Libre", 25, "bold"),
                                  bg="#253568",
                                  cursor="hand2",
                                  command=lambda: display_balance_info(banking_system, username),
                                  width=20)
    open_balance_info.pack(pady=5, ipadx=(20), ipady=(10))


    open_deposit = tk.Button(display_button, text="Deposit",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=lambda: deposit_handle(username, update_balance),
                             width=20)
    open_deposit.pack(pady=5, ipadx=(20), ipady=(10))


    open_withdraw = tk.Button(display_button, text="Withdraw",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda: withdraw_handle(username, update_balance),
                              width=20)
    open_withdraw.pack(pady=5, ipadx=(20), ipady=(10))
    

    open_transfer = tk.Button(display_button,
                              text="Transfer",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda: display_transfer(username,update_balance),
                              width=20)
    open_transfer.pack(pady=5, ipadx=(20), ipady=(10))

    open_transaction = tk.Button(display_button,
                                 text="Transaction",
                                 font=("Abhaya Libre", 25, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 command=lambda : display_transaction(username, update_balance),
                                 width=20)
    open_transaction.pack(pady=5, ipadx=(20), ipady=(10))

    open_loan = tk.Button(display_button,
                          text="Loan",
                          font=("Abhaya Libre", 25, "bold"),
                          bg="#253568",
                          cursor="hand2",
                          command=lambda: display_loan(username, update_balance),
                          width=20)
    open_loan.pack(pady=5, ipadx=(20), ipady=(10))

    open_settings = tk.Button(display_button,
                              text="Settings",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=display_settings,
                              width=20)
    open_settings.pack(pady=5, ipadx=(20), ipady=(10))

    main_window.mainloop()


def check_balance(username, transaction, update_balance, authenticate, ):

    #recipient = recipient_input.get().strip()
    #amount = float(amount_input.get())
    #ocr_number = int(ocr_input.get())

    global operation_type

   
    if amount < 0:
        messagebox.showerror("Invalid amount! Amount must be greater than 0.")

    current_balance = banking_system.accounts.get(username, 0)

    if current_balance >= amount:
        banking_system.accounts[username] -= amount
        messagebox.showinfo(
                "Transaction Successfull",
                f"Transferred {amount:.2f} kr to {recipient}. OCR: {ocr}.")
        
        update_balance()
        operation_type = "Transaction"
        display_history(username, amount)
        transaction.destroy()
        authenticate.destroy()
   
    else:
        messagebox.showerror(
             "Insufficient Balance",
              f"Transaction failed. Your current balance is {current_balance:.2f} kr.")
        
    
   
def do_transaction(transaction, username, update_balance, ):
  
  global recipient_input, amount_input, date_input, message_input, ocr_input

  tk.Label(master = transaction, 
                         text = "Recipient", 
                         font = ("Abhaya Libre", 20, "bold"),
                        fg = "White", 
                        bg = "#253568").pack(pady = 5)
  recipient_input = tk.Entry(master = transaction, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  recipient_input.pack(pady=10, ipadx=20, ipady=10)
  
  tk.Label(master = transaction,
                      text = "Amount", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568").pack(pady = 5)
  amount_input = tk.Entry(master = transaction, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  amount_input.pack(pady=10, ipadx=20, ipady=10)

  tk.Label(master = transaction, 
                  text = "Date", 
                  font = ("Abhaya Libre", 20, "bold"), 
                  fg = "White", 
                  bg = "#253568"). pack(pady = 5)
  date_input = tk.Entry(master = transaction, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  date_input.pack(pady=10, ipadx=20, ipady=10)

  tk.Label(master = transaction, 
                       text = "OCR Number", 
                       font = ("Abhaya Libre", 20, "bold"),
                         fg = "White", 
                         bg = "#253568").pack(pady = 5)
  ocr_input = tk.Entry(master = transaction, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  ocr_input.pack(pady=10, ipadx=20, ipady=10)

  tk.Label(master = transaction, 
                      text = "Message", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568"). pack(pady = 5)
  message_input = tk.Entry(master = transaction, font=("Abhaya Libre", 18, "bold"),
                         cursor="hand2",
                         width=20)
  message_input.pack(pady=10, ipadx=20, ipady=10)

  submit = tk.Button(master = transaction, 
                     text = "Submit", 
                     font = ("Abhaya Libre", 20, "bold"), 
                     fg = "White", 
                     bg = "#253568", 
                     cursor="hand2", 
                     command = lambda : save_input(username, transaction, update_balance, ))
  submit.pack(pady=20, ipadx=20, ipady=10)

  transaction.mainloop()


def save_input(username, transaction, update_balance, ):

    global amount, recipient, date, message, ocr

    recipient = recipient_input.get()
    amount = float(amount_input.get())
    date = date_input.get()
    message = message_input.get()
    ocr = int(ocr_input.get())

    authenticate_transaction(username, transaction, update_balance, )



def authenticate_transaction(username, transaction, update_balance, ):

    authenticate = Toplevel(main_window)
    authenticate.title("Transaction")
    authenticate.geometry("800x600")
    authenticate.config(bg="#253568")

    img = Image.open('FF_logo.png')
    img = img.resize((500,180))
    img = ImageTk.PhotoImage(img)

    Label(authenticate, 
          image=img, 
          anchor="center", 
          bg="#253568").pack(pady=15, padx=50)

    Label(authenticate,
                 text="Authentication",
                 anchor="center",
                 font=("Abhaya Libre", 40, "bold"),
                 bg="#253568").pack(pady=10)
    
    Label(authenticate,
                 text="Are you sure you want this transaction to go through?",
                 anchor="center",
                 font=("Abhaya Libre", 30, "bold"),
                 bg="#253568").pack(pady=10)
    
    Label(authenticate,
                 text=f"""
        Sender: {username}
        Amount: {amount} kr
        Recipent: {recipient} 
        Date: {date} 
        Message: {message}
        OCR: {ocr} """,
                 anchor="center",
                 font=("Abhaya Libre", 20, "bold"),
                 bg="#253568").pack(pady=10)



    Button(authenticate, text = "Cancel", font=("Abhaya Libre", 18, "bold"),
                         bg="#253568",
                         cursor="hand2",
                         width=20,
                         command=authenticate.destroy).pack(pady=10, ipadx=(20), ipady=(10))
    
def checking_balance(username, update_balance, transfer):

    global operation_type, amount_to_transfer

    balance = banking_system.accounts.get(username,0)

    if amount_to_transfer <= balance:
        banking_system.accounts[username] -= amount_to_transfer
        messagebox.showinfo("Money Transferred","Money Transferred")

        operation_type = "Transfer"
        display_history(username, amount)

    elif amount_to_transfer == 0:
        banking_system.accounts[username] -= amount_to_transfer
        messagebox.showinfo("Money Transferred","Money Transferred")

        #operation_type = "Transfer"
        #display_history(username, amount)

    else:
        messagebox.showerror("Transfer Declined","Transfer Declined")

    update_balance()
    transfer.destroy()


def transfering_money(username,update_balance,transfer):
    
    global amount_to_transfer, recepient, account_number, date_transfer

    recepient = recepient_input.get()
    account_number = account_number_input.get()
    date_transfer = date_transfer.get()
    amount_to_transfer = float(amount_to_transfer.get())

    checking_balance(username,update_balance,transfer)

def do_transfer(transfer,username,update_balance):
    
    global recepient_input, account_number_input, date_transfer ,amount_to_transfer 
    
    tk.Label(transfer, text="Recepient Name: ", 
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    recepient_input = tk.Entry(transfer,font = ("Abhaya Libre", 20, "bold"))
    recepient_input.pack(pady=10, ipadx=20, ipady=10)

    tk.Label(transfer, text="Account Number: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    account_number_input = tk.Entry(transfer,font = ("Abhaya Libre", 20, "bold"))
    account_number_input.pack(pady=10, ipadx=20, ipady=10)

    tk.Label(transfer, text="Date: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    date_transfer = tk.Entry(transfer,font = ("Abhaya Libre", 20, "bold"))
    date_transfer.pack(pady=10, ipadx=20, ipady=10)

    tk.Label(transfer, text="Amount: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    amount_to_transfer = tk.Entry(transfer,font = ("Abhaya Libre", 20, "bold"))
    amount_to_transfer.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(transfer,
           text = "Transfer Amount", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command = lambda :transfering_money(username,update_balance,transfer)).pack(pady=10, ipadx=(20), ipady=(10))
    

def create_child_account():
    
    child_window = tk.Toplevel(main_window)
    child_window.title("Child Services")
    child_window.geometry("800x600")
    child_window.config(bg="#253568")

    close_button = tk.Button(child_window, 
                            text="Close", font=("Abhaya Libre", 18, "bold"),
                            bg="#253568",
                            cursor="hand2",
                            width=20, 
                            command=child_window.destroy)
    close_button.pack(pady=10, ipadx=(20), ipady=(10))


def create_delete_account():

    delete_window = tk.Toplevel(main_window)
    delete_window.title("Child Services")
    delete_window.geometry("800x600")
    delete_window.config(bg="#253568")


    Label(delete_window, 
          image=img_7, 
          anchor="n", 
          bg="#253568").pack(pady=15, padx=50)
    
    tk.Label(delete_window, 
             text="Choose which account to delete:", 
             font=("Abhaya Libre", 25, "bold"), 
             bg="#253568", fg="white").pack(pady=20)

    personal_account_button = tk.Button(delete_window,
                                        text = "Personal Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= delete_primary_account)
    personal_account_button.pack(pady=10, ipadx=(20), ipady=(10))


    child_account_button = tk.Button(delete_window,
                                        text = "Child Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= delete_child_account)
    child_account_button.pack(pady=10, ipadx=(20), ipady=(10))


def delete_child_account():

    confirm_delete_window = Toplevel(main_window)
    confirm_delete_window.title("Delete child account")
    confirm_delete_window.geometry("800x600")
    confirm_delete_window.config(bg="#253568")

    Label(confirm_delete_window, 
         image=img_7, 
         anchor="center", 
          bg="#253568").pack(pady=15, padx=50)
   
    cancel_button = Button(confirm_delete_window, 
                            text = "Cancel", 
                            font=("Abhaya Libre", 18, "bold"),
                            bg="#253568",
                            cursor="hand2",
                            width=20,
                            command=confirm_delete_window.destroy)
    cancel_button.pack(pady=10, ipadx=(20), ipady=(10))


def delete_primary_account():

    confirm_delete_window = Toplevel(main_window)
    confirm_delete_window.title("Delete primary account")
    confirm_delete_window.geometry("800x600")
    confirm_delete_window.config(bg="#253568")

    account_number = banking_system.account_numbers.get(username, "N/A")

    Label(confirm_delete_window, 
          image=img_7, 
          anchor="center", 
          bg="#253568").pack(pady=15, padx=50)

    Label(confirm_delete_window,
                text="Are you sure you want delete this account:",
                anchor="center",
                font=("Abhaya Libre", 40, "bold"),
                fg = "White",
                bg="#253568").pack(pady=10)
    
    Label(confirm_delete_window,
                 text= f"""
    {username}
    {account_number}""",
                 anchor="center",
                 font=("Abhaya Libre", 30, "bold"),
                 fg = "White",
                 bg="#253568").pack(pady=10)
    

    confirmation_button = Button(confirm_delete_window, 
                                 text = "Delete", 
                                 font=("Abhaya Libre", 18, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 width=20, 
                                 command = lambda : confirm_deleting(username))
    confirmation_button.pack(pady=10, ipadx=(20), ipady=(10))
    
    cancel_button = Button(confirm_delete_window, 
                           text = "Cancel", 
                           font=("Abhaya Libre", 18, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           width=20,
                           command=confirm_delete_window.destroy)
    cancel_button.pack(pady=10, ipadx=(20), ipady=(10))

    confirm_delete_window.mainloop()


def confirm_deleting(username):

    banking_system.users.pop(username)
    banking_system.account_numbers.pop(username)
    banking_system.saving_account_number.pop(username)
   
        
    banking_system.save_data()
    messagebox.showinfo("Delete Account","Account was successfully deleted.")


def open_update_info_page():

    update_info = tk.Toplevel(main_window)
    update_info.geometry("800x600")
    update_info.title("Update Personal Information")
    update_info.config(bg="#253568")

    tk.Label(update_info, text="Update Personal Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    tk.Button(update_info, text="Close", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2", command=update_info.destroy).pack(pady=10, ipadx=20, ipady=10)
    open_change_info(update_info)

def open_chatbot_page():

    chatbot_window = tk.Toplevel(main_window)
    chatbot_window.geometry("800x600")
    chatbot_window.title("Chatbot")
    chatbot_window.config(bg="#253568")

    tk.Label(chatbot_window, text="Chatbot Interaction", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    tk.Button(chatbot_window, text="Close", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2", command=chatbot_window.destroy).pack(pady=10, ipadx=20, ipady=10)

def display_username(update_info,username):
    global enter_username
    username_change = Toplevel(update_info)
    username_change.title("Changing Username")
    username_change.geometry("800x600")
    username_change.config(bg="#253568")

    Label(username_change, text="Update Username", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    
    tk.Label(username_change, text="Enter new username: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    enter_username = tk.Entry(username_change,font = ("Abhaya Libre", 20, "bold"))
    enter_username.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(username_change,
           text = "Change username", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_username(username,username_change)).pack(pady=10, ipadx=(20), ipady=(10))

    
def display_phone_number(updating_info):
    global enter_phonenumber
    change_phone_number = Toplevel(updating_info)
    change_phone_number.title("Changing Phone Number")
    change_phone_number.geometry("800x600")
    change_phone_number.config(bg="#253568")
    Label(change_phone_number, text="Update Phone Number", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    tk.Label(change_phone_number, 
             text="Enter new phone number: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    
    enter_phonenumber = tk.Entry(change_phone_number,font = ("Abhaya Libre", 20, "bold"))
    enter_phonenumber.pack(pady=10, ipadx=20, ipady=10)
    

    tk.Button(change_phone_number,
           text = "Change phone number", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_phonenumber(username,change_phone_number)).pack(pady=10, ipadx=(20), ipady=(10))   

def display_address(updating_info):
    global enter_address
    address_change = Toplevel(updating_info)
    address_change.title("Changing Username")
    address_change.geometry("800x600")
    address_change.config(bg="#253568")
    Label(address_change, text="Update address", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    tk.Label(address_change, text="Enter new address: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5) 
    enter_address = tk.Entry(address_change,font = ("Abhaya Libre", 20, "bold"))
    enter_address.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(address_change,
           text = "Change address", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_address(username,address_change)).pack(pady=10, ipadx=(20), ipady=(10))

def display_email(update_info,username):
    global enter_email
    email_change = Toplevel(update_info)
    email_change.title("Changing Username")
    email_change.geometry("300x300")
    Label(email_change, text="Update email", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    email_change.config(bg="#253568")
    
    tk.Label(email_change, text="Enter new email: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    enter_email = tk.Entry(email_change,font = ("Abhaya Libre", 20, "bold"))
    enter_email.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(email_change,
           text = "Change email", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_email(username,email_change)).pack(pady=10, ipadx=(20), ipady=(10))

    
def update_username(username,username_change):
    update_username = enter_username.get()
    banking_system.users[update_username] = banking_system.users.pop(username)
        
    banking_system.save_data()
    messagebox.showinfo(f"Your new username is {update_username}",f"Your new username is {update_username}")

    username_change.destroy() 

def update_email(username,email_change):
    update_email = enter_email.get()
    if "@" not in update_email or "." not in update_email:
            messagebox.showerror("Error", "Invalid email address.")
            return
    
    banking_system.users[username]['email']= update_email
        
    banking_system.save_data()
    messagebox.showinfo(f"Your new email is {update_email}",f"Your new email is {update_email}")

    email_change.destroy()

def update_phonenumber(username,change_phone_number):
    new_phonenumber = enter_phonenumber.get()
    banking_system.users[username]["Mobile Number"] = new_phonenumber

    banking_system.save_data()
    
    messagebox.showinfo(f"Phone number updated successfully to {new_phonenumber}",f"Phone number updated successfully to {new_phonenumber}")
          
    change_phone_number.destroy()

def update_address(username,user_change):
    new_address = enter_address.get()
    banking_system.users[username]["address"] = new_address

    banking_system.save_data()

    messagebox.showinfo(f"address updated successfully to {new_address}",f"address updated successfully to {new_address}")

    user_change.destroy()
   

def open_change_info(update_info):
    open_username = tk.Button(update_info,
                              text="User name",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda:display_username(update_info,username),
                              width=20)
    open_username.pack(pady=5, ipadx=(20), ipady=(10))
    
    phone_number = tk.Button(update_info,
                             text="Phone Number",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=lambda: display_phone_number(update_info),
                             width=20)
    phone_number.pack(pady=5, ipadx=(20), ipady=(10))

    open_email = tk.Button(update_info,
                           text="email",
                           font=("Abhaya Libre", 25, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           command=lambda: display_email(update_info,username),
                           width=20)
    open_email.pack(pady=5, ipadx=(20), ipady=(10))
    
    address = tk.Button(update_info,
                        text="address",
                        font=("Abhaya Libre", 25, "bold"),
                        bg="#253568",
                        cursor="hand2",
                        command=lambda: display_address(update_info),
                        width=20)
    address.pack(pady=5, ipadx=(20), ipady=(10))

main_window.mainloop()