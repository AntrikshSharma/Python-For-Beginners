"""
Fibonacci 
Author - @Antriksh_Sharma
Date - 02/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(4))