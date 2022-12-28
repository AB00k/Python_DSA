#implementing single linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Slinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertinlinkedlist(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==1:
                newnode.next=None
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
    #traverse single linked list
    def traversel(self):
        if self.head is None:
            print('list does not exist')
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    #search value in linked list
    def search(self,nodevalue):
        if self.head is None:
            print('list does not exists')
        else:
            node=self.head
            while node is not None:
                if node.value==nodevalue:
                    print(node.value)
                node=node.next
            print('value does not exist')
    #delete an node in single linked list
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
                    node.next=None
                    self.tail=node
            else:
                tempnode=self.head
                index=0
                while index < location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next
    #delete entire single linked list
    def deleteentiresll(self):
        if self.head is None:
            print('list does not exist')
        else:
            self.head=None
            self.tail=None

singlylinkedlist=Slinkedlist()
singlylinkedlist.insertinlinkedlist(1,0)
singlylinkedlist.insertinlinkedlist(2,1)
singlylinkedlist.insertinlinkedlist(3,2)
singlylinkedlist.insertinlinkedlist(4,3)
print([node.value for node in singlylinkedlist])
singlylinkedlist.deleteentiresll()
print([node.value for node in singlylinkedlist])
