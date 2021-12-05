from Submarine import BasicSubmarine, SubmarineCommandProcessor, AimingSubmarine
from urllib.request import urlopen


def to_tuple(line):
    array = line.split(" ")
    return (array[0], int(array[1]))

data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/day2/input.txt').read().decode().split('\n')[:-1]
data = list(map(to_tuple,data))

basic_submarine = BasicSubmarine()
basic_scp = SubmarineCommandProcessor(basic_submarine)

aiming_submarine = AimingSubmarine()
aiming_scp = SubmarineCommandProcessor(aiming_submarine)

for command, value in data:
    basic_scp.process(command, value)
    aiming_scp.process(command,value)

basic_position = basic_submarine.position
print(basic_position.horizontal * basic_position.depth)

aiming_position = aiming_submarine.position
print(aiming_position.horizontal * aiming_position.depth)