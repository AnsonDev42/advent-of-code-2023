def q1(fname="input.txt"):
    data = []
    with open(fname) as f:
        for line in f:
            l = line.strip().split(" ")
            data.append([int(x) for x in l])

    def predict(history):
        """
        history: list of integers
        """
        if len(history) == 0:
            return 0
        diff = 0
        diff_list = []
        for i in range(1, len(history)):
            diff = history[i] - history[i - 1]
            diff_list.append(diff)

        return history[-1] + predict(diff_list)

    ans = 0
    for history in data:
        ans += predict(history)
    return ans


print(q1("test.txt"))
print(q1("input.txt"))
