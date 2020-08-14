num = int(input("enter number of terms: "))
a = 0
b = 1
print(a,",",b,end = ",")
for x in range(num-2):
    a+=b
    b+=a
    print (a,",",b,end = ",")
