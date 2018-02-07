def binarytree(r):
    return [r,[],[]]
def insertleft(root,newbranch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])
    else:
        root.insert(1,[newbranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root


def getrootvalue(root):
    return root[0]


def setrootvalue(root,newvalue):
    root[0] = newvalue


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = binarytree(3)
insertleft(r,4)
insertleft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setrootvalue(l,9)
print(r)
insertleft(l,11)
print(r)
print(getRightChild(getRightChild(r)))
