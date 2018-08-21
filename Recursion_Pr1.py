"""
Rcursion_Factorial
Author - @Antriksh_Sharma
Date - 03/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def fact(n):
    if n <= 0:
        return 1
    else:
        return n*(fact(n-1))
    
print(fact(8))