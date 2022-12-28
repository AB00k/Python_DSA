#Lession no : 18     cracking linked list interview questions
#question no 5 : given two singly linked list determine if these two intersects , return intersecting node
from linkedlist import Linkedlist,Node
def intersection(lla,llb):
    if lla.tail is not llb.tail:
        return False

    lena=len(lla)
    lenb=len(llb)

    shorter=lla if lena < lenb else llb
    longer=llb if lena < lenb else lla

    difference=len(longer)-len(shorter)

    longernode=longer.head
    shorternode=shorter.head

    for i in range(difference):
        longernode=longernode.next

    while shorternode is not longernode:
        shorternode=shorternode.next
        longernode=longernode.next
    return longernode

# Helper addition method
def addsamenode(lla,llb,value):
    tempnode=Node(value)
    lla.tail.next=tempnode
    lla.tail=tempnode
    llb.tail.next = tempnode
    llb.tail = tempnode
lla=Linkedlist()
lla.generate(3,0,10)
llb=Linkedlist()
llb.generate(4,0,10)

addsamenode(lla,llb,11)
addsamenode(lla,llb,12)
addsamenode(lla,llb,13)

print(lla)
print(llb)
print(intersection(lla,llb))