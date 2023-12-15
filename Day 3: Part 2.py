import re
import numpy

path = '../day3_input.txt'
grid = open(path).read().splitlines()

xlen = len(grid)
ylen = len(grid[0])
total = 0

for x, row in enumerate(grid):
    for y, col in enumerate(row):
        xTopEdge = max(x-1,0)
        yLeftEdge = max(y-1,0)
        xBottomEdge = min(x+1,xlen)
        yRightEdge = min(y+1,ylen)
        nums = []
        if not(row[y].isdigit()) and row[y] != '.':
            for searchX in range(xTopEdge,xBottomEdge+1):
                for searchY in range(yLeftEdge,yRightEdge):
                    leftBound = True
                    rightBound = True
                    i = searchY
                    while leftBound and i>=0:
                        if grid[searchX][i].isdigit():
                            i -= 1
                        else:
                            leftBound = False
                    i += 1
                    digit = ""
                    while rightBound and i<=ylen-1:
                        if grid[searchX][i].isdigit():
                            digit += grid[searchX][i]
                            grid[searchX] = grid[searchX][:i]+'.'+grid[searchX][i+1:]
                            i += 1
                        else:
                            rightBound = False
                    if digit != "":
                        nums.append(digit)
        if len(nums) > 1:
            total += numpy.prod(list(map(int,nums)))

print(total)
