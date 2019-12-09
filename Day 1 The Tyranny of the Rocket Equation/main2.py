'''
https://adventofcode.com/2019/day/1
What is the sum of the fuel requirements for all of 
the modules on your spacecraft when also taking into 
account the mass of the added fuel? (Calculate the fuel 
requirements for each module separately, then add them all up at the end.)
'''
import math

def calculateAmountOfFuel(mass):
    return math.floor(mass/3)-2

mass = 0
with open(file='day01/input.txt', mode='r') as file:
    for line in file:
        fuelMass =  calculateAmountOfFuel(int(line))
        foo = calculateAmountOfFuel(fuelMass)
        while foo > 0:
            fuelMass += foo
            foo = calculateAmountOfFuel(foo)
        mass += fuelMass
        print(fuelMass)

print('Answer: ' + str(mass))