from urllib.request import urlopen
data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/input.txt').read().decode().split('\n')[:-1]
data = [int(x) for x in data]

t = 0
for i in range(1, len(data)-2): 
    t += sum(data[i : i+3]) > sum(data[i-1 : i+2])
print(t)
