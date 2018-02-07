def mergesort(mylist):
    if len(mylist) >1:
        mid = len(mylist)//2
        lefthalf= mylist[:mid]
        righthalf = mylist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mylist[k] = lefthalf[i]
                i += 1
            else:
                mylist[k]= righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            mylist[k]= lefthalf[i]
            i=i+1
            k = k+1
        while j < len(righthalf):
            mylist[k] =righthalf[j]
            j = j+1
            k=k+1




mylist= [54,26,93,17,77,31,44,55,20]
mergesort(mylist)
print(mylist)


