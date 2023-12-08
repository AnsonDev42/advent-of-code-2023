import math


def part2(fname="input.txt"):
    with open(fname, "r") as f:
        lines = f.readlines()
        cmd = lines[0].strip()
        source_to_targets = {}
        lines = lines[2:]
        for choice in lines:
            # print(choice)
            source = choice.split(" = ")[0].strip()
            target = choice.split("= (")[1].strip()
            [t1, t2] = target.split(", ")
            t2 = t2.strip(")")
            t1 = t1.strip()
            source_to_targets[source] = (t1, t2)

    step = 0
    cmd = cmd.replace("L", "0").replace("R", "1")
    starts = [x for x in source_to_targets if x[-1] == "A"]
    been_Z = [[] for _ in range(len(starts))]
    LCMs = [[] for _ in range(len(starts))]
    while True:
        for c in cmd:
            lr = int(c)
            # print('from' , now, 'to', source_to_targets[now][lr], 'by', c )
            step += 1
            starts = [source_to_targets[s][lr] for s in starts]

            for idx, x in enumerate(starts):
                # print(x, step) if x[-1] == 'Z' else None
                if x[-1] == "Z":
                    been_Z[idx].append(step)
                    if len(been_Z[idx]) == 2:
                        LCMs[idx] = been_Z[idx][1] - been_Z[idx][0]
                        if all([lcm for lcm in LCMs]):
                            return LCMs


# print(part2('test2.txt'))

print(math.lcm(*part2("input.txt")))
