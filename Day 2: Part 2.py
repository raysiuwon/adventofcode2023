import re

path = '../day2_input.txt'

with open(path,'r') as file:
    line = file.readlines()

sumID = 0

for l in range(len(line)):
    red = max(list(map(int,re.findall('(\d+) red',line[l]))))
    green = max(list(map(int,re.findall('(\d+) green',line[l]))))
    blue = max(list(map(int,re.findall('(\d+) blue',line[l]))))
    cubed = red*green*blue
    sumID += cubed

print(sumID)
