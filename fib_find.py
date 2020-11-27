fib = (0,1)
n = int(input("enter a number: "))
flag = False
while flag == False:
    fib += (fib[len(fib)-1]+fib[len(fib)-2]),
    if fib[len(fib)-1] == n:
        print(len(fib))
        flag = True
