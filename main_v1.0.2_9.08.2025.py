"""
Muslim Helper App (GUI)

Name: Tehreem Fatima
Date: 6/08/2025 - 10/08/2025
Purpose: Create a functional GUI program that can allow hosting of community events and guide users to helpful applications for prayer times.
"""

# Import libraries needed
# Try except blocks used to indicate un-imported/missing library
import tkinter as tk
from tkinter import *
import tkinter.font

try:
    from PIL import Image, ImageTk
except:
    print("You must pip install pillow from your command prompt.")

from tkinter import scrolledtext

import platform

from tkinter import ttk

try:
    import sv_ttk
except:
    print("You must pip install sv_ttk from your command prompt.")

from tkinter import messagebox

import re

import webbrowser

try:
    from tkintermapview import TkinterMapView
except:
    print("You must pip install TkinterMapView from your command prompt.")

# Call global counter
global counter

# Set counter to 1
counter = 1

# Define functions needed
def event_details():
    global counter
    # Create counter logic
    if counter < 2:
        def save_to_fileb():
            name = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            eventdetails = eventdetails_entry.get()
            location = location_entry.get()
            
            
            if not name or not email or not password or not eventdetails or not location:
                messagebox.showerror("Error", "All fields are required!")

            pattern = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
            if not pattern.match(email):
                messagebox.showerror("Error", "Invalid email format! Use example@gmail.com")
                return
            
            with open("Events.txt", "a", encoding="utf-8") as file:
                file.write(f"Name: {name}\nEmail: {email}\nPassword: {password}\nEvent details: {eventdetails}\n\nLocation: {location}")
            
            messagebox.showinfo("Success", "Successful detail input! Your event will be displayed shortly after we add it into our program!")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            eventdetails_entry.delete(0, tk.END)
            location_entry.delete(0, tk.END)

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
        event_details = tk.Tk()
        event_details.title("Login to Muslim Helper NZ")
        event_details.geometry("400x400")

        vcmd = (event_details.register(only_letters), '%S')

        # Title Label (centered at top)
        title_label = tk.Label(event_details, text="Event detials")
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Name Field (positioned manually)
        tk.Label(event_details, text="Name:").place(x=50, y=80)
        name_entry = tk.Entry(event_details, width=30)
        name_entry.place(x=150, y=80)
        name_entry.configure(validate="key", validatecommand=vcmd)

        # Email Field (shifted down)
        tk.Label(event_details, text="Email:").place(x=50, y=120)
        email_entry = tk.Entry(event_details, width=30)
        email_entry.place(x=150, y=120)
        email_entry.bind("<FocusOut>", validate_email_on_focus_out)

        # Password
        tk.Label(event_details, text="Password:").place(x=50, y=160)
        password_entry = tk.Entry(event_details, width=30)
        password_entry.place(x=150, y=160)

        # event details
        tk.Label(event_details, text="Event details:").place(x=50, y=200)
        eventdetails_entry = tk.Entry(event_details, width=30)
        eventdetails_entry.place(x=150, y=200)

        # location
        tk.Label(event_details, text="Location:").place(x=50, y=240)
        location_entry = tk.Entry(event_details, width=30)
        location_entry.place(x=150, y=240)

        # Submit Button (custom position + styling)
        submit_button = tk.Button(
            event_details, 
            text="Submit Details", 
            command=save_to_fileb,
            padx=10,
            pady=5
        )
        submit_button.place(relx=0.5, rely=0.8, anchor="center")

        exitButton = tk.Button(event_details, text="Click to exit", command=event_details.destroy).place(relx=0.5, rely=0.9, anchor="center")

        def on_close():
            global counter
            counter -= 1
            event_details.destroy()
        event_details.protocol("WM_DELETE_WINDOW", on_close)
        
        counter +=1

    else:
        messagebox.showinfo("Error", "Hey! You've already opened a new window!")

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
                return
            pattern = re.compile(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")
            if not pattern.match(email):
                messagebox.showerror("Error", "Invalid email format! Use example@gmail.com")
                return
            
            with open("LoginDetails.txt", "a", encoding="utf-8") as file:
                file.write(f"Name: {name}\nEmail: {email}\nPassword: {password}\n\n")
            
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


class ScrollableFrame(tk.Frame):
    def __init__(self, container, orient="vertical", *args, **kwargs):
        
        super().__init__(container, *args, **kwargs)
        self.orient = orient

        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient=orient, command=self.canvas.yview if orient=="vertical" else self.canvas.xview)
        self.scrollable_frame = tk.Frame(self.canvas)

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
                elif system == "Darwin":  # macOS naming
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

