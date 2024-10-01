import tkinter as tk
from tkinter import *
import custom_button
import main_menu
import utils
from PIL import ImageTk, Image
import random

def load_menu(window, frame):
    frame.pack_forget()
    main_menu.start(window)

def start(window):
    window.title("Graphical Authentication System")
    window.geometry("1280x600")

    segments_frame = Frame(window, height=600, width=1280)
    segments_frame.pack(fill='both', expand=1)

    label = Label(segments_frame, text="Please select the pictures in correct order", font=('Calibri', 20))
    label.pack(padx=400, pady=10)

    ## Draw order image

    canvas = Canvas(segments_frame, width=300, height=250)
    canvas.pack(padx=10, pady=10)

    # Load and display the order image
    img = Image.open("segmentedImages/order.jpg")
    img = img.resize((300, 250), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    img = ImageTk.PhotoImage(img)
    canvas.create_image(10, 10, anchor=NW, image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection

    imgList = utils.getSegmentedImages("circle")
    random.shuffle(imgList)
    imgClickData = []

    for imgPath in imgList:
        var = utils.imageClick(imgPath)
        imgClickData.append(var)

    # Draw shuffled segments
    for idx, imgPath in enumerate(imgList):
        canvas_segment = Canvas(segments_frame, width=200, height=150)
        canvas_segment.bind("<Button-1>", imgClickData[idx].clicked)
        canvas_segment.place(x=100 + (idx * 300), y=400)  # Adjust position based on index
        img_segment = Image.open(imgPath)
        img_segment = img_segment.resize((200, 150), Image.LANCZOS)  # Use LANCZOS here too
        img_segment = ImageTk.PhotoImage(img_segment)
        canvas_segment.create_image(10, 10, anchor=NW, image=img_segment)
        canvas_segment.image = img_segment  # Keep a reference to avoid garbage collection

    # Add a custom button to go back
    custom_button.TkinterCustomButton(
        master=segments_frame,
        text="Go Back",
        height=40,
        corner_radius=10,
        command=lambda: load_menu(window, segments_frame)
    ).place(relx=0.08, rely=0.08, anchor=CENTER)

    while True:
        window.update_idletasks()
        window.update()

        if utils.checkAllClicked(imgClickData):
            sortedClickList = sorted(imgClickData)

            # Check if images were clicked in the correct order
            if (sortedClickList[0].id == 1) and (sortedClickList[1].id == 2) and \
               (sortedClickList[2].id == 3) and (sortedClickList[3].id == 4):
                utils.create_popup(msg="Authenticated :)", font="Gabriola 28 bold")
            else:
                utils.create_popup(msg="Go Away Robot >_<", font="Gabriola 28 bold")

            utils.setAllUnclicked(imgClickData)

if __name__ == "__main__":


    root = Tk()
    start(root)
    root.mainloop()