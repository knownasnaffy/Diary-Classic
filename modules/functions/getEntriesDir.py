import os
import platform
from data.app import name
from data.settings import dev

def getEntriesDir():
	if not dev:
		if platform.system() == "Windows":
			entriesPath = os.getenv('LOCALAPPDATA') + "\\" + name + "\\entries\\"
		else:
			entriesPath = os.getcwd() + "\\entries\\"

	else:
		entriesPath = os.getcwd() + "\\cache\\entries\\"

	if os.path.isdir(entriesPath):
		print("Enties directory exixts")
	else:
		try:
			os.makedirs(entriesPath+1)
			print("Created entries directory")
		except Exception as e:
			# print("An exception occured while creating entries directory")
			print("An exception occured while creating entries directory:\n{e}")

	return entriesPath
