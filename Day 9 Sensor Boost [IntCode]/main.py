'''
https://adventofcode.com/2019/day/9
Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning opcodes when run in test mode; 
it should only output a single value, the BOOST keycode. What BOOST keycode does it produce?
'''

from computer import IntCodeComputer

cpu = IntCodeComputer(input=(2,))
cpu.readCodeFromFile('day09/input.txt')

cpu.run()

print(f'{cpu.output=}')