def display_phone_number(updating_info):
    global enter_phonenumber
    change_phone_number = Toplevel(updating_info)
    change_phone_number.title("Changing Phone Number")
    change_phone_number.geometry("800x600")
    change_phone_number.config(bg="#253568")
    Label(change_phone_number, text="Update Phone Number", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)

    tk.Label(change_phone_number, 
             text="Enter new phone number: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5)
    
    enter_phonenumber = tk.Entry(change_phone_number,font = ("Abhaya Libre", 20, "bold"))
    enter_phonenumber.pack(pady=10, ipadx=20, ipady=10)
    

    tk.Button(change_phone_number,
           text = "Change phone number", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_phonenumber(username,change_phone_number)).pack(pady=10, ipadx=(20), ipady=(10))   

def display_address(updating_info):
    global enter_address
    address_change = Toplevel(updating_info)
    address_change.title("Changing Username")
    address_change.geometry("800x600")
    address_change.config(bg="#253568")
    Label(address_change, text="Update address", font=("Abhaya Libre", 20, "bold"), bg="#253568", fg="white").pack(pady=10)
    tk.Label(address_change, text="Enter new address: ",
             font = ("Abhaya Libre", 20, "bold"), 
             fg = "White", 
             bg = "#253568").pack(pady = 5) 
    enter_address = tk.Entry(address_change,font = ("Abhaya Libre", 20, "bold"))
    enter_address.pack(pady=10, ipadx=20, ipady=10)

    tk.Button(address_change,
           text = "Change address", 
           font = ("Abhaya Libre", 20, "bold"), 
           bg="#253568",
           cursor="hand2",
           width=20,
           command =lambda: update_address(username,address_change)).pack(pady=10, ipadx=(20), ipady=(10))





def update_phonenumber(username,change_phone_number):
    new_phonenumber = enter_phonenumber.get()
    banking_system.users[username]["Mobile Number"] = new_phonenumber

    banking_system.save_data()
    
    messagebox.showinfo(f"Phone number updated successfully to {new_phonenumber}",f"Phone number updated successfully to {new_phonenumber}")
          
    change_phone_number.destroy()

def update_address(username,user_change):
    new_address = enter_address.get()
    banking_system.users[username]["address"] = new_address

    banking_system.save_data()

    messagebox.showinfo(f"address updated successfully to {new_address}",f"address updated successfully to {new_address}")

    user_change.destroy()
