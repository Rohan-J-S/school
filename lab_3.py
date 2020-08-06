roll = int(input("enter roll number: "))
name = str(input("enter name: "))
course = str(input("enter course code(A or B): "))
if course == "A":

    stat_fee = 1200
    tut_fee = 15000
    lab_fee = 1000
elif course == "B":
    stat_fee = 1500
    tut_fee = 20000
    lab_fee = 2500
else:
    print("invalid input please re-enter")
total = stat_fee + tut_fee + lab_fee

print ("___________________________________________________________")
print ("Date: 6/8/2020      DELHI PUBLIC SCHOOL")
print (roll,"               ",name,"            code:",course)
print ("___________________________________________________________")
print("particulars:                Rs.p")
print ()
print ("___________________________________________________________")
print ("stationary fee: ",stat_fee)
print ("tution fee: ",tut_fee)
print ("lab fee: ",lab_fee)
print ("___________________________________________________________")
print ("total_fee: ",total)
print ()
print ("___________________________________________________________")
