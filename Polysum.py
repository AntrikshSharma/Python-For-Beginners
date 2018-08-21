"""
Polysum
Author - @Antriksh_Sharma
Date - 07/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
import math
def polysum(n, s):
    area = (0.25*n*(s**2)) / (math.tan(math.pi/n))
    perimeter = n*s
    return round(area + (perimeter**2), 4)