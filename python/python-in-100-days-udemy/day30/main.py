from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    try:
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        pyperclip.copy(password)
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred while generating the password: {e}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    newData = {website: {"email": email, "password": password}}

    try:
        # Check if the data file exists, if not create it
        if os.path.exists("python/python-in-100-days-udemy/day30/data.json"):
            with open("python/python-in-100-days-udemy/day30/data.json", "r") as dataFile:
                data = json.load(dataFile)
        else:
            data = {}

        data.update(newData)

        with open("python/python-in-100-days-udemy/day30/data.json", "w") as dataFile:
            json.dump(data, dataFile, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Your data has been saved successfully!")

    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="The data file was not found. Please check the file path.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="There was an error reading the JSON file.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An unexpected error occurred: {e}")

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search.")
        return

    try:
        with open("python/python-in-100-days-udemy/day30/data.json", "r") as dataFile:
            data = json.load(dataFile)

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {website} exist.")
    
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="The data file was not found. Please check the file path.")
    except json.JSONDecodeError:
        messagebox.showerror(title="Error", message="There was an error reading the JSON file.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An unexpected error occurred: {e}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="python/python-in-100-days-udemy/day30/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3, pady=20)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e", pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", pady=5)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "m.sadegh.hemati.dev@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, padx=5, pady=5)

# Configure column and row weights
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.mainloop()
