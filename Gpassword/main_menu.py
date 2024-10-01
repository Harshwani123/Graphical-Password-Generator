# Import the required libraries
from tkinter import *
import custom_button
import garbled
import password
import segments

# Function to load Garbled Images testing
def load_garbled(window, menu_frame):
    menu_frame.pack_forget()
    garbled.start(window)

# Function to load Segmented Images testing
def load_segmented(window, menu_frame):
    menu_frame.pack_forget()
    segments.start(window)

# Function to load Password/Image Authentication
def load_password(window, menu_frame):
    menu_frame.pack_forget()
    password.start(window)

# Function to start the main menu
def start(win):
    win.geometry("1280x600")
    win.title("Graphical Authentication System")

    # Main menu frame
    menu_frame = Frame(win, height=600, width=1280)
    menu_frame.pack(fill='both', expand=1)

    # Title label
    label = Label(menu_frame, text="Graphical Authentication System", font=('Freestyle Script', 54))
    label.pack(padx=40, pady=30)

    # Button settings
    btn_height = 90
    btn_width = 450
    btn_font = ('Trebuchet MS', 14)

    # Arrange buttons vertically (one after another)
    custom_button.TkinterCustomButton(
        master=menu_frame, text="Test Garbled Images", text_font=btn_font,
        height=btn_height, width=btn_width, corner_radius=10,
        command=lambda: load_garbled(win, menu_frame)
    ).pack(pady=10)

    custom_button.TkinterCustomButton(
        master=menu_frame, text="Test Segmented Images", text_font=btn_font,
        height=btn_height, width=btn_width, corner_radius=10,
        command=lambda: load_segmented(win, menu_frame)
    ).pack(pady=10)

    custom_button.TkinterCustomButton(
        master=menu_frame, text="Test Password/Image Authentication", text_font=btn_font,
        height=btn_height, width=btn_width, corner_radius=10,
        command=lambda: load_password(win, menu_frame)
    ).pack(pady=10)

    # Start the Tkinter event loop
    win.mainloop()

# Main execution
if _name_ == "_main_":
    win = Tk()
    start(win)