"""
COMPONENT #1
[Navigation Bar]

Name: Tehreem Fatima
Date: 16/07/2025 - 24/07/2025
Purpose: Create a working navigation bar on the bottom of my app frame. 
"""

# Import libraries needed 
import tkinter as tk
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

def on_button_click(button):
    #Changes the button image on click and reverts after a delay.
    button.config(image=button_image_1b)
    
    # Revert image back to default image after 500 milliseconds
    button.after(500, lambda: button.config(image=button_image_1))
    
# Creating main window called 'root'
# Using variables
root = tk.Tk()

# Load images for button1 (default and clicked) and display error message if images do not exist
try:
    button_image_1 = ImageTk.PhotoImage(Image.open("assets/home_page_icon.png").resize((100,100)))
    button_image_1b = ImageTk.PhotoImage(Image.open("assets/home_page_iconb.png").resize((50,50)))
except tk.TclError:
    print("Error: Ensure 'home_page_icon.png' and 'home_page_iconb.png' exist in the same directory.")
    # Create template images if images cannot be displayed
    button_image_1 = tk.PhotoImage(width=100, height=50)
    button_image_1.put("blue", to=(0,0,99,49))
    button_image_1b = tk.PhotoImage(width=100, height=50)
    button_image_1b.put("red", to=(0,0,99,49))

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

# Button Images
button_image_2 = ImageTk.PhotoImage(Image.open("assets/prayers_page_icon.png").resize((100,100)))
button_image_3 = ImageTk.PhotoImage(Image.open("assets/qibla_page_icon.png").resize((100,100)))
button_image_4 = ImageTk.PhotoImage(Image.open("assets/community_page_icon.png").resize((100,100)))
button_image_5 = ImageTk.PhotoImage(Image.open("assets/masjid_page_icon.png").resize((100,100)))
button_image_6 = ImageTk.PhotoImage(Image.open("assets/settings_page_icon.png").resize((100,100)))

# All pages will be in the main container of win
page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)
page4 = Frame(root)
page5 = Frame(root)
page6 = Frame(root)
page1.config()
page2.config()
page3.config()
page4.config()
page5.config()
page6.config()

# Putting pages into containers
page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")
page6.grid(row=0, column=0, sticky="nsew")

# Displaying the pages
label1 = tk.Label(page1, text="Home Page", font=style1, fg="black")
label1.pack(pady=20)

label2 = tk.Label(page2, text="Prayers Page", font=style1, fg="black")
label2.pack(pady=20)

label3 = tk.Label(page3, text="Qibla Finder Page", font=style1, fg="black")
label3.pack(pady=20)

label4 = tk.Label(page4, text="Community Page", font=style1, fg="black")
label4.pack(pady=20)

label5 = tk.Label(page5, text="Masjid locator Page", font=style1, fg="black")
label5.pack(pady=20)

label6 = tk.Label(page6, text="Settings Page", font=style1, fg="black")
label6.pack(pady=20)

# Displaying buttons on page 1 that lead to their own frames
button1 = Button(page1, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560)
button1.config(command=lambda: on_button_click(button1))

button2 = Button(page1, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page1, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page1, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page1, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page1, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 2
button1 = Button(page2, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page2, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page2, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page2, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page2, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page2, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 3
button1 = Button(page3, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page3, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page3, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page3, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page3, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page3, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 4
button1 = Button(page4, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page4, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page4, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page4, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page4, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page4, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 5
button1 = Button(page5, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560) 

button2 = Button(page5, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page5, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page5, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page5, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page5, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Displaying buttons on page 6
button1 = Button(page6, image=button_image_1, command=lambda: page1.tkraise(), font=style2)
button1.pack(side=tk.LEFT, padx=0, pady=560)

button2 = Button(page6, image=button_image_2, command=lambda: page2.tkraise(), font=style2)
button2.pack(side=tk.LEFT, padx=0, pady=560)

button3 = Button(page6, image=button_image_3, command=lambda: page3.tkraise(), font=style2)
button3.pack(side=tk.LEFT, padx=0, pady=560)

button4 = Button(page6, image=button_image_4, command=lambda: page4.tkraise(), font=style2)
button4.pack(side=tk.LEFT, padx=0, pady=560)

button5 = Button(page6, image=button_image_5, command=lambda: page5.tkraise(), font=style2)
button5.pack(side=tk.LEFT, padx=0, pady=560)

button6 = Button(page6, image=button_image_6, command=lambda: page6.tkraise(), font=style2)
button6.pack(side=tk.LEFT, padx=0, pady=560)

# Page 1 (Frame 1) will show on the initial window when run
page1.tkraise()

# Load the image using PhotoImage
icon_image = tk.PhotoImage(file="assets/icon.png")

# Set the icon
root.iconphoto(False, icon_image)

# Specifications/Dimensions
root.title("Muslim Helper NZ")
root.geometry("630x750")
root.mainloop()
