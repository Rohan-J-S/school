n = int(input("enter a number: "))
l = []
for x in range(1,n+1):
    l += [int(input(".."))]
print("original list: ",l)
r = int(input("enter number : "))
for y in range(r):
    a = int(input("enter number to be inserted: "))
    for z in range(0,len(l)):
        if a<=l[z]:
            d = l[len(l)-1]
            for c in range(len(l)-1,z-1,-1):
                l[c] = l[c-1]
            l[z] = a
            l += [d]
            break
    print("list after inserting",a,"is",l)
