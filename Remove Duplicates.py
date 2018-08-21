"""
Remove Duplicates
Author - @Antriksh_Sharma
Date - 09/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def remDup(L1, L2):
    LC = L1[:]
    for e in LC:
        if e in L2:
            L1.remove(e)
    return L1 