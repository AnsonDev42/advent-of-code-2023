def q2(fname="input.txt", c=9):
    with open(fname, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
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

    map = lines
    expanded_galaxies = []

    def get_expanded_galaxies(c=9):
        """
        Expand map according empty col and row,
        and return new map
        """
        nonlocal expanded_galaxies, original_galaxies
        for x0, y0 in original_galaxies:
            x = x0 + (c - 1) * len([d for d in empty_col if d < x0])
            y = y0 + (c - 1) * len([d for d in empty_row if d < y0])
            # print("map from {} to {}".format((x0, y0), (x, y)))
            expanded_galaxies.append((x, y))

        return

    original_galaxies = find_origin_galaxies(map)
    get_expanded_galaxies(c)
    total = 0
    for i in range(len(expanded_galaxies)):
        for j in range(i + 1, len(expanded_galaxies)):
            x1, y1 = expanded_galaxies[i]
            x2, y2 = expanded_galaxies[j]
            total += abs(x2 - x1) + abs(y2 - y1)

    return total


print(q2("test.txt", c=100))
print(q2("input.txt", c=1000000))
