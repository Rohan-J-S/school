num = int(input("enter a number: "))
factor_sum = 0
for x in range(1,num//2+1):
    if num%x == 0:
        factor_sum += x
if factor_sum == num:
    print("perfect number")
else:
    print("not a perfect number")
