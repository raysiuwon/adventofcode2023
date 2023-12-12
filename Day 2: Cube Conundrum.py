import re
from itertools import chain

path = '/home/ray/Documents/programming/python/coding problems/advent of code/day2_input.txt'

with open(path,'r') as file:
    line = file.readlines()

sumID = 0

for l in range(len(line)):
    if len(re.findall('1[3-9] red|[2-9][0-9] red',line[l])) == 0 and len(re.findall('1[4-9] green|[2-9][0-9] green',line[l])) == 0 and len(re.findall('1[5-9] blue|[2-9][0-9] blue',line[l])) == 0:
        sumID += l+1
        print('true',line[l],sumID, 'l =', l+1)
    else:
        print('false',line[l],sumID, 'l =', l+1)
print(sumID)