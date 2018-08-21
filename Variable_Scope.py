"""
Variable Scope
Author - @Antriksh_Sharma
Date - 01/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def f(x = int(input(""))):
    x = x**2 
    return x == 4

def compare():
    if True:
        print('x = 2 and x**2 = 4')
    else:
        print('x != 2')

f()
compare()

