days = int(input("enter number of days: "))
l = []
for x in range(days):
    item = float(input("enter temp "))
    l += [item]
for y in range(len(l)):
    if l[y] < 0:
        z = l[0]
        l[0] = l[y]
        for i in range(y,1,-1):
            
            l[i] = l[i-1]
        l[1] = z
