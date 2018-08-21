"""
Guess Game
Author - @Antriksh_Sharma
Date - 31/05/2018
MITx -> Edx Course -> Computer Science
Python 3.6

"""
from os import system
num = 0
high = 100
low = 0
ans = (high + low) // 2

print("Please think of a number between 0 and 100!\n")
print("")

while True:
    print("Is your secret number " + str(ans) + "?", end = " ")
    print("Enter 'h' to indicate the guess is too high.\nEnter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly.")
    check = input(":  ")
    print("")
    
    if check == "l":
        low = ans
        ans = (high + low) // 2
        num += 1
    elif check == "h":
        high = ans
        ans = (high + low) // 2
        num += 1
    elif check == "c":
        num += 1
        print("Game over. Your secret number was: " + str(ans) + "\nIt took me " + str(num) + " guesses.") 
        break
    else:
        print("Sorry, I did not understand your input.")
        print("")
system('pause')       


