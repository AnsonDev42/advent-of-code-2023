def part1(fname="input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        cmd = lines[0].strip()
        # print(f'---{cmd}----')
        source_to_linenum = {}
        source_to_targets = {}
        lines = lines[2:]
        for i, choice in enumerate(lines):
            # print(choice)
            source = choice.split(" = ")[0].strip()
            target = choice.split("= (")[1].strip()
            [t1, t2] = target.split(", ")
            t2 = t2.strip(")")
            t1 = t1.strip()
            # print(f'--{source}--{t1}--{t2}--')
            source_to_linenum[source] = i
            source_to_targets[source] = (t1, t2)

    assert "ZZZ" in source_to_targets
    step = 0
    cmd = cmd.replace("L", "0").replace("R", "1")
    print("start hardcode ", "Aaa")
    now = "AAA"
    while True:
        for c in cmd:
            # lr = 0 if c == 'L' else 1
            lr = int(c)
            # print('from' , now, 'to', source_to_targets[now][lr], 'by', c )
            step += 1
            now = source_to_targets[now][lr]
            if now == "ZZZ":
                return step
        print("loop", step // len(cmd))


print(part1("test.txt"))
print(part1("input.txt"))
