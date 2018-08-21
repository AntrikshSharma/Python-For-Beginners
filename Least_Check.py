"""
#Python 3.6
#Created by @Antriksh_Sharma
#26 Apr 2018
#MITx 6.0.0.1

"""
x = int(input('Enter a number for x:   '))
y = int(input('Enter a number for y:   '))
z = int(input('Enter a number for z:   '))

if x<y and x<z:
    print('')
    print('x is the least')
    
    
elif y<z:
    
    if x == y :
        print('')
        print(' x = y. x and y are the least')
    else:
        print('')
        print('y is the least')
        
        
elif x==y==z:
    print('')
    print('All are equal')
    
    
else:
    if z==x:
        print('')
        print('x = z. x and z are the least.')
    elif z==y:
        print('')
        print('y = z. y and z are the least. ')
    else:
            print('')
            print('z is least')
            
#Program Ends


