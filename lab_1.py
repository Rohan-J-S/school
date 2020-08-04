clas = int(input("enter class: "))
sec = str(input("enter section: "))
eng = float(input("enter marks in sem 2 english exam: "))
math = float(input("enter marks in sem 2 math exam: "))
phy = float(input("enter marks in sem 2 physics exam: "))
comp = float(input("enter marks in sem 2 computers exam: "))
chem = float(input("enter marks in sem 2 chemistry exam: "))
avg = (eng+math+chem+comp+phy)/5
if avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "D"

print ("                      National public school")
print ("                      Rajajinagar.Bangalore-10")
print("Marks sheet")
print("_____________________________________________________________________")
print ("admission number      : ",ad)
print ("class                 : ",clas)
print ("sec                   : ",sec)
print ("Average               : ",avg)
print ("grade                 : ",grade)
print("_____________________________________________________________________")
