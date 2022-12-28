def function():
    print(__name__)


def fact(n):

    f=1
    for i in range(1,n):
        f=f*i
    print(f)
def main():
    fact(2)
    function()

#if __name__ == '__main__':
    main()