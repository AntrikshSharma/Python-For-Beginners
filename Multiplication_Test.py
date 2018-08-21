"""
Random Multiplication
@Antriksh_Sharma
Date here

"""

#generating test's limits 
import random
Welcm = "Welcome to the table test.\nEnter the limits for test.\nScore a 10 to complete.\nEnter 'exit' anytime to end the test.\n"
print(Welcm + "Every right answer gives +1 score. There is no negative marking ")
limit_start= int(input("Enter the starting limit for multiplication test: "))
limit_end = int(input("Enter the ending limit for multiplication test: "))
exit_me = "exit"

def test():
    score = 0
    while score < 10:
        
        x = random.randint(limit_start, limit_end)
        y = random.randint(0, 10)
        ans = x*y
        question = "\nWhat is " + str(x) + " x " + str(y) + " ?"
        #Diff responses 
        a = "Correct! Well done!"
        b = "Correct! Good!"
        c = "Correct! Awesome!"
        so_close = "Wrong! You were so close!"
        not_so_close = "Wrong! Check again."
        blunder = "Wrong! That's a blunder!!"
        
        #creating responses randomly
        choices_win = [a, b, c]
        win = random.choice(choices_win)
        
        
        #Starting with the program:
        print(question)
        ans_given = input(": ")
        if ans_given == exit_me:
            break
        elif int(ans_given) == ans:
            print(win)
            score += 1
            print("Your score is: " + str(score))
            if score == 10:
                print("Congratulations, you have succesfully completed the test.")
                def complete():
                    print("\nDo you want to start again? Enter 'Y' or 'N'")
                    start = input(": ")
                    if start == "Y" or start == "y":
                        test()
                    elif start == "N" or start == "n":
                        exit()
                    else:
                        print("Enter a valid choics please.")
                        complete()
                complete()   
        elif abs(ans - int(ans_given)) == 1:
            print(so_close)
            print("Your score is: " + str(score))
        elif abs(ans-int(ans_given)) <= 10:
            print(not_so_close)
            print("Your score is: " + str(score))
        else:  
            print(blunder)
            print("Your score is: " + str(score))
            
test()



    
