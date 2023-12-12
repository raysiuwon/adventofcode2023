import re
from itertools import chain

path = '../day2_input.txt'

with open(path,'r') as file:
    line = file.readlines()

sumID = 0

for l in range(len(line)):
    if re.search('(1[3-9]|[2-9][0-9]) red|(1[4-9]|[2-9][0-9]) green|(1[5-9]|[2-9][0-9]) blue',line[l]):
        pass
    else:
        sumID += l+1
        
print(sumID)
