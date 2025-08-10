import tkinter as tk
from tkinter import messagebox
import re

def save_to_file():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")

    pattern = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if not pattern.match(email):
        messagebox.showerror("Error", "Invalid email format! Use example@gmail.com")
        return
    
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name}\nEmail: {email}\n\nPassword: {password}")
    
    messagebox.showinfo("Success", "Successfully Logged in, and Details saved!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

error_shown = False  # flag to prevent repeated popups

def only_letters(char):
    global error_shown
    if char.isalpha() or char == "":
        error_shown = False
        return True
    else:
        if not error_shown:
            messagebox.showerror("Invalid Input", "You can only enter letters in the username field.")
            error_shown = True
        return False
    
def validate_email_on_focus_out(event):
    value = email_entry.get()
    pattern = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
    if value and not pattern.match(value):
        messagebox.showerror("Invalid Input", "Use email format: example@gmail.com")
        email_entry.focus_set()  # keep focus for correction

# Creating Login Window
login_window = tk.Tk()
login_window.title("Login to Muslim Helper NZ")
login_window.geometry("400x400")

vcmd = (login_window.register(only_letters), '%S')

# Title Label (centered at top)
title_label = tk.Label(login_window, text="Login Form")
title_label.place(relx=0.5, rely=0.1, anchor="center")

# Name Field (positioned manually)
tk.Label(login_window, text="Name:").place(x=50, y=80)
name_entry = tk.Entry(login_window, width=30)
name_entry.place(x=150, y=80)
name_entry.configure(validate="key", validatecommand=vcmd)

# Email Field (shifted down)
tk.Label(login_window, text="Email:").place(x=50, y=120)
email_entry = tk.Entry(login_window, width=30)
email_entry.place(x=150, y=120)
email_entry.bind("<FocusOut>", validate_email_on_focus_out)

# Password
tk.Label(login_window, text="Password:").place(x=50, y=160)
password_entry = tk.Entry(login_window, width=30)
password_entry.place(x=150, y=160)

# Submit Button (custom position + styling)
submit_button = tk.Button(
    login_window, 
    text="Submit Details", 
    command=save_to_file,
    padx=10,
    pady=5
)
submit_button.place(relx=0.5, rely=0.6, anchor="center")

exitButton = tk.Button(login_window, text="Click to exit", command=login_window.destroy).place(relx=0.5, rely=0.8, anchor="center")

# Load the image using PhotoImage
icon_image = tk.PhotoImage(file="Login_icon.png")

# Set the icon
login_window.iconphoto(False, icon_image)

login_window.mainloop()

