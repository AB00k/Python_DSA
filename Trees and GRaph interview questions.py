#Graph Algorithms
# Lesson NO: 40
#Cracking trees and graphs interview questions
#Question no 1: Given a direted graph and two vertices (s and e) design an alorithm to find werther there is a route
# from s to e
"""class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addedge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def checkroute(self,startnode,endnode):
        visited=[startnode]
        queue=[startnode]
        path=False
        while queue:
            dvertex=queue.pop(0)
            for adjacentvertex in self.gdict[dvertex]:
                if adjacentvertex not in visited:
                    if adjacentvertex==endnode:
                        path=True
                        break
                    else:
                        visited.append(adjacentvertex)
                        queue.append(adjacentvertex)
        return path
customdict={'a': ['c','d','b'],
            'b': ['j'],
            'c': ['g'],
            'd': [],
            'e': ['f','a'],
            'f': ['i'],
            'g': ['d,''h'],
            'h': [],
            'i': [],
            'j': []
            }
g=Graph(customdict)
print(g.checkroute('e','c'))"""
# Question no 2: given sorted (increasing order) array with unique integer elements write algorithm to create binary
# search tree with minimal height
"""class BSTNode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        #Returns list of strings, width, height, and horizontal coordinate of the root.
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
def minimaltree(sortedarray):
    if len(sortedarray)==0:
        return None
    if len(sortedarray)==1:
        return BSTNode(sortedarray[0])
    mid=int(len(sortedarray)/2)
    left=minimaltree(sortedarray[:mid])
    right=minimaltree(sortedarray[mid+1:])
    return BSTNode(sortedarray[mid],left,right)
sortedarray=[1,2,3,4,5,6,7,8,9]
bst=minimaltree(sortedarray)
bst.display()"""
# Question no 3: Given a binary search tree design an algoithm to create a linked list of all nodes at each depth(i.e if
# you have a tree with depth 'd' you'll have 'd' linked list)
"""class linkedlist:
    def __init__(self,val):
        self.val=val
        self.next=None
    def add(self,val):
        if self.next==None:
            self.next=linkedlist(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)
class BT:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def depth(tree):
    if tree==0:
        return 0
    if tree.left==None and tree.right==None:
        return 1
    else:
        depthleft=1+depth(tree.left)
        depthright=1+depth(tree.right)
        if depthright>depthleft:
            return depthright
        else:
            return depthleft

def treetolinkedlist(tree,customdict={},d=None):
    if d==None:
        d=depth(tree)
    if customdict.get(d)==None:
        customdict[d]=linkedlist(tree.val)
    else:
        customdict[d].add(tree.val)
        if d==1:
            return customdict
    if tree.left !=None:
        customdict=treetolinkedlist(tree.left,customdict,d-1)
    if tree.right !=None:
        customdict=treetolinkedlist(tree.right,customdict,d-1)
    return customdict
maintree=BT(1)
two=BT(2)
three=BT(3)
four=BT(4)
five=BT(5)
six=BT(6)
seven=BT(7)
maintree.left=two
maintree.right=three
two.left=four
two.right=five
three.left=six
three.right=seven

custdict=treetolinkedlist(maintree)
for depthlevel,linkedlist in custdict.items():
    print('{0} {1}'.format(depthlevel,linkedlist))"""

# Question no 4: Implement a function if BT is balanced or not
"""def isbalancedhelper(root):
    if root is None:
        return 0
    leftheight=isbalancedhelper(root.left)
    if leftheight==-1:
        return -1
    rightheight = isbalancedhelper(root.right)
    if rightheight == -1:
        return -1
    if abs(leftheight-rightheight)>1:
        return -1

    return max(leftheight,rightheight)+1

def isbalaced(root):
    return isbalancedhelper(root)>-1

class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left = left
        self.right=right


n1=Node('n1')
n2=Node('n2')
n3=Node('n3')
n4=Node('n4')
n5=Node('n5')
n6=Node('n6')
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.right=n6
print(isbalaced(n1))"""
# Question no 5: Write function is binary tree is binary search tree
"""class treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def helper(node,minvalue=float('-inf'),maxvalue=float('inf')):
    if not node:
        return True
    val=node.value
    if val<=minvalue or val >=maxvalue:
        return False
    if not helper(node.left,minvalue,val):
        return False
    if not helper(node.right,val,maxvalue):
        return False
    return True
def isvalidBT(root):
    return helper(root)
root1=treenode(6)
root1.left=treenode(1)
root1.right=treenode(4)
print(isvalidBT(root1))"""

