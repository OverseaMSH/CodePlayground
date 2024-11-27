import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password():
    # Create a string of uppercase, lowercase, digits, and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose 12 characters for the password
    password = ''.join(random.choice(all_characters) for i in range(12))
    password_entry.delete(0, tk.END)  # Clear the current password entry
    password_entry.insert(0, password)  # Insert the generated password

# Function to add the password to the password list
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any field is empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    # Append password to a file (or a database, if desired)
    with open("passwords.txt", "a") as file:
        file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
    
    # Clear the input fields
    website_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    
    # Show a success message
    messagebox.showinfo("Success", "Password added successfully!")

# Create the main window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a canvas for the logo (optional)
canvas = tk.Canvas(window, height=200, width=200)
# You can replace the following line with your actual logo image file path
logoImg = tk.PhotoImage(file="python/python-in-100-days-udemy/day29/logo.png")  # Replace with correct path
canvas.create_image(100, 100, image=logoImg)
canvas.grid(row=0, column=1, pady=20)

# Labels for the fields
website_label = tk.Label(window, text="Website:")
website_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

email_label = tk.Label(window, text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)

password_label = tk.Label(window, text="Password:")
password_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)

# Entry fields for the user to input the website, email, and password
website_entry = tk.Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)

email_entry = tk.Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = tk.Entry(window, width=20)  # Shorter width for password entry
password_entry.grid(row=3, column=1, pady=5)

# Buttons for generating password and adding password
generate_button = tk.Button(window, text="Generate Password", width=15, command=generate_password)
generate_button.grid(row=3, column=2, padx=0, pady=5)

add_button = tk.Button(window, text="Add Password", width=20, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

# Start the Tkinter main loop
window.mainloop()
