import os
import zipfile
import urllib.request
from tkinter import Tk
from tkinter.filedialog import askdirectory
Tk().withdraw()

print("Choose installation location.")
dir = askdirectory()
tmp = os.path.join(dir, "tmp")
file = "2d_minecraft-"
print("Installing...")
try:
    urllib.request.urlretrieve("https://github.com/ArjunSahlot/2d_minecraft/archive/main.zip", tmp)
    file += "main"
except urllib.error.HTTPError:
    urllib.request.urlretrieve("https://github.com/ArjunSahlot/2d_minecraft/archive/master.zip", tmp)
    file += "master"

print("Unzipping")
with zipfile.ZipFile(tmp, 'r') as zip:
    zip.extractall(dir)

print("Cleaning up")
os.rename(os.path.join(dir, file), os.path.join(dir, file.split("-")[0]))
os.remove(os.path.join(tmp))

print("Done!")
