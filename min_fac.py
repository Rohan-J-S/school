n = int(input("enter a number: "))
sign = -1
final = 0
out = 1
for x in range(1,n+1):
    sign *= -1
    out *= x
    final += sign*out
print(final)
