from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/day3/input.txt').read().decode().split('\n')[:-1]

gamma = "".join(
    "10" if bits.count("1") > len(bits) / 2 else "01"
    for bits in zip(*data)
)
print(int(gamma[::2], 2) * int(gamma[1::2], 2))

def func(data,cmp):
    for i in range(len(data[0])):
        _01 = { "0" : [], "1" : []}
        for line in data:
            _01[line[i]].append(line)
        if len(data := _01[
                "1" if cmp(len(_01["1"]), len(_01["0"])) else "0"
            ]) == 1:
                return int(data[0], 2)

    print(data)

print(func(data[:],int.__ge__) * func(data[:],int.__lt__))



    