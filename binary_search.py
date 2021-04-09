def test(l,low,high,e):
    
    mid = (low+high)//2

    if e == l[mid]:
        return mid

    elif low == high:
        return -1

    elif l[mid] > e:
        return test(l,low,mid-1,e)

    else:
        return test(l,mid+1,high,e)


l = [1,2,3,4,5]
n = int(input("enter element to search: "))
print(test(l,0,len(l)-1,n))
