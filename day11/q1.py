def q1(fname="input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(lines)
    X = len(lines[0])
    Y = len(lines)
    # check any col is empty
    empty_col = []
    for x in range(X):
        empty = True
        for y in range(Y):
            if lines[y][x] != ".":
                empty = False
                break
        if empty:
            empty_col.append(x)
    print(empty_col)

    empty_row = []
    for y in range(Y):
        empty = True
        if lines[y] != "." * X:
            empty = False
        if empty:
            empty_row.append(y)

    def find_origin_galaxies(map):
        """
        Find the origin of the galaxies and return a list of the origin
        """
        # print(map)
        # print(x, y)
        # print(map[y][x])
        galaxies = []
        for y in range(Y):
            for x in range(X):
                if map[y][x] == "#":
                    galaxies.append((x, y))
        return galaxies

    print(empty_row)
    map = lines
    expanded_galaxies = []

    def expand_map(map):
        """
        Expand map according empty col and row,
        and return new map
        """
        original_galaxies = find_origin_galaxies(map)
        for x0, y0 in original_galaxies:
            x = x0 + len([d for d in empty_col if d < x0])
            y = y0 + len([d for d in empty_row if d < y0])
            print("map from {} to {}".format((x0, y0), (x, y)))
            expanded_galaxies.append((x, y))
        new_map = [["."] * (X + len(empty_col)) for _ in range(Y + len(empty_row))]
        for x, y in expanded_galaxies:
            print("new xy", x, y)
            new_map[y][x] = "#"
        return new_map

    new_map = expand_map(map)
    print(new_map)
    # with open("test_1.txt", "r") as f:
    #     check = f.readlines()
    # check = [line.strip() for line in check]
    # for line in zip(check, new_map):
    #     assert line[0] == "".join(line[1])

    total = 0
    for i in range(len(expanded_galaxies)):
        for j in range(i + 1, len(expanded_galaxies)):
            x1, y1 = expanded_galaxies[i]
            x2, y2 = expanded_galaxies[j]
            total += abs(x1 - x2) + abs(y1 - y2)
    return total


print(q1("test.txt"))
print(q1("input.txt"))
