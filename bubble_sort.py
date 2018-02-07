def bubblesort(mylist):
    flag= True
    passnum= len(mylist) -1
    counter = 0
    while flag and passnum > 0:
        flag = False

        for element in range(passnum):
            if mylist[element] > mylist[element + 1]:
                flag = True

                temp= mylist[element]
                mylist[element]= mylist[element+1]
                mylist[element + 1] = temp
        counter += 1
        passnum -= 1
    return mylist, counter


def bubble(yourlist):
    count=0
    for i in range(len(yourlist)-1, 0, -1):
        for swap in range(i):
            if yourlist[swap] > yourlist[swap + 1]:
                temp=yourlist[swap]
                yourlist[swap]=yourlist[swap + 1]
                yourlist[swap + 1]= temp
        count += 1
    return yourlist, count

mylist = [20,30,40,90,50,60,70,80,100,110]
mylistx = [20,30,40,90,50,60,70,80,100,110]
sortedList, counter= bubblesort(mylist)
sortList, count= bubble(mylistx)
print(sortedList,counter)
print(sortList,count)
mylista=[9,1,2,3,4,5,6,7,8]
mylistb=[9,1,2,3,4,5,6,7,8]
sortedLista, countera= bubblesort(mylista)
sortListb, countb= bubble(mylistb)
print(sortedLista,countera)
print(sortListb,countb)

