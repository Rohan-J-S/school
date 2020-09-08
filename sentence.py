st = input("enter a word: ")
upper = 0
lower = 0
spaces = 1
digits = 0
symbols = 0
for x in st:
    if x == " ":
        spaces += 1
    elif ord(x)>= 65 and ord(x)<= 90:
        upper += 1
    elif ord(x)>= 97 and ord(x) <= 122:
        lower += 1
    elif x in range(1,10):
        digits += 1
    else:
        symbols += 1
print(spaces,upper,lower,digits,symbols)
    
