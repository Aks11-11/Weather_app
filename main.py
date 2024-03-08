from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox, Label
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()

root.title("AK's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#search box
Search_image=PhotoImage(file = "/Users/akshat/Desktop/icons/Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root,justify = "center",width =17,font = ("poppins",25,"bold"),bg ="#404040", border = 0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon = PhotoImage(file = "/Users/akshat/Desktop/icons/Copy of search_icon.png")
myimage_icon = Button(image = Search_icon,borderwidth=0,cursor="hand2",bg = "#404040")
myimage_icon.place(x=400,y=34)

 #logo

Logo_image = PhotoImage(file = "/Users/akshat/Desktop/icons/Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150,y=80)

#Bottom Box
Frame_image = PhotoImage(file = "/Users/akshat/Desktop/icons/Copy of box.png")
frame_myimage = Label(image = Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)








root.mainloop()