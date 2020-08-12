num = int(input("enter a number: "))
num_2 = int(input("enter a number: "))
num_3 = int(input("enter a number: "))
num_4 = int(input("enter a number: "))
num_5 = int(input("enter a number: "))
num_6 = int(input("enter a number: "))
num_7 = int(input("enter a number: "))
num_8 = int(input("enter a number: "))
num_9 = int(input("enter a number: "))
num_10 = int(input("enter a number: "))
out = 0

lis = [num,num_2,num_3,num_4,num_5,num_6,num_7,num_8,num_9,num_10]
for x in lis:
    if x%2 == 0:
        out += x
print (out)
