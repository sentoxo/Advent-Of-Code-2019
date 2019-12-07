'''
https://adventofcode.com/2019/day/7
Try every combination of phase settings on the amplifiers. 
What is the highest signal that can be sent to the thrusters?
'''

def intcodeCPU(shelcode = [], input_ = ()):
    IP = 0 # instruction pointer 
    IC = 0 # instruction counter
    InputCounter = 0
    while shelcode:
        if shelcode[IP] == 99:
            break

        DE = shelcode[IP] % 100
        C = int(shelcode[IP] % 1000 / 100)      #first parameter
        B = int(shelcode[IP] % 10000 / 1000)
        A = int(shelcode[IP] % 100000 / 10000)

        if DE == 1:
            if A:
                shelcode[IP+3] = ( shelcode[IP+1] if C else shelcode[shelcode[IP+1]] )+( shelcode[IP+2] if B else shelcode[shelcode[IP+2]] )
            else:
                shelcode[shelcode[IP+3]] = ( shelcode[IP+1] if C else shelcode[shelcode[IP+1]] )+( shelcode[IP+2] if B else shelcode[shelcode[IP+2]] )
            IP += 4
        elif DE == 2:
            if A:
                shelcode[IP+3] = ( shelcode[IP+1] if C else shelcode[shelcode[IP+1]] )*( shelcode[IP+2] if B else shelcode[shelcode[IP+2]] )
            else:
                shelcode[shelcode[IP+3]] = ( shelcode[IP+1] if C else shelcode[shelcode[IP+1]] )*( shelcode[IP+2] if B else shelcode[shelcode[IP+2]] )
            IP += 4
        elif DE == 3:
            if C:
                shelcode[IP+1] = input_[InputCounter]
            else:
                shelcode[shelcode[IP+1]] = input_[InputCounter]
            IP += 2
            InputCounter += 1
        elif DE == 4:
            if C:
                return shelcode[IP+1]
            else:
                return shelcode[shelcode[IP+1]]
            IP += 2
        elif DE == 5:
            if (shelcode[IP+1] if C else shelcode[shelcode[IP+1]]):
                IP = shelcode[IP+2] if B else shelcode[shelcode[IP+2]]
            else:
                IP += 3
        elif DE == 6:
            if not (shelcode[IP+1] if C else shelcode[shelcode[IP+1]]):
                IP = shelcode[IP+2] if B else shelcode[shelcode[IP+2]]
            else:
                IP += 3
        elif DE == 7:
            if (shelcode[IP+1] if C else shelcode[shelcode[IP+1]]) < (shelcode[IP+2] if B else shelcode[shelcode[IP+2]]):
                shelcode[shelcode[IP+3]] = 1
            else:
                shelcode[shelcode[IP+3]] = 0
            IP += 4
        elif DE == 8:
            if (shelcode[IP+1] if C else shelcode[shelcode[IP+1]]) == (shelcode[IP+2] if B else shelcode[shelcode[IP+2]]):
                shelcode[shelcode[IP+3]] = 1
            else:
                shelcode[shelcode[IP+3]] = 0
            IP += 4
        else:
            raise Exception("Unknown opcode {0}".format(DE))
        IC += 1
    print("End of program,{0} instructions were executed.".format(IC,))

with open(file='day07/input.txt', mode='r') as file:
    code = file.readline().split(',')
    code = list(map(int, code))

    maxN = 0
    for i in range(3125):
        a = [int(i%5),int(i%25/5),int(i%125/25),int(i%625/125),int(i/625)]
        if a.count(0) > 1 or a.count(1) > 1 or a.count(2) > 1 or a.count(3) > 1 or a.count(4) > 1:
            continue

        amp1 = intcodeCPU(code.copy(), (int(i%5), 0))
        amp2 = intcodeCPU(code.copy(), (int(i%25/5), amp1))
        amp3 = intcodeCPU(code.copy(), (int(i%125/25), amp2))
        amp4 = intcodeCPU(code.copy(), (int(i%625/125), amp3))
        amp5 = intcodeCPU(code.copy(), (int(i/625), amp4))

        if amp5 > maxN:
            maxN = amp5
        
    print(maxN)
