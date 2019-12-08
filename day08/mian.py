'''
https://adventofcode.com/2019/day/8
To make sure the image wasn't corrupted during transmission, 
the Elves would like you to find the layer that contains the 
fewest 0 digits. On that layer, what is the number of 1 digits 
multiplied by the number of 2 digits?
'''
with open(file='day08/input.txt', mode='r') as file:

    layers = []

    while code := file.read(150):
        layers.append(code)
        print(f'{code=}')
    
    zero = 99999999
    zeroi = 0
    i = 0
    for foo in layers:
        if foo == '\n':
            break
        a = str(foo).count('0')
        if zero > a:
            zero = a
            zeroi = i
        i+=1
    print(zero)
    print(layers[zeroi])

    foo = layers[zeroi].count('1') *layers[zeroi].count('2')
    print(foo)
