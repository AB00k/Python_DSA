#Lesson no : 41
# Greedy Algorithms
# Question no 1 : Activiy selection problem(statement in notes)
"""def maxactivitis(activities):
    activities.sort(key=lambda x:x[2])
    i=0
    firstactivity=activities[0][0]
    print(firstactivity)
    for j in range(len(activities)):
        if activities[j][1]>activities[i][2]:
            print(activities[j][0])
            i=j

activities=[ ['a1',0,6],
             ['a2',3,4],
             ['a3',1,2],
             ['a4',5,8],
             ['a5',5,7],
             ['a6',8,9]
           ]
maxactivitis(activities)"""
# Question no 2 : coin change problem(statement in notes)
"""def coinchange(totalamont,coinslist):
    coinslist.sort()
    coinslist.reverse()
    index=0
    while True:
        if coinslist[index]<=totalamont:
            print(coinslist[index])
            totalamont-=coinslist[index]
        else:
            index+=1
        if totalamont==0:
            break

coins=[1,2,5,20,50,100]
coinchange(201,coins)"""
# Question no 3 :fractional knaosack problem(statement in notes)
"""class items:
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight
def knapsack(itemslist,weightcapacity):
    itemslist.sort(key=lambda x:x.ratio,reverse=True)
    totalvalue=0
    usedweight=0
    for i in itemslist:
        if usedweight+i.weight<=weightcapacity:
            usedweight += i.weight
            totalvalue+=i.value
        else:
            unusedweight=weightcapacity-usedweight
            value=i.ratio*unusedweight
            totalvalue+=value
            usedweight+=unusedweight
        if weightcapacity==0:
            break
    print('max value obtained is '+ str(totalvalue))

item1=items(20,100)
item2=items(30,120)
item3=items(10,60)
items=[item1,item2,item3]
knapsack(items,50)"""




