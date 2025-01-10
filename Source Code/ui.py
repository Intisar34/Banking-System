from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import logic
import common

activity_history = []


#---------------------------------------------------------------------------------------------#
#this function creates the first page where the user will be able to log in or register

def creating_main_page(main_window):

    Label(main_window,text="Log in as a private customer:", anchor="center", font=("Abhaya Libre", 20, "bold"), bg="#253568").pack(pady=10)

    login_button = Button(main_window, text="LOGIN",
                          font=("Abhaya Libre", 18, "bold"),
                          bg="#253568",
                          cursor="hand2",
                          width=20,
                          command=lambda:login(main_window)).pack(pady=10, ipadx=(20), ipady=(10))
    
    Label(main_window,text="Register to become a customer:", anchor="center", font=("Abhaya Libre", 20, "bold"), bg="#253568").pack(pady=10)

    register_button = Button(main_window,
                             text="REGISTER",
                             font=("Abhaya Libre", 18, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             width=20,
                             command=lambda:register()).pack(pady=10, ipadx=(20), ipady=(10))
    
    return login_button, register_button


#---------------------------------------------------------------------------------------------#

#Handling Login Screen and Form Logic
def login(main_window):
    login_screen = Tk()
    login_screen.geometry("800x600")
    login_screen.title("Login Form")
    login_screen.config(bg="#253568")


    # Logic for creating input fields
    Label(login_screen, text="Username:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    username_entry = Entry(login_screen, font=("Abhaya Libre", 20, "bold"))
    username_entry.pack()

    Label(login_screen, text="Password:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    password_entry = Entry(login_screen, font=("Abhaya Libre", 20, "bold"), show="*")
    password_entry.pack()

    # Logic for buttons and funcition assignment
    Button(login_screen, text="Login", font=("Abhaya Libre", 18, "bold"),
           bg="#253568", cursor="hand2", width=20,
           command=lambda: logic.attempt_login(username_entry, password_entry, login_screen, choose_option_menu, main_window)).pack(pady=20, ipadx=20, ipady=10)

    Button(login_screen, text="Forget password",
           font=("Abhaya Libre", 18, "bold"),
           bg="#253568",
           cursor="hand2",
           width=12,
           command=lambda: forget_password()).pack(pady=10, ipadx=10, ipady=5)
    

#---------------------------------------------------------------------------------------------#

#this function shows the page where you willl be able to enter new password incase of forgotten
def forget_password():
    forget_password_window = Tk()
    forget_password_window.geometry("800x600")
    forget_password_window.title("Forget password")
    forget_password_window.config(bg="#253568")

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
           command=lambda: logic.forget_password_handle(username_entry.get(), new_password_entry.get(), confirm_password_entry.get(),forget_password_window)).pack(pady=20, ipadx=20, ipady=10)


#---------------------------------------------------------------------------------------------#


# Logic for handling user registration process
def register():
    register_screen = Tk()
    register_screen.geometry("800x600")
    register_screen.title("Register Form")
    register_screen.config(bg="#253568")

    # Explicitly create fields
    Label(register_screen, text="Full Name:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    full_name_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    full_name_entry.pack()

    # Logic for creating input fields
    Label(register_screen, text="Username:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    username_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    username_entry.pack()

    Label(register_screen, text="Password:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    password_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"), show="*")
    password_entry.pack()

    Label(register_screen, text="Mobile Number:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    mobile_number_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    mobile_number_entry.pack()

    Label(register_screen, text="Email:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    email_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    email_entry.pack()

    Label(register_screen, text="Address:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    address_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    address_entry.pack()

    Label(register_screen, text="Date of Birth:", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
    dob_entry = Entry(register_screen, font=("Abhaya Libre", 20, "bold"))
    dob_entry.pack()

    # Button for packing input screen
    Button(register_screen, text="Register", font=("Abhaya Libre", 18, "bold"),
           bg="#253568", cursor="hand2", width=20,
           command=lambda: logic.attempt_register(full_name_entry, username_entry, password_entry,
                                            mobile_number_entry, email_entry, address_entry,
                                            dob_entry, register_screen)).pack(pady=20, ipadx=20, ipady=10)


#---------------------------------------------------------------------------------------------#

#Deposit function validate input, process the deposit, and update the user's account balance.
def deposit_screen(username, update_balance):

    global deposit_window

    deposit_window = Tk()
    deposit_window.geometry("800x600")
    deposit_window.config(bg="#253568")
    deposit_window.title("Deposit")

    Label(deposit_window, text="Make a Deposit", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)
    Label(deposit_window, text="Enter Amount (kr):", font=("Abhaya Libre", 18), bg="#253568", fg="white").pack(pady=10)

    entry_amount = Entry(deposit_window, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    Button(deposit_window, text="Confirm", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=lambda: logic.validate_deposit(username, entry_amount, update_balance, print_activity, deposit_window)).pack(pady=10, ipadx=20, ipady=10)

    Button(deposit_window, text="Close", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=deposit_window.destroy).pack(pady=10, ipadx=20, ipady=10)

#---------------------------------------------------------------------------------------------#

#this function shows the page where you will be able to withdraw
def withdraw_screen(username, update_balance):

    global withdraw_window

    withdraw_window = Tk()
    withdraw_window.geometry("800x600")
    withdraw_window.config(bg="#253568")
    withdraw_window.title("Withdraw")

    Label(withdraw_window, text="Make a Withdraw", font=("Abhaya Libre", 30, "bold"), bg="#253568", fg="white").pack(pady=20)
    Label(withdraw_window, text="Enter Amount (kr):", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    entry_amount = Entry(withdraw_window, font=("Abhaya Libre", 18, "bold"), cursor="hand2", width=20)
    entry_amount.pack(pady=10, ipadx=20, ipady=10)

    Button(withdraw_window, text="Confirm", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20,
              command=lambda: logic.validate_withdraw(username, entry_amount, update_balance)).pack(pady=10, ipadx=20, ipady=10)

    Button(withdraw_window, text="Close", font=("Abhaya Libre", 18, "bold"),
              bg="#253568", cursor="hand2", width=20, command=withdraw_window.destroy).pack(pady=10, ipadx=20, ipady=10)

    return withdraw_window


#---------------------------------------------------------------------------------------------#

#this function  creates the page to show your current balance
def display_balance(username):

    menu_window = Tk()
    menu_window.geometry("800x600")
    menu_window.config(bg="#253568")
    menu_window.title("Main Page")

    amount = common.accounts.get(username, "N/A")

    current_balance = Label(menu_window, 
                            text="Current Amount", 
                            background="#253568",
                            foreground="White", 
                            font=("Abahya Libre", 30, "bold"))
    current_balance.pack(anchor="center")

    display_amount = Label(menu_window, 
                           text = f"{amount} kr", 
                           font=("Abahya Libre", 20), 
                           background="#253568",
                            foreground="White")
    display_amount.pack()

    return menu_window, display_amount

#---------------------------------------------------------------------------------------------#

#this function displays/creates the page where you will be  able to see your acitivity
def display_activity(username):

    global activity_window 

    #This part of the codee fetches the account number of the user in order to display it.
    account_number = common.account_numbers.get(username, 0)

    activity_window = Tk()
    activity_window.title("Balance Information")
    activity_window.config(bg="#253568")
    activity_window.geometry("800x600")

    display_name = Label(activity_window,
                            text=username,
                            foreground="White",
                            background="#253568",
                            font=("Times New Roman", 30, "bold"))
    display_name.pack(anchor="center", pady=5)

    display_account_number = Label(activity_window,
                              text=account_number,
                              foreground="White",
                              background="#253568",
                              font=("Abhaya Libre", 20))
    display_account_number.pack(anchor="center", pady=5)

    latest_activity = Label(activity_window, 
                            text="Latest activity", 
                            font=("Abhaya Libre", 20, "bold"), 
                            bg="#253568")
    latest_activity.pack(anchor="center", pady=10)

    #This for loop is used to iterate through the list of activities done and print them in the Latest Activity page. 
    for activity in activity_history:
        activity_info = Label(activity_window, text=f"{activity}", font=("Abhaya Libre", 18), bg="#253568")
        activity_info.pack(anchor="center", padx=40, pady=2)

    activity_window.mainloop()


#---------------------------------------------------------------------------------------------#
#this function shows your activity

def print_activity(username, amount):


    if logic.operation_type == "Deposit":
        output = f" Deposit: {username} ---> Amount: {amount} kr"

    elif logic.operation_type == "Withdraw":
        output = f" Withdraw: {username} ---> Amount: {amount} kr"

    elif  logic.operation_type== "Transaction":
        output = f" Transaction: {username} ---> Amount: {amount} kr ---> Recipent: {logic.recipient} --- Date: {logic.date}"

    elif  logic.operation_type == "Transfer":
        output = f" Transfer: {username} ---> Amount: {logic.amount_to_transfer} kr ---> Recipent: {logic.recipient} --- Date: {logic.date_transfer}"

    
    activity_history.append(output)

    return activity_history


#---------------------------------------------------------------------------------------------#

# this function displays the page where you are able to transfer
def display_transfer(username,update_balance):

    transfer = Tk()
    transfer.title("Transfer")
    transfer.geometry("800x600")
    transfer.config(bg="#253568")


    logic.do_transfer(transfer,username,update_balance, print_activity)


#---------------------------------------------------------------------------------------------#

#this function displays the page where you are able to do transactions
def display_transaction(username, update_balance):

    transaction_window = Tk()
    transaction_window.title("Transaction")
    transaction_window.geometry("800x600")
    transaction_window.config(bg="#253568")
    
    logic.do_transaction(transaction_window, username, update_balance, print_activity)

#---------------------------------------------------------------------------------------------#
    
#this function  displays the loan page
def display_loan(username, update_balance):

    loan_screen = Tk()
    loan_screen.geometry("800x600")
    loan_screen.title("Loan")
    loan_screen.config(bg="#253568")

    logic.do_loan(loan_screen,username, update_balance)


#---------------------------------------------------------------------------------------------#

#this function displays the settings page where they choose any of the options below
def display_settings(username):

    settings_window = Tk()
    settings_window.title("Settings")
    settings_window.geometry("800x600")
    settings_window.config(bg ="#253568")

    delete_account = Button(settings_window, text="Delete Account",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=lambda : choose_delete_account(username))
    delete_account.pack(pady=5, ipadx=(20), ipady=(10))

    update_info = Button(settings_window, 
                            text="Update Information", 
                            font=("Abhaya Libre", 18, "bold"), 
                            bg="#253568", 
                            cursor="hand2", 
                            width=20,
                            command=lambda : open_update_info_page(username))
    update_info.pack(pady=5, ipadx=(20), ipady=(10))
    
    saving_account = Button(settings_window,
                              text="Saving Account",
                              font=("Abhaya Libre", 18, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              width = 20,
                             command=lambda : display_saving_account(username))
    saving_account.pack(pady=5, ipadx=(20), ipady=(10))

    
#---------------------------------------------------------------------------------------------#
#this functions lets the user choose what to do after logging in

def choose_option_menu(username):

    display_button, display_amount = display_balance(username)

    #User story 4:Ghassan
    #Updates the balance display for a user.
    def update_balance():
        balance = common.accounts.get(username, 0)
        display_amount.config(text=f"{balance:.2f} kr")
        
    open_balance_info = Button(display_button,
                                  text="Balance Information",
                                  font=("Abhaya Libre", 25, "bold"),
                                  bg="#253568",
                                  cursor="hand2",
                                  command=lambda: display_activity(username),
                                  width=20)
    open_balance_info.pack(pady=5, ipadx=(20), ipady=(10))

    open_deposit = Button(display_button, text="Deposit",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=lambda: deposit_screen(username,update_balance),
                             width=20)
    open_deposit.pack(pady=5, ipadx=(20), ipady=(10))

    open_withdraw = Button(display_button, text="Withdraw",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda: withdraw_screen(username, update_balance),
                              width=20)
    open_withdraw.pack(pady=5, ipadx=(20), ipady=(10))
    

    open_transfer = Button(display_button,
                              text="Transfer",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda: display_transfer(username, update_balance),
                              width=20)
    open_transfer.pack(pady=5, ipadx=(20), ipady=(10))

    open_transaction = Button(display_button,
                                 text="Transaction",
                                 font=("Abhaya Libre", 25, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 command=lambda : display_transaction(username, update_balance),
                                 width=20)
    open_transaction.pack(pady=5, ipadx=(20), ipady=(10))

    open_loan = Button(display_button,
                          text="Loan",
                          font=("Abhaya Libre", 25, "bold"),
                          bg="#253568",
                          cursor="hand2",
                          command=lambda: display_loan(username, update_balance),
                          width=20)
    open_loan.pack(pady=5, ipadx=(20), ipady=(10))

    open_settings = Button(display_button,
                              text="Settings",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda : display_settings(username),
                              width=20)
    open_settings.pack(pady=5, ipadx=(20), ipady=(10))



#---------------------------------------------------------------------------------------------#

# this is the delete window page that the user will see when they decide to delete their personal account 
# or their savings account
def choose_delete_account(username):

    delete_window = Tk()
    delete_window.title("Delete account")
    delete_window.geometry("800x600")
    delete_window.config(bg="#253568")
    
    Label(delete_window, 
             text="Choose which account to delete", 
             font=("Abhaya Libre", 25, "bold"), 
             bg="#253568", fg="white").pack(pady=20)
     
    personal_account_button = Button(delete_window,
                                        text = "Personal Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= lambda : delete_primary_account(username))
    personal_account_button.pack(pady=10, ipadx=(20), ipady=(10))

    savings_account_button = Button(delete_window,
                                        text = "Savings Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= lambda : delete_savings_account(username))
    savings_account_button.pack(pady=10, ipadx=(20), ipady=(10))

#---------------------------------------------------------------------------------------------#
#this function deletes the primary account

def delete_primary_account(username):

    confirm_delete_window = Tk()
    confirm_delete_window.title("Delete primary account")
    confirm_delete_window.geometry("800x600")
    confirm_delete_window.config(bg="#253568")

    account_number = common.account_numbers.get(username, 0)

    Label(confirm_delete_window,
                text="Are you sure you want delete this account",
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
                                 command = lambda : confirm_deleting_primary(username, confirm_delete_window))
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

#---------------------------------------------------------------------------------------------#
#this function confirmes that the primary account has been deleted
def confirm_deleting_primary(username, confirm_delete_window):

    common.users.pop(username)
    common.accounts.pop(username)
    common.account_numbers.pop(username)

    common.save_data()
    messagebox.showinfo("Delete Account","Account was successfully deleted.")
    confirm_delete_window.destroy

#---------------------------------------------------------------------------------------------#
# this function sends a confirmation that the savings account is deleted.
def confirm_deleting_savings(username, confirm_delete_window):

    common.savings_account.pop(username)
  
    common.save_data()
    messagebox.showinfo("Delete Savings Account","Account was successfully deleted.")
    confirm_delete_window.destroy



#---------------------------------------------------------------------------------------------#

#This functions opens up the confirmation page for when wanting to delete a savings account.
def delete_savings_account(username):

    confirm_delete_window = Tk()
    confirm_delete_window.title("Delete savings account")
    confirm_delete_window.geometry("800x600")
    confirm_delete_window.config(bg="#253568")

    savings_number = common.savings_account.get(username, 0)


    Label(confirm_delete_window,
                text="Are you sure you want delete this account",
                anchor="center",
                font=("Abhaya Libre", 40, "bold"),
                fg = "White",
                bg="#253568").pack(pady=10)
    
    Label(confirm_delete_window,
                 text= f"""
    {username}
    {savings_number}""",
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
                                 command = lambda : confirm_deleting_savings(username, confirm_delete_window))
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

#---------------------------------------------------------------------------------------------#

# this function displays the page where the person chooses to update their personal information

def open_update_info_page(username):

    update_info = Tk()
    update_info.geometry("800x600")
    update_info.title("Update Personal Information")
    update_info.config(bg="#253568")

    Label(update_info, text="Update Personal Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    open_change_info(username, update_info)

#---------------------------------------------------------------------------------------------#


#this function displays the page to update the username
def display_username(username):

    global enter_username

    username_change = Tk()
    username_change.title("Changing Username")
    username_change.geometry("800x600")
    username_change.config(bg="#253568")

    Label(username_change, text="Update Username", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    
    Label(username_change, text="Enter new username: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
   
    enter_username = Entry(username_change,font = ("Abhaya Libre", 20, "bold"))
    enter_username.pack(pady=10, ipadx=20, ipady=10)

    Button(username_change,
           text = "Change username", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: logic.update_username(username,username_change, enter_username)).pack(pady=10, ipadx=(20), ipady=(10))


#---------------------------------------------------------------------------------------------#

#this functions displays the page for changing the phone number
def display_phone_number(username):

    global enter_phonenumber

    change_phone_number = Tk()
    change_phone_number.title("Changing Phone Number")
    change_phone_number.geometry("800x600")
    change_phone_number.config(bg="#253568")
    Label(change_phone_number, text="Update Phone Number", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    Label(change_phone_number, 
             text="Enter new phone number: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    
    enter_phonenumber = Entry(change_phone_number,font = ("Abhaya Libre", 20, "bold"))
    enter_phonenumber.pack(pady=10, ipadx=20, ipady=10)
    

    Button(change_phone_number,
           text = "Change phone number", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: logic.update_phonenumber(username,change_phone_number, enter_phonenumber)).pack(pady=10, ipadx=(20), ipady=(10))   

#---------------------------------------------------------------------------------------------#
#this functions displays the page for changing the address

def display_address(username):

    global enter_address

    adress_window = Tk()
    adress_window.title("Changing Username")
    adress_window.geometry("800x600")
    adress_window.config(bg="#253568")

    Label(adress_window, text="Update Address", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    Label(adress_window, text="Enter new address: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5) 
    
    enter_address = Entry(adress_window,font = ("Abhaya Libre", 20, "bold"))
    enter_address.pack(pady=10, ipadx=20, ipady=10)

    Button(adress_window,
           text = "Change address", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: logic.update_address(username, adress_window, enter_address)).pack(pady=10, ipadx=(20), ipady=(10))


#---------------------------------------------------------------------------------------------#
#this function displays the page to update your email

def display_email(username):

    global enter_email

    email_change = Tk()
    email_change.title("Changing Username")
    email_change.geometry("800x600")
    email_change.config(bg="#253568")

    Label(email_change, text="Update Email", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    
    
    Label(email_change, text="Enter new email: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    enter_email = Entry(email_change,font = ("Abhaya Libre", 20, "bold"))
    enter_email.pack(pady=10, ipadx=20, ipady=10)

    Button(email_change,
           text = "Change email", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: logic.update_email(username,email_change, enter_email)).pack(pady=10, ipadx=(20), ipady=(10))


#---------------------------------------------------------------------------------------------#
#this function opens the settings page for updating the personal information and the user clicks on 
# which personal information they choose to update

def open_change_info(username, update_info):
    
    open_username = Button(update_info,
                              text="Username",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda:display_username(username),
                              width=20)
    open_username.pack(pady=5, ipadx=(20), ipady=(10))
    
    open_phone_number = Button(update_info,
                             text="Phone Number",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=lambda: display_phone_number(username),
                             width=20)
    open_phone_number.pack(pady=5, ipadx=(20), ipady=(10))

    open_email = Button(update_info,
                           text="Email",
                           font=("Abhaya Libre", 25, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           command=lambda: display_email(username),
                           width=20)
    open_email.pack(pady=5, ipadx=(20), ipady=(10))
    
    open_address = Button(update_info,
                        text="Address",
                        font=("Abhaya Libre", 25, "bold"),
                        bg="#253568",
                        cursor="hand2",
                        command=lambda: display_address(username),
                        width=20)
    open_address.pack(pady=5, ipadx=(20), ipady=(10))

    Button(update_info, 
           text="Close", 
           font=("Abhaya Libre", 18, "bold"), 
           bg="#253568", 
           fg="white", 
           cursor="hand2", 
           command=update_info.destroy).pack(pady=10, ipadx=20, ipady=10)

#---------------------------------------------------------------------------------------------#

    #this function is the window that the user will see when they click on savings account button on the delete page where they will be able
# to enter their username and the amount they wish to have in their savings account 

def display_saving_account(username):

    global enter_money

    saving_window = Tk()
    saving_window.title("Savings account")
    saving_window.geometry("300x300")
    saving_window.config(bg="#253568")

    Label(saving_window,
          text="Savings Account",
          font=("Abhaya Libre", 20, "bold"),
          bg="#253568",
          fg="white").pack(pady=10)

    Label(saving_window,
          text="Fill in your username here:",
          font=("Abhaya Libre", 20, "bold"),
          bg="#253568",
          fg="white").pack(pady=10)

    enter_name = Entry(saving_window, font=("Abhaya Libre", 20, "bold"))
    enter_name.pack(pady=10, ipadx=20, ipady=10)

    Label(saving_window,
          text="Specify the desired amount you wish to have in your savings account:",
          font=("Abhaya Libre", 20, "bold"),
          bg="#253568",
          fg="white").pack(pady=10)

    enter_money = Entry(saving_window, font=("Abhaya Libre", 20, "bold"))
    enter_money.pack(pady=10, ipadx=20, ipady=10)

    generate_saving_account = Button(saving_window,
                                        text="Create",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        cursor="hand2",
                                        width=20,
                                        command=lambda :logic.create_savings_account(username, add_money, enter_money))
    generate_saving_account.pack(pady=10, ipadx=(20), ipady=(10))

    close_button = Button(saving_window,
                             text="Close",
                             font=("Abhaya Libre", 18, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             width=20,
                             command=saving_window.destroy)
    close_button.pack(pady=10, ipadx=(20), ipady=(10))

#---------------------------------------------------------------------------------------------#
#this function adds money to the savings account
def add_money(username):
    
    add_amount = Tk()
    add_amount.title("Savings account")
    add_amount.geometry("300x300")
    add_amount.config(bg ="#253568")
    
    Label(add_amount,
     text=f"Savings Account: {username}", 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568", 
     fg="white").pack(pady=10)
    
    Label(add_amount,
     text= logic.savings_balance, 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568", 
     fg="white").pack(pady=10)
