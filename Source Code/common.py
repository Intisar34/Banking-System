import json 
import random
import re

#---------------------------------------------------------------------------------------------#

# This is empty dictionaries that will later hold and save data
users = {}
accounts = {}
account_numbers = {}
savings_account = {}

#---------------------------------------------------------------------------------------------#

# This fucntion loads, reads and adds data to the json file
def load_data():
    global users, accounts, account_numbers
    with open("bank_users.json","r") as file:
        data = json.load(file)
    users = data.get("users", {})
    account_numbers = data.get("account_numbers", {})
    accounts = data.get("accounts", {})

load_data()


#---------------------------------------------------------------------------------------------#

# This fucntion appends the data into the dictionaries and adds it to json file.
def save_data():
    data = {
        "users": users,
        "accounts": accounts,
        "account_numbers": account_numbers,
        "savings_account": savings_account
    }
    with open("bank_users.json", "w") as file:
        json.dump(data, file, indent=4)

#---------------------------------------------------------------------------------------------#

# This fucntion checks if the users password equals the one saved in the jason file.
def login_user(username, password):
    if username in users and users[username]["password"] == password:
        return True
    return False


#---------------------------------------------------------------------------------------------#

# This fucntion checks if a string is valid (e.g string must include positive number, floating numbers).
def valid_amount(input_value):
    valid_input = input_value.replace('.', '', 1)
    valid = valid_input and float(input_value) > 0
    return valid


#---------------------------------------------------------------------------------------------#

# This fucntion validates the password making sure the givin input meets the requirements.
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

# This fucntion generates an 10 digit number to act as the personal account number for each user.
def generate_account_number():
    generate = False
    while not generate:
        account_number = str(random.randint(10 ** 9, 10 ** 10 - 1))
        if account_number not in account_numbers.values():
            generate = True
    return account_number

#---------------------------------------------------------------------------------------------#


