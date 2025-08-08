"""
Full Muslim Helper App (GUI)
[First Draft]

Name: Tehreem Fatima
Date: 6/08/2025 - 10/08/2025
Purpose: Create a semi-functional full first GUI program
"""

# Import libraries needed 
import tkinter as tk
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk
from tkinter import scrolledtext
import platform
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, orient="vertical", *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.orient = orient

        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient=orient, command=self.canvas.yview if orient=="vertical" else self.canvas.xview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        if orient == "vertical":
            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            self.canvas.configure(yscrollcommand=scrollbar.set)
            self.canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        else:
            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
            self.canvas.configure(xscrollcommand=scrollbar.set)
            self.canvas.pack(side="top", fill="both", expand=True)
            scrollbar.pack(side="bottom", fill="x")

        self._setup_mousewheel()

    def _setup_mousewheel(self):
        system = platform.system()
        if self.orient == "vertical":
            if system == "Windows":
                self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_vertical)
            else:
                self.canvas.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
                self.canvas.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))
        else:
            if system == "Windows":
                self.canvas.bind_all("<Shift-MouseWheel>", self._on_mousewheel_horizontal)
            else:
                self.canvas.bind_all("<Shift-Button-4>", lambda e: self.canvas.xview_scroll(-1, "units"))
                self.canvas.bind_all("<Shift-Button-5>", lambda e: self.canvas.xview_scroll(1, "units"))

    def _on_mousewheel_vertical(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _on_mousewheel_horizontal(self, event):
        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")

root = tk.Tk()
root.geometry("635x720")
root.title("Muslim Helper NZ")

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

# Main vertical scrollable frame
main_vertical = ScrollableFrame(root, orient="vertical")
main_vertical.pack(fill="both", expand=True)

# Add some vertical content
Label1=ttk.Label(main_vertical.scrollable_frame, text="Home Page", font=style1, padding=5).pack(padx=210)

Label2=ttk.Label(main_vertical.scrollable_frame, font=style2, padding=5)
Label2.pack(anchor="w")


# Horizontal scrollable frame INSIDE the vertical one
horizontal_bar = ScrollableFrame(main_vertical.scrollable_frame, orient="horizontal")
horizontal_bar.pack(fill="x")

# Add some wide horizontal content (buttons)
for i in range(30):
    ttk.Button(horizontal_bar.scrollable_frame, text="Masjid Box").pack(side="left", padx=5)

def on_button_click(button):
    #Changes the button image on click and reverts after a delay.
    button.config(image=button_image_1b)
    
    # Revert image back to default image after 500 milliseconds
    button.after(500, lambda: button.config(image=button_image_1))

def show_frame(frame):
    frame.tkraise()

# Load images for button1 (default and clicked) and display error message if images do not exist
try:
    button_image_1 = ImageTk.PhotoImage(Image.open("assets/home_page_icon.png").resize((100,100)))
    button_image_1b = ImageTk.PhotoImage(Image.open("assets/home_page_iconb.png").resize((100,100)))
except tk.TclError:
    print("Error: Ensure 'home_page_icon.png' and 'home_page_iconb.png' exist in the same directory.")
    # Create template images if images cannot be displayed
    button_image_1 = tk.PhotoImage(width=100, height=50)
    button_image_1.put("blue", to=(0,0,99,49))
    button_image_1b = tk.PhotoImage(width=100, height=50)
    button_image_1b.put("red", to=(0,0,99,49))

# Button Images
button_image_2 = ImageTk.PhotoImage(Image.open("assets/prayers_page_icon.png").resize((100,100)))
button_image_3 = ImageTk.PhotoImage(Image.open("assets/qibla_page_icon.png").resize((100,100)))
button_image_4 = ImageTk.PhotoImage(Image.open("assets/community_page_icon.png").resize((100,100)))
button_image_5 = ImageTk.PhotoImage(Image.open("assets/masjid_page_icon.png").resize((100,100)))
button_image_6 = ImageTk.PhotoImage(Image.open("assets/settings_page_icon.png").resize((100,100)))

# All pages will be in the main container of win
page1 = Frame(root)
page1.pack(fill="both", expand=True)

# Frame for navigation buttons
nav_bar = tk.Frame(root, height=100)
nav_bar.pack(side="bottom", fill="x")

# Displaying buttons on page 1 that lead to their own frames
button1 = Button(nav_bar, image=button_image_1, command=lambda: show_frame(page1), font=style2)
button1.pack(side="left")

button2 = Button(nav_bar, image=button_image_2, command=lambda: show_frame(page1), font=style2)
button2.pack(side="left")

button3 = Button(nav_bar, image=button_image_3, command=lambda: show_frame(page1), font=style2)
button3.pack(side="left")

button4 = Button(nav_bar, image=button_image_4, command=lambda: show_frame(page1), font=style2)
button4.pack(side="left")

button5 = Button(nav_bar, image=button_image_5, command=lambda: show_frame(page1), font=style2)
button5.pack(side="left")

button6 = Button(nav_bar, image=button_image_6, command=lambda: show_frame(page1), font=style2)
button6.pack(side="left")

# Page 1 (Frame 1) will show on the initial window when run
show_frame(page1)

# Load the image using PhotoImage
icon_image = tk.PhotoImage(file="assets/icon.png")

# Set the icon
root.iconphoto(False, icon_image)

# Specifications/Dimensions
root.mainloop()