def open_MasjidBox():
    webbrowser.open("https://masjidbox.com/")

def open_MuslimPro():
    webbrowser.open("https://muslimpro.com/")  

def open_FIANZ():
    webbrowser.open("https://fianz.com/")

def show_frame(frame):
    frame.tkraise()

def open_Ashburton():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Helensville():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025") 

def open_Warkworth():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")
    
def open_Wellsford():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Kumeu():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Pukekohe():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Celevedon():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Epsom():
    webbrowser.open("https://www.islamicfinder.org/prayer-times/print-yearly-prayers/?timeInterval=year&calendarType=Gregorian&year=2025")

def open_Qibla():
    webbrowser.open("https://qiblafinder.withgoogle.com/intl/en/desktop")

def toggle_theme():
    if sv_ttk.get_theme() == "dark":
        print("Setting theme to light")
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == "light":
        print("Setting theme to dark")
        sv_ttk.use_dark_theme()
    else:
        print("No theme to display")

# Create main window
root = tk.Tk()
root.geometry("635x720")
root.title("Muslim Helper NZ")
root.resizable(False, False)

# Create variables, frames, and images
# Flag to repeat multiple groups
error_shown = False 

# Container for pages (takes all space except nav bar)
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Images needed for buttons
login_button_image = ImageTk.PhotoImage(Image.open("assets/Login_button.png").resize((180,70)))

help_button_image = ImageTk.PhotoImage(Image.open("assets/Help_button.png").resize((180,70)))

submit_button_image = ImageTk.PhotoImage(Image.open("assets/Submit_button.png").resize((120,50)))

exit_button_image = ImageTk.PhotoImage(Image.open("assets/Exit_button.png").resize((120,50)))

location_button_image = ImageTk.PhotoImage(Image.open("assets/Location_button.png").resize((180,70)))

mosque_button_image = ImageTk.PhotoImage(Image.open("assets/Mosque_button.png").resize((180,70)))

host_button_image = ImageTk.PhotoImage(Image.open("assets/Host_button.png").resize((180,70)))

theme_button_image = ImageTk.PhotoImage(Image.open("assets/Theme_button.png").resize((180,70)))

# Navbar Button Images
button_image_1 = ImageTk.PhotoImage(Image.open("assets/home_page_icon.png").resize((100,100)))
button_image_2 = ImageTk.PhotoImage(Image.open("assets/prayers_page_icon.png").resize((100,100)))
button_image_3 = ImageTk.PhotoImage(Image.open("assets/qibla_page_icon.png").resize((100,100)))
button_image_4 = ImageTk.PhotoImage(Image.open("assets/community_page_icon.png").resize((100,100)))
button_image_5 = ImageTk.PhotoImage(Image.open("assets/masjid_page_icon.png").resize((100,100)))
button_image_6 = ImageTk.PhotoImage(Image.open("assets/settings_page_icon.png").resize((100,100)))

# Create pages as frames inside container
page1 = ScrollableFrame(container, orient="vertical")
page2 = ScrollableFrame(container, orient="vertical")
page3 = ScrollableFrame(container, orient="vertical")
page4 = ScrollableFrame(container, orient="vertical")
page5 = ScrollableFrame(container, orient="vertical")
page6 = ScrollableFrame(container, orient="vertical")
location_prayer = ScrollableFrame(container, orient="vertical")
mosque_prayer = ScrollableFrame(container, orient="vertical")

