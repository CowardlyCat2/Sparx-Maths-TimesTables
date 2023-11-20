import pyautogui
import easyocr
from pynput import keyboard

#choices for filename
FILENAME = "games.csv"
#FILENAME = "100 club check.csv"

reader = easyocr.Reader(['en'])

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

print("Ready")

def press_callback(key):
    print(key)
    if key.char == "s":
        pyautogui.screenshot('image.png',region=(x1,x2, x3, x4))
        result = reader.readtext('image.png', detail = 0)

        result = result[0] 

        print(result)

        result = result.replace("= ?","")
        result = result.replace("=?","")
        result = result.replace("=","")
        result = result.replace("*"," ")
        result = result.split()

        for x in range(2):
            result.append("")
        print(result)

        if result[0] == "?" and (result[1] not in divideVaues):
            answer = str(int(int(result[2])/int(result[1])))

        elif result[1] in divideVaues:
            answer = str(int(int(result[0])/int(result[2])))


        elif result[1] == "?" and (result[1] not in divideVaues):
            answer = str(int(result[2])/int(result[0]))

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

l = keyboard.Listener(on_press=press_callback)
l.start()
l.join()
