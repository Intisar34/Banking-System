from PIL import Image, ImageTk
import common
import UI

def main():
    # The json file is being imported
    common.load_data()
    
    # Creating the main menu
    main_window = UI.Tk()
    main_window.attributes("-fullscreen", True) 
    main_window.title("Banking Application")
    main_window.config(bg="#253568")

    # Creating the main logo
    logo = Image.open('FF_logo.png')
    logo = logo.resize((700, 240))
    logo = ImageTk.PhotoImage(logo)

    # The user interface is being imported
    UI.creating_main_page(main_window,logo)

    # This loop makes sure that the application executes
    main_window.mainloop()

if __name__ == "__main__":
    main()