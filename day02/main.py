'''
https://adventofcode.com/2019/day/2
Once you have a working computer, the first step is to restore the gravity assist program 
(your puzzle input) to the "1202 program alarm" state it had just before the last computer 
caught fire. To do this, before running the program, replace position 1 with the value 12 
and replace position 2 with the value 2. What value is left at position 0 after the program halts?
'''

with open(file='day02/input.txt', mode='r') as file:
    shelcode = file.readline().split(',')
    shelcode = list(map(int, shelcode))

    shelcode[1] = 12
    shelcode[2] = 2

    IP = 0 # instruction pointer 
    IC = 0 # instruction counter
    while True:
        if shelcode[IP] == 1:
            shelcode[shelcode[IP+3]] = shelcode[shelcode[IP+2]] + shelcode[shelcode[IP+1]]
        elif shelcode[IP] == 2:
            shelcode[shelcode[IP+3]] = shelcode[shelcode[IP+2]] * shelcode[shelcode[IP+1]]
        elif shelcode[IP] == 99:
            break #HALT!
        IP += 4
        IC += 1
        #print(shelcode)
    print(shelcode[0])
    print(IC)
