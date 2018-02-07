def Linear_Search(myitem, mylist):
    found = False
    position=  0

    while position < len(mylist) and not found:
        if mylist[position] == myitem:
            return True, position
        position += 1
    return found, -1
if __name__ == "__main__":
    shopping = ["chocolates", "eggs", "tomatoes", "apples", "bananas"]
    shopping_cnt = [0, 0, 0, 0, 0]
    while True:
        item = input("What item do you want?")
        isfound, pos = Linear_Search(item, shopping)


        if isfound:
            shopping_cnt[pos] += 1

            print("your item is in the list:{0}".format(item))
            print("Access count for item " + item + ":" + str(shopping_cnt[pos]))
        else :
            print("sorry")
            out= input("Do you want to add that item Y or N")
            if out == "Y" or "y":
                shopping.append(item)

                print("your item is now in the list")
                shopping_cnt = [0 for item in shopping]
            else:
                if out == "N" or "n":

                    print("thank you")

