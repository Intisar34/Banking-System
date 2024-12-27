def add_money():
    
    add_amount = Toplevel(main_window)
    add_amount.title("Savings account")
    add_amount.geometry("300x300")
    add_amount.config(bg ="#253568")
    
    Label(add_amount,
     text=f"Savings Account: {username}", 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568", 
     fg="white").pack(pady=10)
    
    Label(add_amount,
     text= savings_balance, 
     font=("Abhaya Libre", 20, "bold"), 
     bg="#253568", 
     fg="white").pack(pady=10)

 

def adding_money():

    global savings_balance

    savings_balance = 0
    money_saving = float(enter_money.get())
    savings_balance += money_saving
    savings_balance = f"{money_saving:.2f} kr"