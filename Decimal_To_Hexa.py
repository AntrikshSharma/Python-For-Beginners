"""
Decimal To Hexadecimal
Author - @Antriksh_Sharma
Date - 15/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""

#Refrence Point for base conversions
ref = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

#start
def DecToHex(n):
    result = ''
    #if no is a base case
    if n in ref.keys():
        result = str(ref[n]) + result

    #else convert
    else:
        #create an empty list
        L = []
        #append the list starting from
        #the last bit
        while n > 0:
            L.append(n%16)
            n = n//16
        #check for base cases in list
        for i in range(len(L)):
            if i in ref.keys():
                L[i] = ref[L[i]]
            else:
                continue
        #reverse the list to
        #correct the sequence
        L.reverse()
        #convert all bits to strings
        #to make them concatenatable
        for i in range(len(L)):
            L[i] = str(L[i])
        #convert the list into string
        result = ''.join(L)
    return result

while True:
    print('Enter a Number')
    n = int(input(':'))
    print(DecToHex(n))
    print('----------------------------------')
    print('Do You Want to exit?')
    print('Y for Yes')
    ans = str(input(":"))
    print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
    if ans.lower() == 'y':
        break
    else:
        continue
            
            
    
