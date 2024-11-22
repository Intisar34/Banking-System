import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import re
import random


# Main window
main_window = Tk()
main_window.title('Banking System')
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
img_3 = img_3.resize((500,180))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('FF_logo.png')
img_4 = img_4.resize((500,180))
img_4 = ImageTk.PhotoImage(img_4)


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
                      command=lambda: login()).pack(pady=10, ipadx=(20), ipady=(10))

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
        self.accounts = {}
        self.account_numbers = {}

    def generate_account_number(self):
        generate = False
        while not generate:
            account_number = str(random.randint(10**9, 10**10 - 1))
            if account_number not in self.account_numbers.values():
                generate = True
        return account_number


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
        self.accounts[username] = 0
        return f"User registered successfully! Your account number is {account_number}."
    

    def login_user(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False


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
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        if banking_system.login_user(username, password):
            messagebox.showinfo("Login", f"Welcome, {username}!")
            login_screen.destroy()
            open_buttons(username)

        else:
            messagebox.showerror("Error", "Invalid username or password.")

    Button(login_screen, text="Login", font=("Abhaya Libre", 18, "bold"),
           bg="#253568", cursor="hand2", width=20, command=attempt_login).pack(pady=20, ipadx=20, ipady=10)

# This handles the user registration process
def register():
    register_screen = Toplevel(main_window)
    register_screen.geometry("800x600")
    register_screen.title("Register Form")
    register_screen.config(bg="#253568")

    labels = ["Full Name", "Username", "Password", "Mobile Number", "Email", "Address", "Date of Birth"]
    entries = {}

    Label(register_screen,
      image = img_3, 
      anchor="center", 
      bg="#253568").pack(pady=15, padx=50)

    for i, label_text in enumerate(labels):
        Label(register_screen, text=label_text + ":", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=5)
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



def display_balance():
    menu_screen = Toplevel()
    menu_screen.geometry("800x600")
    menu_screen.config(bg="#253568")
    menu_screen.title("Main Page")

    tk.Label(menu_screen,image = img_4, anchor="center", bg="#253568").pack(pady=15, padx=50)
  
    frame_name = tk.Frame(menu_screen, background="#253568")
    frame_name.pack()
    frame_amount = tk.Frame(menu_screen, background="#253568")
    frame_amount.pack()

    current_balance = tk.Label(master=frame_name, text="Current Amount", background="#253568",
                               foreground="White", font=("Abahya Libre", 30, "bold"))
    display_amount = tk.Label(master=frame_amount, text="0,00 kr", font=("Abahya Libre", 20), background="#253568",
                              foreground="White")

    current_balance.pack(anchor = "center")
    display_amount.pack()
    return menu_screen


def display_balance_info(banking_system, username):

      account_number = banking_system.account_numbers.get(username, "N/A")

      #trans_history = display_history()
    
      balance_info = tk.Toplevel(main_window) 
      balance_info.title("Balance Information")
      balance_info.config(bg="#253568")
      balance_info.geometry("800x600")

      img_3 = Image.open('FF_logo.png')
      img_3 = img_3.resize((300,100))
      img_3 = ImageTk.PhotoImage(img_3)

      tk.Label(balance_info, image = img_3, anchor="w", bg="#253568").pack(pady = 10, padx = 20)

      #close_balance_info = tk.Button(balance_info, 
                                   #text = "Close", 
                                   #font=("Abhaya Libre", 20, "bold"), 
                                   #bg="White", 
                                   #cursor="hand2",
                                   #width=10,
                                   #command = balance_info.destroy)
      #close_balance_info.pack(anchor = "se")
  
      account_name = tk.Frame(balance_info, background = "#253568")
      account_name.pack(anchor = "nw")
      new_account_number = tk.Frame(balance_info, background = "#253568")
      new_account_number.pack(anchor = "nw")

    #transaction = tk.Frame(balance_info, background = "#253568")
    #transaction.pack(anchor = "w", padx = 10, pady = (10,0))

    
      display_name = tk.Label(master = account_name, 
                              text = username, 
                              foreground = "White", 
                             background = "#253568", 
                             font = ("Times New Roman", 30, "bold"))
      
      display_number = tk.Label(master = new_account_number, 
                                text = account_number, 
                                foreground = "White", 
                                background = "#253568", 
                                font = ("Abhaya Libre", 20))
      #display_amount = tk.Label(master = transaction, text = "Transaction History:", foreground = "Black", background = "White",
                                #font = ("Abhaya Libre", 20))
    
      display_name.pack(anchor = "nw", pady = 5)
      display_number.pack(anchor = "nw", pady = 5)

     #From here it displays transaction history:
      trans_history = display_history()

      history_trans = tk.Label(balance_info, text = "Transaction History", font = ("Abhaya Libre", 20, "bold"), bg = "#253568" )
      history_trans.pack(anchor = "center", pady = 10)
      
      for transaction in trans_history:
          transaction_info = tk.Label(balance_info , text = f"{transaction}", font = ("Abhaya Libre", 18), bg = "#253568")
          transaction_info.pack(anchor = "w", padx = 40, pady = 2)


      balance_info.mainloop()
      #display_amount.grid(row = 2, column = 0, sticky = "w")
  
def display_history():

    transaction_history = []
    for i in range(5):
        transaction_history.append(f"Sender: xxxxx --- Amount: xxxxx kr --- Recipent: xxxxx")
        return transaction_history


def display_transfer():
    transfer = Toplevel(main_window)
    transfer.title("Transfer")
    transfer.geometry("300x300")
    close_transfer = tk.Button(transfer,
                               text="Close",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="White",
                               cursor="hand2",
                               width=20,
                               command=transfer.destroy)
    close_transfer.pack(pady=140)

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

def display_transaction():
    transaction = Toplevel(main_window)
    transaction.title("Transaction")
    transaction.geometry("800x600")
    close_transaction = tk.Button(transaction, text="Close",
                                  font=("Abhaya Libre", 18, "bold"),
                                  bg="#253568",
                                  cursor="hand2",
                                  width=20,
                                  command=transaction.destroy)
    close_transaction.pack(pady=140)


def display_loan():
    loan = Toplevel(main_window)
    loan.title("Loan")
    loan.geometry("300x300")
    close_loan = tk.Button(loan, text="Close",
                           font=("Abhaya Libre", 18, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           width=20,
                           command=loan.destroy)
    close_loan.pack(pady=140)


def display_settings():
    settings = Toplevel(main_window)
    settings.title("Settings")
    settings.geometry("300x300")
    close_settings = tk.Button(settings, text="Close",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=settings.destroy)
    close_settings.pack(pady=140)



def open_buttons(username):

    display_button = display_balance()

    open_balance_info = tk.Button(display_button,
                                  text="Balance Information",
                                  font=("Abhaya Libre", 25, "bold"),
                                  bg="#253568",
                                  cursor="hand2",
                                  command=lambda : display_balance_info(banking_system, username),
                                  width=20)
    open_balance_info.pack(pady=5, ipadx=(20), ipady=(10))

    open_deposit = tk.Button(display_button, text="Deposit",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=display_deposit,
                             width=20)
    open_deposit.pack(pady=5, ipadx=(20), ipady=(10))

    open_withdraw = tk.Button(display_button, text="Withdraw",
                             font=("Abhaya Libre", 25, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             command=display_withdraw,
                             width=20)
    open_withdraw.pack(pady=5, ipadx=(20), ipady=(10))


    open_transfer = tk.Button(display_button,
                              text="Transfer",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=display_transfer,
                              width=20)
    open_transfer.pack(pady=5, ipadx=(20), ipady=(10))

    open_transaction = tk.Button(display_button,
                                 text="Transaction",
                                 font=("Abhaya Libre", 25, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 command=display_transaction,
                                 width=20)
    open_transaction.pack(pady=5, ipadx=(20), ipady=(10))

    open_loan = tk.Button(display_button,
                          text="Loan",
                          font=("Abhaya Libre", 25, "bold"),
                          bg="#253568",
                          cursor="hand2",
                          command=lambda: display_loan,
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


main_window.mainloop()