st = input("enter a word: ")
for x in range(1,len(st),2):
    st = st[:x]+chr(ord(st[x])-32)+st[x+1:]
print(st)
