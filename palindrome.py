num = int(input("enter a number: "))
str_num = str(num)
num_rev = ""
for x in range(len(str_num)-1,-1,-1):
    num_rev += str_num[x]
if int(num_rev) == num:
    print("it is a palindrome number")
