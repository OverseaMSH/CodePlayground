from tkinter import *

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
# Create a canvas for the logo
canvas = Canvas(window, height=200, width=200)
logoImg = PhotoImage(file="python/python-in-100-days-udemy/day29/logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1)  # Use grid for the canvas

# Create labels and entries using grid
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)

websiteEntry = Entry(width=35)
websiteEntry.grid(row=1, column=1)

emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=2, column=0)

emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1)

passwordLabel = Label(text="Password:")
passwordLabel.grid(row=3, column=0)

passwordEntry = Entry(width=21)
passwordEntry.grid(row=3, column=1)

# Start the main loop
window.mainloop()
