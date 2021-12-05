from urllib.request import urlopen

data = urlopen('https://raw.githubusercontent.com/ndergal/Advent_of_code/master/day3/input.txt').read().decode().split('\n')[:-1]

gamma = "".join(
    "10" if bits.count("1") > len(bits) / 2 else "01"
    for bits in zip(*data)
)
print(int(gamma[::2], 2) * int(gamma[1::2], 2))