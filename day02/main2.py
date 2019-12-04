'''
https://adventofcode.com/2019/day/2
Find the input noun and verb that cause the program to produce 
the output 19690720. What is 100 * noun + verb? 
(For example, if noun=12 and verb=2, the answer would be 1202.)
'''
import random

with open(file='day02/input.txt', mode='r') as file:
    code = file.readline().split(',')
    code = list(map(int, code))

    for none in range(100):
        for verb in range(100):
            shelcode = code.copy()
            shelcode[1] = none
            shelcode[2] = verb

            IP = 0 # instruction pointer 
            while True:
                if shelcode[IP] == 1:
                    shelcode[shelcode[IP+3]] = shelcode[shelcode[IP+2]] + shelcode[shelcode[IP+1]]
                elif shelcode[IP] == 2:
                    shelcode[shelcode[IP+3]] = shelcode[shelcode[IP+2]] * shelcode[shelcode[IP+1]]
                elif shelcode[IP] == 99:
                    break #HALT!
                IP += 4

            if shelcode[0] == 19690720:
                print(none)
                print(verb)
                print(100*none+verb)

