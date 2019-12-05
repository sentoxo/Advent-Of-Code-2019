'''
https://adventofcode.com/2019/day/4
How many different passwords within the range given 
in your puzzle input meet these criteria?
'''

def number_adjacent(number):
    a = str(number)
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            return True
    return False

def number_never_decrease(number):
    a = str(number)
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True

puzzle_input = (272091, 815432)
number = 0
for i in range(puzzle_input[0], puzzle_input[1]):
    if number_adjacent(i) and number_never_decrease(i):
        number += 1
print(number)