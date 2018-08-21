"""
Project Claculator
@Antriksh_Sharma
Date here

"""
loop = 0
   
while loop == 0:
    
    #preparing and introduction
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print('')
    print('What do you want to do?')
    print("1. Add\n2. Sub\n3. Mul\n4. Div\n")
    choice = int(input("Give the serial no of the operation: "))
    
    
    #do the following with choice
    if choice == 1:
        ans = a + b
        print(str(a) + " + " + str(b) + " = " + str(ans))
    elif choice == 2:
        ans = a - b
        print(str(a) + " - " + str(b) + " = " + str(ans))
    elif choice == 3:
        ans = a * b
        print(str(a) + " x " + str(b) + " = " + str(ans))
    elif choice == 4:
        ans = a / b
        ans_int = a // b
        r = a%b        
        print(str(a) + " / " + str(b) + " = " + str(ans))
        print("That is, Quot. = " + str(ans_int) + " and Remainder = " + str(r))
    else:
        print("\nPlease enter a valid choice\n")
    #ask to end
    ask  = input("Press Y to end or press Enter to Continue: ")
    if ask == "Y" or ask == "y":
        break
    else:
        print("\n\n")
        

#end command
print("Thank You!")


