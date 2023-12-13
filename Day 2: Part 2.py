import re

path = '/home/ray/Documents/programming/python/coding problems/advent of code/day2_input.txt'

with open(path,'r') as file:
    line = file.readlines()

sumID = 0

for l in range(len(line)):
    red = max(list(map(int,re.findall('([0-9]|[1-9][0-9]) red',line[l]))))
    green = max(list(map(int,re.findall('([0-9]|[1-9][0-9]) green',line[l]))))
    blue = max(list(map(int,re.findall('([0-9]|[1-9][0-9]) blue',line[l]))))
    cubed = red*green*blue
    sumID += cubed

print(sumID)