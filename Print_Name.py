"""
Print Name
Author - @Antriksh_Sharma
Date - 02/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def printname(fname, lname, reverse = False):
    if reverse:
        print(lname + " " +  fname)
    else:
        print(fname + " " + lname)