num = int(input("enter a number: "))
num2 = int(input("enter a number: "))

for x in range(1,num+1):
    if num % x == 0 and num2 % x == 0:
        hcf = x
print (hcf)
lcm = (num*num2)//hcf
print(lcm)
