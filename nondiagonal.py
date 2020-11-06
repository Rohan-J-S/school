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
        if j == i:
            left += grid[i][j]
            
        elif i+j == r-1:
            right *= grid[i][j]
        
for x in range(r):
    for y in range(c):
        if x == y or x+y == r-1:
            print(" ",end = "")
        else:
            print(grid[x][y],end = "")
    print ()
