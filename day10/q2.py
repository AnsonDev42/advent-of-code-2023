"""
q2 tbd: expand the map (both width and height by 2)
and build pipes to prevent flooding into the new space
    
"""


def q2(fname="input.txt"):
    map = []
    x0, y0 = 0, 0
    with open(fname) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            # add squzzable space to the map
            new_l = []
            for i in range(len(line)):
                new_l.append(line[i])
                new_l.append(" ")
            map.append(new_l)
            if "S" in line:
                x0 = line.index("S")
                y0 = idx

    # print(x0, y0)
    # print(map)
    X = len(map[0])
    Y = len(map)
    check_outside = set()
    visited = set()
    # initialize check_outside
    for x in (0, X - 1):
        for y in range(Y):
            if map[y][x] == ".":
                check_outside.add((x, y))
                # visited.add((x, y))
                # map[y][x] = "O"
    for y in (0, Y - 1):
        for x in range(X):
            if map[y][x] == ".":
                check_outside.add((x, y))
                # visited.add((x, y))
                # map[y][x] = "O"
    print(f"edge outside O num {len(check_outside)}")

    def find_outside_neib(x, y):
        nonlocal check_outside
        if y + 1 < Y and map[y + 1][x] == "." and (x, y + 1) not in visited:
            check_outside.append((x, y + 1))
        if y - 1 >= 0 and map[y - 1][x] == "." and (x, y - 1) not in visited:
            check_outside.append((x, y - 1))
        if x + 1 < X and map[y][x + 1] == "." and (x + 1, y) not in visited:
            check_outside.append((x + 1, y))
        if x - 1 >= 0 and map[y][x - 1] == "." and (x - 1, y) not in visited:
            check_outside.append((x - 1, y))

    check_outside = list(check_outside)
    while check_outside:
        x, y = check_outside.pop()
        if (x, y) in visited:
            continue
        find_outside_neib(x, y)
        visited.add((x, y))
    print(X, Y)
    return len(visited)


print("test2", q2("test2.txt"))
# print(q2("input.txt"))
map = []
x0, y0 = 0, 0
with open("test2.txt") as f:
    for idx, line in enumerate(f):
        line = line.strip()
        map.append(line)
        if "S" in line:
            x0 = line.index("S")
            y0 = idx


def print_map(map):
    for line in map:
        print(line)


c = 0
for line in map:
    c += line.count("O")
print("num of O in map: ", c)
