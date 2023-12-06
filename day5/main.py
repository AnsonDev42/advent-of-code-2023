def func1(fname='test.txt'):
    fourdarry = []
    with open(fname) as f:
        iterf = iter(f)
        seeds = next(iterf) 
        seeds = [int(n) for n in seeds.strip().split(' ')[1:]]
        print(seeds)
        nmap = -1
        for line in f:
            if line == '\n':
                fourdarry.append([])
                nmap += 1
            else:
                fourdarry[nmap].append(line.strip().split())
                    
                
    def seed_to_location(seed):
        print('seed is :',seed)
        for si,step in enumerate(fourdarry):
            for ci, choice in enumerate(fourdarry[si][1:]):
                # print(f'choice:{choice}')
                [d, s, r] = [int(n) for n in choice]
                if s<= seed< s+r:
                    seed+= (d-s)
                    break
        return seed
    
    ans = 0
    min_loc = float('inf')
    for seed in seeds:
        tmp = seed_to_location(seed)
        if tmp < min_loc:
            min_loc=tmp
            ans = seed
        
        
    return min_loc

        


# print(func1('input.txt'))
        
def func2(fname='test.txt'):
    fourdarry = []
    with open(fname) as f:
        iterf = iter(f)
        seeds = next(iterf) 
        seeds = [int(n) for n in seeds.strip().split(' ')[1:]]
        seeds_pair = [seeds[npair:npair+2] for npair in range(0,len(seeds),2)]
        seeds_pair =  [(x, x+y) for (x,y) in seeds_pair] # convert to range
        seeds = seeds_pair
        print(seeds)
        nmap = -1
        for line in f:
            if line == '\n':
                fourdarry.append([])
                nmap += 1
            else:
                fourdarry[nmap].append(line.strip().split())
                    
                

    
    def seed_range_to_location_min(seed_ranges):
        # seed_range is a [] contains range e.g. [(1,3),(5,8)]
        curr_remain= seed_ranges.copy()

        for si,step in enumerate(fourdarry):
            # hit = 0
            next_step = set()
            for ci, choice in enumerate(step[1:]):
                [d, s, r] = [int(n) for n in choice]
                print(f'choice {ci}', choice)
                offset = d-s
                seed_ranges = curr_remain.copy()
                for  seed_minmax in seed_ranges:
                    (seed_min, seed_max)  = seed_minmax
                    curr_remain.remove(seed_minmax)
                    # intersection:
                    if max(seed_min,s) < min(seed_max,s+r) and seed_max > s:
                        next_step.add((max(seed_min,s)+offset,min(seed_max,s+r)+offset))
                        print('added intersect', (max(seed_min,s)+offset,min(seed_max,s+r)+offset))
                    # left:
                    if seed_min<s and seed_min <min(s, seed_max): 
                        curr_remain.add((seed_min, min(s, seed_max)))
                        print('added left',(seed_min, min(s, seed_max)))
                    # right 
                    if seed_max >=s+r and max(s+r,seed_min)< seed_max:
                        curr_remain.add((max(s+r,seed_min), seed_max))
                        print('added right',(max(s+r,seed_min), seed_max))
            curr_remain =curr_remain.union(next_step)
            
        return seed_ranges
                    
    min_loc = float('inf')
    tmp = seed_range_to_location_min(set(seeds))
    for seed_range in tmp:
        min_loc= min(min_loc, seed_range[0])
        
    return min_loc


assert func2() ==46, func2()
print(func2('input.txt'))

