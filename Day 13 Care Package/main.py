from computer import IntCodeComputer
from draw import drawFrom1dim
import os,time

cpu = IntCodeComputer(input=(0,))
cpu.readCodeFromFile("Day 13 Care Package/input.txt")
cpu.ram[0] = 2

buffor = list(range(40*25))

score = 0
frames = 0
paletka = 20

while True:
    #buffor = list(range(40*25))
    while cpu.state != 'halt':

        x = cpu.run()
        y = cpu.run()
        id = cpu.run()
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

        #if x == 39 and y == 24:
        #    break


    frames += 1
    cpu.reset()
    os.system('cls')
    drawFrom1dim(buffor, 40)
    print(f'score: {score}  frames:{frames}')
    time.sleep(2)