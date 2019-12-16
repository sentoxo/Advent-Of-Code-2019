from computer import IntCodeComputer
from draw import drawFrom1dim
import os,time

cpu = IntCodeComputer()
cpu.readCodeFromFile("Day 13 Care Package/input.txt")
cpu.ram[0] = 2

buffor = list(range(40*25))

score = 0
frames = 0
paletka = 20

while True:

    while True:

        x = cpu.run()
        y = cpu.run()
        id = cpu.run()

        if x is None or y is None or id is None:
            break

        if id == 4:
            if x > paletka:
                cpu.inputQ.put(1)
            elif x < paletka:
                cpu.inputQ.put(-1)
            else:
                cpu.inputQ.put(0)
        elif id == 3:
            paletka == x

        if x == -1 and y == 0:
            score = id
        elif (39 >= x >= 0) and (24 >= y >= 0):
            buffor[y*40+x] = id

    frames += 1
    cpu.reset()

    os.system('cls')
    drawFrom1dim(buffor, 40)
    print(f'score: {score}  frames:{frames}')
    time.sleep(1)