path = '../day5_input.txt'
almanac = open(path).read().splitlines()

seeds = list(map(int,almanac[0].split()[1:]))
lowest_seed_list = []
for seed in seeds:
    lowest_seed = seed
    flag = False
    for a in almanac[1:]:
        if a.endswith('map:') or a == '':
            flag = True
        else:
            x2yMap = list(map(int,a.split()))
            if flag == True and lowest_seed in range(x2yMap[1],x2yMap[1]+x2yMap[2]):
                lowest_seed += x2yMap[0] - x2yMap[1]
                flag = False
    lowest_seed_list.append(lowest_seed)

print(min(lowest_seed_list))
