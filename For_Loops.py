"""
#Python 3.6
#Created by @Antriksh_Sharma
#On 29th April 2018
#MITx - 6.00.1x

"""
#While Loop Example 1 - 
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!
#code - 

for i in range(2, 11, 2):
    print(i)
    
print("Goodbye!")

#Eample 2 - 
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2
#code -

print("")
print("Hello!")

for n in range(10, 1, -2):
    print(n)
    
#alternative
print("")
print("Hello!")    

for x in range(0, 9, 2):
    print(10 - x)


#Example 3
# Write a while loop that sums the values 1 through end, inclusive. 
#end is a variable that user define for you. 
#So, for example, if we define end to be 6, your code should print out the result: 21
#i.e = 1+2+3+4+5+6
#code - 

end = int(input("Enter an integer: "))
z = 0    
for y in range(1, end+1):
    print("y =", y)
    z += y
    print("z =", z)
    print('')

print("")
print(z)