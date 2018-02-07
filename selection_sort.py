def selection(mylist):
    for fillslot in range(len(mylist)-1,0,-1):
        positionofmax=0
        for i in range(1,fillslot+1):
            if mylist[i]>mylist[positionofmax]:
                positionofmax = i

        mylist[i],mylist[positionofmax] =mylist[positionofmax],mylist[i]             #temp = mylist[i]
                                                                                     #mylist[i]= mylist[positionofmax]
                                                                                     #mylist[positionofmax] = temp

    return mylist


mylist =[54,26,93,17,77,31,44,55,20]
sortlist= selection(mylist)
print(sortlist)