st = input("enter a word: ")
out = ""
for x in range(len(st)):
    if x%2 == 0:
        out += st[x]
    else:
        out += chr(ord(st[x])-32)
print(out)
    
