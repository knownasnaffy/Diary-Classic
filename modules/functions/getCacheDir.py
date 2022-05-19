import os
import platform
from data.app import name
from data.settings import dev

def getCacheDir():
	if not dev:
		if platform.system() == "Windows":
			cachePath = os.getenv('LOCALAPPDATA') + "\\" + name + "\\cache\\"
		else:
			cachePath = os.getcwd() + "\\cache\\"

	else:
		cachePath = os.getcwd() + "\\cache\\"

	if os.path.isdir(cachePath):
		print("Cache directory exixts")
	else:
		try:
			os.makedirs(cachePath)
			print("Created cache directory")
		except:
			print("An exception occured")

	return cachePath