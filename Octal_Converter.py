"""
Covert To Octal
Author - @Antriksh_Sharma
Date - 15/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
num = int(input("Enter a number to covert to octal: "))
result = ""
numNeg = False

if num < 0:
    numNeg = True
    num = abs(num)    
    
if num == 0:
    result = "0"
else:
    while num > 0:
        result = str(num%8) + result 
        num = num//8

if numNeg:
    result = "-" + result 
print("The number in Octal is = " + result)
