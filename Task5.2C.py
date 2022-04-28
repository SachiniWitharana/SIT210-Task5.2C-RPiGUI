## Task 5.2C SIT210 RPiGUI ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## 3 LED bulb configurations ##
ledO=LED(14)
ledG=LED(23)
ledB=LED(24)

### GUI IMPLEMENTATIONS  ###
win = Tk()
win.title("3 LED Togglers")
myFont = tkinter.font.Font(family = 'Helvetica', size = 14, weight = "bold")


### Event Function for Orange LED ###
def ledToggleO():
    if ledO.is_lit:
        ledO.off()
        ledButtonO["text"]="Turn Orange LED on" 
    else:
        ledO.on()
        ledButtonO["text"]="Turn Orange LED off"

### Event Functions for Green LED ###
def ledToggleG():
    if ledG.is_lit:
        ledG.off()
        ledButtonG["text"]="Turn Green LED on" 
    else:
        ledG.on()
        ledButtonG["text"]="Turn Green LED off"
        
### Event Functions for Blue LED ###
def ledToggleB():
    if ledB.is_lit:
        ledB.off()
        ledButtonB["text"]="Turn Blue LED on" 
    else:
        ledB.on()
        ledButtonB["text"]="Turn Blue LED off"
        

def close():
    RPi.GPIO.cleanup()
    win.destroy()



### Button implementations for the GUI  ###

# Button trigger the selected LED 
ledButtonO = Button(win, text='Turn Orange LED on', font=myFont, command=ledToggleO, bg='orange', height=2, width=26)
ledButtonO.grid(row=0,column=1)

ledButtonG= Button(win, text='Turn Green LED on', font=myFont, command=ledToggleG, bg='green', height=2, width=26)
ledButtonG.grid(row=2,column=1)

ledButtonB = Button(win, text='Turn Blue LED on', font=myFont, command=ledToggleB, bg='blue', height=2, width=26)
ledButtonB.grid(row=4,column=1)

exitButton = Button(win, text='Exit all', font=myFont, command=close, bg='red', height=2, width=6)
exitButton.grid(row=6, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Looping repeated