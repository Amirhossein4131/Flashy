from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.title("Flash Card App")
screen.config(width=800, height=526, padx=50, pady=50)

# right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=0)

# wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)
