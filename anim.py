import os
import time

def drawframe(symbol, nowframe, frametotal):
    os.system("clear")
    ss = ""
    cf = 0
    while cf <= frametotal:
        if cf == nowframe:
            ss += symbol
        else:
            ss += " "
        cf += 1
    print(ss)
    time.sleep(0.05)

while True:
    for x in range(1, 15):
        drawframe("#", x, 15)
    for x in range(1, 15):
        drawframe("#", 15-x, 15)
