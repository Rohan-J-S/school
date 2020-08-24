x = float(input("enter a number: "))
n = int(input("enter nth power: "))
out = 0
for y in range(n+1):
    out += x**y
print (out)
