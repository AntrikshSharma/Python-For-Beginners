"""
Guess and Check Algorithm 2
Author - @Antriksh_Sharma
Date - 26/05/2018
MITx - Edx Course - Computer Science
Python 3.6

"""

value = 0.0001
incriment = 0.000001
sq = int(input("Enter a number: "))
guess = 0.0
guess_no =0
while (sq - guess**2) >= value and guess <= sq:
    guess += incriment
    guess_no += 1
if (sq - guess**2) >= value:
    print("Failed!")
else:
    print("Square root is apprx = " + str(guess))
    print(guess_no)
    