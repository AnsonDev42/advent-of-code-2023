'''
part two  day1

'''
def func1(fname ='input.txt' ):
    ans = 0
    with open(fname) as f:
        for line in f:
            first_num,second_num=-1,-1
            for idx,i  in enumerate(line):
                if first_num==-1:
                    if i.isnumeric():
                        first_num = int(i)
                    else:
                        n =check_single(idx,line,len(line)) 
                        first_num= n if n!=-1 else first_num
                else:
                    if i.isnumeric():
                        second_num = int(i)
                    else:
                        n =check_single(idx,line,len(line)) 
                        second_num= n if n!=-1 else second_num
            if first_num != -1 and second_num==-1:
                second_num = first_num
            # # assert first_num==-1
            print(first_num,second_num)
            # assert second_num ==-1
            line_number = first_num*10+second_num
            ans +=line_number

        return ans    
    


# create a dic that has starting point and their lengh

d = {'o':['one'],'t':['two','three'],'f':['four','five'],'s':['six','seven'],'e':['eight'],'n':['nine']}
w2n = {'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8, 'nine': 9}
def check_single(idx,line,ll):
    initial=line[idx] # inital for a fake number .e.g.   o -> 'one'
    if initial in d:
        for fake_num  in d[initial]:
            if idx+len(fake_num)< ll and line[idx:idx+len(fake_num)] == fake_num: 
                return w2n[fake_num]
    return -1
        

print(func1('input.txt'))