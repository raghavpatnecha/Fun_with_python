class binaryheap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0


    def precup(self,i):
        while i//2 > 0:
            if self.heaplist[i] <self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i]=tmp
        i= i//2

    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize = self.currentsize + 1
        self.precup(self.currentsize)

    def precdown(self,i):
        while i *2 <= self.currentsize:
            mc= self.minchild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc


    def minchild(self,i):
        if i*2 +1 > self.currentsize:
            return  i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2 +1]:
                return  i *2
            else:
                return  i*2 +1

    def delmin(self):
        retval = self.heaplist[1]
        self.heaplist[1]=  self.heaplist[self.currentsize]
        self.currentsize = self.currentsize -1
        self.heaplist.pop()
        self.precdown(1)
        return retval

    def buildheap(self, mylist):
        i = len(mylist) //2
        self.currentsize = len(mylist)
        self.heaplist = [0] + mylist[:]
        while i >0:
            self.precdown(i)
            i = i - 1


bh = binaryheap()
bh.buildheap([9,5,6,2,3])

print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())





