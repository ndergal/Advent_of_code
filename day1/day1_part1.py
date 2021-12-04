from urllib.request import urlopen
data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/input.txt').read().decode().split('\n')[:-1]

data = [int(x) for x in data]
print(sum([1 for x, y in zip(data, data[1:]) if y -x > 0]))
