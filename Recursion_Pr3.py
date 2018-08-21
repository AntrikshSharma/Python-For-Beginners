"""
Tower Of Hanoi
Author - @Antriksh_Sharma
Date - 02/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def printmove(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))
def hanoi(n, fr, to, spare):
    if n == 1:
        printmove(fr, to)
    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to , spare)
        hanoi(n-1, spare, to, fr)

print(hanoi(1, 'P1', 'P2', 'P3'))