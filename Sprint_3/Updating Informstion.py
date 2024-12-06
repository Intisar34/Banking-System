# dropdown menu

def open_change_info(updating_info):
    open_username = tk.Button(updating_info,
                              text="User name",
                              font=("Abhaya Libre", 25, "bold"),
                              bg="#253568",
                              cursor="hand2",
                              command=lambda:display_username(updating_info,username),
                              width=20)
    open_username.pack(pady=5, ipadx=(20), ipady=(10))

    open_email = tk.Button(updating_info,
                           text="email",
                           font=("Abhaya Libre", 25, "bold"),
                           bg="#253568",
                           cursor="hand2",
                           command=lambda: display_email(updating_info,username),
                           width=20)
    open_email.pack(pady=5, ipadx=(20), ipady=(10))

# updating the json file 


def display_username(updating_info,username):
    global enter_username
    username_change = Toplevel(updating_info)
    username_change.title("Changing Username")
    username_change.geometry("300x300")
    Label(username_change, text="Update Username", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    username_change.config(bg="#253568")
    
    tk.Label(username_change, text="Enter new username: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    enter_username = tk.Entry(username_change,font = ("Abhaya Libre", 20, "bold"))
    enter_username.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(username_change,
           text = "Change username", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_username(username,username_change)).pack(pady=10, ipadx=(20), ipady=(10))

def update_username(username,username_change):
    update_username = enter_username.get()
    for username in banking_system.users:
        banking_system.users[update_username] = banking_system.users.pop(username)
        
        banking_system.save_data()
        messagebox.showinfo(f"Your new username is {update_username}",f"Your new username is {update_username}")

        username_change.destroy() 

def display_email(updating_info,username):
    global enter_email
    email_change = Toplevel(updating_info)
    email_change.title("Changing Username")
    email_change.geometry("300x300")
    Label(email_change, text="Update email", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    email_change.config(bg="#253568")
    
    tk.Label(email_change, text="Enter new email: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    enter_email = tk.Entry(email_change,font = ("Abhaya Libre", 20, "bold"))
    enter_email.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(email_change,
           text = "Change email", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_email(username,email_change)).pack(pady=10, ipadx=(20), ipady=(10))


def update_email(username,email_change):
    update_email = enter_email.get()
    if "@" not in update_email or "." not in update_email:
            messagebox.showerror("Error", "Invalid email address.")
            return
    
    for username in banking_system.users:
        banking_system.users[username]['email']= update_email
        
        banking_system.save_data()
        messagebox.showinfo(f"Your new email is {update_email}",f"Your new email is {update_email}")

        email_change.destroy()

