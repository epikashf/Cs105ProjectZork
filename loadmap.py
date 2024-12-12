def loadMap(filename: str) -> list:

    with open(filename, 'r') as file:
        lines = file.readlines()


    mp = []
    for line in range(1, len(lines)):
        lines[line] = str(lines[line]).strip("\n")
        mp.append(lines[line])
    mapdict = {}
    for y, row in enumerate(mp):
        for x, value in enumerate(row):
            mapdict[(x + 1, y + 1)] = int(value)
    return mapdict


map_1 = loadMap('map1.txt')
map_2 = loadMap("map2.txt")
map_3 = loadMap("map3.txt")




