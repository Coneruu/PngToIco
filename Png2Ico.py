import tkinter as tk
from tkinter import filedialog

import ttkbootstrap as ttk
import os
from PIL import Image

def PngToIco():
    png_filename = stroot.get() + ".png"
    ico_filename = stroot.get() + ".ico"
    icon_size = (40, 40)
    folder = os.getcwd()
    PngPath = os.path.join(folder, png_filename)
    IcoPath = os.path.join(folder, ico_filename)
    png_image = Image.open(PngPath)
    png_image.save(IcoPath, format='ICO', sizes=[icon_size])
    label2 = ttk.Label(master=window, text="Done", foreground="green")
    label2.pack()



window = tk.Tk()
window.title("PNG to ICO")
window.geometry("600x400")
stroot = tk.StringVar()
label = tk.Label(window, text="Filename (Without .png, must be in same folder as this application)")
label.pack()
entry = tk.Entry(window, textvariable=stroot)
entry.pack()
button = tk.Button(window, text="Convert", command=PngToIco)
button.pack()
window.mainloop()