a = float(input("enter a number: ")) 
b = float(input("enter a number: "))
c = float(input("enter a number: "))
if a == b or b == c or c == a:
    print (" enter unique numbers")
else:
    if a>b>c:
        print (c,b,a)
    elif b>c>a:
        print (a,c,b)
    elif c>a>b:
        print (b,a,c)
    elif a>c>b:
        print (b,c,a)
    elif b>a>c:
        print (c,a,b)
    else:
        print (b,a,c)
