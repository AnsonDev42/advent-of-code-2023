from collections import defaultdict


def func1(fname = 'input.txt'):
    ans = 0
    # convert the txt into a list of strings
    list_of_strings = []
    # any symbols that is not dot 
    
    with open(fname) as f:
        for linef in f:
            list_of_strings.append(linef.strip())
    for nline in range(len(list_of_strings)):
        #get number 
        line = list_of_strings[nline]
        curr_num_str = ''      
        valid = False
        for i in range(0,len(line)):
            if line[i].isdigit():
                curr_num_str+=(line[i])
                if not valid:
                    neightbors = find_neighbors((nline,i))
                    for neightbor in neightbors:
                        if neightbor[0] >= 0 and neightbor[0] < len(list_of_strings) and neightbor[1] >= 0 and neightbor[1] < len(line):
                            if list_of_strings[neightbor[0]][neightbor[1]] != '.' and not list_of_strings[neightbor[0]][neightbor[1]].isdigit():
                                valid = True
                                break
            else:
                if curr_num_str.isdigit() and valid:
                    # print(curr_num)
                    ans += int(curr_num_str)
                curr_num_str = ''
                valid = False
            # resolve the last number in a line
            if i == len(line)-1 and curr_num_str.isdigit() and valid:
                    # print(curr_num)
                ans += int(curr_num_str)
                curr_num_str = ''
                valid = False
         
    return ans
    
def find_neighbors(node):
    x = node[0]
    y = node[1]
    neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1), 
                (x+1,y+1), (x+1,y-1), (x-1,y+1), (x-1,y-1)]
    return neighbors
def func2(fname = 'input.txt'):
    ans = 0
    # convert the txt into a list of strings
    list_of_strings = []
    # any symbols that is not dot 
    
    with open(fname) as f:
        for linef in f:
            list_of_strings.append(linef.strip())
    gear_set = defaultdict(list)
    for nline in range(len(list_of_strings)):
        #get number 
        line = list_of_strings[nline]
        curr_num_str = ''      
        curr_gears = set()
        valid = False
        for i in range(0,len(line)):
            if line[i].isdigit():
                curr_num_str+=(line[i])
                if not valid:
                    neightbors = find_neighbors((nline,i))
                    for neightbor in neightbors:
                        if neightbor[0] >= 0 and neightbor[0] < len(list_of_strings) and neightbor[1] >= 0 and neightbor[1] < len(line):
                            if list_of_strings[neightbor[0]][neightbor[1]] == '*':
                                valid = True
                                curr_gears.add((neightbor[0],neightbor[1]))
                                
            else:
                if curr_num_str.isdigit() and valid:
                    # print(curr_num)
                    # ans += int(curr_num_str)
                    for gear in curr_gears:
                        gear_set[gear].append(int(curr_num_str))
                curr_num_str = ''
                valid = False
                curr_gears = set()
            # resolve the last number in a line
            if i == len(line)-1 and curr_num_str.isdigit() and valid:
                    # print(curr_num)
                # ans += int(curr_num_str)
                for gear in curr_gears:
                    gear_set[gear].append(int(curr_num_str))
                curr_num_str = ''
                valid = False
                curr_gears = set()
    for gear in gear_set:
        if len(gear_set[gear]) == 2:
            print(gear_set[gear], gear)
            tmp =  gear_set[gear].pop() * gear_set[gear].pop()
            ans += tmp
    return ans
# print(func1('test.txt'))
# print(func1())

print(func2('test.txt'))
print(func2())