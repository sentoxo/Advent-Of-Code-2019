'''
https://adventofcode.com/2019/day/10
The Elves are placing bets on which will be the 200th asteroid to be vaporized. 
Win the bet by determining which asteroid that will be; 
what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? 
(For example, 8,2 becomes 802.)

Made after 24h
(6, 10)
(11,13) testdata
'''

import math

file = open('Day 10 Monitoring Station/input.txt','r')

asteroidsPos = []
asteroidsAngle = []
y = 0
while foo := file.readline():
    for x,a in enumerate(foo):
        if a == '#':
            asteroidsPos.append((x, y))
    y += 1

pos = (8, 16)

for i in range(len(asteroidsPos)):
    asteroidsPos[i] = ( asteroidsPos[i][0]-pos[0], asteroidsPos[i][1]-pos[1] )

    angle = math.degrees( math.atan2( asteroidsPos[i][1], asteroidsPos[i][0] ) )
    
    if -180.0 < angle < -90.0:
        angle = 360 + angle + 90
    else:
        angle = angle + 90
    
    asteroidsAngle.append( angle )

ast = []
for i in range(len(asteroidsPos)):
    if asteroidsPos[i][0] == 0 and asteroidsPos[i][1] == 0:
        continue
    foo = [asteroidsAngle[i],math.sqrt( (asteroidsPos[i][0]**2) + (asteroidsPos[i][1]**2) ) ,asteroidsPos[i]]
    ast.append(foo)

so = sorted(ast)
counterOfHits = 0
beforeObj = -1
for obj in so:
    if obj[0] == -1 or beforeObj == obj[0]:
        continue
    beforeObj = obj[0]
    obj[0] = -1
    counterOfHits += 1
    print(f'{counterOfHits} {obj[2][0]+pos[0]},{obj[2][1]+pos[1]}')
    if counterOfHits == 200:
        print(obj)
        exit()

for foo in so:
    print(foo)