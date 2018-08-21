"""
Quadratic Equations
Author - @Antriksh_Sharma
Date - 30/06/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
def Quad_Solver(a, b, c):
    """
    Takes in the values of coefficients
    Checks the discriminant value 
    If D >= 0
    Evaluated the zeroes
    Prints them out
    """
    polynomial = str(a) + 'x**2 + ' + str(b) + 'x + ' +  str(c) + " "
    pr = "The values of x in " + polynomial + " are: "
    discriminant = b**2 - 4*a*c
    print("-"*len(pr))
    if discriminant >= 0:
        x1 = (-b + (b**2 - 4*a*c)**(1/2)) / 2*a
        x2 = (-b - (b**2 - 4*a*c)**(1/2)) / 2*a
        print(pr)
        print(x1)
        print(x2)        
    else:
        print(polynomial + "does not have real roots")
    print("-"*len(pr))
    print("\n\n")


Quad_Solver(1, -5, 6)
Quad_Solver(1, 1, 1)
Quad_Solver(1, 1, -6)