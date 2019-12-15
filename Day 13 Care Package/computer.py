import queue

class IntCodeException(Exception):
    pass

class HALT(IntCodeException):
    ''' Exception raised by halt opcode in computer code '''
    def __init__(self, arg):
        self.args = arg

class UnknownOpcode(IntCodeException):
    ''' Exception raised by unknown opcode in computer code '''
    def __init__(self, arg):
        self.args = arg

class IntCodeComputer():

    def __init__(self, ram = [], input = ()):
        self.ram = ram
        self.IP = 0
        self.IC = 0
        self.inputQ = queue.Queue()
        self.output = []
        self.state = 'init'
        self.RelativeBase = 0
        for obj in input:
            self.inputQ.put(obj)
    
    def reset(self):
        ''' reset counters, output '''
        self.IP = 0
        self.IC = 0
        self.InputCounter = 0
        self.state = 'reset'
        self.output = []
        self.RelativeBase = 0
        
    def run(self):
        ''' Execute code from memory. Return: Output '''
        self.state = 'running'
        while self.ram:
            if self.ram[self.IP] == 99:
                self.state = 'halt'
                #self.IP += 1
                return 0
            
            DE = self.ram[self.IP] % 100
            C = int(self.ram[self.IP] % 1000 / 100)      #first parameter
            B = int(self.ram[self.IP] % 10000 / 1000)
            A = int(self.ram[self.IP] % 100000 / 10000)
            #if A:
            #    raise IntCodeException('third parameter is not handle')
                
            if C == 0:
                one = self.ram[self.ram[self.IP+1]]
            elif C == 1:
                one = self.ram[self.IP+1]
            elif C == 2:
                one = self.ram[self.ram[self.IP+1] + self.RelativeBase]

            if B == 0:
                two = self.ram[self.ram[self.IP+2]]
            elif B == 1:
                two = self.ram[self.IP+2]
            elif B == 2:
                two = self.ram[self.ram[self.IP+2] + self.RelativeBase]

                
            if DE == 1:     #Add
                if A == 2:
                    self.ram[self.ram[self.IP+3] + self.RelativeBase] = one + two
                elif A ==0:
                    self.ram[self.ram[self.IP+3]] = one + two
                self.IP += 4
            elif DE == 2:   #Multiply
                if A == 2:
                    self.ram[self.ram[self.IP+3] + self.RelativeBase] = one * two
                elif A ==0:
                    self.ram[self.ram[self.IP+3]] = one * two
                self.IP += 4
            elif DE == 3:   #Input
                if self.inputQ.empty():
                    raise IntCodeException("Input empty")
                if C==1:
                    self.ram[self.IP+1] = self.inputQ.get()
                elif C==0:
                    self.ram[self.ram[self.IP+1]] = self.inputQ.get()
                elif C==2:
                    self.ram[self.ram[self.IP+1] + self.RelativeBase] = self.inputQ.get()
                self.IP += 2
            elif DE == 4:   #Output
                self.IP += 2
                #self.output.append( one )
                return one
            elif DE == 5:   #jump-if-true
                if one:
                    self.IP = two
                else:
                    self.IP += 3
            elif DE == 6:   #jump-if-false
                if not one:
                    self.IP = two
                else:
                    self.IP += 3
            elif DE == 7:   #less than
                result = 1 if one < two else 0
                if A == 2:
                    self.ram[self.ram[self.IP+3] + self.RelativeBase] = result
                elif A == 0:
                    self.ram[self.ram[self.IP+3]] = result
                self.IP += 4
            elif DE == 8:   #equals
                result = 1 if one == two else 0
                if A == 2:
                    self.ram[self.ram[self.IP+3] + self.RelativeBase] = result
                elif A == 0:
                    self.ram[self.ram[self.IP+3]] = result
                self.IP += 4
            elif DE == 9:   #adjusts the relative base
                self.RelativeBase += one
                self.IP += 2
            else:
                raise UnknownOpcode(f'opcode:{DE} IP:{self.IP}')
            self.IC += 1
    

    def readCodeFromFile(self, filename):
        ''' Read intcode from given file to computer ram memory. 
            Return: sum of intcodes'''
        file = open(file=filename, mode='r')
        code = file.readline().split(',')
        self.ram = list(map(int, code))
        for i in range(100000):
            self.ram.append(0)
        return len(code)
 
