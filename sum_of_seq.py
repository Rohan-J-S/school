def sign(a):
    if a > 0:
        return "+"
    else: 
        return ""
   
var= -1 
sum = 0
for x in range(1,11):
    var *= -1
    sum += (x*var)
    print (sign(x*var),x*var,end = " ")
print(" =",sum)
