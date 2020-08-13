num = int(input("enter a number: "))
fac = 0
print ("factors are: ",end = " ")
for x in range(1,num+1):
    if num % x == 0:
        print (x,end = " ")
        fac += 1
print ("\n number of factors are: ",fac)
    
