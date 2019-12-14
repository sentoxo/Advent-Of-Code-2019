'''
https://adventofcode.com/2019/day/12
How many steps does it take to reach the first state that exactly matches a previous state?

NWW*2
'''

from collections import namedtuple

class Moon():
    def __init__(self, pos = [0, 0, 0]):
        self.Pos = pos
        self.Vel = [0, 0, 0]
    def __repr__(self):
        return f'\n{self.Pos}\t{self.Vel}'

inputData = [ Moon([12, 0, -15]), Moon([-8, -5, -10]), Moon([7, -17, 1]), Moon([2, -11, -6]) ]
testData = [ Moon([-1, 0, 2]), Moon([2, -10, -7]), Moon([4, -8, 8]), Moon([3, 5, -1]) ]
test2Data = [ Moon([-8, -10, 0]), Moon([5, 5, 10]), Moon([2, -7, 3]), Moon([9, -8, -3]) ]
moons = test2Data

foo = [0,0,0]
b = False

for i in range(3):
    axle = i

    sumOfEnergy1 = 0
    for moon in moons:
        pot = abs(moon.Pos[axle])
        kin = abs(moon.Vel[axle])
        sumOfEnergy1 += kin*pot

    i = 0
    while True:
        #GRAVITY
        for moon in moons:
            for secondMoon in moons:
                if moon == secondMoon:
                    continue
                if moon.Pos[axle] > secondMoon.Pos[axle]:
                    moon.Vel[axle] -= 1
                elif moon.Pos[axle] < secondMoon.Pos[axle]:
                    moon.Vel[axle] += 1
        #VELOCITY
        for moon in moons:
            moon.Pos[axle] += moon.Vel[axle]

        if moons[0].Vel[axle] == 0 :
            sumOfEnergy = 0
            pot = 0
            kin = 0
            for moon in moons:
                pot = abs(moon.Pos[axle])
                kin = abs(moon.Vel[axle])
                sumOfEnergy += kin*pot
            if sumOfEnergy == sumOfEnergy1:
                print(i+1)
                break

        i+=1
