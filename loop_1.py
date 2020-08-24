x = float(input("enter a number: "))
n = int(input("enter nth power: "))
out = 0
sign = -1

for y in range(1,n+1):
    sign *= -1
    out += ((x**y)*2*y)*sign
print(out)

