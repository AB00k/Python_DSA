#implementing circular single linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class CSlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next
    def createcll(self,nodevalue=None):
        node=Node(nodevalue)
        node.next=None
        self.head=node
        self.tail=node
    def insertincsll(self,value,location):
        if self.head is None:
            print("list does not exist")
        else:
            newnode=Node(value)
            if location==0:
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode
            elif location==1:
                newnode.next=self.tail.next
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode

    # traverse circular single linked list
    def cslltraverse(self):
        if self.head is None:
            print('list does not exist')
        else:
            tempnode = self.head
            while tempnode is not None:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break
# search value in circular linked list
    def searchcsll(self, nodevalue):
        if self.head is None:
            print('list does not exists')
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    print(tempnode.value)
                tempnode = tempnode.next
                if tempnode==self.tail.next:
                    break

    # delete an node in single linked list
    def deletenode(self,location):
        if self.head is None:
            print('list does not exists')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempnode=self.head
                index=0
                while index < location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next

    # delete entire single linked list
    def deleteentirecsll(self):
        if self.head is None:
            print('list does not exist')
        else:
            self.head=None
            self.tail=None
            #self.tail.next=None

circularsinglelinkedlist=CSlinkedlist()
circularsinglelinkedlist.createcll(2)
circularsinglelinkedlist.insertincsll(1,0)
circularsinglelinkedlist.insertincsll(3,1)
circularsinglelinkedlist.insertincsll(4,3)
#circularsinglelinkedlist.cslltraverse()
#circularsinglelinkedlist.searchcsll(2)
#circularsinglelinkedlist.deletenode(2)
circularsinglelinkedlist.deleteentirecsll()
print([node.value for node in circularsinglelinkedlist])