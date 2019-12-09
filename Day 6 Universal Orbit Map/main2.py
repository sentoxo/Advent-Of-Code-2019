'''
https://adventofcode.com/2019/day/6
What is the total number of direct and 
indirect orbits in your map data?
'''
you = []
san = []

def foo(orb, obj, tab = []):
    if obj == 'COM':
        tab.append(obj)
    else:
        tab.append(obj)
        return foo( orb, orb[obj], tab )

with open(file='day06/input.txt', mode='r') as file:

    orb = {} # 'obiekt orbitujacy':'obiekt w centrum'

    for line in file:
        a,b = line.split(')')
        orb[b.rstrip('\n')] = a

    s = 0
    foo(orb, orb['YOU'], you)
    foo(orb, orb['SAN'], san)

    a = len(san)-1
    b = len(you)-1
    c = 0
    while True:
        if san[a] != you[b]:
            break
        else:
            a-=1
            b-=1
            c+=1
    print(len(san)+len(you) - c*2)
