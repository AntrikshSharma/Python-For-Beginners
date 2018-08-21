"""
Binary to Decimal
Author - @Antriksh_Sharma
Date - 15/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
num = int(input("Enter a binary to covert to decimal: "))
n = True
for i in str(num):    
    if int(i) > 1:
        print(str(i) + ' is not a valid number')
        n = False
if n:        
    result = '0'
    numNeg = False
    
    if num < 0:
        numNeg = True
        num = abs(num)    
        
    if num == 0:
        result = '0'
    else:
        for i in range(len(str(num))):
            snum = str(num)
            iresult = int(result)
            l_bit = int(snum[-1])
            result = str(iresult + l_bit*(2**i))
            if len(snum) == 1:    
                break
            else:
                num = int(snum[:-1])
            
    
    if numNeg:
        result = "-" + result 
    print("The number in deciaml is = " + result)
