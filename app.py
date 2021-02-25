from tkinter import *
import random
from datetime import datetime
from geopy import geocoders
from astral import LocationInfo
from geopy import Nominatim
from astral.sun import sun


# Name Generator Files

with open("sunadj.txt", "r") as file:
    allText = file.read()
    adj = list(map(str, allText.split()))

with open("skynoun.txt", "r") as file:
    allNoun = file.read()
    noun = list(map(str, allNoun.split()))


# Button Actions

def bearing_button_click():
    bearing_text = str(random.randrange(0,360,5))
    entry.delete(0, END)
    entry.insert(0, bearing_text)

def name_button_click():
    name_text = random.choice(adj) + " " + random.choice(noun) + "\n"
    entry3.delete(0, END)
    entry3.insert(0, name_text)

def confirm_click():
    new_window = Toplevel(root)
    new_window.geometry("400x100")
    confirmLabel = Label(new_window, text=f"\n{entryText3.get()} \n A photograph taken in {city_enter.get()} at {entryText2.get()} at a bearing of {entryText.get()}.")
    confirmLabel.pack(side=TOP)

def city_click():
    geolocator = Nominatim(user_agent="Jack")
    location = geolocator.geocode(city_enter.get())
    city = LocationInfo(city_enter.get(), "", "", location.latitude, location.longitude)
    s = sun(city.observer, date=datetime.now())
    setrise_time.set(" ")
    rise = s["sunrise"]
    sett = s["sunset"]
    setrise_time.set(f'Sunrise: {rise}\nSunset:  {sett}\n')

def time_button_click():
    time_text = str(random.randrange(8,16,1)) + ":" + str(random.randrange(0,5,1)) + str(random.randrange(0,9,1))
    entry2.delete(0, END)
    entry2.insert(0, time_text)

# GUI Creation and Layout

root = Tk(className=" Sky Photograph Parameter Generator")
root.geometry("400x500")
root.configure(bg="white")

# Spacer 1

spacer1 = Label("", bg="white")
spacer1.pack(side=TOP)

# Title Heading

title = Label(text="Photograph Parameter Generator", bg="white")
title.pack(side=TOP)

# Spacer 2

spacer2 = Label("", bg="white")
spacer2.pack(side=TOP)

# Location Entry

location_title = Label(root, text="Enter Town/City:", bg="white")
location_title.pack(side=TOP)

city_enter = Entry(root)
city_enter.pack(side=TOP)

city_button = Button(root, text="Submit", command=city_click)
city_button.pack(side=TOP)

# Spacer 3

spacer3 = Label("", bg="white")
spacer3.pack(side=TOP)

# Sunrise/Sunset Information

setrise_time = StringVar()
sun_times = Label(root, textvariable=setrise_time)
sun_times.pack(side=TOP)

# Spacer 4

spacer4 = Label("", bg="white", height=2)
spacer4.pack(side=TOP)

# Bearing Generator

entryText = StringVar()
entry = Entry(root, textvariable=entryText)
bearing_button = Button(root, text="Generate Bearing", command=bearing_button_click)

entry.pack(side=TOP)
bearing_button.pack(side=TOP)

# Spacer 5

spacer5 = Label("", bg="white")
spacer5.pack(side=TOP)

# Time of Day Generator

entryText2 = StringVar()
entry2 = Entry(root, textvariable=entryText2)
time_button = Button(root, text="Generate Time of Day", command=time_button_click)

entry2.pack(side=TOP)
time_button.pack(side=TOP)

# Spacer 6

spacer6 = Label("", bg="white")
spacer6.pack(side=TOP)

# Title Generator

entryText3 = StringVar()
entry3 = Entry(root, textvariable=entryText3)
name_button = Button (root, text="Generate Photograph Title", command=name_button_click)

entry3.pack(side=TOP)
name_button.pack(side=TOP)

# Spacer 7

spacer7 = Label("", bg="white")
spacer7.pack(side=TOP)

# Confirm Button

confirm_button = Button(root, text="Confirm", command=confirm_click)
confirm_button.pack(side=TOP)

########

root.mainloop()