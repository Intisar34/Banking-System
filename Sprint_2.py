
# Create a transaction form that displays different inputs

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


#Check if the current balance is enough for the transaction
def check_balance(amount_input, number_input, recipient_input, message_input):
   
    amount = float(amount_input.get())
    recipient = recipient_input.get().strip()
    ocr_number = number_input.get().strip()
    transaction_message = message_input.get().strip()
   
   current_balance = 200
   #transaction_amount = 100

   if amount <= current_balance:
      messagebox.showinfo("Your transaction was successfull")
      
   else:
      messagebox.showerror("Not enough saldo")





#Ghassans code for updating balance:

tk.Label(menu_screen, text="Enter Amount (kr):", font=("Abhaya Libre", 18), bg="#253568", fg="white").pack(pady=10)

entry_amount = tk.Entry(menu_screen, font=("Abhaya Libre", 18))
entry_amount.pack(pady=10)

def validate_deposit():
     amount = float(entry_amount.get())
     if amount <= 0:
         messagebox.showerror("Invalid Input", "The deposit must be a positive amount and exceed zero.")
         return
     message = banking_system.deposit(username, amount)
     messagebox.showinfo("Deposit", message)
     update_balance()
     menu_screen.destroy()

def deposit(self, username, amount):
        if amount <= 0:
            return "The deposit must be a positive amount and exceed zero."
        if username not in self.accounts:
            return "The user could not be found!"
        self.accounts[username] += amount
        return f"Deposit of {amount:.2f} kr completed successfully."


def do_transaction():

  window = tk.Tk()
  window.geometry("800x600")
  window.title("Transaction")
  window.configure(bg = "#253568")

  img_5 = Image.open('FF_logo.png')
  img_5 = img_5.resize((500, 180))
  img_5 = ImageTk.PhotoImage(img_5)

  tk.Label(window, image = img_5, anchor="n", bg="#253568").pack(pady = 5, padx = 20)

  recipient = tk.Label(master = window, 
                       text = "Recipient", 
                       font = ("Abhaya Libre", 20, "bold"),
                       fg = "White", 
                       bg = "#253568").pack(pady = 5)

  recipient_input = tk.Entry(master = window, font = ("Abhaya Libre", 20, "bold")).pack()
  

  transaction_amount = tk.Label(master = window,
                      text = "Amount", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568"). pack(pady = 5)
  
  amount_input = tk.Entry(master = window, font = ("Abhaya Libre", 20, "bold")).pack()

  amount = transaction_amount.get()


  date = tk.Label(master = window, 
                  text = "Date", 
                  font = ("Abhaya Libre", 20, "bold"), 
                  fg = "White", 
                  bg = "#253568"). pack(pady = 5)
  
  date_input = tk.Entry(master = window, font = ("Abhaya Libre", 20, "bold")). pack()


  recipient_number = tk.Label(master = window, 
                       text = "OCR Number", 
                       font = ("Abhaya Libre", 20, "bold"),
                         fg = "White", 
                         bg = "#253568").pack(pady = 5)

  number_input = tk.Entry(master = window, font = ("Abhaya Libre", 20, "bold")). pack()



  message =  tk.Label(master = window, 
                      text = "Message", 
                      font = ("Abhaya Libre", 20, "bold"), 
                      fg = "White", 
                      bg = "#253568"). pack(pady = 5)
  
  message_input = tk.Entry(master = window, font = ("Abhaya Libre", 20, "bold")). pack()


  submit = tk.Button(master = window, text = "Submit", font = ("Abhaya Libre", 20, "bold"), fg = "White", bg = "#253568", cursor="hand2", command = check_balance ).pack(pady=20, ipadx=20, ipady=10)


  window.mainloop()

  return amount
 

do_transaction()



