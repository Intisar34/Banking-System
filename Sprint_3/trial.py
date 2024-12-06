def open_update_info_page():
    update_window = Toplevel(main_window)
    update_window.geometry("800x600")
    update_window.title("Update Personal Information")
    update_window.config(bg="#253568")

    tk.Label(update_window, text="Update Personal Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    tk.Button(update_window, text="Close", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2", command=update_window.destroy).pack(pady=10, ipadx=20, ipady=10)

def open_chatbot_page():
    chatbot_window = Toplevel(main_window)
    chatbot_window.geometry("800x600")
    chatbot_window.title("Chatbot")
    chatbot_window.config(bg="#253568")

    tk.Label(chatbot_window, text="Chatbot Interaction", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    tk.Button(chatbot_window, text="Close", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2", command=chatbot_window.destroy).pack(pady=10, ipadx=20, ipady=10)


def open_delete_info_page():
    delete_window = Toplevel(main_window)
    delete_window.geometry("800x600")
    delete_window.title("Delete Personal Information")
    delete_window.config(bg="#253568")

    tk.Label(delete_window, text="Delete Personal Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white").pack(pady=20)

    tk.Button(delete_window, text="Close", font=("Abhaya Libre", 18, "bold"), bg="#253568", fg="white", cursor="hand2", command=delete_window.destroy).pack(pady=10, ipadx=20, ipady=10)


def open_buttons(username):
    display_button, display_amount = display_balance()

    def update_balance():
        balance = banking_system.accounts.get(username, 0)
        display_amount.config(text=f"{balance:.2f} kr")


    tk.Button(display_button, text="Update Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white", cursor="hand2", command=lambda: update_user_info(username)).pack(pady=5, ipadx=(20), ipady=(10))
    
    tk.Button(display_button, text="Chatbot", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white", cursor="hand2", command=launch_chatbot).pack(pady=5, ipadx=(20), ipady=(10))

    tk.Button(display_button, text="Delete Information", font=("Abhaya Libre", 25, "bold"), bg="#253568", fg="white", cursor="hand2", command=lambda: delete_user_info(username)).pack(pady=5, ipadx=(20), ipady=(10))
