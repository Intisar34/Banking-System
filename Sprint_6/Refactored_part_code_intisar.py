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