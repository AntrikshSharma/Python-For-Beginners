"""
Cube root guess [Using While Loop only]
@Antriksh_Sharma
Date here

"""
a = int(input('Enter a number: '))
num = 0
while num**3 < abs(a):
    num+=1
if num**3 != abs(a):
    print("\n" + str(a) + " is not a perfect cube")
        
else:
    if a < 0:
        num = -num
    print("\n" + str(num) + " is the cube root of " + str(a))
    
print("\nThank You!")