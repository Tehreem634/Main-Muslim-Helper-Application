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
from tkinter import messagebox
import re
import webbrowser

global counter
counter = 1

root = tk.Tk()
root.geometry("635x720")
root.title("Muslim Helper NZ")
root.resizable(False, False)

# Container for pages (takes all space except nav bar)
container = tk.Frame(root)
container.pack(fill="both", expand=True)

def help_window():
    global counter
	# Create counter logic
    if counter < 2:
        help_win = tk.Toplevel()
        help_win.geometry("700x400")
        help_win.title("Help and Instructions")
        scroll_frame = ScrollableFrame(help_win, orient="vertical")
        scroll_frame.pack(fill="both", expand=True)
        label_help = tk.Label(
        scroll_frame.scrollable_frame,
        text="""Help and Instructions\n\n\n Purpose: My app will allow
        people part of the Muslim Community to access prayer times for their specific location/mosque prayer time, Islamic facilities (mosques) as well as a place to add and find local community events.\n
        How to Use:\n\
        Step 1:\n
        Log in using the 'login' button on the home page.\n
        Step 2:\n
        Use the bottom navigation bar to navigate through the 6 app pages of the home page, prayer times, direction finder, community, masjid locator, and settings widgets.
        Instructions:
        1. Prayer times will not display on home page, as this app was designed to be able to be used without wifi, you can use the prayers page (from navigation bar) to find pdf prayer times to download.\n
        2. See if you can unlock recognition of being a premium user experience by sharing the application to 3 or more Muslim friends who are new users to the app - go to the settings navigation bar option in order to gain more information on this.\n
        """,
        justify="center",
        wraplength=650)
        label_help.pack(padx=10, pady=10)
        exitButton_help = tk.Button(scroll_frame.scrollable_frame, text="Click to exit", command=help_win.destroy).place(relx=0.5, rely=0.1, anchor="center")
        def on_close():
            global counter
            counter -= 1
            help_win.destroy()
        help_win.protocol("WM_DELETE_WINDOW", on_close)
        counter +=1
    else:
        messagebox.showinfo("Error", "Hey! You've already opened a new window!")

