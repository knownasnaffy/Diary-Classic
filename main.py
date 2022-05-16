# ============================
# Imports
# ============================

import tkinter as tk
import datetime
from tkinter import PhotoImage, Button, Tk, Label, Frame, Text, Toplevel
from tkcalendar import Calendar
from modules.functions import closeWindow, getCacheDir, getEntriesDir, done
from data.settings import env
from modules.menubar import menu
# ============================
# 
# ============================

# ============================
# Defining Variables
# ============================


# ============================
# 
# ============================


# ============================
# Determining Environment
# ============================

if env ==  "dev":
    dev=True
    print("Working in Development Environment")
else:
    dev=False
    print("Working in Production Environment")

# ============================
# 
# ============================


# ============================
# Defining Variables
# ============================

entriesDir = getEntriesDir(dev)
cacheDir = getCacheDir(dev)

# ============================
# 
# ============================


# ============================
# Gui Config
# ============================

window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry(
    str(width) + "x" + str(height-70) + "+0+0"
)
window.title(
    "Diary Journal"
)
window.configure(
    bg='#444444'
)

# ============================
# 
# ============================


# ============================
# Defining Functions
# ============================
def close():
    closeWindow(dev, window, entriesDir)

def other():
    top = Toplevel(
        window
    )

    today = datetime.date.today()

    cal = Calendar(
        top,
        font="Ubuntu 14",
        selectmode='day',
        locale='en_US',
        cursor="hand1",
        maxdate=today
    ).pack(
        fill="both",
        expand=True
    )

    def otherDone():
        date = datetime.date.fromisoformat(
            str(
                cal.selection_get()
            )
        )
        done(entry.get("1.0", tk.END), date, entry, entriesDir)
        top.destroy()
    
    Button(
        top,
        text="    OK    ",
        font="Ubuntu 15",
        command=otherDone
    ).pack(
        padx=5,
        pady=5
    )
    

def yesterday():
    date = datetime.date.today() - datetime.timedelta(
        days=1
    )
    done(entry.get("1.0", tk.END), date, entry, entriesDir)

def today():
    date = datetime.date.today()
    done(entry.get("1.0", tk.END), date, entry, entriesDir)

# ============================
# 
# ============================


# ============================
# Body
# ============================

frame = Frame(
    window,
    bg='#444444'
)

greeting = Label(
    text="Hello Naffy, What is new today?",
    height=3,
    font=("Comic Sans MS", 20, "bold"),
    bg='#444444',
    fg='#cccccc'
).pack()

entry = Text(
    height=20,
    font=("Comic Sans MS", 13),
    bg='#cccccc'
)
entry.pack()

nowImg = PhotoImage(
    file='./assets/today.png'
)
yestImg = PhotoImage(
    file='./assets/yesterday.png'
)
otherImg = PhotoImage(
    file='./assets/other.png'
)

button2 = Button(
    frame,
    image=yestImg,
    borderwidth=0,
    bg='#444444',
    command=yesterday
).pack(
    side="left",
    padx=5,
    pady=2
)

button3 = Button(
    frame,
    image=otherImg,
    borderwidth=0,
    bg='#444444',
    command=other
).pack(
    side="right",
    padx=5,
    pady=2
)

button = Button(
    frame,
    image=nowImg,
    borderwidth=0,
    bg='#444444',
    command=today
).pack(
    side="right",
    padx=5,
    pady=2
)

frame.pack(
    expand=True,
    padx=10,
    pady=10
)

# ============================
# 
# ============================


# ============================
# Calling and Binding Functions
# ============================

menu(window, close)
window.protocol(
    'WM_DELETE_WINDOW',
    close
)

# ============================
# 
# ============================


# ============================
# Start App
# ============================

window.mainloop()