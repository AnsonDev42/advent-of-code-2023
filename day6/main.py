"""
Time:      7  15   30 (lasts     milli-sec
Distance:  9  40  200 (recorded / milli-meter

"""

def func1(fname='test.txt'):
    ans = 1
    array = [[],[]]
    with open(fname) as f:
        for  idx,line, in enumerate(f):
            array[idx]=[int(n) for n in line.strip().split(':')[1].strip().split()]
    [time, distance]=array 
    def cal_range(t,d): # get range length
        r =0 
        begin,end = 0,0
        for hold in range(1,t):
            if -hold**2+t*hold > d:
                if begin == 0:
                    begin = hold
                r+=1
            end = hold
        # print(begin,end)
        return r
    for i in range(len(time)):
        # print(time[i],distance[i])
        # print(cal_range(time[i],distance[i]))
        ans*=cal_range(time[i],distance[i])
    
    return ans


# assert func1('test.txt') == 288
# print(func1('input.txt'))

"""
Time:      71530
Distance:  940200
"""

def func2(fname='test.txt'):
    ans = 1
    array = [[],[]]
    with open(fname) as f:
        for  idx,line, in enumerate(f):
            array[idx]=[int(line.strip().split(':')[1].replace(' ','').strip())]
    [time, distance]=array 
    def cal_range(t,d): # get range length
        r =0 
        begin,end = 0,0
        for hold in range(1,t):
            if -hold**2+t*hold > d:
                if begin == 0:
                    begin = hold
                r+=1
            end = hold
        # print(begin,end)
        return r
    for i in range(len(time)):
        print('time and range',time[i],distance[i])
        # print(cal_range(time[i],distance[i]))
        ans*=cal_range(time[i],distance[i])
    
    return ans

assert func2('test.txt') == 71503
print(func2('input.txt'))