"""
Guess and Check Algorithm 2
Author - @Antriksh_Sharma
Date - 26/05/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
cube = int(input("Enter a number: "))
guess_no = 0
for guess in range(abs(cube) + 1):
    guess_no += 1
    if guess**3 >= abs(cube):
        break
    
if guess**3 != abs(cube):
    print("Not a perfect cube.")
else:
    if cube < 0:
        guess = -guess
    print("The cube root = " + str(guess))
print("It took " + str(guess_no) + " guesses.")