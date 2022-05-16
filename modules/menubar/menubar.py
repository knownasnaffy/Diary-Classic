from tkinter import Menu
from modules.menubar import about, openEntries


def menu(window, close):

    menubar = Menu(
        window
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