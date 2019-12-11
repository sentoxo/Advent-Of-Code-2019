'''
https://adventofcode.com/2019/day/10
Find the best location for a new monitoring station. 
How many other asteroids can be detected from that location?

Second attemption. This time works fine :)
'''

import math

file = open('Day 10 Monitoring Station/input.txt','r')

asteroidsPos = []

y = 0
while foo := file.readline():
    for x,a in enumerate(foo):
        if a == '#':
            asteroidsPos.append((x, y))
    y += 1

for pos in asteroidsPos:
    asteroidsAngle = []
    for i in range(len(asteroidsPos)):

        angle = math.degrees( math.atan2( asteroidsPos[i][1]-pos[1], asteroidsPos[i][0]-pos[0] ) )

        if -180.0 < angle < -90.0:
            angle = 360 + angle + 90
        else:
            angle = angle + 90

        asteroidsAngle.append( angle )

    ast = []
    for i in range(len(asteroidsPos)):
        if asteroidsPos[i][0] == pos[0] and asteroidsPos[i][1] == pos[1]:
            continue
        foo = [asteroidsAngle[i],asteroidsPos[i]]
        ast.append(foo)

    so = sorted(ast)

    counterOfHits = 0
    beforeObj = -1
    for obj in so:
        if beforeObj == obj[0]:
            continue
        beforeObj = obj[0]
        counterOfHits += 1
        


    print(f'{counterOfHits} pos:{pos}')