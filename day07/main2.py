'''
https://adventofcode.com/2019/day/7#part2
Try every combination of the new phase settings on the amplifier feedback loop. 
What is the highest signal that can be sent to the thrusters?

It's take way to much time... sa many small mistakes. And from beginig cpu should by a class.
'''

class HALT(Exception):
   def __init__(self, arg):
      self.args = arg

def intcodeCPU(shelcode = [], input_ = (), IP = 0):
    IC = 0
    InputCounter = 0
    while shelcode:
        if shelcode[IP] == 99:
            raise HALT('halt')
 
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
            IP += 2
            if C:
                return shelcode[IP-1], shelcode.copy(), IP
            else:
                return shelcode[shelcode[IP-1]], shelcode.copy(), IP
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
    inn = 0
    for i in range(3125):
        a = [int(i%5),int(i%25/5),int(i%125/25),int(i%625/125),int(i/625)]
        #a = [4,2,3,0,1]
        #a = [4,3,2,1,0]
        
        if a.count(0) > 1 or a.count(1) > 1 or a.count(2) > 1 or a.count(3) > 1 or a.count(4) > 1:
            continue
 
        shelcode1 = code.copy()
        shelcode2 = code.copy()
        shelcode3 = code.copy()
        shelcode4 = code.copy()
        shelcode5 = code.copy()

        IC = [0,0,0,0,0,0]
        
        once = True
        amp5 = 0
        while True:
            try:
                amp5, shelcode1, IC[1] = intcodeCPU(shelcode1,  (a[0]+5, amp5) if once else (amp5,),  IC[1])
                amp5, shelcode2, IC[2] = intcodeCPU(shelcode2, (a[1]+5, amp5) if once else (amp5,), IC[2])
                amp5, shelcode3, IC[3] = intcodeCPU(shelcode3, (a[2]+5, amp5) if once else (amp5,), IC[3])
                amp5, shelcode4, IC[4] = intcodeCPU(shelcode4, (a[3]+5, amp5) if once else (amp5,), IC[4])
                amp5, shelcode5, IC[5] = intcodeCPU(shelcode5, (a[4]+5, amp5) if once else (amp5,), IC[5])
            except HALT:
                break

            once = False
        if amp5 > maxN:
            maxN = amp5
        print([x+5 for x in a])
        print(amp5)
        inn +=1
        
    print(maxN)