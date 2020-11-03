r = int(input(",,"))
c = int(input(".."))
grid = []
for x in range(r):
    col = []
    for y in range(c):
        col += [0]
    grid += [col]
print (grid)

for i in range(r):
    for j in range(c):
        grid[i][j] = int(input(".."))
print (grid)


