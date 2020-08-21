n = int(input("enter a number: "))
out = 0
for x in range(n+1):
    out += x*(x+1)
    print(x,"*",x+1,sep = "",end = " + ")
print("=",out)
