# Graphical Password Generator Project in Python

"""
Description:
The Graphical Password Generator project aims to enhance security using images or patterns for user authentication.
Instead of a traditional text-based password, the user selects specific areas of an image or draws a pattern, 
which is stored and validated for future logins.
"""

import tkinter as tk  # Tkinter for GUI
from PIL import Image, ImageTk  # For handling images
import random  # Random module for generating unique patterns
import hashlib  # For hashing graphical passwords to store securely

class GraphicalPasswordGenerator:
    def __init__(self, root):
        """
        Initializes the main GUI window and loads the graphical password generator.
        """
        self.root = root
        self.root.title("Graphical Password Generator")
        
        # Load an image as the base for the graphical password
        self.image = Image.open("background_image.jpg")  # You can use any image file
        self.image = self.image.resize((500, 500))  # Resize the image to fit the window
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Create a label to hold the image
        self.image_label = tk.Label(root, image=self.image_tk)
        self.image_label.pack()

        # Store click coordinates for graphical password
        self.click_positions = []

        # Bind the mouse click event to capture graphical password
        self.image_label.bind("<Button-1>", self.capture_click)

        # Button to finalize password entry
        self.finalize_button = tk.Button(root, text="Set Password", command=self.set_password)
        self.finalize_button.pack(pady=20)

        self.stored_password_hash = None

    def capture_click(self, event):
        """
        Captures the user's click positions on the image for graphical password generation.
        """
        x, y = event.x, event.y  # Capture coordinates of the mouse click
        self.click_positions.append((x, y))  # Append coordinates to the list
        print(f"Click captured at position: {x}, {y}")

        # Optional: For visual feedback, draw a small circle where the click happened
        canvas = tk.Canvas(self.root, width=500, height=500)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')  # Draw a small red circle
        canvas.place(x=0, y=0)

    def set_password(self):
        """
        Finalizes and hashes the graphical password based on clicked positions.
        """
        if not self.click_positions:
            print("No clicks recorded. Please click on the image to set your password.")
            return

        # Convert the list of click coordinates to a unique string
        password_str = "".join([f"{x},{y}" for x, y in self.click_positions])
        print(f"Graphical Password (clicks): {password_str}")

        # Hash the graphical password for secure storage
        hashed_password = hashlib.sha256(password_str.encode()).hexdigest()
        self.stored_password_hash = hashed_password  # Store hashed password
        print(f"Password set and hashed: {hashed_password}")

        # Clear click positions for the next action
        self.click_positions.clear()

    def validate_password(self):
        """
        Validates the entered graphical password during login.
        """
        # Capture the new sequence of clicks and compare its hash to the stored one
        password_str = "".join([f"{x},{y}" for x, y in self.click_positions])
        entered_password_hash = hashlib.sha256(password_str.encode()).hexdigest()

        # Compare entered hash with stored hash
        if entered_password_hash == self.stored_password_hash:
            print("Password validation successful. Access granted.")
        else:
            print("Password validation failed. Access denied.")

def main():
    """
    Main function to run the Graphical Password Generator.
    """
    root = tk.Tk()
    app = GraphicalPasswordGenerator(root)
    root.geometry("500x600")
    root.mainloop()

if __name__ == "__main__":
    main()
