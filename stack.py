#Lesson no 19 : STACK
# implementing stack using  linkedlist
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def __iter__(self):
        currnode=self.head
        while currnode:
            yield currnode
            currnode=currnode.next
class stack:
    def __init__(self):
        self.linkedlist=linkedlist()
    def __str__(self):
        values=[str(x.value) for x in self.linkedlist]
        print('\n'.join(values))
    def isempty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False
    def push(self,value):
        node=Node(value)
        node.next=self.linkedlist.head
        self.linkedlist.head=node
    def pop(self):
        if self.isempty():
            print('there is no element in this list')
        else:
            nodevalue=self.linkedlist.head
            self.linkedlist.head=self.linkedlist.head.next
            print(nodevalue.value)
    def peek(self):
        if self.isempty():
            print('there is no element in this list')
        else:
            nodevalue = self.linkedlist.head
            print(nodevalue.value)
    def delete(self):
        self.linkedlist.head=None

customstack=stack()
customstack.push(1)
#customstack.pop()
#customstack.peek()
#customstack.delete()
print(customstack)


