"""
Cheer For Me!
Author - @Antriksh_Sharma
Date - 26/05/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
an_letters = "aeioufhlmnrsAEIOUFHLMNRS"
word = input("I will cheer for you. Enter a word: ")
exc = int(input("How exited are you? Rate between 1-10: "))
i = 0
while i < (len(word)):
    if word[i] in an_letters:
        print("Give me an " + word[i] + "!")
    else:
        print("Give me a " + word[i] + "!")
    i += 1
for level in range(exc):
    print(word + "!")
    