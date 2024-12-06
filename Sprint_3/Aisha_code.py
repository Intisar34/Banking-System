Button(login_screen, text="Forget password",
                      font=("Abhaya Libre", 18, "bold"),
                      bg="#253568",
                      cursor="hand2",
                      width=12,
                      command=lambda:forget_password(img_5)).pack(pady=10, ipadx=(10), ipady=(5))
    
    
def forget_password(img_5):
    forget_password_window = Toplevel()
    forget_password_window.geometry("800x600")
    forget_password_window.title("Forget password")
    forget_password_window.config(bg="#253568")


def update_password_json(username_entry, confirm_password_entry):
    # read the json file first
    with open("bank_users.json", "r") as file:
        data = json.load(file)

    if username_entry not in data["users"]:
        return "The username is not found."

    # we update the password
    data["users"][username_entry]["password"] = confirm_password_entry

    # we overwrite the json file
    with open("bank_users.json", "w") as file:
        json.dump(data, file, indent=4)

    return "The password has been successfully updated in the JSON file."