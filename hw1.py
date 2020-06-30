date = int(input("enter date: "))
month = int(input("enter month: "))
year = int(input("enter year: "))
flag = False
if year % 400 == 0:
    flag = True
elif year % 100 == 0:
    flag = False
elif year % 400 == 0:
    flag = True

if month in (1,3,5,7,8,10,12):
    total = 31
elif month in (4,6,9,11):
    total = 30
elif flag == False:
    total = 28
else:
    total = 29
output = total - date
print ("total number of days left in the month is: ", output)
