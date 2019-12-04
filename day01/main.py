'''
https://adventofcode.com/2019/day/1
What is the sum of the fuel requirements for all of 
the modules on your spacecraft?
'''
import math

mass = 0
with open(file='day01/input.txt', mode='r') as file:
    for line in file:
        mass +=  math.floor(int(line)/3)-2

print(mass)