st = input("enter a word: ")
st1 = input("enter a word: ")
out = ""
for x in range(len(st)):
    out += st[x]
for y in range(len(st1)):
    out = out[:y+1+y]+st1[y]+out[y+1+y:]
print(out)
