l = [1,2,3,0,4,5,0,6]
n = []
count = 0
for x in range(len(l)):

    if l[x] == 0:
        count += 1
    else:
        n.append(l[x])
for y in range(count):
    n.append(0)
print(n)
