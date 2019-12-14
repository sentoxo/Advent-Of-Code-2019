from computer import IntCodeComputer
from draw import drawFrom1dim
import os,time

cpu = IntCodeComputer(input=(0,))
cpu.readCodeFromFile("Day 13 Care Package/input.txt")
cpu.ram[0] = 2

buffor = list(range(40*25))

score = 0
frames = 0

while True:
    buffor = list(range(40*25))
    while True:

        cpu.inputQ.put(1)
        x = cpu.run()
        y = cpu.run()
        id = cpu.run()
        if x == -1 and y == 0:
            score = id
        
        try:
            buffor[y*40+x] = id
        except IndexError:
            pass

        if x == 39 and y == 24:
            break


    frames += 1
    cpu.reset()
    os.system('cls')
    drawFrom1dim(buffor, 40)
    print(f'score: {score}  frames:{frames}')
    time.sleep(0.1)