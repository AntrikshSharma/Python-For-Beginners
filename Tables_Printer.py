"""
Simple Calculator 
@Antriksh_Sharma
01/05/2018

"""
a = 0
n = 1
y = 0 
while y==0:
    a = 0
    n = 1
    tn = int(input("Enter a number whose table you want:-  "))
    end_range = (tn*10) + 1
    for b in range(tn, end_range, tn):
        print(str(tn) +' x ' + str(n) + ' = ' + str(b) )
        n = n + 1
    per = input("\nEnter Y if you want to end or else press enter to contnue. :- ")    
    if per == "Y" or per == "y":
        break
    print("\nThank You! Created by Antriksh Sharma.")
    print("\n\n")
    
print("\nThank You! Created by Antriksh Sharma.")
print("\n\n")




