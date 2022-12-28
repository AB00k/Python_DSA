#Lesson no 20 : QUEUE
# implementing queue using linkedlist
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        currnode=self.head
        while currnode:
            yield currnode
            currnode=currnode.next

class queue:
    def __init__(self):
        self.linkedlist=Linkedlist()
    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self,value):
        newnode=Node(value)
        if self.linkedlist.head==None:
            self.linkedlist.head=newnode
            self.linkedlist.tail=newnode
        else:
            self.linkedlist.tail.next=newnode
            self.linkedlist.tail=newnode
        return 'element inserted successfully'
    def isempty(self):
        if self.linkedlist.head==None:
            return True
        else:
            False
    def dequeue(self):
        if self.isempty():
            print('there is no element in this list')
        else:
            tempnode=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return tempnode
    def peek(self):
        if self.isempty():
            print('there is no element in this list')
        else:
            return self.linkedlist.head
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None

customqueue=queue()
customqueue.enqueue(1)
customqueue.enqueue(2)
#print(customqueue.dequeue())
#print(customqueue.peek())
#customqueue.delete()
print(customqueue)