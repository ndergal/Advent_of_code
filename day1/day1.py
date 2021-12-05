from urllib.request import urlopen
data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/day1/input.txt').read().decode().split('\n')[:-1]

data = [int(x) for x in data]
func = lambda steps: sum([x < y for x, y in zip(data[:-steps], data[steps:])])
print(func(1),func(3))
