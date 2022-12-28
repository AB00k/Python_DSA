# Lesson no : 42
# Divide and conquer Algorithms
# Question no 1 : fibonacci(statement in notes)
"""def fibonacci(n):
    if n<1:
        return 'number must be greater than one'
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))"""
# Question no 2 : Number factor problem(statement in notes)
"""def NF(n):
    if n in (0,1,2):
        return 1
    if n==3:
        return 2
    else:
        sub1=NF(n-1)
        sub2=NF(n-3)
        sub3=NF(n-4)
        return sub3+sub2+sub1
print(NF(4))"""
# Question no 3 : House Robber Problem(statement in notes)
"""def houserobber(houseslist,currindex):
    if currindex>=len(houseslist):
        return 0
    else:
        stealhouse1=houseslist[currindex]+houserobber(houseslist,currindex+2)
        skiphouse1=houserobber(houseslist,currindex+1)
        return max(stealhouse1,skiphouse1)
list=[6,7,1,30,8,2,4]
print(houserobber(list,0))"""
# Question no 4 : convert string to another(statement in notes)
"""def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min (deleteOp, insertOp, replaceOp)

print(findMinOperation("abdulbasit", "basit", 0, 0))"""

# Question no 5 : zero one knapsack pronblem(statement in notes)
"""class items:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


def maxprofit(items, capacity, currindex):
    if currindex >= len(items) or capacity <= 0 or currindex < 0:
        return 0
    elif items[currindex].weight <= capacity:
        profit1 = items[currindex].profit + maxprofit(items, capacity - items[currindex].weight, currindex + 1)
        profit2 = maxprofit(items, capacity, currindex + 1)
        return max(profit2, profit1)
    else:
        return 0


item1 = items(3, 31)
item2 = items(1, 26)
item3 = items(2, 17)
item4 = items(5, 72)
list = [item1, item2, item3, item4]
print(maxprofit(list, 7, 0))"""

# Question no 6 : longest common sequence(statement in notes)
"""def LCS(s1,s2,index1,index2):
    if index1>=len(s1) or index2>=len(s2):
        return 0
    if s1[index1]==s2[index2]:
        return 1+LCS(s1,s2,index1+1,index2+1)
    else:
        opt1=LCS(s1,s2,index1+1,index2)
        opt2=LCS(s1,s2,index1,index2+1)
        return max(opt2,opt1)
print(LCS('elephant','erepat',0,0))"""
# Question no 7 : longest palandromic sequence(statement in notes)
"""def LPS(s,startindex,lastindex):
    if startindex>lastindex:
        return 0
    elif startindex==lastindex:
        return 1
    elif s[startindex]==s[lastindex]:
        return 2+LPS(s,startindex+1,lastindex-1)
    else:
        opt1=LPS(s,startindex+1,lastindex)
        opt2=LPS(s,startindex,lastindex-1)
        return max(opt2,opt1)
print(LPS('elrmenmet',0,8))"""







# Question no 8 : min cost to reach last cell(statement in notes)
"""def mincost(array,rows,colums):
    if rows==-1 or colums==-1:
        return float('inf')
    elif rows==0 and colums==0:
        return array[0][0]
    else:
        opt1=mincost(array,rows-1,colums)
        opt2=mincost(array,rows,colums-1)
        return array[rows][colums]+min(opt2,opt1)

tempList = [[4,7,8,6,4],
           [6,7,3,9,2],
           [3,8,1,2,4],
           [7,1,7,3,7],
           [2,9,8,9,3]
           ]

print(mincost(tempList, 4,4))"""

# Question no 9 : number of paths to reach the last cell with given cost(statement in notes)
def numberofpaths(matrix,row,col,cost):
    if cost<0:
        return 0
    elif row==0 and col==0:
        if matrix[row][col]-cost==0:
            return 1
        else:
            return 0
    elif row == 0:
        return numberofpaths(matrix, 0, col - 1, cost - matrix[row][col])
    elif col == 0:
        return numberofpaths(matrix, row - 1, 0, cost - matrix[row][col])
    else:
        opt1=numberofpaths(matrix,row-1,col,cost-matrix[row][col])
        opt2 = numberofpaths(matrix, row, col-1, cost - matrix[row][col])
        return opt2+opt1

TwoDList = [[4, 7, 1, 6],
            [5, 7, 3, 9],
            [3, 2, 1, 2],
            [7, 1, 6, 3]
            ]

print(numberofpaths(TwoDList, 3, 3, 25))
