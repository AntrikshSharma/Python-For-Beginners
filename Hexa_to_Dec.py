"""
Hexadecimal To Decimal Converter
@Author - Antriksh Sharma
Date - 17/7/18
"""

def HexToDec(s):
    ref = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    L = list(s)
    for n in L:
        if n in ref.keys():
            L[L.index(n)] = ref[n]
    for item in L:
        L[L.index(item)] = int(item)
    k = len(L) - 1
    for val in L:
        mult = 16**k
        L[L.index(val)] = val*mult
        k = k - 1
    res = 0
    for R in L:
        res = res + R
    return res
print(HexToDec('BF'))
while True:
    s = str(input('Please Enter a String of Hexadecimal: '))        
    print(HexToDec(s))
    print('-------------------------------------\nDo you want to exit?')
    print('Press "Y" to exit else press Enter')
    choice = input(':  ')
    if choice.lower() == 'y':
        break
    else:
        continue
    
    
