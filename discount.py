cost = int(input("enter cost of items purchased: "))
if cost <= 2000:
    dis = (5/100)*cost
                
if cost <= 2000:
    dis = (5/100)*cost

elif cost >= 2001 and cost <= 5000:
    dis = (25/100)*cost

elif cost >= 5001 and cost <= 10000:
    dis = (35/100)*cost

else:
    dis = cost/2

total = cost-dis
print ("total cost is: ",total)
