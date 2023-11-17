from collections import defaultdict


def build_graph(filename):
    #26, 29
    # Create an empty graph
    pacman_map = defaultdict(list)

    # Define the dimensions of the grid
    columns, rows = 26, 29

    coords = set()

    with open(filename) as f:
        for line in f:
            pos = tuple(int(x) for x in line.strip().split(','))
            coords.add(pos)

    # Create nodes and connections
    for i in range(columns):
        for j in range(rows):
            node = (i, j)
            if node in coords:

                neighbors = []

                # Check and add connections to neighboring nodes
                for diff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    pos = addition(node, diff)
                    x, y = pos

                    # if 0 <= x < rows and 0 <= y <= columns:
                    if pos in coords:
                        neighbors.append((x, y))


                pacman_map[node] = neighbors

    pacman_map[(0, 13)].append((-1, 13))
    pacman_map[(25, 13)].append((26, 13))
    pacman_map[(-1, 13)].append((-2, 13))
    pacman_map[(26, 13)].append((27, 13))
    pacman_map[(27, 13)].append((-2, 13))
    pacman_map[(-2, 13)].append((27, 13))

    return pacman_map

def movement_graph(G, pixel_separation, columns):
    G2 = defaultdict(list)
    for node, adjacent_nodes in G.items():
        for adj_node in adjacent_nodes:
            new_node = (node[0]*pixel_separation, node[1]*pixel_separation)
            diff = difference(adj_node, node)
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                continue
            
            for _ in range(pixel_separation):
                next_node = addition(new_node, diff)

                # connect passageway
                if next_node[0] <= -pixel_separation*2:
                    next_node = ((columns + 2)*pixel_separation, next_node[1])
                elif next_node[0] >= (columns + 2)*pixel_separation:
                    next_node = (-pixel_separation*2, next_node[1])
                
                G2[new_node].append(next_node)
                new_node = next_node
    
    return G2


def difference(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def addition(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

# print(build_graph("Assets/pacman_pellets.txt"))


# graph = {(0, 0): [(0, 1), (1, 0)], (1, 0): [(0, 0), (1, 1), (2, 0)], (0, 1): [(0, 0), (1, 1)], (1, 1): [(1, 0), (0, 1), (2, 1)], (2, 0): [(1, 0), (2, 1)], (2, 1): [(1, 1), (2, 0)]}

# print(movement_graph(graph, 8, 3))

