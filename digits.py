num = int(input("enter a number: "))
num = str(num)
for x in range(0,len(num)):
    print (num[x],end = " ")
print ()
for x in range(0,len(num)):
    print (int(num[x])**2,end = " ")
