#lesson no: 3 CRACKING RECURSION INTERVIEW QUESIONS
# QUESTION NO 4 : HOW TO CONVERT A DECIMAL NUMBER TO BINARY USING RECURSION

def f(n):
    assert int(n)==n,'given parameter must be an integer'
    if n==0:
        return 0
    else:
        return n%2 + 10 * f(int(n/2))

print(f(10))


