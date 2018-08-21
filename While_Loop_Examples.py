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

i = 2
while i<=10:
    print(i)
    i+=2
    
print('Goodbye!')

#Eample 2 - 
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2
#code -

print("")
j = 10
print("Hello!")
 
while j >= 2:
    print(j)
    j -= 2

#Example 3
# Write a while loop that sums the values 1 through end, inclusive. 
#end is a variable that user define for you. 
#So, for example, if we define end to be 6, your code should print out the result: 21
#i.e = 1+2+3+4+5+6
#code - 
    
end = int(input("Enter an integer: "))
i = 0
n = 0
while i <= end:
    print("n =", n)
    n += i
    print("i =", i)
    i += 1
    print('')
print("")
print(n)

#end
