#implemening doubly linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class Dlinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def createDll(self,nodevalue):
        node=Node(nodevalue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return 'dll is created'
    def insertinDll(self,nodevalue,location):
        if self.head is None:
            print("list does not exist")
        else:
            newnode=Node(nodevalue)
            if location==0:
                newnode.prev=None
                newnode.next=self.head
                self.head.prev=newnode
                self.head=newnode
            elif location==1:
                newnode.next=None
                newnode.prev=self.tail
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                newnode.next=tempnode.next
                newnode.prev=tempnode
                newnode.next.prev=newnode
                tempnode.next=newnode
# traverse doubly linked list
    def traversel(self):
        if self.head is None:
            print('list does not exist')
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
#reverse traverse doubly linked list
    def reversetrav(self):
        if self.head is None:
            print('list does not exist')
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.prev
# search value in doubly linked list
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
                    self.head.prev=None
            elif location==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail=self.tail.next
                    self.tail.prev=None
            else:
                tempnode=self.head
                index=0
                while index < location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next
                tempnode.next.prev=tempnode
    # delete entire single linked list
    def DeleteentireDLL(self):
        if self.head is None:
            print('nonlist exist')
        else:
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None

doublelinkedlist=Dlinkedlist()
doublelinkedlist.createDll(1)
doublelinkedlist.insertinDll(2,1)
print([node.value for node in doublelinkedlist])
doublelinkedlist.traversel()
