'''
https://adventofcode.com/2019/day/12
How many steps does it take to reach the first state that exactly matches a previous state?
'''

from collections import namedtuple

class Moon():
    def __init__(self, pos = [0, 0, 0]):
        self.Pos = pos
        self.Vel = [0, 0, 0]
    def __repr__(self):
        return f'\n{Pos}\t{Vel}'

inputData = [ Moon([12, 0, -15]), Moon([-8, -5, -10]), Moon([7, -17, 1]), Moon([2, -11, -6]) ]
testData = [ Moon([-1, 0, 2]), Moon([2, -10, -7]), Moon([4, -8, 8]), Moon([3, 5, -1]) ]
test2Data = [ Moon([-8, -10, 0]), Moon([5, 5, 10]), Moon([2, -7, 3]), Moon([9, -8, -3]) ]
moons = inputData

sumOfEnergy1 = 0
for moon in moons:
    pot = 0
    kin = 0
    for p in range(3):
        pot += abs(moon.Pos[p])
        kin += abs(moon.Vel[p])
    sumOfEnergy1 += kin*pot

i = 0
while True:
    #GRAVITY
    for moon in moons:
        for secondMoon in moons:
            if moon == secondMoon:
                continue
            for p in range(3):
                if moon.Pos[p] > secondMoon.Pos[p]:
                    moon.Vel[p] -= 1
                elif moon.Pos[p] < secondMoon.Pos[p]:
                    moon.Vel[p] += 1
    #VELOCITY
    for moon in moons:
        for p in range(3):
            moon.Pos[p] += moon.Vel[p]

    sumOfEnergy = 0
    for moon in moons:
        pot = 0
        kin = 0
        for p in range(3):
            pot += abs(moon.Pos[p])
            kin += abs(moon.Vel[p])
        sumOfEnergy += kin*pot

    i+=1
    if sumOfEnergy == sumOfEnergy1:
        print(i)
        break

    if i % 10000 ==0:
        print(i)

    

print(moons)
print(sumOfEnergy)