# Nav bar button paths
for page in (page1, page2, page3, page4, page5, page6, location_prayer, mosque_prayer):
    page.place(relwidth=1, relheight=1)

# Styles for increasing font size
style1 = tk.font.Font(size = 25)
style2 = tk.font.Font(size = 20)

# frames for page content
content_frame = Frame(page1.scrollable_frame)
content_frame.pack(fill='both', expand=True, padx=20, pady=20)

content_frame2 = Frame(page2.scrollable_frame)
content_frame2.pack(fill='both', expand=True, padx=20, pady=20)

# Top centered label
Label1 = ttk.Label(content_frame, text="Home Page", font=("Comfortaa", 25, "bold"))
Label1.pack(pady=(10, 20))

# Frame to hold Login and Help buttons side by side
button_frame1 = Frame(content_frame)
button_frame1.pack()

button_frame2 = Frame(content_frame2)
button_frame2.pack()

Login_window_button = tk.Button(button_frame1, borderwidth=0, image=login_button_image, command=login_window)
Login_window_button.pack(side="left", padx=40)

Help_window_button = tk.Button(button_frame1, borderwidth=0, image=help_button_image, command=help_window)
Help_window_button.pack(side="left", padx=40)

# Header label below buttons
Header1 = ttk.Label(content_frame, text="Explore some helpful apps!", font=style2, padding=5)
Header1.pack(pady=(40, 10))

# Frame to hold MasjidBox and MuslimPro side by side
apps_frame = Frame(content_frame)
apps_frame.pack(pady=10, fill="x")

#Masjid Box Recommendation
MasjidBox = Frame(apps_frame, bg="#B77B7E", width=150, height=150, relief="solid")
MasjidBox.pack(side="left", padx=20, fill="both", expand=True)
MasjidBoxText = Label(MasjidBox, font=("Arial", 10), text="Masjid Box\n Allows you to find\n different masjid prayer\n times and locational\n prayer times!", bg="#B77B7E")
MasjidBoxText2 = Label(
    MasjidBox,
    text="Masjid Box Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#B77B7E"
)
MasjidBoxText.pack(expand=True)
MasjidBoxText2.pack(expand=True)
MasjidBoxText2.bind("<Button-1>", lambda e: open_MasjidBox())

#Muslim Pro Recommendation
MuslimPro = Frame(apps_frame, bg="#B77B7E", width=150, height=150, relief="solid")
MuslimPro.pack(side="left", padx=20, fill="both", expand=True)
MuslimProText = Label(MuslimPro, font=("Arial", 10), text="Muslim Pro\n Allows both mosque and\n location prayers, as well as\n facilities like halal\n food places and shops!", bg="#B77B7E")
MuslimProText2 = Label(
    MuslimPro,
    text="Muslim Pro Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#B77B7E"
)
MuslimProText.pack(expand=True)
MuslimProText2.pack(expand=True)
MuslimProText2.bind("<Button-1>", lambda e: open_MuslimPro())

#FIANZ Recommendation
FIANZ = Frame(apps_frame, bg="#B77B7E", width=150, height=150, relief="solid")
FIANZ.pack(side="left", padx=20, fill="both", expand=True)
FIANZText = Label(FIANZ, font=("Arial", 10), text="FIANZ\n World wide organisation\n that can help\n you find halal\n certified products, as well\n as prayer times!", bg="#B77B7E")
FIANZText2 = Label(
    FIANZ,
    text="FIANZ Info",
    fg="blue",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#B77B7E"
)
FIANZText.pack(expand=True)
FIANZText2.pack(expand=True)
FIANZText2.bind("<Button-1>", lambda e: open_MuslimPro())

