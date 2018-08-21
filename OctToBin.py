"""
Faster Binary To Oct
Author - @Antriksh Sharma
30/07/2018
"""
def BinToOct(n):
    n = str(n)
    ref = {'000':'0', '001':'1', '010':'2', '011':'3', '100':'4', '101':'5', '110':'6', '111':'7'}
    l = len(n)
    pre = l
    while l%3 != 0:
        l+=1
    n = (l-pre)*'0' + n
    L = []
    for i in range(0, l, 3):
        if i == 0:
            L.append(n[i:i+3])
        else:
            L.append(n[i:i+3])
    for bit in  L:
        if bit in ref.keys():
            L[L.index(bit)] = ref[bit]
    
    result = ''.join(L)
    return result

print(BinToOct(100111010))

