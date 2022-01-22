#!/usr/bin/env python

import os
try:
	from tkinter import *
except ImportError:
	print("Expectation Import error")

#from tkinter.ttk import *
from subprocess import *
import time

root= Tk() 

root.title("OpenOTT")

canvas1 = Canvas(root, width = 360, height = 360) 

canvas1['bg']= "light blue"

root.resizable(0,0)

canvas1.pack()

try:
	mass = PhotoImage(file = r"./collegeresize.png") 
	i=canvas1.create_image(0,0,anchor = NW, image=mass)

except:
    print("bg fails")
    pass

selection = "com.netflix.mediaclient/com.netflix.mediaclient.ui.launch.UIWebViewActivity"

def dropdown():
    selection = clicked.get()
    return selection
  
options = [ "Netflix","YouTube","Hotstar","Zee5","SonyLiv","Gaana","Spotify" ]

activities = { 
    "Netflix":"com.netflix.mediaclient/com.netflix.mediaclient.ui.launch.UIWebViewActivity",
    "YouTube":"com.google.android.youtube/com.google.android.youtube.HomeActivity",
    "Hotstar":"in.startv.hotstar/.rocky.launch.deeplink.DeeplinkActivity",
    "Zee5":"com.graymatrix.did/com.zee5.MainActivity",
    "SonyLiv":"com.sonyliv/.ui.home.HomeActivity",
    "Gaana":"com.gaana/.DeeplinkHandlingActivity",
    "Spotify":"com.spotify.music/.MainActivity" }
  
clicked = StringVar()
  
clicked.set( "Select an OTT" )

def start_app():
    selection = dropdown()
    os.system("adb shell am start -n "+ activities[selection])
    time.sleep(10)
    if selection == "Spotify":
        os.system("adb shell input keyevent 84")
        os.system("adb shell input text stay")
        time.sleep(1)
        for i in range(0,9):
            os.system("adb shell input keyevent 61")
            time.sleep(1)
        os.system("adb shell input keyevent 66")
        time.sleep(300)
    elif selection == "YouTube":
        os.system("adb shell input keyevent 84")
        os.system("adb shell input text stay")
        time.sleep(1)
        for i in range(0,3):
            os.system("adb shell input keyevent 61")
            time.sleep(1)
        os.system("adb shell input keyevent 66")
        time.sleep(3)
        os.system("adb shell input tap 550 650")
        time.sleep(300)

    package = activities[selection][:activities[selection].index("/")]
    print(package)
    os.system("adb shell am force-stop "+ package )

drop = OptionMenu( root , clicked , *options )
canvas1.create_window(120, 200, window=drop)

button15 = Button (root, text='RUN',command=start_app, height =2, width = 7,font = "Arial 12 bold")
canvas1.create_window(300, 180, window=button15)

inputtxt = Text(root, height = 1,width = 22,bg = "grey",fg = "white",font="Arial 10 bold")
canvas1.create_window(120,160, window=inputtxt)

#canvas1.create_text(180, 30,text="OPEN OTT APP",font = "Arial 12 bold",fill="white")

root.mainloop()
