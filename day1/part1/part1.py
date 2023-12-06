def func1(fname ='input.txt' ):
    ans = 0
    with open(fname) as f:
        for line in f:
            first_num,second_num=-1,-1
            for i in line:
                if i.isnumeric():
                    if first_num==-1:
                        first_num = int(i)
                    else:
                        second_num= int(i)
                if first_num != -1 and second_num==-1:
                    second_num = first_num
            # # assert first_num==-1
            print(first_num,second_num)
            # assert second_num ==-1
            line_number = first_num*10+second_num
            ans +=line_number

        return ans    
print(func1())