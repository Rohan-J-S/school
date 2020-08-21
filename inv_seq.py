n = int(input("enter a number: "))
out = 0
for x in range(1,n+1):
    frac = x/(31-x)
    out += frac
print(out)
