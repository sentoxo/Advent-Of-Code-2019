'''
https://adventofcode.com/2019/day/11
Build a new emergency hull painting robot and run the Intcode program on it. 
How many panels does it paint at least once?
'''
from draw import drawFrom1dim
from computer import IntCodeComputer
import time, os

cpu = IntCodeComputer(input=())
cpu.readCodeFromFile('Day 11 Space Police/input.txt')

length = 45
space = []
space.extend([0, 0] for x in range(length**2))
pos = [3, 5]
way = 0 # 0-up 1-right ...
c = 0
space[ pos[0]+(pos[1]*length) ][0] = 1
while True:
    cpu.inputQ.put( space[ pos[0]+(pos[1]*length) ][0] )
    a = cpu.run()
    b = cpu.run()
    if cpu.state == 'halt':
        break

    if a != space[ pos[0]+(pos[1]*length) ][0] :
        if space[ pos[0]+(pos[1]*length) ][1] == 0 :
            c+=1
        space[ pos[0]+(pos[1]*length) ][1] = 1
    space[ pos[0]+(pos[1]*length) ][0] = a

    if b:
        way+=1
        if way>3:
            way=0
    else:
        way -=1
        if way<0:
            way=3
    
    if way == 0:
        pos[1] += 1
    elif way == 1:
        pos[0] += 1
    elif way == 2:
        pos[1] -= 1
    elif way == 3:
        pos[0] -= 1

    os.system('cls')
    drawFrom1dim([x[1] for x in space], length)
    time.sleep(0.02)
print(c)