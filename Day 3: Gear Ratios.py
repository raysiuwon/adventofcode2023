import re

path = '../day3_input.txt'

with open(path,'r') as file:
    lines = file.readlines()

partNumSum = 0
for l in range(len(lines)):
    lines[l] = lines[l].replace('.','_')

for x in range(len(lines)):
    nums = re.findall('\d+',lines[x])
    for n in nums:
        n_position = re.search(n,lines[x]).span()
        # print(n, n_position)
        start = n_position[0]
        end = n_position[1]
        line_len = len(lines[x][0])
        for i in range(max(0,x-1),min(x+2,len(lines))):
            if re.search('\W+',lines[i][max(0,start-1):min(end+1,len(lines[i]))]):
                partNumSum += int(n)
                print(n)
                break
        lines[x] = lines[x].replace(n,'_'*len(n),1)

print(partNumSum)
