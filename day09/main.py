from computer import IntCodeComputer

cpu = IntCodeComputer(input=(2,))
cpu.readCodeFromFile('day09/input.txt')

cpu.run()

print(f'{cpu.output=}')