import tkinter as tk
import datetime
import ctypes.wintypes
from tkinter import messagebox

window = tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry(str(width)+"x"+str(height-70)+"+0+0")
window.title("Diary Entry")

CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

def msg(title, message):
    messagebox.showinfo(title,  message)

def done():
    note = entry.get("1.0", tk.END)
    x = datetime.datetime.now()
    dayStr = x.strftime("%A")
    month = x.strftime("%B")
    yearStr = str(x.year)
    dateStr = str(x.strftime("%d"))
    yearInt = x.year
    dateInt = x.strftime("%d")
    monthStr = x.strftime("%m")

    Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
    header = "Date: " + dateStr + " " + month + " " + yearStr + "\nDay: " + dayStr + "\n\n"
    destination = buf.value + "\\Naffy's Diary\\" + Filename

    try:
    	file = open(destination, "rt")
    	file.read()
    	file.close()
    except:
    	file = open(destination, "at")
    	file.write(header + note)
    	file.close()
    	print("Created a new file: " + Filename)
    	entry.delete("1.0", tk.END)
    	msg("Success!", "New file created and saved.")
    else:
    	file = open(destination, "at")
    	file.write("\n" + note)
    	file.close()
    	entry.delete("1.0", tk.END)
    	print("Edited the file: " + Filename)
    	msg("Success!", "Edited the previous file")

greeting = tk.Label(text="Hello Naffy, What is new today?", height=10)
greeting.pack()

entry = tk.Text()
entry.pack()

button = tk.Button(text="Done for now", relief=tk.RAISED, border=3, width=10, height=2, command=done)
button.pack()

window.mainloop()
