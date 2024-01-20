import pyautogui
import easyocr
from pynput import keyboard


#choices for filename
FILENAME = "games.csv"
#FILENAME = "100 club check.csv"

FILENAMEIMPROVEMENTS = "improvements.csv"

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

#makes the list for data
file = open(FILENAME,"r")

list = []
divideVaues = ["+","#"]

for x in file:

    value = (x.split(","))
    value[-1] = int(value[-1].strip())
    value[-2] = int(value[-2])

    list.append(value)

file.close()

x1 = list[12][1]
x2 = list[12][2]

x3 = list[13][1] - x1
x4= list[13][2] - x2

file = open(FILENAMEIMPROVEMENTS,"r")

improvementsList = []

for x in file:

    value = (x.split(","))
    value[-1] = int(value[-1].strip())
    value[-2] = int(value[-2])

    improvementsList.append(value)

file.close()

y1 = improvementsList[1][1]
y2 = improvementsList[1][2]

y3 = improvementsList[2][1] - y1
y4= improvementsList[2][2] - y2

print("Ready")

def answer():
    pyautogui.screenshot('image.png',region=(x1,x2, x3, x4))
    result = reader.readtext('image.png', detail = 0)


    print(result)

    result = result[0] 

    print(result)

    result = result.replace("= ?","")
    result = result.replace("=?","")
    result = result.replace("=","")
    result = result.replace("*"," ")
    result = result.replace("x"," ")
    result = result.replace("X"," ")
    result = result.split()

    for x in range(2):
        result.append("")
    print(result)

    if result[0] == "?" and (result[1] not in divideVaues):
        answer = str(int(int(result[2])/int(result[1])))

    elif result[1] in divideVaues:
        answer = str(int(int(result[0])/int(result[2])))


    elif result[1] == "?" and (result[1] not in divideVaues):
        answer = str(int(int(result[2])/int(result[0])))

    elif result[0] == "?" and (result[1] in divideVaues):
        answer = str(int(int(result[3])/int(result[2])))
    elif result[2] == "?" and (result[1] not in divideVaues):
        answer = str(int(int(result[3])/int(result[0])))

    
    else:
        answer = str((int(result[0])*int(result[1])))

    print(answer)

    for x in answer:
        if x == "-":
            pyautogui.click(list[10][1],list[10][2])
        else:
            for y in list:
                if y[0] == x:
                    pyautogui.click(y[1],y[2])
                    break

    pyautogui.click(list[11][1],list[11][2])

def press_callback(key):
    try:
        print(key)

        if key.char == "s":
            try:
                answer()
            except:
                print("Crash Try Again")

        if key.char == "z":
            crash = 0
            while True:
                try:
                    answer()
                    crash = 0
                except:
                    print("Crash Trying Again")
    except:
        print("invalid key input")

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()
