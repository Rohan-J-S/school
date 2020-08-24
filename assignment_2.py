#q1
s = 0
for x in range(1,11,2):
    s += x*(x+1)
print(s)

#q2
s = 0
for x in range(1,10,1):
    s += x*(x+2)
print(s)

#q3
sign = -1
n = int(input("enter a number: "))
s = 0
for x in range(1,n+1,2):
    sign *= -1
    fac = 1
    for y in range(1,x+1):
        fac *= y
    s += fac*sign
print(s)

#q4
n = int(input("enter a number: "))
s = 0
fact = 1
for x in range(1,n+1):
    fact *= x
    if x%3 == 1:
        s += fact
print( s )

#q5
n = int(input("enter a number: "))
s = 0
for x in range(1,n+1,2):
    s += x*x
print(s)

#q6
s = 0
sign = -1
for x in range(10):
    sign *= -1
    s += ((2+(x*3))/(9+(x*4)))*sign
print(s)

#q7
s = 0
sign = -1
for x in range(1,11):
    sign *= -1
    s += (1/x)*sign
print(s)

#q8
s = 0
for x in range(1,10):
    s += x/(x+1)
print(s)
