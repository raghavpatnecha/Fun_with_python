def binary_search(myitem, mylist):

    top = len(mylist)-1
    bottom = 0
    found = False

    while bottom <=top and not found:
        middle = (top + bottom) // 2
        if mylist[middle] == myitem:
            return True,middle
        elif mylist[middle] < myitem:

            bottom = middle + 1
        else:
            top = middle - 1
    return found,-1

if __name__ == "__main__":
    numbers = [11, 22, 33, 44, 55, 66, 77, 88]
    numbers.sort()
    numbers_cnt= [0, 0, 0, 0, 0, 0, 0, 0]
    while True:
        item = int(input("what number you want to search:"))
        isfound, pos = binary_search(item, numbers)
        if isfound:

            numbers_cnt[pos] += 1
            print("your no. is in the list")
            print( "Access count for {0}:{1}".format(item ,str(numbers_cnt[pos])))


        else:
            print("sorry")




