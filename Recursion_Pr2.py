"""
Rcursion_Power
Author - @Antriksh_Sharma
Date - 03/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def exp(base, power):
    if power <= 0:
        return 1
    else:
        return base*(exp(base, power-1))

print(exp(2, 2))