class hashTable:
    def __init__(self):
        self.size = 11
        self.slots= [None] * self.size
        self.data= [None] * self.size

    def put(self,key,data):
        hashvalue= self.hash(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue]=key
            self.slots[hashvalue]=data

        else:
            if self.slots[hashvalue]== key :
                self.data[hashvalue]= data #replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data

                else:
                    self.data[nextslot] = data  #replace

    def hash(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size


    def get(self,key):
        startslot = self.hash(key, len(self.slots))
        data = None
        stop= False
        found = False
        position = startslot
        while not found and not stop and self.slots[position] != None:
            if self.slots[position] == key:
                found =  True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                position == startslot
                stop = True

        return True

    def __getitem__(self, key):
        return  self.get(key)

    def __setitem__(self, key, data):
        return self.put(key,data)


H=hashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
