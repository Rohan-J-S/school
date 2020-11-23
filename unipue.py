l = eval(input(".."))
unique = []
x = 0
removed = 0 
while x <= len(l)-removed:
    if l[x] in unique:
        l = l[:x]+l[x+1:]
        removed += 1
        continue
    unique += [l[x]]
    x += 1
print (unique)
