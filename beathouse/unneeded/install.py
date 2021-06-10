import tkinter as tk
from PIL import ImageTk, Image
import os
import subprocess
installed = False
global loop
loop = True
import sys
import time
parent = ".\\"
def on_closing():
    globals()['loop'] = False
def install():
    subprocess.call(parent+"\\installer help\\install.bat")
    time.sleep(2)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("installing")
path = parent+"\\installer help\\installing.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.protocol("WM_DELETE_WINDOW", on_closing)
while loop:
    root.update()
    if not installed:
        install()
        installed = True
        root.destroy()
        sys.exit()
