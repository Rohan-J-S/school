A = eval(input("enter a list: "))
B = eval(input("enter a list: "))
k = 0
for x in range(len(B)):
    k += x
    A.insert(x+k,B[x])
print(A)
