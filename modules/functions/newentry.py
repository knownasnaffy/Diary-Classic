import os
from tkinter.messagebox import showerror, showinfo
import tkinter
from modules.emojify import emojify

def done(text, date, entryBox, entriesDir):
    note = str(emojify(text))
    dayStr = date.strftime("%A")
    month = date.strftime("%B")
    yearStr = str(date.year)
    dateStr = str(date.strftime("%d"))
    yearInt = date.year
    dateInt = date.strftime("%d")
    monthStr = date.strftime("%m")

    Filename = dateStr + "-" + monthStr + "-" + yearStr + ".txt"
    header = "Date: " + dateStr + " " + month + \
        " " + yearStr + "\nDay: " + dayStr + "\n\n"

    destination = entriesDir + Filename

    if os.path.isfile(destination):
        try:
            file = open(destination, "at", encoding="utf-8")
            file.write("\n" + note)
            file.close()
            entryBox.delete(
                "1.0",
                tkinter.END
            )
            showinfo("Success", "Previous entry edited")
        except:
            print("An exception occured while editing a previous file.")
            showerror("Error", "An exception occured while editing a previous file.")
            
    else:
        try:
            file = open(destination, "wt", encoding="utf-8")
            file.write(header + note)
            file.close()
            entryBox.delete(
                "1.0",
                tkinter.END
            )
            showinfo("Success", "New entry saved")
        except:
            print("An exception occured while writing a new file.")
            showerror("Error", "An exception occured while writing a new file.")
