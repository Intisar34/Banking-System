

#This function displays the current balance in the account along with the users account number. 
def display_balance():

    menu_window = tk.Toplevel(main_window)
    menu_window.geometry("800x600")
    menu_window.config(bg="#253568")
    menu_window.title("Main Page")

    tk.Label(menu_window, 
             image=img_4, 
             anchor="center", 
             bg="#253568").pack(pady=15, padx=50)

    amount = "0,00 kr"

    current_balance = tk.Label(menu_window, 
                               text="Current Amount",
                                background="#253568",
                               foreground="White", 
                               font=("Abahya Libre", 30, "bold"))
    current_balance.pack(anchor="center")
    
    display_amount = tk.Label(menu_window, 
                              text = amount, 
                              font=("Abahya Libre", 20), 
                              background="#253568",
                              foreground="White")
    display_amount.pack()

    choose_option_menu(username, menu_window)

    return display_amount


#This function displays the latest actitivy. It prints if a withdrawl/deposit/activity or transfer has been done in the account.
def display_activity(username):

    #This part of the codee fetches the account number of the user in order to display it.
    account_number = account_numbers.get(username, 0)

    activity_window = tk.Toplevel(main_window)
    activity_window.title("Balance Information")
    activity_window.config(bg="#253568")
    activity_window.geometry("800x600")

    tk.Label(activity_window, 
            image=img_3, 
            anchor="w",
            bg="#253568").pack(pady=10, padx=20)

    display_name = tk.Label(activity_window,
                            text=username,
                            foreground="White",
                            background="#253568",
                            font=("Times New Roman", 30, "bold"))
    display_name.pack(anchor="center", pady=5)

    display_account_number = tk.Label(activity_window,
                              text=account_number,
                              foreground="White",
                              background="#253568",
                              font=("Abhaya Libre", 20))
    display_account_number.pack(anchor="center", pady=5)

    latest_activity = tk.Label(activity_window, 
                            text="Latest activity", 
                            font=("Abhaya Libre", 20, "bold"), 
                            bg="#253568")
    latest_activity.pack(anchor="center", pady=10)

    #This for loop is used to iterate through the list of activities done and print them in the Latest Activity page. 
    for activity in activity_history:
        activity_info = tk.Label(activity_window, text=f"{activity}", font=("Abhaya Libre", 18), bg="#253568")
        activity_info.pack(anchor="center", padx=40, pady=2)

    activity_window.mainloop()



#This function validates and saves the inputs from the user when doing a transaction.
def validate_activity_input(username, update_balance, activity_window):

    global amount, recipient, date, message, ocr

    recipient = recipient_input.get()
    amount = float(amount_input.get())
    ocr = int(ocr_input.get())
    date = date_input.get()
    message = message_input.get()

    #The if-elif-else statements are error handlings that check if the inputs are correct, so that the user is aware that there are certain requirements.
    if not all([recipient, amount, ocr, date]):
            messagebox.showerror("Error", "All fields are required!")
            return do_activity(activity_window, username, update_balance)
   
    elif amount <= 0:
        messagebox.showerror("Invalid amount! Amount must be greater than 0.")
   
    elif ocr < 5 and ocr > 10:
        messagebox.showerror("Invalid OCR number. OCR number must be 5 - 10 digits.")

    elif not date.isdigit():
        messagebox.showerror("Invalid date. Date must be digits.")

    else: 
        authenticate_activity(username, update_balance)




#This function lets you choose which account you want to delete. Gives you the option to choose between personal and savings account.
def choose_delete_account():

    delete_window = tk.Toplevel(main_window)
    delete_window.title("Delete account")
    delete_window.geometry("800x600")
    delete_window.config(bg="#253568")

    tk.Label(delete_window, 
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

    savings_account_button = tk.Button(delete_window,
                                        text = "Savings Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= delete_savings_account)
    savings_account_button.pack(pady=10, ipadx=(20), ipady=(10))


#This functions opens up the confirmation page for when wanting to delete a savings account.
def delete_savings_account():

    confirm_delete_window = tk.Toplevel(main_window)
    confirm_delete_window.title("Delete savings account")
    confirm_delete_window.geometry("800x600")
    confirm_delete_window.config(bg="#253568")

    tk.Label(confirm_delete_window, 
          image=img_7, 
          anchor="center", 
          bg="#253568").pack(pady=15, padx=50)

    tk.Label(confirm_delete_window,
                text="Are you sure you want delete this account:",
                anchor="center",
                font=("Abhaya Libre", 40, "bold"),
                fg = "White",
                bg="#253568").pack(pady=10)
    
    tk.Label(confirm_delete_window,
                 text= f"""
    {username}
    Savings Acount""",
                 anchor="center",
                 font=("Abhaya Libre", 30, "bold"),
                 fg = "White",
                 bg="#253568").pack(pady=10)
    
    confirmation_button = tk.Button(confirm_delete_window, 
                                 text = "Delete", 
                                 font=("Abhaya Libre", 18, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 width=20, 
                                 command = lambda : confirm_deleting(username))
    confirmation_button.pack(pady=10, ipadx=(20), ipady=(10))
    
    cancel_button = tk.Button(confirm_delete_window, 
                           text = "Cancel", 
                           font=("Abhaya Libre", 18, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           width=20,
                           command=confirm_delete_window.destroy)
    cancel_button.pack(pady=10, ipadx=(20), ipady=(10))

    confirm_delete_window.mainloop()