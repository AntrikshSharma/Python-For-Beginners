"""
Function
Author - @Antriksh_Sharma
Date - 30/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def is_even(i, j):
    """
    Input 'i', a positive integer
    Returns True if Even
    Else False
    """
    print("You have entered " + str(i) + " and " + str(j) + ".")
    a = i%2 == 0
    b = j%2 == 0
    print("For", i , a)
    print("For", j, b)
    print()

#calling the function now
is_even(3, 2)
is_even(2, 13)
is_even(14, 29)