# Developers Note
Header3 = Label(content_frame, font= style2, text="Developers Note")
Header3.pack(expand=True, pady=40)
Text1 = Label(content_frame, font=("Arial", 10), text="""
Hi, I am Tehreem Fatima and am the person who developed this app.I wanted to create this\n\n app mainly so that people can find prayer times of both mosques and cities \n\n(mainly in Auckland), as well ascommunity events. This app includes link to a qibla finder site\n\n as wellso that you can find the direciton of prayer. Logging into \n\nthe app willalso allow you to save your details, and I will be able to see them\n\n andtherefore see how many people I can reach with it! Please enjoy exploring my app!""")
Text1.pack(expand=True)
    
# Navigation bar fixed at bottom of root
nav_bar = tk.Frame(root, height=100)
nav_bar.pack(side="bottom", fill="x")

# Displaying the pages
label2 = ttk.Label(page2.scrollable_frame, text="Prayers Page", font=style1)
label2.pack(padx=230)

label9 = ttk.Label(page2.scrollable_frame, text="Explore compiled 'annual' prayer times for \nyour location, or a mosques prayer times!\nClick back on the prayer mat icon to switch\nbetween prayer time types!", font=style2)
label9.pack(pady=100)

location_prayer_button = tk.Button(page2.scrollable_frame, image=location_button_image, borderwidth=0, command=lambda: show_frame(location_prayer))
location_prayer_button.pack(side = LEFT, padx=80)

mosque_prayer_button = tk.Button(page2.scrollable_frame, image=mosque_button_image, borderwidth=0, command=lambda: show_frame(mosque_prayer))
mosque_prayer_button.pack(side=LEFT, padx=30)

# Showing Content on Pages
apps_frame3 = Frame(location_prayer.scrollable_frame)
apps_frame3.pack(side=BOTTOM, fill="x")

apps_frame4 = Frame(location_prayer.scrollable_frame)
apps_frame4.pack(side=BOTTOM, fill="x")

apps_frame5 = Frame(location_prayer.scrollable_frame)
apps_frame5.pack(side=BOTTOM, fill="x")

