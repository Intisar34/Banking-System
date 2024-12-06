import tkinter as tk


def display_settings():

    #This is in the setting page and opens a page where you can handle deleting accounts
    delete_account = tk.Button(settings_window, 
                               text="Delete Account",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=create_delete_account)
    delete_account.pack(pady=10, ipadx=(20), ipady=(10))

    #This is in the setting page and the button opens a page where you can handle child services.
    child_services = tk.Button(settings_window, 
                               text="Child Services",
                               font=("Abhaya Libre", 18, "bold"),
                               bg="#253568",
                               cursor="hand2",
                               width=20,
                               command=create_child_account)
    child_services.pack(pady=10, ipadx=(20), ipady=(10))

def create_child_account():
    
    #This is the window that opens when the child button is pressed.
    child_window = tk.Toplevel(main_window)
    child_window.title("Child Services")
    child_window.geometry("800x600")
    child_window.config(bg="#253568")

    close_button = tk.Button(child_window, 
                             text="Close", 
                             font=("Abhaya Libre", 18, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             width=20, 
                             command=child_window.destroy)
    close_button.pack(pady=10, ipadx=(20), ipady=(10))


def create_delete_account():

    #This is the window that opens when the delete account button is pressed.
    delete_window = tk.Toplevel(main_window)
    delete_window.title("Delelte Account")
    delete_window.geometry("800x600")
    delete_window.config(bg="#253568")

    close_button = tk.Button(delete_window, 
                             text="Close", 
                             font=("Abhaya Libre", 18, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             width=20, 
                             command=delete_window.destroy)
    close_button.pack(pady=10, ipadx=(20), ipady=(10))


