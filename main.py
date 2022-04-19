# ============================
# Imports
# ============================

import tkinter as tk
import datetime
import ctypes.wintypes
from tkinter import messagebox, PhotoImage, Menu
from tkcalendar import Calendar
from dotenv import load_dotenv
import os
import logging
import shutil
import subprocess

# ============================
# 
# ============================

# ============================
# Defining Variables
# ============================

AppDataPath = os.getenv('LOCALAPPDATA')+"\\Diary\\"

CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(
    ctypes.wintypes.MAX_PATH
)
ctypes.windll.shell32.SHGetFolderPathW(
    None,
    CSIDL_PERSONAL,
    None,
    SHGFP_TYPE_CURRENT,
    buf
)

source = buf.value+"\\Naffy's Diary\\"
cacheDirDev = "cache\\"
cEntriesDirDev = "cache\\entries\\"
cacheDirPro = AppDataPath + "cache\\"
entriesDirPro = AppDataPath + "entries\\"
entriesDirPro = AppDataPath + "entries\\"
logFilePath = cacheDirPro + "app.log"

# ============================
# 
# ============================


# ============================
# Init
# ============================

load_dotenv()

env = os.getenv(
    "environment"
)


if env ==  "dev":
    dev=True
else:
    dev=False


if dev:
    print("Working in Development Environment\n")
    if os.path.isdir(cEntriesDirDev):
        print("Development Cache Dir Exists\n")
    else:
        print("Creating Development Cache + Entries Dir...")
        os.makedirs(cEntriesDirDev)
        print("Development Cache + Entries Dir Created\n")
else:
    print("Working in Production Environment\n")
    if os.path.isdir(cacheDirPro):
        print("Cache Dir Exists\n")
    else:
        print("Creating Cache Dir...")
        os.makedirs(cacheDirPro)
        print("Cache Dir Created\n")

    if os.path.isdir(entriesDirPro):
        print("Entries Dir Exists\n")
    else:
        print("Creating Entries Dir...")
        os.makedirs(entriesDirPro)
        print("Entries Dir Created\n")


if dev:
    logging.basicConfig(
        format='%(asctime)s - [%(levelname)s] %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.DEBUG
    )
else:
    logging.basicConfig(
        filename=logFilePath,
        filemode='a',
        format='%(asctime)s - [%(levelname)s] %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.DEBUG
    )


# ============================
# 
# ============================


# ============================
# Gui Config
# ============================

window = tk.Tk()
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

def openEntries():
    subprocess.Popen(f'explorer "{entriesDirPro}"')

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def restore():
    response = messagebox.askyesno(
        'Restore',
        'Restore the entries made by previous version?'
    )
    if response:
        for file in files(source):
            pf = source+file
            df = entriesDirPro+file
            shutil.move(pf, df)

        messagebox.showinfo("Success", "Restore completed succesfully")

def close():
    if env != "dev":
        response = messagebox.askyesno(
            'Exit',
            'Are you sure you want to exit?'
        )
        if response:
            window.destroy()
    else:
        window.destroy()

def other():
    def otherDone():
        date = datetime.date.fromisoformat(
            str(
                cal.selection_get()
            )
        )
        done(
            date
        )
        top.destroy()

    top = tk.Toplevel(
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
    )

    cal.pack(
        fill="both",
        expand=True
    )
    tk.Button(
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
    done(
        date
    )

def today():
    date = datetime.date.today()
    done(
        date
    )

def done(date):
    note = entry.get(
        "1.0",
        tk.END
    )
    dayStr = date.strftime(
        "%A"
    )
    month = date.strftime(
        "%B"
    )
    yearStr = str(
        date.year
    )
    dateStr = str(
        date.strftime(
            "%d"
        )
    )
    yearInt = date.year
    dateInt = date.strftime(
        "%d"
    )
    monthStr = date.strftime(
        "%m"
    )

    Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
    header = "Date: " + dateStr + " " + month + " " + yearStr + "\nDay: " + dayStr + "\n\n"

    if env == "dev":
        destination = cEntriesDirDev + Filename
    else:
        destination = entriesDirPro + Filename

    try:
        file = open(destination, "rt")
        file.read()
        file.close()
    except:
        try:
            os.makedirs(
                path
            )
        except:
            pass
        file = open(
            destination,
            "wt"
        )
        file.write(
            header + note
        )
        file.close()
        print(
            "Created a new file: " + Filename
        )
        entry.delete(
            "1.0",
            tk.END
        )
        messagebox.showinfo(
            "Success!",
            "New file created and saved."
        )
    else:
        file = open(
            destination,
            "at"
        )
        file.write(
            "\n" + note
        )
        file.close()
        entry.delete(
            "1.0",
            tk.END
        )
        print(
            "Edited the file: " + Filename
        )
        messagebox.showinfo(
            "Success!",
            "Edited the previous file"
        )

def about():
    messagebox.showinfo(
        "About",
        "This app is a transformation given to the normal Diary Journal that we write in our daily lives into a better GUI to work in. Now you can edit your previous entries without the need to strike any word or paragraph which makes the normal handwriten Diary a bit dirty."
    )

# ============================
# 
# ============================


# ============================
# Menubar
# ============================
def create_menu():
    menubar = Menu(
        window,
        background='#ff8000', foreground='black', activebackground='white', activeforeground='black'
    )


    help_ = Menu(
    	menubar,
    	tearoff = 0
    )
    
    menubar.add_cascade(
        label = 'Help',
        menu = help_
    )

    h_ = Menu(
    	menubar,
    	tearoff = 0
    )

    help_.add_cascade(
        label = 'Help',
        menu = h_
    )

    h_.add_command(
        label = 'Restore data from previous version',
        command = restore
    )
    h_.add_command(
        label = 'Open entries folder',
        command = openEntries
    )

    help_.add_separator()

    help_.add_command(
        label = 'About Diary',
        command = about
    )

    menubar.add_command(
        label='Exit',
        command = close
    )

    window.config(
        menu=menubar
    )

# ============================
# Menubar End
# ============================


# ============================
# Body
# ============================

frame = tk.Frame(
    window,
    bg='#444444'
)

greeting = tk.Label(
    text="Hello Naffy, What is new today?",
    height=3,
    font=("Comic Sans MS", 20, "bold"),
    bg='#444444',
    fg='#cccccc'
)
greeting.pack()

entry = tk.Text(
    height=20,
    font=("Comic Sans MS", 13),
    bg='#cccccc'
)
entry.pack()

nowImg = PhotoImage(
    file='./assets/done_for_now.png'
)
yestImg = PhotoImage(
    file='./assets/done_for_yest.png'
)
tomImg = PhotoImage(
    file='./assets/done_for_tom.png'
)

button2 = tk.Button(
    frame,
    image=yestImg,
    borderwidth=0,
    bg='#444444',
    command=yesterday
)
button2.pack(
    side="left",
    padx=5,
    pady=2
)

button3 = tk.Button(
    frame,
    image=tomImg,
    borderwidth=0,
    bg='#444444',
    command=other
)
button3.pack(
    side="right",
    padx=5,
    pady=2
)

button = tk.Button(
    frame,
    image=nowImg,
    borderwidth=0,
    bg='#444444',
    command=today
)
button.pack(
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

create_menu()
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