#Ashburton Prayer Times
Ashburton = Frame(apps_frame3, bg="#456073", width=150, height=150, relief="solid")
Ashburton.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
AshburtonText = Label(Ashburton, font=("Arial", 10), fg="light grey", text="Ashburton Prayer Times\n\n", bg="#456073")
AshburtonText2 = Label(
    Ashburton,
    text="Ashburton",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
AshburtonText.pack(expand=True)
AshburtonText2.pack(expand=True)
AshburtonText2.bind("<Button-1>", lambda e: open_Ashburton())

#Helensville Prayer Times
Helensville = Frame(apps_frame3, bg="#456073", width=150, height=150, relief="solid")
Helensville.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
HelensvilleText = Label(Helensville, fg="light grey", font=("Arial", 10), text="Helensville Prayer Times\n\n", bg="#456073")
HelensvilleText2 = Label(
    Helensville,
    text="Helensville",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
HelensvilleText.pack(expand=True)
HelensvilleText2.pack(expand=True)
HelensvilleText2.bind("<Button-1>", lambda e: open_Helensville())

#Warkworth Prayer Times
Warkworth = Frame(apps_frame3, bg="#456073", width=150, height=150, relief="solid")
Warkworth.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
WarkworthText = Label(Warkworth, font=("Arial", 10), fg="light grey", text="Warkworth Prayer Times\n\n", bg="#456073")
WarkworthText2 = Label(
    Warkworth,
    text="Warkworth",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
WarkworthText.pack(expand=True)
WarkworthText2.pack(expand=True)
WarkworthText2.bind("<Button-1>", lambda e: open_Warkworth())

#Wellsford Prayer Times
Wellsford = Frame(apps_frame4, bg="#456073", width=150, height=150, relief="solid")
Wellsford.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
WellsfordText = Label(Wellsford, font=("Arial", 10), fg="light grey", text="Wellsford Prayer Times\n\n", bg="#456073")
WellsfordText2 = Label(
    Wellsford,
    text="Helensville",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
WellsfordText.pack(expand=True)
WellsfordText2.pack(expand=True)
WellsfordText2.bind("<Button-1>", lambda e: open_Wellsford())

#Kumeu Prayer Times
Kumeu = Frame(apps_frame4, bg="#456073", width=150, height=150, relief="solid")
Kumeu.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
KumeuText = Label(Kumeu, font=("Arial", 10), fg="light grey", text="Kumeu Prayer Times\n\n", bg="#456073")
KumeuText2 = Label(
    Kumeu,
    text="Kumeu",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
KumeuText.pack(expand=True)
KumeuText2.pack(expand=True)
KumeuText2.bind("<Button-1>", lambda e: open_Kumeu())

#Pukekohe Prayer Times
Pukekohe = Frame(apps_frame4, bg="#456073", width=150, height=150, relief="solid")
Pukekohe.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
PukekoheText = Label(Pukekohe, fg="light grey", font=("Arial", 10), text="Pukekohe Prayer Times\n\n", bg="#456073")
PukekoheText2 = Label(
    Pukekohe,
    text="Pukekohe",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
PukekoheText.pack(expand=True)
PukekoheText2.pack(expand=True)
PukekoheText2.bind("<Button-1>", lambda e: open_Pukekohe())

#Waiuku Prayer Times
Waiuku = Frame(apps_frame5, bg="#456073", width=150, height=150, relief="solid")
Waiuku.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
WaiukuText = Label(Waiuku, font=("Arial", 10), fg="light grey", text="Waiuku Prayer Times\n\n", bg="#456073")
WaiukuText2 = Label(
    Waiuku,
    text="Waiuku",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
WaiukuText.pack(expand=True)
WaiukuText2.pack(expand=True)
WaiukuText2.bind("<Button-1>", lambda e: open_Waiuku())

#WClevedon Prayer Times
Clevedon = Frame(apps_frame5, bg="#456073", width=150, height=150, relief="solid")
Clevedon.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
ClevedonText = Label(Clevedon, font=("Arial", 10), fg="light grey", text="Clevedon Prayer Times\n\n", bg="#456073")
ClevedonText2 = Label(
    Clevedon,
    text="Clevedon",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
ClevedonText.pack(expand=True)
ClevedonText2.pack(expand=True)
ClevedonText2.bind("<Button-1>", lambda e: open_Clevedon())

#Epsom Prayer Times
Epsom = Frame(apps_frame5, bg="#456073", width=150, height=150, relief="solid")
Epsom.pack(side = LEFT, padx=29, pady=20, fill="both", expand=True)
EpsomText = Label(Epsom, font=("Arial", 10), fg="light grey", text="Epsom Prayer Times\n\n", bg="#456073")
EpsomText2 = Label(
    Epsom,
    text="Epsom",
    fg="light grey",
    cursor="hand2",
    font=("Arial", 9, "underline"),
    bg="#456073"
)
EpsomText.pack(expand=True)
EpsomText2.pack(expand=True)
EpsomText2.bind("<Button-1>", lambda e: open_Epsom())

label3 = tk.Label(page3.scrollable_frame, text="Qibla Finder Page", font=style1)
label3.pack(padx=180, pady=20)

label3b = tk.Label(page3.scrollable_frame, text="To find the Qibla, you can use your phones \ncompass and find the direction of west, \nat 260 degrees. Or you can use this qibla finder \n(linked below), and it acurately shows \nthe direction to Makkah from your own \nlocation!!!\n\n", font=style2)
label3b.pack()

Qibla = Label(
    page3.scrollable_frame,
    text="Qibla Finder",
    fg="blue",
    cursor="hand2",
    font=style1
)
Qibla.pack(expand=True)
Qibla.bind("<Button-1>", lambda e: open_Qibla())

label4 = tk.Label(page4.scrollable_frame, text="Community Page", font=style1)
label4.pack(padx=190, pady=40)

label4b = tk.Label(page4.scrollable_frame, text="You can host your own event by \nclicking on the 'Host an Event' button below, \nor see others events. Please ensure you \nenter your correct address, incorrect addresses \nwill not be documented, you can enter your \nevent twice if that occurs!\n\n --Currently No Events to Show (0)--", font=style2)
label4b.pack()

Event_window_button = tk.Button(page4.scrollable_frame, image=host_button_image, borderwidth=0, command=event_details)
Event_window_button.pack(side="left", padx=220, pady=40, fill="x")

# Page 5 content
# Label for header
label5 = tk.Label(page5.scrollable_frame, text="Masjid locator Page", font=style1)
label5.pack(anchor="center", pady=50)

# Map widget for page 5 (under label 5)
map_widget = TkinterMapView(page5.scrollable_frame, width=600, height=400)
map_widget.pack(padx=10, pady=20)
# Create max zoom, as well as default/initial zoom
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
map_widget.set_zoom(12)

# Setting multiple markers with their positons and texts
marker_1 = map_widget.set_position(-36.907259, 174.738291,  marker=True)
print(marker_1.position, marker_1.text) 
marker_1.set_text("Masjid Umar")  

marker_2 = map_widget.set_position(-36.30411, 174.737949,  marker=True)
print(marker_2.position, marker_2.text)  
marker_2.set_text("Hillsborough Masjid")

marker_3 = map_widget.set_position(-36.894830, 174.700954,  marker=True)
print(marker_3.position, marker_3.text)  
marker_3.set_text("Avondale Islamic Centre")

marker_4 = map_widget.set_position(-36.912810, 174.749600,  marker=True)
print(marker_4.position, marker_4.text) 
marker_4.set_text("Al-Rahman Masjid") 

marker_5 = map_widget.set_position(-36.908420, 174.724064,  marker=True)
print(marker_5.position, marker_5.text) 
marker_5.set_text("Al-Hijaz Masjid")  

marker_6 = map_widget.set_position(-36.908420, 174.724064,  marker=True)
print(marker_6.position, marker_6.text)
marker_6.set_text("New Lynn Islamic Trust")

marker_7 = map_widget.set_position(-36.908537, 174.737515,  marker=True)
print(marker_7.position, marker_7.text)
marker_7.set_text("NZICT")

marker_8 = map_widget.set_position(-36.852685, 174.743768,  marker=True)
print(marker_8.position, marker_8.text)
marker_8.set_text("Ponsonby Masjid")

marker_9 = map_widget.set_position(-36.887907, 174.660422,  marker=True)
print(marker_9.position, marker_9.text)
marker_9.set_text("Masjid As-Salam")

marker_10 = map_widget.set_position(-36.901789, 174.724429,  marker=True)
print(marker_10.position, marker_10.text) 
marker_10.set_text("UKLA (Umar Bin Khattab Learning Academy)")

# Contents of page 6
# Header label
label6 = tk.Label(page6.scrollable_frame, text="Settings Page", font=style1)
label6.pack(padx=200, pady=100)

# Dark/Light Mode Switching button
sv_ttk.use_dark_theme()
sv_ttk.use_light_theme()

button = ttk.Button(page6.scrollable_frame, width=20, text="Change Theme", command=toggle_theme)
button.pack()

#Headers for pages of Location and Mosque prayer times
label7 = tk.Label(location_prayer.scrollable_frame, text="Location Prayer Times", font=style1)
label7.pack(anchor="center")

label8 = tk.Label(mosque_prayer.scrollable_frame, text="Mosque Prayer Times", font=style1)
label8.pack(padx=160, pady=20)

# Recommended mosque prayer time site
recommend = tk.Label(mosque_prayer.scrollable_frame, text="To find prayer times for each mosque,\n we recommend using Masjid Box, a digital \nsolution for msoques, as well as displaying \nmosques prayer times around the globe!", font=style2)
recommend.pack(pady=20)

#Link for masjid box link
MasjidBoxT = Label(
    mosque_prayer.scrollable_frame,
    text="Masjid Box",
    fg="blue",
    cursor="hand2",
    font=style1,
    bg="white",
)
MasjidBoxT.pack(expand=True)
MasjidBoxT.bind("<Button-1>", lambda e: open_MasjidBox())

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

# Run application
root.mainloop()
