import re
from itertools import chain

path = '../day1_input.txt'

with open(path,'r') as file:
    cal_value = file.readlines()

total_val = 0

numWord = 'one two three four five six seven eight nine'.split()
revNumWord = 'one two three four five six seven eight nine'[::-1].split()
numList = list(map(str,[i for i in range(1,10)]))
numList.append(numWord)
numList.append(revNumWord)
numList = list(chain.from_iterable(numList))
numListRegex = '|'.join(numList)
reversedNumListRegex = numListRegex[::-1]

numWordDic = {value: str(count) for count, value in enumerate(numWord, start=1)}
for nw in numWord:
    numWordDic[nw[::-1]] = numWordDic[nw]
for i in range(1,10):
    numWordDic[str(i)] = str(i)

for cv in cal_value:
    try: 
        total_val += int(numWordDic[re.search(numListRegex,cv).group()])*10
        total_val += int(numWordDic[re.search(numListRegex,cv[::-1]).group()])
    except AttributeError:
        pass
    
print(total_val)
