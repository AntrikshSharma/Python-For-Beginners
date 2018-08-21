"""
Recursion v/s Iteration
"""

def factR(n):
    if n == 0:
        return 1
    else:
        return n*factR(n-1)

def factI(n):
    if n == 0 or n == 1:
        return 1
    else:
        ans = n 
        while n > 1:
            ans *= (n-1)
            n -= 1
        return ans
    
def Inf(a = 0, b = 0):
    import random
    while a == 0:
        c = random.randint(1, 10)
        print(str(b), end=c*' ')
        b += factI(10011) 

