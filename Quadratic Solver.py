"""
Quadratic Equation Solver
Author - @Antriksh_Sharma
Date - 26/05/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
a = int(input("Enter the coeff. of x square: "))
b = int(input("Enter the coeff. of x : "))
c = int(input("Enter the constant term: "))

def formula():
    
    if (b**2) - (4*a*c)>= 0:        
        x = (-b - (b**2 - 4*a*c)**(1/2))/2*a
        y = x = (-b + (b**2 - 4*a*c)**(1/2))/2*a
        print("\nValue of x are = "+ str(x) + " or " + str(y))
    else:
        print("\nThe equation does not have real roots.")

formula()

print("/nDo you want to start again", end = " ")
print("Enter 'Y' or 'N'.")
inp = input(":   ")

if inp == "Y" or inp == "y":
     formula()

