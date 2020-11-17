days = int(input("enter number of days: "))
l = []
for x in range(days):
    item = float(input("enter temp "))
    l += [item]
j = 0
for y in range(len(l)):
    if l[y] < 0:
        z = l[j]
        l[j] = l[y]
        for i in range(y,j+1,-1):          
            l[i] = l[i-1]
        j += 1
        l[j+1] = z
print (l)
