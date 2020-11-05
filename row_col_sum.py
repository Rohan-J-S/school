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

for i in range(r):
    row = 0 
    col = 0
    for j in range(c):
        print ("row: ",i+1,"col: ",j+1)
        grid[i][j] = int(input())
        row += grid[i][j]
        col += grid[j][i]
    print ("row: ",i+1,"sum = ",row)
    print ("col: ",j+1,"sum = ",col)
print (grid)
print (s)