def login_window():
    global counter
    # Create counter logic
    if counter < 2:
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

        def on_close():
            global counter
            counter -= 1
            login_window.destroy()
        login_window.protocol("WM_DELETE_WINDOW", on_close)
        
        counter +=1

    else:
        messagebox.showinfo("Error", "Hey! You've already opened a new window!")


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
            ))
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

        def bind_mousewheel(widget):
            if self.orient == "vertical":
                if system == "Windows":
                    widget.bind("<Enter>", lambda e: widget.bind_all("<MouseWheel>", self._on_mousewheel_vertical))
                    widget.bind("<Leave>", lambda e: widget.unbind_all("<MouseWheel>"))
                elif system == "Darwin":  # macOS uses different event names
                    widget.bind("<Enter>", lambda e: widget.bind_all("<MouseWheel>", self._on_mousewheel_vertical))
                    widget.bind("<Leave>", lambda e: widget.unbind_all("<MouseWheel>"))
                else:  # Linux
                    widget.bind("<Enter>", lambda e: (widget.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units")),
                                                      widget.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))))
                    widget.bind("<Leave>", lambda e: (widget.unbind_all("<Button-4>"),
                                                      widget.unbind_all("<Button-5>")))
            else:  # horizontal scroll (if needed)
                if system == "Windows":
                    widget.bind("<Enter>", lambda e: widget.bind_all("<Shift-MouseWheel>", self._on_mousewheel_horizontal))
                    widget.bind("<Leave>", lambda e: widget.unbind_all("<Shift-MouseWheel>"))
                elif system == "Darwin":
                    widget.bind("<Enter>", lambda e: widget.bind_all("<Shift-MouseWheel>", self._on_mousewheel_horizontal))
                    widget.bind("<Leave>", lambda e: widget.unbind_all("<Shift-MouseWheel>"))
                else:
                    widget.bind("<Enter>", lambda e: (widget.bind_all("<Shift-Button-4>", lambda e: self.canvas.xview_scroll(-1, "units")),
                                                      widget.bind_all("<Shift-Button-5>", lambda e: self.canvas.xview_scroll(1, "units"))))
                    widget.bind("<Leave>", lambda e: (widget.unbind_all("<Shift-Button-4>"),
                                                      widget.unbind_all("<Shift-Button-5>")))
        bind_mousewheel(self.canvas)

    def _on_mousewheel_vertical(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create pages as frames inside container
page1 = ScrollableFrame(container, orient="vertical")
page2 = ScrollableFrame(container, orient="vertical")
page3 = ScrollableFrame(container, orient="vertical")
page4 = ScrollableFrame(container, orient="vertical")
page5 = ScrollableFrame(container, orient="vertical")
page6 = ScrollableFrame(container, orient="vertical")

error_shown = False  # flag to prevent repeated popups

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

content_frame = Frame(page1.scrollable_frame)
content_frame.pack(fill='both', expand=True, padx=20, pady=20)

# Top centered label
Label1 = ttk.Label(content_frame, text="Home Page", font=style1)
Label1.pack(pady=(10, 20))

# Frame to hold Login and Help buttons side by side
button_frame1 = Frame(content_frame)
button_frame1.pack()

Login_window_button = tk.Button(button_frame1, text="Login", width=30, height=3, command=login_window)
Login_window_button.pack(side="left", padx=40)

Help_window_button = tk.Button(button_frame1, text="Help and Instructions", width=30, height=3, command=help_window)
Help_window_button.pack(side="left", padx=40)

# Header label below buttons
Header1 = ttk.Label(content_frame, text="Explore some helpful apps!", font=style2, padding=5)
Header1.pack(pady=(40, 10))

# Frame to hold MasjidBox and MuslimPro side by side
apps_frame = Frame(content_frame)
apps_frame.pack(pady=10, fill="x")

def open_MasjidBox():
    webbrowser.open("https://masjidbox.com/")

def open_MuslimPro():
    webbrowser.open("https://muslimpro.com/")  # Replace with your actual link

def open_FIANZ():
    webbrowser.open("https://fianz.com/")  # Replace with your actual link

#Masjid Box Recommendation
MasjidBox = Frame(apps_frame, bg="white", width=150, height=150, relief="solid")
MasjidBox.pack(side="left", padx=20, fill="both", expand=True)
MasjidBoxText = Label(MasjidBox, font=("Arial", 10), text="Masjid Box\n Allows you to find\n different masjid prayer\n times and locational\n prayer times!", bg="white")
MasjidBoxText2 = Label(
    MasjidBox,
    text="Masjid Box Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="white"
)
MasjidBoxText.pack(expand=True)
MasjidBoxText2.pack(expand=True)
MasjidBoxText2.bind("<Button-1>", lambda e: open_MasjidBox())

#Muslim Pro Recommendation
MuslimPro = Frame(apps_frame, bg="white", width=150, height=150, relief="solid")
MuslimPro.pack(side="left", padx=20, fill="both", expand=True)
MuslimProText = Label(MuslimPro, font=("Arial", 10), text="Muslim Pro\n Allows both mosque and\n location prayers, as well as\n facilities like halal\n food places and shops!", bg="white")
MuslimProText2 = Label(
    MuslimPro,
    text="Muslim Pro Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="white"
)
MuslimProText.pack(expand=True)
MuslimProText2.pack(expand=True)
MuslimProText2.bind("<Button-1>", lambda e: open_MuslimPro())

#FIANZ Recommendation
FIANZ = Frame(apps_frame, bg="white", width=150, height=150, relief="solid")
FIANZ.pack(side="left", padx=20, fill="both", expand=True)
FIANZText = Label(FIANZ, font=("Arial", 10), text="FIANZ\n World wide organisation\n that can help\n you find halal\n certified products, as well\n as prayer times!", bg="white")
FIANZText2 = Label(
    FIANZ,
    text="FIANZ Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="white"
)
FIANZText.pack(expand=True)
FIANZText2.pack(expand=True)
FIANZText2.bind("<Button-1>", lambda e: open_MuslimPro())

# Developers Note
Header3 = Label(content_frame, font= style2, text="Developers Note")
Header3.pack(expand=True, pady=40)
Text1 = Label(content_frame, font=("Arial", 10), text="Hi, I am Tehreem Fatima and am the person who developed this app. I wanted to create this\n\n app mainly so that people can find prayer times of both mosques and cities \n\n(mainly in Auckland), as well as community events. This app includes link to a qibla finder site\n\n as well so that you can find the direciton of prayer. Logging into \n\nthe app will also allow you to save your details, and I will be able to see them\n\n and therefore see how many people I can reach with it! Please enjoy exploring my app!")
Text1.pack(expand=True)


"""
def open_youtube():
    webbrowser.open("https://www.youtube.com")  # Replace with your actual link

# Then pack the YouTube link underneath by packing it without side=left (default is top)
Link_frame_1 = Frame(main_vertical.scrollable_frame, bg="white")
Link_frame_1.pack(padx=10, pady=20, fill="x")

Link1 = tk.Label(
    Link_frame_1,
    text="Masjid Box",
    fg="blue",
    cursor="hand2",
    font=("Arial", 12, "underline"),
    bg="white"
)
Link1.pack(pady=10)
Link1.bind("<Button-1>", lambda e: open_youtube())
"""

def on_button_click(button):
    #Changes the button image on click and reverts after a delay.
    button.config(image=button_image_1b)
    
    # Revert image back to default image after 500 milliseconds
    button.after(500, lambda: button.config(image=button_image_1))

def show_frame(frame):
    frame.tkraise()

# Button Images
button_image_1 = ImageTk.PhotoImage(Image.open("assets/home_page_icon.png").resize((100,100)))
button_image_2 = ImageTk.PhotoImage(Image.open("assets/prayers_page_icon.png").resize((100,100)))
button_image_3 = ImageTk.PhotoImage(Image.open("assets/qibla_page_icon.png").resize((100,100)))
button_image_4 = ImageTk.PhotoImage(Image.open("assets/community_page_icon.png").resize((100,100)))
button_image_5 = ImageTk.PhotoImage(Image.open("assets/masjid_page_icon.png").resize((100,100)))
button_image_6 = ImageTk.PhotoImage(Image.open("assets/settings_page_icon.png").resize((100,100)))

for page in (page1, page2, page3, page4, page5, page6):
    page.place(relwidth=1, relheight=1)

# Navigation bar fixed at bottom of root
nav_bar = tk.Frame(root, height=100)
nav_bar.pack(side="bottom", fill="x")

# Displaying the pages
label2 = tk.Label(page2.scrollable_frame, text="Prayers Page", font=style1)
label2.pack(anchor="center")

label3 = tk.Label(page3.scrollable_frame, text="Qibla Finder Page", font=style1)
label3.pack(anchor="center")

label4 = tk.Label(page4.scrollable_frame, text="Community Page", font=style1)
label4.pack(anchor="center")

label5 = tk.Label(page5.scrollable_frame, text="Masjid locator Page", font=style1)
label5.pack(anchor="center")

label6 = tk.Label(page6.scrollable_frame, text="Settings Page", font=style1)
label6.pack(anchor="center")

# Navigation buttons in nav_bar
button1 = Button(nav_bar, image=button_image_1, command=lambda: show_frame(page1))
button1.pack(side="left", pady=0)
button2 = Button(nav_bar, image=button_image_2, command=lambda: show_frame(page2))
button2.pack(side="left", pady=0)
button3 = Button(nav_bar, image=button_image_3, command=lambda: show_frame(page3))
button3.pack(side="left", pady=0)
button4 = Button(nav_bar, image=button_image_4, command=lambda: show_frame(page4))
button4.pack(side="left", pady=0)
button5 = Button(nav_bar, image=button_image_5, command=lambda: show_frame(page5))
button5.pack(side="left", pady=0)
button6 = Button(nav_bar, image=button_image_6, command=lambda: show_frame(page6))
button6.pack(side="left", pady=0)

# Show initial page
show_frame(page1)

# Load the image using PhotoImage
icon_image = tk.PhotoImage(file="assets/icon.png")

# Set the icon
root.iconphoto(False, icon_image)

# Specifications/Dimensions
root.mainloop()
