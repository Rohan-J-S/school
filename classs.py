d = {1:67.5,2:47.5,3:78}
r = int(input("enter roll num: "))
if r in d:
    marks = float(input(".."))
    d[r] = marks
else:
    print("roll number doesnt exist")