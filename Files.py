"""
Files
Author - @Antriksh_Sharma
Date - 06/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
print("How many data entries will you make?")
n = int(input(":"))
nameHandle= open('Grades.txt', 'a')
for i in range(n):
    name = input('Enter name: ')
    grades = input('Enter the grade: ')
    print()
    nameHandle.write(name + ' : ' + grades + '\n')
nameHandle.close()

