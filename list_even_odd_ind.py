l = eval(input(",,"))
even = 0
odd = 0
for x in range(len(l)):
    if x%2 == 0:
        even += l[x]
    else:
        odd += l[x]
print(odd-even)        
