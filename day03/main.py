'''
https://adventofcode.com/2019/day/3
What is the Manhattan distance from the central port
to the closest intersection?
'''

def getListOfCord(wire1puzzle):
    ''' return [(x, y),...] '''
    wire1 = [(0, 0),]
    pos = (0, 0) # x, y
    for move in wire1puzzle:
        if move[0] == 'U':
            pos = (pos[0], pos[1] + int(move[1:]) )
        elif move[0] == 'D':
            pos = (pos[0], pos[1] - int(move[1:]) )
        elif move[0] == 'L':
            pos = (pos[0] - int(move[1:]), pos[1])
        elif move[0] == 'R':
            pos = (pos[0] + int(move[1:]), pos[1])

        wire1.append(pos)
    return wire1

def intersection(p1, p2, p3, p4):
    '''p1,p2 first line... pn=(x, y) '''
    if p1[1]==p2[1] and p3[0]==p4[0]:
        # -|
        if inn(p1[1], p3[1], p4[1]) and inn(p3[0], p1[0], p2[0]):
            return (p3[0], p1[1])
        else:
            return False
    elif p1[0]==p2[0] and p3[1]==p4[1]:
        # |-
        if inn(p3[1], p1[1], p2[1]) and inn(p1[0], p3[0], p4[0]):
            return (p1[0], p3[1])
        else:
            return False

    return False
    

def inn(one, two, three):
    ''' is one beetwen two and three? '''
    if three > two:
        return three >= one >= two
    else:
        return two >= one >= three


with open(file='day03/input.txt', mode='r') as file:
    wire1puzzle = file.readline().split(',')
    wire2puzzle = file.readline().split(',')

    wire1 = getListOfCord(wire1puzzle)
    wire2 = getListOfCord(wire2puzzle)

    listOfIntersection = []

    for i in range(len(wire1)-1):
        for n in range(len(wire2)-1):
            foo = intersection(wire1[i], wire1[i+1], wire2[n], wire2[n+1])
            if foo:
                listOfIntersection.append(foo)
                print(wire1[i])
                print(wire1[i+1])
                print(wire2[n])
                print(wire2[n+1])

    smallestDistance = 4294967296
    for i in listOfIntersection:
        distance = abs(i[0]) + abs(i[1])
        if distance < smallestDistance and distance != 0:
            smallestDistance = distance
    print(listOfIntersection)
    print(smallestDistance)
