r = int(input(",,"))
c = int(input(".."))
grid = []
s = 0
for x in range(r):
    col = []
    for y in range(c):
        col += [0]
    grid += [col]
print (grid)
left = 0
right = 1
for i in range(r):
    for j in range(c):
        print ("row: ",i+1,"col: ",j+1)
        grid[i][j] = int(input())
        if grid[i][j]%2 == 0:
            grid[i][j] = 0
        
print(grid)       
