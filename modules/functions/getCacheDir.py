import os
import platform

def getCacheDir(dev):
	if not dev:
		if platform.system() == "Windows":
			cachePath = os.getenv('LOCALAPPDATA') + "\\cache\\"
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