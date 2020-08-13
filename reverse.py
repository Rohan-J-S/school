num = int(input("enter a number: "))
st = str(num)
out = ""
for x in range(len(st)-1,-1,-1):
    out += st[x]

print (out)
   
