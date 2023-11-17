

row, columns = 26, 29

def build_pellet_coords():
    pellet_coords = set()
    for i in range(26):
        pellet_coords.add((5, i))
        pellet_coords.add((20, i))

    for i in range(8):
        pellet_coords.add((0, i))
        pellet_coords.add((25, i))
    for i in range(19, 23):
        pellet_coords.add((0, i))
        pellet_coords.add((25, i))
    for i in range(25, 29):
        pellet_coords.add((0, i))
        pellet_coords.add((25, i))
    for i in range(1,25):
        pellet_coords.add((i, 28))
    for i in range(26):
        pellet_coords.add((i, 4))
        pellet_coords.add((i, 0))
    for i in range(1, 4):
        pellet_coords.add((11, i))
        pellet_coords.add((14, i))
    for i in range(25):
        pellet_coords.add((i, 19))
        pellet_coords.add((i, 7))
        pellet_coords.add((i, 25))
    for i in range(6, 21):
        pellet_coords.add((i, 22))
    for i in range(5,7):
        pellet_coords.add((8, i))
        pellet_coords.add((17, i))
    for i in range(3):
        pellet_coords.add((2,22+i))
        pellet_coords.add((23,22+i))
        pellet_coords.add((17, 22+i))
        pellet_coords.add((8, 22+i))
        pellet_coords.add((11, 19+i))
        pellet_coords.add((14, 19+i))
        pellet_coords.add((11, 25+i))
        pellet_coords.add((14, 25+i))


    pellet_coords.add((1,22))
    pellet_coords.add((24,22))
    pellet_coords.remove((12, 25))
    pellet_coords.remove((13, 25))
    pellet_coords.remove((12, 22))
    pellet_coords.remove((13, 22))
    pellet_coords.remove((6, 25))
    pellet_coords.remove((7, 25))
    pellet_coords.remove((18, 25))
    pellet_coords.remove((19, 25))
    pellet_coords.remove((6, 7))
    pellet_coords.remove((7, 7))
    pellet_coords.remove((18, 7))
    pellet_coords.remove((19, 7))
    pellet_coords.remove((12, 19))
    pellet_coords.remove((13, 19))
    pellet_coords.remove((12, 7))
    pellet_coords.remove((13, 7))
    pellet_coords.remove((12,0))
    pellet_coords.remove((13,0))
    
    pellet_list = list(pellet_coords)
    pellet_list.sort()
    lines = [str(pos).strip('()') for pos in pellet_list]
    with open("Assets/pacman_pellets.txt", "w") as f:
        f.write('\n'.join(lines))


def build_all_coords():

    coords = set()
    for i in range(26):
        coords.add((5, i))
        coords.add((20, i))

    for i in range(8):
        coords.add((0, i))
        coords.add((25, i))
    for i in range(19, 23):
        coords.add((0, i))
        coords.add((25, i))
    for i in range(25, 29):
        coords.add((0, i))
        coords.add((25, i))
    for i in range(1,25):
        coords.add((i, 28))
    for i in range(26):
        coords.add((i, 4))
        coords.add((i, 0))
    for i in range(1, 4):
        coords.add((11, i))
        coords.add((14, i))
    for i in range(25):
        coords.add((i, 19))
        coords.add((i, 7))
        coords.add((i, 25))
    for i in range(6, 21):
        coords.add((i, 22))
    for i in range(5,7):
        coords.add((8, i))
        coords.add((17, i))
    for i in range(3):
        coords.add((2,22+i))
        coords.add((23,22+i))
        coords.add((17, 22+i))
        coords.add((8, 22+i))
        coords.add((11, 19+i))
        coords.add((14, 19+i))
        coords.add((11, 25+i))
        coords.add((14, 25+i))
        coords.add((8, 10+i))
        coords.add((8, 14+i))
        coords.add((8, 17+i))
        coords.add((17, 10+i))
        coords.add((17, 14+i))
        coords.add((17, 17+i))
        coords.add((11, 7+i))
        coords.add((14, 7+i))

    for i in range(26):
        coords.add((i, 13))
    for i in range(9, 17):
        coords.remove((i, 13))
        coords.add((i, 10))
        coords.add((i, 16))

    coords.add((1,22))
    coords.add((24,22))
    
    coords.remove((12, 25))
    coords.remove((13, 25))
    coords.remove((6, 25))
    coords.remove((7, 25))
    coords.remove((18, 25))
    coords.remove((19, 25))
    coords.remove((6, 7))
    coords.remove((7, 7))
    coords.remove((18, 7))
    coords.remove((19, 7))
    coords.remove((12, 19))
    coords.remove((13, 19))
    coords.remove((12, 7))
    coords.remove((13, 7))
    coords.remove((12,0))
    coords.remove((13,0))

    coord_list = list(coords)
    coord_list.sort()
    lines = [str(pos).strip('()') for pos in coord_list]
    with open("Assets/pacman_positions.txt", "w") as f:
        f.write('\n'.join(lines))


print(build_all_coords())
build_pellet_coords()

