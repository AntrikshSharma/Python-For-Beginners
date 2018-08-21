"""
Covert To Binary
Author - @Antriksh_Sharma
Date - 04/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
num = int(input("Enter a number to covert to binary: "))
result = ""
numNeg = False

if num < 0:
    numNeg = True
    num = abs(num)    
    
if num == 0:
    result = "0"
else:
    while num > 0:
        result = str(num%2) + result 
        num = num//2

if numNeg:
    result = "-" + result 
print("The number in Binary is = " + result)
import os
os.system('pause')
