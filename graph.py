def build_graph():
    #26, 29
    # Create an empty graph
    pacman_map = {}

    # Define the dimensions of the grid
    rows, columns = 26, 29

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


    # Create nodes and connections
    for i in range(rows):
        for j in range(columns):
            node = (i, j)
            if node in pellet_coords:

                neighbors = []

                # Check and add connections to neighboring nodes

                if i > 0:
                    neighbors.append((i - 1, j))  # Connect to the node above
                if i < rows - 1:
                    neighbors.append((i + 1, j))  # Connect to the node below
                if j > 0:
                    neighbors.append((i, j - 1))  # Connect to the node on the left
                if j < columns - 1:
                    neighbors.append((i, j + 1))  # Connect to the node on the right

                pacman_map[node] = neighbors

    # Visualize a small portion of the graph

    return pacman_map



print(build_graph())
