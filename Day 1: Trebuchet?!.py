import re
path = '../day1_input.txt'
with open(path,'r') as file:
    cal_value = file.readlines()
total_val = 0
for v in cal_value:
    x = list(map(int,re.findall("[0-9]", v)))
    if len(x) == 1:
        total_val += x[0]*11
    else:
        total_val += (x[0]*10)+(x[-1])

print(total_val)
