from tkinter import *
from PIL import ImageTk, Image

#This function opens a confirmation page after the user has chosen an account to delete.
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
    
#The user confirms the deleting by pressing this button.
    confirmation_button = Button(confirm_delete_window, 
                                 text = "Delete", 
                                 font=("Abhaya Libre", 18, "bold"),
                                 bg="#253568",
                                 cursor="hand2",
                                 width=20, 
                                 command = lambda : confirm_deleting(username))
    confirmation_button.pack(pady=10, ipadx=(20), ipady=(10))

#In case the user chooses to not delete its account it can click on this button that will cancel the deleting process.
    cancel_button = Button(confirm_delete_window, 
                           text = "Cancel", 
                           font=("Abhaya Libre", 18, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           width=20,
                           command=confirm_delete_window.destroy)
    cancel_button.pack(pady=10, ipadx=(20), ipady=(10))

    confirm_delete_window.mainloop()


#This function deletes the account and updates the json file where the accounts are stored.
def confirm_deleting(username):

    banking_system.users.pop(username)
        
    banking_system.save_data()
    messagebox.showinfo("Delete Account","Account was successfully deleted.")
