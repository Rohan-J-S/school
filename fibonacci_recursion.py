def test(n,a,b,count = 0):

    if count == n-1:
        return ""
    elif count == 0:
        count = 1
        return str(a) + " "+ str(b) + " " + test(n,a,b,count)
    else:
        a,b = b,a+b 
        count += 1
        return str(b)+" "+test(n,a,b,count)
a = int(input("enter first value: "))
b = int(input("enter second value: "))
s = int(input("enter a number: "))
print(test(s,a,b))
