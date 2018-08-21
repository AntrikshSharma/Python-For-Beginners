"""
Square root guess [Using while loop only]
@Antriksh_Sharma
Date here

"""
a = int(input('Enter a number: '))
num = 0
while num**2 < a:
    num+=1
if num**2 != a:
    print("\n" + str(a) + " is not a perfect square")
        
else:
    print("\n" + str(num) + " is the square root of " + str(a))