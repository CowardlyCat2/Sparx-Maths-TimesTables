import mouse
from win32com.client import Dispatch
import time

FILEINPUT = "100 club check.csv"

speak = Dispatch("SAPI.SpVoice").Speak

def countdown(time_sec):
    while time_sec:
        time.sleep(1)
        time_sec -= 1

    time.sleep(1)

def getLocation():
    tempLocation = mouse.get_position()
    tempLocation = str(tempLocation)
    tempLocation = tempLocation.replace("(","")
    tempLocation = tempLocation.replace(")","")

    return(tempLocation)

file = open(FILEINPUT,"w")

for x in range(10):
    toWrite = ""

    speak(("go to position" + str(x)))
    countdown(2)

    location = getLocation()

    toWrite = str(x) + "," + str(location) + "\n"

    file.write(toWrite)

speak("go to minus")
countdown(2)
location = getLocation()
toWrite = "-," + str(location) + "\n"
file.write(toWrite)

speak("go to enter")
countdown(2)
location = getLocation()
toWrite = "enter," + str(location)  + "\n"
file.write(toWrite)

speak("go to top left corner of question")
countdown(2)
location = getLocation()
toWrite = "top Left," + str(location)  + "\n"
file.write(toWrite)

speak("go to bottom right corner of question")
countdown(2)
location = getLocation()
toWrite = "bottom Right," + str(location)
file.write(toWrite)

file.close()
