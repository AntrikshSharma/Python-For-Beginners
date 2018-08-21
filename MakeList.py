"""
Make List
Author - @Antriksh_Sharma
Date - 09/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def MakeList(string):
    L = []
    for i in range(len(string)):
        if string[i] == " ":
            continue
        else:
            L.append(string[i])
    return L




