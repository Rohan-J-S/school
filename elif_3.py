mon = str(input("enter the first 3 letters of a month in caps: "))
if mon in ("JAN","MAR","MAY","JUL","AUG","OCT","DEC"):
    print ("the month has 31 days")
elif mon in ("APR,","JUN","SEP","NOV"):
    print ("the month has 30 days")
elif mon == "FEB":
    print("the month has 28 days")
else:
    print ("invalid")
