con_no = int(input("enter consumer number: "))
units = int(input("enter number of units consumed: "))
if units <= 100 and units >= 0:
    charge = 2.5*units
elif units <= 200:
    charge = (2.5*100) + (3.5*(units - 100))

else:
    charge = (2.5*100) + (3.5*100) + (5*(units - 200))
total = charge + 75
print ("                   Bangalore elctricity board")
print ("date: 4/8/2020                               bill no. 123")
print ("consumer No.: ",con_no)
print ("_______________________________________________________________________")
print ("no. of units consumed        :",units)
print ("total charge                 :",total)
print ("_______________________________________________________________________")
