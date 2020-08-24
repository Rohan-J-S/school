x = float(input("enter a number: "))
n = int(input("enter nth power: "))
out = 0
sign = -1
for y in range(0,n+1):
    out += ((x**y)/((x*2)+1))*sign
print(out)
