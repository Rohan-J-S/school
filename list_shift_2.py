l = [1,2,3,4,5]
for x in range(4):
    last = l[len(l)-1]
    for y in range(len(l)-1,0,-1):
        l[y] = l[y-1]
    l[0] = last

    print(l)
