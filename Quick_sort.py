def quicksort(mylist):

    mylistx,count= quicksorthelper(mylist, 0, len(mylist) - 1)

    return mylistx, count


def quicksorthelper(mylist, first, last):
    if first < last:
        splitpoint, count = partition(mylist, first, last)
        quicksorthelper(mylist, first, splitpoint - 1)
        quicksorthelper(mylist, splitpoint + 1, last)
    return mylist, -1


def partition(mylist, first, last):
    pivot = mylist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    counter = 0
    while not done:
        while leftmark <= rightmark and mylist[leftmark] < pivot:
            leftmark = leftmark + 1
        while leftmark <= rightmark and mylist[rightmark] > pivot:
            rightmark = rightmark - 1

        if leftmark > rightmark:
            done = True
        else:
            temp = mylist[leftmark]
            mylist[leftmark] = mylist[rightmark]
            mylist[rightmark] = temp
            counter += 1

    temp = mylist[first]  # pivot = mylist[first]
    mylist[first] = mylist[rightmark]
    mylist[rightmark] = temp

    return rightmark, counter

mylist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mylistx, counter=quicksort(mylist)
print(mylistx,counter)
