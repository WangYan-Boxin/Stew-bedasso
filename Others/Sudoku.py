from operator import truediv

grid = []
for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)

# grid = [[int(x) for x in input().split()] for i in range (9)]

print(grid)
print(len(set(grid[0])))

good = True
if len(set(grid[0])) < 9:
    good = False
if len(set(grid[1])) < 9:
    good = False

temp=[]
for r in range(9):
    temp.append(grid[r][0])
print(temp)