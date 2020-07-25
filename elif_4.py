name = str(input("enter a name: "))
col = str(input("enter colour code: "))
if col == "r"or col == "R": 
    print (name,"is in centaur")
elif col == "g"or col == "G": 
    print (name,"is in orion")
    
elif col == "y"or col == "Y": 
    print (name,"is in pegasus")
    
elif col == "b"or col == "B": 
    print (name,"is in phoenix")
else:
    print("invalid input")   
