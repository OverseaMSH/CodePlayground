from tkinter import *

def miles_to_km():
    try:
        miles = float(mile.get())
        km.config(text=f"{miles * 1.609:.2f}")
    except ValueError:
        km.config(text="Invalid input")

window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx=16, pady=16)

mile = Entry()
mile.grid(column=1, row=0)

mileLabel = Label(text="Miles")
mileLabel.grid(column=2, row=0)

isEqualToLabel = Label(text="is equal to")
isEqualToLabel.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

calcButton = Button(text="Calculate", command=miles_to_km)  # Removed the parentheses
calcButton.grid(column=1, row=2)

window.mainloop()