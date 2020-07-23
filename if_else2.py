sales = float(input("enter sales amount: "))
if sales < 0:
    raise ValueError

if sales >= 10000:
    discount = (1/10)*sales
else:
    iscount = (1/20)*sales

print ("final amount is: ",sales-discount)
