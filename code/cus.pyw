import pyautogui as ui
import time 
import os
import keyboard
import threading
from win10toast import ToastNotifier
toaster = ToastNotifier()
#Import stuff

#Function for starting a notification thread
def d():
    x = threading.Thread(target=rec, args=(1,))
    x.start()

#Function for the most stuff    
def rec(a):
    toaster.show_toast("Now recording text for notification", "Press enter to stop recording and proceed to time input", threaded=True,duration=1.5)  # Show notification 
    
    recorded = keyboard.record(until="enter")   
    keys = []
    n= []
    cnt = 0                                      #Set up variables and record keyboard input
    whole_text = ""
    timeout = 0
    
    for i in recorded:
        if cnt != 0 and cnt != 1 and cnt != len(recorded)-1 and cnt % 2 == 1:
            text = str(i)                                                               #Go trough each second event (Keys are up and down so each second is enough) exept for the first two(Hotkey input) and the last(Enter input)
            n.append(text[text.find("(")+1:text.find(")")])                             #Strip it so that we only have eg. "k up" and append to temporary list
        cnt += 1
        
    for i in n:
        print(i)
        if i != "space down":                                                           #Check if theres a space event and then add an empty space
            parts = i.strip(" ")
            whole_text += parts[0]                                                      #Strip the eg. "k up" at the space and take the first part ("k")
        else:
            whole_text += " "
    toaster.show_toast("Now recording delay for notification", "Press enter to stop the input and and start the timer", threaded=True,duration=1.5)  # 3 seconds
    
    rt = keyboard.record(until="enter")
    cnt = 0                                                                             #Record the time and set up variables
    print(rt)
    
    for i in rt:
        if cnt != 0 and cnt != len(rt)-1 and cnt % 2 == 0:
            if len(rt) == 6 and cnt == 2:
                text = str(i)
                timeout = int((text[text.find("(")+1:text.find(")")]).strip(" ")[0]) * 10
            elif len(rt) == 6 and cnt == 4:
                text = str(i)                                                           #Go through each event as above and when there were 5 events its one digit("4") when 6 events two Digits("69") strip it then and add to the timeout
                timeout += int((text[text.find("(") + 1:text.find(")")]).strip(" ")[0])
            elif len(rt) == 4:
                text = str(i)
                timeout = int((text[text.find("(") + 1:text.find(")")]).strip(" ")[0])
        cnt += 1
    
    toaster.show_toast("%s will be shown in %i minutes!" %(whole_text,timeout), "RemindMe", threaded=True,duration=3)  # 3 seconds
    time.sleep(timeout * 60)                                                            #Wait the delay
    toaster.show_toast("%s was logged %i minutes ago!" %(whole_text,timeout), "RemindMe", threaded=True,duration=5)  # 3 seconds

#Add the Hotkey and when its pressed call the d function
keyboard.add_hotkey('shift + q + y', lambda: d(),suppress=True)

#idk if this is necessary
while True:
    time.sleep(1)

