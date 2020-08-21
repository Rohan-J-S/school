n = int(input("enter a number: "))
out = 0
for x in range(1,n+1):
  
    for y in range(1,x+1):
        out += y
        # print(y)
print(out)
