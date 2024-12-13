
#this function is used to create the main page after the person chooses to delete their account from the settings.
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
#the user will click on personal account button if they want to delete their personal account.
    personal_account_button = tk.Button(delete_window,
                                        text = "Personal Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= delete_primary_account)
    personal_account_button.pack(pady=10, ipadx=(20), ipady=(10))

#the user will click on child account button if the user chooses to delete their child account.
    child_account_button = tk.Button(delete_window,
                                        text = "Child Account",
                                        font=("Abhaya Libre", 18, "bold"),
                                        bg="#253568",
                                        fg = "White",
                                        cursor="hand2",
                                        width=20, 
                                        command= delete_child_account)
    child_account_button.pack(pady=10, ipadx=(20), ipady=(10))

#this creates a top-up window after the person clicks on the child-account button.
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
