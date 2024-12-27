



def update_phonenumber(username,change_phone_number):
    new_phonenumber = enter_phonenumber.get()
   
    if re.findall(r"[a-zA-Z@.]",new_phonenumber):
        messagebox.showerror("Error", "please type in a valid phone number")

    else: 
       users[username]["Mobile Number"] = new_phonenumber
       save_data()
       messagebox.showinfo(f"Phone number updated successfully to {new_phonenumber}",f"Phone number updated successfully to {new_phonenumber}")
          
    change_phone_number.destroy()

def update_address(username,user_change):
    new_address = enter_address.get()
    
    if re.findall(r"\d", new_address):
        messagebox.showerror("Error", "please type in a valid address")
    
    else: 
     users[username]["address"] = new_address
     save_data()
     messagebox.showinfo(f"address updated successfully to {new_address}",f"address updated successfully to {new_address}")

    user_change.destroy()
    #this function is creating a Json file that is storing the users account number and their personal information.
#when a user first registers,their information is saved in the file.

def save_data():
    data = {
        "users": users,
        "accounts": accounts,
        "account_numbers": account_numbers,
        "savings_account": saving_account_number
    }
    with open("bank_users.json", "w") as file:
        json.dump(data, file, indent=4)

# This function loads the data from the Json file.
# It is called when a user attempts to log in so their username,password and other account details can be retrieved.

def load_data():
    global users, accounts, account_numbers
    with open("bank_users.json","r") as file:
        data = json.load(file)
    users = data.get("users", {})
    account_numbers = data.get("account_numbers", {})
    accounts = data.get("accounts", {})

load_data()

def login_user(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False
#once the user clicks on generate, the account will be created as the function generate account number is being called and the account number along
# with the username is being saved into the Json file by calling the save_data function.

def create_savings_account():
    global savings_account_number
    
    savings_account_number = generate_account_number()

    saving_account_number[username] = savings_account_number #assigning a key-value pair in the saving_account_number dictionary.
    
    save_data()

    messagebox.showinfo(f"savings account", f"You created a savings account! your savings account number is {savings_account_number}")
    
# this is the delete window page that the user will see when they decide to delete their personal account and click on the delete button on the settings page
def create_delete_account():

    delete_window = tk.Toplevel(main_window)
    delete_window.title("delete account")
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

    #this function is the window that the user will see when they click on savings account button on the delete page where they will be able
# to enter their username and the amount they wish to have in their savings account  

def display_saving_account():
    
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
    
    generate_saving_account = tk.Button(saving_window,
                                        text="generate",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        cursor="hand2",
                                        width=20,
                                        command = create_savings_account)
    generate_saving_account.pack(pady=10, ipadx=(20), ipady=(10))
    
    close_button = tk.Button( saving_window,
                              text="close",
                              font=("Abhaya Libre", 18, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              width=20,
                              command = saving_window.destroy)
    close_button.pack(pady=10, ipadx=(20), ipady=(10))
