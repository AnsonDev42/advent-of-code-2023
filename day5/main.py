from collections import defaultdict


def func1(fname ='test.py'):
    ans = 0
    with open(fname) as f:
        for idx,linef in enumerate(f):
            line = linef.strip()
            [header_part1, part2]  = line.split('| ')
            part1 = header_part1.split(':')[1]

            left = set()
            right = set()
            for n in part1.split():
                if n.isdigit():
                    left.add(int(n))
            for n in part2.split():
                if n.isdigit():
                    right.add(int(n))
            # part1 e.g. ' 41 48 83 86 17 ' get the numbers 
            ans +=score(len(left.intersection(right)))
    return ans

def score(n):
    if n == 0:
        return 0
    return 2**(n-1)
print(func1('test.txt'))
print(func1('input.txt'))

def func2(fname ='test.py'):
    ans = 0
    lines = []
    with open(fname) as f:
        for idx,linef in enumerate(f):
            lines.append(linef.strip())
    card_to_point = [0]*(len(lines))
    # length of card_number is the number of cards
    card_number = [0]*(len(lines))

    for idx, line in  enumerate(lines):
        [header_part1, part2]  = line.split('| ')
        part1 = header_part1.split(':')[1]
        left = set()
        right = set()
        for n in part1.split():
            if n.isdigit():
                left.add(int(n))
        for n in part2.split():
            if n.isdigit():
                right.add(int(n))
        # part1 e.g. ' 41 48 83 86 17 ' get the numbers 
        card_to_point[idx] = len(left.intersection(right))
        card_number[idx] +=1

    print(card_to_point)
    print(card_number)
    for i in range(len(lines)): # iterate all no.cards
        if card_number[i] > 0: 
            # ans += card_number[i]
            print(i, card_to_point[i], card_number[i])
            # if i + card_to_point[i]+1 < len(lines):
            for j in range(i+1,i+1+card_to_point[i]):
                card_number[j] += card_number[i] 


    return sum(card_number)
print(func2('test.txt'))
print(func2('input.txt'))