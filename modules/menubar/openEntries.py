import subprocess

def openEntries(entriesDir):
    subprocess.Popen(f'explorer "{entriesDir}"')