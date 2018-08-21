"""
Efficient Fibonacci
Author - @Antriksh_Sharma
Date - 14/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""

def fib(n, d = {1:1, 2:2}):
    global num
    num+=1
    if n in d:
        ans = d[n]
        return ans
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

num = 0    