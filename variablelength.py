def person (name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('abdul',age=21,id=3610314803199,degree='bscs',semester=4)
