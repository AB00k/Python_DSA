def topten ():
    n =1
    while n<=10:
        s = n * n
        yield s
        n +=1
values=topten ()
for i in values:
    print(i)