


loadmap = [
    "00001000000",
    "00001100000",
    "00000100000",
    "00000100000",
]


coordinates = {}

for y, row in enumerate(loadmap):
    for x, value in enumerate(row):
        coordinates[(x, y)] = int(value)


print(coordinates)
