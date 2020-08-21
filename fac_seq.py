n = int(input("enter a number: "))
final = 0
out = 1
for x in range(2,n+1,2):
    out = 1
    for y in range(1,x+1):
        out *= y
    final += out
print(final)
