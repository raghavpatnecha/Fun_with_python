def insertion(mylist):
    counter=0
    for index in range(1,len(mylist)):
        current_value= mylist[index]
        position = index
        while position > 0 and mylist[position-1]>current_value:
            mylist[position]=mylist[position-1]
            position= position-1

        mylist[position]=current_value
        counter += 1
    return mylist,counter


mylist = [54,26,93,17,77,31,44,55,20]
sortedlist,counter= insertion(mylist)
print(mylist,counter)

