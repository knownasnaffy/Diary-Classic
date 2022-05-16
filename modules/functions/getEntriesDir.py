import os
import platform

def getEntriesDir(dev):
	if not dev:
		if platform.system() == "Windows":
			entriesPath = os.getenv('LOCALAPPDATA') + "\\entries\\"
		else:
			entriesPath = os.getcwd() + "\\entries\\"

	else:
		entriesPath = os.getcwd() + "\\cache\\entries\\"

	if os.path.isdir(entriesPath):
		print("Enties directory exixts")
	else:
		try:
			os.makedirs(entriesPath)
			print("Created entries directory")
		except:
			print("An exception occured while creating entries directory")

	return entriesPath
