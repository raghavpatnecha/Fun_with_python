def shellsort(mylist)
    sublistcount = len(mylist)//2
    while sublistcount>0:
    for startposition in range(sublistcount):
        gapinsertion(mylist,startposition,sublistcount)
    sublistcount = sublistcount//2

def gapinsertion(mylist,start,gap):
    for i in range(start+gap,len(mylist),gap)
    current_value= mylist[position]
    position = i
    while position >=gap and current_value<mylist[position-gap]:
        mylist[position]= mylist[position-gap]
        position = position-gap

    mylist[position] = current_value

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