# Question no 6: Algorithm to find next node (i.e in order successor) of given node in binary search tree you may assume
# that each node has a link to it's parent
"""class Node:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def minvalue(node):
    current=node
    while current is not None:
        break
    current=current.left
    return current
def inordersuccessor(root,n):
    if n.right is not None:
        return minvalue(n.right)
    p=n.parent
    while p is not None:
        if n!=p.right:
            break
        n=p
        p=p.parent
    return p
def insert(node,data):
    if node is None:
        return Node(data)
    else:
        if data<=node.data:
            temp=insert(node.left,data)
            node.left=temp
            temp.parent=node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node
root=Node(4)
insert(root,2)
insert(root,8)
insert(root,1)
insert(root,3)
insert(root,5)
insert(root,9)


temp=root.left.right
successor=inordersuccessor(root,temp)

if successor is not None:
    print('inorder successor of %s is %s'%(temp.data,successor.data))
else:
    print("inorder uccessor does'not exist")"""

# Question no 7: you're given a list of projects and list of dependencies ( which is the list of pair's of projects
# , where the second projest is dependent on first one) all the project dependencies must be built before the project is
# find a build order that'll allow the projects to be built, if there is no build order return an error
#we can use topological sort (used for task like task scheudling)
"""from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,vertex,edge=None):
        self.graph[vertex].append(edge)

    def topologicalsortuti(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalsortuti(i,visited,stack)
        stack.insert(0,v)
    def topologicalsort(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalsortuti(k,visited,stack)
        print(stack)

g=Graph()
g.addedge('a')
g.addedge('b')
g.addedge('c')
g.addedge('d')
g.addedge('e')
g.addedge('f')
g.addedge('a','d')
g.addedge('f','b')
g.addedge('b','d')
g.addedge('f','a')
g.addedge('d','c')
g.topologicalsort()"""

# Question no 8: Alorithm to find the first common ancestor of two nodes in a binary tree. Avoid storing additional
# nodes in any data structure. NOte:This is not necessarily a binary search tree
class TreeNode:
    def __init__(self,vlaue,left=None,right=None):
        self.value=vlaue
        self.left=left
        self.right=right
def findnodeintree(target,rootnode):
    if not rootnode:
        return False
    if target==rootnode:
        return True
    else:
        return (findnodeintree(target,rootnode.left) or findnodeintree(target, rootnode.right))
def findfirstcommonancestor(n1,n2,rootnode):
    n1onleft=findnodeintree(n1,rootnode.left)
    n2onleft = findnodeintree(n2, rootnode.left)

    if n1onleft ^ n2onleft:
        return rootnode
    else:
        if n1onleft:
            return findfirstcommonancestor(n1,n2,rootnode.left)
        else:
            return findfirstcommonancestor(n1,n2,rootnode.right)

node54=TreeNode(54)
node88=TreeNode(88,node54)
node35=TreeNode(35)
node22=TreeNode(22,node35,node88)
node33=TreeNode(33)
node90=TreeNode(90,None,node33)
node95=TreeNode(95)
node99=TreeNode(99,node90,node95)
node44=TreeNode(44,node22,node99)
node77=TreeNode(77)
rootnode=TreeNode(55,node44,node77)
ca=findfirstcommonancestor(node90,node95,rootnode)
print(ca.value)

