"""
Rcursion
Author - @Antriksh_Sharma
Date - 03/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
print(mult(2, 4))

def fact(n):
    if n == 1:
        return 1 
    else:
        return n*fact(n-1)
print(fact(8))

