num = int(input("enter a number: "))
flag = True
for x in range(2,num):
    if num % x == 0:
        flag = False
        break

if flag == True:
    print ("Prime")
else:
    print("Composite")
