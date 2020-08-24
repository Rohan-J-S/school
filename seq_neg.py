x = float(input("enter a number: "))
n = int(input("enter nth power: "))
out = 0
sign = -1
for y in range(n+1):
    sign *= -1
    out += (x**y)*sign
    if y != n:
        if sign == -1:
            print(x,"^",y,sep = "",end = " - ")
        else:
            print(x,"^",y,sep = "",end = " + ")
    else:
        print(x,"^",y,sep = "",end = " ")
print ("=",out)
