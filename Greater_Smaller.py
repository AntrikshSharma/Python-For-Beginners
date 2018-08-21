"""
#Python 3.6
#Created by @Antriksh_Sharma
#26 Apr 2018
#MITx 6.0.0.1

"""

x = float(input('Enter a number for x: '))
y = float(input('Enter a number for y: '))

if x == y:
    print('')
    print('X = Y')
    if y!=0:
        print('')
        print('X / Y = ', x/y)
elif x>y:
    print('')
    print('X > Y')
else:
    print('')
    print('X < Y')
    
    
print('')
print('Thank You')
