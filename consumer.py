num = int(input("enter consumer number: "))
__type = str(input("enter a type(R for residence and C for consumer): "))
calls = int(input("enter number of calls made: "))
if __type == "R":
    if calls > 100:
        val = 100+((calls-100)*1.5)
    else:
        val = calls
elif __type == "C":
    if calls > 200:
        val = (200*1.5)+((calls-200)*2)
    else:
        val = calls*1.5

else:
    print ("invalid type")
total = val+(val*0.1)
print (num,__type,calls,total)
