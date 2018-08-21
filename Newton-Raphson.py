"""
Newton-Raphson 
Author - @Antriksh_Sharma
Date - 04/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
epsilon = 0.00000001
sq = float(input("Enter a number: "))
guess = sq / 2.0
ng = 0

while abs(guess**2 - sq) >= epsilon:
    ng += 1
    guess = guess - (((guess**2) - sq) / (2*guess))

print("No of guess = " + str(ng))
print("Square root of " + str(sq) + " is near to = " + str(guess))
