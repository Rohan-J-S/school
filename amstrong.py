num = int(input("enter a number: "))
str_num = str(num)

var_2 = 0
for x in (str_num):
    var_2 += int(x)**len(str_num)
if num == var_2:
    print("it is an amstrong number ")
else:
    print("it is not an amstrong number")

