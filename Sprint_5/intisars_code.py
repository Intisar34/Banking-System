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
    generate_saving_account.pack(pady=10,ipadx=(20), ipady=(10)

def create_savings_account():
    global savings_account_number

    savings_account_number = banking_system.generate_account_number()
    
    banking_system.saving_account_number[username] = savings_account_number
    
    banking_system.save_data()

    messagebox.showinfo(f"savings account", f"You created a savings account! your savings account number is {savings_account_number}")