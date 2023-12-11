def q1(fname="input.txt"):
    map = []
    x0, y0 = 0, 0
    with open(fname) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            map.append(line)
            if "S" in line:
                x0 = line.index("S")
                y0 = idx

    print(x0, y0)
    print(map)
    X = len(map[0])
    Y = len(map)
    max_steps = 0

    def get_choices(
        x,
        y,
    ):
        choices = []
        # up, down, left, right
        print("current:", (x, y))
        if map[y][x] == "S":
            if y + 1 < Y and map[y + 1][x] not in ".7F":
                choices.append((x, y + 1))
            if y - 1 >= 0 and map[y - 1][x] not in ".LJ":
                choices.append((x, y - 1))
            if x + 1 < X and map[y][x + 1] not in ".|L":
                choices.append((x + 1, y))
            if x - 1 >= 0 and map[y][x - 1] not in ".|-":
                choices.append((x - 1, y))
            return [c for c in choices if c not in visited]

        if map[y][x] == "|":
            choices.append((x, y - 1))
            choices.append((x, y + 1))
        elif map[y][x] == "-":
            choices.append((x - 1, y))
            choices.append((x + 1, y))
        elif map[y][x] == "L":
            choices.append((x + 1, y))
            choices.append((x, y - 1))
        elif map[y][x] == "J":
            choices.append((x - 1, y))
            choices.append((x, y - 1))
        elif map[y][x] == "7":
            choices.append((x - 1, y))
            choices.append((x, y + 1))
        elif map[y][x] == "F":
            choices.append((x + 1, y))
            choices.append((x, y + 1))

        return [
            c
            for c in choices
            if (c not in visited) and (0 <= c[0] < X and 0 <= c[1] < Y)
        ]

    visited = set()
    next_step = []

    def find_loop(x, y, begin=False, step=0):
        nonlocal max_steps
        print("find_loop", x, y, step)
        if (x, y) in visited:
            return step + 1
        visited.add((x, y))
        choices = get_choices(x, y)
        print("choices", choices)

        # assert len(choices) > 0, f"No choices in {x}, {y}"
        max_steps = max(max_steps, step + 1)
        if len(choices) == 0:
            return
        x, y = choices[0]
        next_step.append((x, y))
        return

    find_loop(x0, y0, begin=True)
    while next_step:
        x, y = next_step.pop()
        find_loop(x, y, step=max_steps)
    return max_steps


print(q1("test.txt") // 2)
print(q1("input.txt") // 2)
print(q1("message.txt") // 2)
