import os
from tkinter.messagebox import askyesno, showinfo
from modules.functions import getEntriesDir
from data.settings import dev


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def closeWindow(window, entriesDir):
	if not dev:
		response = askyesno(
            'Exit',
            'Are you sure you want to exit?'
        )
		if response:
			window.destroy()
	else:
		if len(os.listdir(entriesDir)) >= 1:
			response = askyesno(
				'Exit',
				'Do you want to clear the cached entries?'
			)
			if response:
				for file in files(entriesDir):
					os.remove(os.path.join(entriesDir, file))
				showinfo("Success", "Cached entries removed")
		window.destroy()
