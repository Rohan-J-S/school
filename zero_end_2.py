l = [1,2,3,0,4,5,0,6]
n = []
count = 0
x = 0
while x < len(l)-count:
    if l[x] == 0:
        l = l[:x] + l[x+1:]
        count += 1
    x += 1
for x in range(count):
    l += [0]
print(l)
