out_1 = 0
out_2 = 0
for x in range (1,11):
    if x%2 == 0:
        out_1 += x
    else:
        out_2 += x

print ("sum of odd is: ",out_2)
print ("sum of even is: ",out_1)
