'''
https://adventofcode.com/2019/day/10
Find the best location for a new monitoring station. 
How many other asteroids can be detected from that location?

Very bad code. Don't work for test data, but worked for input data...   乁( ͡ಠ ʖ̯ ͡ಠ)ㄏ
'''

def substractPos(a = (), b = ()):
    return (a[0]-b[0],a[1]-b[1])
def addPos(a = (), b = ()):
    return (a[0]+b[0],a[1]+b[1])
def existPos(a, b):
    for pos in b:
        if a[0]==pos[0] and a[1]==pos[1]:
            return True
    return False


def checkPos(c = ()):
    '''     abomination!    '''
    if c[0] in (0, 1, -1) and c[1] in (0,1, -1) :
        return []
    ret = []
    a = [0,0]
    a[0] = abs(c[0])
    a[1] = abs(c[1])
    if a[0] == 0 and a[1]>1:
        ret.append((0,1)) if c[1] >0 else ret.append((0,-1))
    if a[1] == 0 and a[0]>1:
        ret.append((1,0)) if c[0] >0 else ret.append((-1, 0))

    if(max(a)==2):
        ret.append((int(c[0]/2), int(c[1]/2)))

    if(a[1]==a[0]):
        ret.append((1 if c[0]>0 else -1,1 if c[1]>0 else -1))

    for i in range(2, max(a), 1):
        if (a[0] % i == 0) and (a[1] % i == 0) and a[0]!=0 and a[1]!=0 and a[0]!=a[1]:
            b = [int(a[0]/i), int(a[1]/i)]
            if c[0]<0:
                b[0] = -b[0]
            if c[1]<0:
                b[1] = -b[1]
            ret.append(b)
        elif a[0] == 0:
            if c[1]<0:
                ret.append((0, -i))
            else:
                ret.append((0, i))
        elif a[1] == 0:
            if c[0]<0:
                ret.append((-i, 0))
            else:
                ret.append((i, 0))
        elif a[0] == a[1]:
            ret.append((i if c[0]>0 else -i,i if c[1]>0 else -i))
    return ret

file = open('Day 10 Monitoring Station/test.txt','r')

asteroidsPos = []
y = 0
while foo := file.readline():
    for x,a in enumerate(foo):
        if a == '#':
            asteroidsPos.append((x, y))
    y += 1

print(f'{len(asteroidsPos)=}')

maxC = 0
for place in asteroidsPos:
    print(f'--{place}--')
    c = 0
    for asteroid in asteroidsPos:
        if place == asteroid:
            continue
        distance = substractPos(asteroid, place) 
        ex = True
        if asteroid == (4, 7) and place == (5,8):
            print()
        for pos in checkPos(distance):
            foo = addPos(place,pos)
            if existPos(foo, asteroidsPos):
                print(f'{foo=}')
                ex = False
                break
        if ex:
            c+=1
            print(f'{asteroid} {c}')
    if c> maxC:
        maxC = c
        print(f'new max: {place}')


print(f'{maxC=}')