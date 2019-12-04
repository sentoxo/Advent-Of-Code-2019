'''
https://adventofcode.com/2019/day/3
What is the fewest combined steps the wires 
must take to reach an intersection?

That's was realy shitty code... wtf i was writing xD But works, so...
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

def lineLength(p1, p2):
    if p1[0]==p2[0]:
        return abs(p1[1]-p2[1])
    elif p1[1]==p2[1]:
        return abs(p1[0]-p2[0])

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

    wire1steps = []
    wire2steps = []

    for intersection in listOfIntersection:
        for i in range(len(wire1)-1):
            if inn(intersection[0], wire1[i][0], wire1[i+1][0]) and inn(intersection[1], wire1[i][1], wire1[i+1][1]):
                foo = 0
                for n in range(i):
                    foo+=lineLength(wire1[n], wire1[n+1])
                foo += lineLength(wire1[i], intersection)
                wire1steps.append(foo)


        for i in range(len(wire2)-1):
            if inn(intersection[0], wire2[i][0], wire2[i+1][0]) and inn(intersection[1], wire2[i][1], wire2[i+1][1]):
                foo = 0
                for n in range(i):
                    foo+=lineLength(wire2[n], wire2[n+1])
                foo += lineLength(wire2[i], intersection)
                wire2steps.append(foo)

    smallestDistance = 4294967296
    for i in range(len(wire1steps)):
        foo = wire1steps[i] + wire2steps[i]
        if foo < smallestDistance and foo != 0:
            smallestDistance = foo

    print(smallestDistance)


    smallestDistance = 4294967296
    for i in listOfIntersection:
        distance = abs(i[0]) + abs(i[1])
        if distance < smallestDistance and distance != 0:
            smallestDistance = distance
