marks = int(input("enter marks in comp exam: "))
if marks >= 90 and marks <= 100:
    print ("a grade")
elif marks >= 70 and marks <= 89:
    print ("b grade")
elif marks >= 50 and marks <= 69:
    print ("c grade")
elif marks >= 0 and marks <= 49:
    print ("d grade")
else:
    print ("invalid input")

