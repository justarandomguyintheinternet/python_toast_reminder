import pyautogui as ui
import time 
import os
import keyboard
import threading
from win10toast import ToastNotifier
toaster = ToastNotifier()


def d():
    x = threading.Thread(target=rec, args=(1,))
    x.start()
    
def rec(a):
    toaster.show_toast("Now recording text for notification", "Press enter to stop recording and proceed to time input", threaded=True,duration=1.5)  # 3 seconds
    recorded = keyboard.record(until="enter")
    keys = []
    n= []
    cnt = 0
    whole_text = ""
    timeout = 0
    for i in recorded:
        if cnt != 0 and cnt != 1 and cnt != len(recorded)-1 and cnt % 2 == 1:
            text = str(i)
            n.append(text[text.find("(")+1:text.find(")")])          
        cnt += 1
    for i in n:
        print(i)
        if i != "space down":
            parts = i.strip(" ")
            whole_text += parts[0]
        else:
            whole_text += " "
    toaster.show_toast("Now recording delay for notification", "Press enter to stop the input and and start the timer", threaded=True,duration=1.5)  # 3 seconds
    rt = keyboard.record(until="enter")
    cnt = 0
    print(rt)
    for i in rt:
        if cnt != 0 and cnt != len(rt)-1 and cnt % 2 == 0:
            if len(rt) == 6 and cnt == 2:
                text = str(i)
                timeout = int((text[text.find("(")+1:text.find(")")]).strip(" ")[0]) * 10
            elif len(rt) == 6 and cnt == 4:
                text = str(i)
                timeout += int((text[text.find("(") + 1:text.find(")")]).strip(" ")[0])
            elif len(rt) == 4:
                text = str(i)
                timeout = int((text[text.find("(") + 1:text.find(")")]).strip(" ")[0])
        cnt += 1
    toaster.show_toast("%s will be shown in %i minutes!" %(whole_text,timeout), "RemindMe", threaded=True,duration=3)  # 3 seconds
    time.sleep(timeout * 60)
    toaster.show_toast("%s was logged %i minutes ago!" %(whole_text,timeout), "RemindMe", threaded=True,duration=5)  # 3 seconds
    
keyboard.add_hotkey('shift + q + y', lambda: d(),suppress=True)

while True:
    time.sleep(1)

