# Lesson no : 43
# Dynamic Programing Algorithms
# Lesson no : 42
# Divide and conquer Algorithms
# Question no 1 : fibonacci(statement in notes)
# Top Down
"""def fibmemo(n,memo):
    if n==1:
        return 0
    if n==2:
        return 1
    if not n in memo:
        memo[n]=fibmemo(n-1,memo)+fibmemo(n-2,memo)
        return memo[n]
    else:
        return memo[n]
tempdict={}
print(fibmemo(6,tempdict))

#Bottom Uo
def fib(n):
    tb=[0,1]
    for i in range(2,n):
        tb.append(tb[i-1]+tb[i-2])
    return tb
print(fib(6))"""
# Question no 2 : Number Factor Problem(statement in notes)
# Top Down
"""def NFTD(n,dict):
    if n in (0,1,2):
        return 1
    if n==3:
        return 2
    if not n in dict:
        subp1=NFTD(n-1,dict)
        subp2=NFTD(n-3,dict)
        subp3=NFTD(n-4,dict)
        dict[n]=subp3+subp2+subp1
    return dict[n]

print(NFTD(5,{}))

# Bottom Up
def NFBU(n):
    tb=[1,1,1,2]
    for i in range(4,n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[i-4])
    return tb[n]
print(NFBU(5))"""



# Question no 3 : house Robber(statement in notes)
# Top Down
"""def houserobber(house,currindex,dict):
    if currindex>=len(house):
        return 0
    if currindex not in dict:
        opt1=house[currindex]+houserobber(house,currindex+2,dict)
        opt2=houserobber(house,currindex+1,dict)
        dict[currindex]= max(opt1,opt2)
        return dict[currindex]
    return dict[currindex]
houses = [6,7,1,30,8,2,4]
print(houserobber(houses, 0, {}))

#Bottom Up
def Houserobber(houses):
    arr=[0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):
        arr[i]=max(houses[i]+arr[i+2],arr[i+1])
    return arr[0]

print(Houserobber(houses))"""


# Question no 4 : convert one string to another(statement in notes)
#Top Down
def strconvertminoperation(s1,s2,index1,index2,dict):
    if index1==len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)-index1
    if s1[index1]==s2[index2]:
        return strconvertminoperation(s1,s2,index1+1,index2+1,dict)
    else:
        key=str(index1)+str(index2)
        if key not in dict:
            deleteop=1+strconvertminoperation(s1,s2,index1,index2+1,dict)
            insertop=1+strconvertminoperation(s1,s2, index1+1, index2, dict)
            replaceop =1+ strconvertminoperation(s1, s2, index1 + 1, index2+1, dict)
            dict[key]=min(deleteop,insertop,replaceop)
        return dict[key]
print(strconvertminoperation("table", "tbres", 0, 0,{}))

#Bottom Up

# Question no 4 : zero knapsack problem(statement in notes)
# have no overlaping subproblem so it will not provide any additional benifit even though we can still solve it with DP


