#lesson no : 22 binary tree
#binary tree using python list

class BT:
    def __init__(self,size):
        self.customlist=size*[None]
        self.lastusedindex=0
        self.maxsize=size
    def insertnode(self,value):
        if self.lastusedindex+1==self.maxsize:
            return "BT is full"
        self.customlist[self.lastusedindex+1]=str(value)
        self.lastusedindex+=1
        return 'node has been sucessfully inserted'

    def searchnode(self,nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i]==nodevalue:
                return self.customlist[i]
            else:
                return 'not found'
    def preordeordertraversal(self,index):
        if index<self.lastusedindex:
            return
        else:
            print(self.customlist[index])
            self.preordeordertraversal(index * 2)
            self.preordeordertraversal(index * 2 + 1)

    def inordertraversal(self,index):
        if index<self.lastusedindex:
            return
        else:
            self.preordeordertraversal(index * 2)
            print(self.customlist[index])
            self.preordeordertraversal(index * 2 + 1)

    def postordertraversal(self,index):
        if index<self.lastusedindex:
            return
        else:
            self.preordeordertraversal(index * 2)
            self.preordeordertraversal(index * 2 + 1)
            print(self.customlist[index])

    def levelordertraversal(self,index):
        for i in range(index,self.lastusedindex+1):
            print(self.customlist[i])

    def deletenode(self,value):
        if self.lastusedindex==0:
            return 'BT does not exist'
        for i in range(1,self.lastusedindex+1):
            if self.customlist[i]==value:
                self.customlist[i]=self.customlist[self.lastusedindex]
                self.lastusedindex=None
            self.lastusedindex+=1
            return 'node successfully deleted'
    def delete(self):
        self.customlist=None
        return
nodebt=BT(10)
nodebt.insertnode('Drinks')
nodebt.insertnode('hot')
nodebt.insertnode('cold')
nodebt.insertnode('tea')
nodebt.insertnode('cofee')
nodebt.insertnode('alcholic')
nodebt.insertnode('non alcholic')

nodebt.delete()
nodebt.levelordertraversal(1)