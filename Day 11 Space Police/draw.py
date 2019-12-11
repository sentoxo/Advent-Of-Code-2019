import sys

def drawFrom2dim(tab = []):
    for line in tab:
        for char in line:
            if char:
                sys.stdout.write('##')
            else:
                sys.stdout.write('  ')
        sys.stdout.write('\n')


def drawFrom1dim(tab = [], lengthOfLine = 0):
    i = 1

    for o in range(lengthOfLine*2):
        sys.stdout.write('-')
    sys.stdout.write('+\n')

    for char in tab:
        if char:
            sys.stdout.write('##')
        else:
            sys.stdout.write('  ')
        if i==lengthOfLine:
            sys.stdout.write('|\n')
            i = 0
        i += 1

    for o in range(lengthOfLine*2):
        sys.stdout.write('-')
    sys.stdout.write('+\n')
