"""
#Python 3.6
#Created by @Antriksh_Sharma
#26 Apr 2018
#MITx 6.0.0.1

"""
print('')
x = int(input('Enter an integer : '))

#conditional
if x%2 == 0 :
    
    if x%3 == 0: #nested conditional
        print ('')
        print(x, ' is divisible by both 2 and 3')
    
    else:       #false block of nested conditional
        print ('')
        print (x, ' is divisible by 2 only')
elif x%3 == 0 : #additional conditional
   print('')
   print(x, ' is divisible by 3 only')    
        
else: #false block for main conditional
    print ('')
    print (x, ' is not divisible by 2 and 3')

#End Of Program