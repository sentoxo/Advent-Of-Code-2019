'''
https://adventofcode.com/2019/day/6
What is the total number of direct and 
indirect orbits in your map data?
'''
def foo(orb, obj):
    if obj == 'COM':
        return 1
    else:
        return foo( orb, orb[obj] ) + 1

with open(file='day06/input.txt', mode='r') as file:

    orb = {} # 'obiekt orbitujacy':'obiekt w centrum'

    for line in file:
        a,b = line.split(')')
        orb[b.rstrip('\n')] = a

    s = 0
    for obj in orb:
        s +=foo(orb, orb[obj])
    print(s)
