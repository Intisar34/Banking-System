main_window = Tk()
main_window.title("Banking System")
main_window.geometry("800x600")
main_window.config(bg="#253568")

# Logo Images of different sizes
def import_image(file_path, width, height):
    img = Image.open(file_path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)


large_image = import_image('FF_logo.png', 700, 240)
medium_image = import_image('FF_logo.png', 500, 180)
small_image = import_image('FF_logo.png', 100, 50)

# Main window
def creating_main_page(main_window):

    tk.Label(main_window,image=large_image,anchor="center",bg="#253568").pack(pady=15, padx=50)

    tk.Label(main_window,text="Log in as a private customer:", anchor="center", font=("Abhaya Libre", 20, "bold"), bg="#253568").pack(pady=10)

    login_button = tk.Button(main_window, text="LOGIN",
                          font=("Abhaya Libre", 18, "bold"),
                          bg="#253568",
                          cursor="hand2",
                          width=20,
                          command=lambda:login()).pack(pady=10, ipadx=(20), ipady=(10))
    
    tk.Label(main_window,text="Register to become a customer:", anchor="center", font=("Abhaya Libre", 20, "bold"), bg="#253568").pack(pady=10)

    register_button = tk.Button(main_window,
                             text="REGISTER",
                             font=("Abhaya Libre", 18, "bold"),
                             bg="#253568",
                             cursor="hand2",
                             width=20,
                             command=lambda:register()).pack(pady=10, ipadx=(20), ipady=(10))
    
    return login_button, register_button