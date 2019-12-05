'''
https://adventofcode.com/2019/day/5
What is the diagnostic code for system ID 5?
'''

with open(file='day05/input.txt', mode='r') as file:
    shelcode = file.readline().split(',')
    shelcode = list(map(int, shelcode))

    IP = 0 # instruction pointer 
    IC = 0 # instruction counter
    while True:
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
                shelcode[IP+1] = int(input("Input: "))
            else:
                shelcode[shelcode[IP+1]] = int(input("Input: "))
            IP += 2
        elif DE == 4:
            if C:
                print( "Output: " + str(shelcode[IP+1]) )
            else:
                print( "Output: " + str(shelcode[shelcode[IP+1]]) )
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

        IC += 1
        if IC == 1000000:
            raise Exception('1mln instructions, too much, damage cpu or program')

    print("End of program,{0} instructions were executed.1".format(IC,))