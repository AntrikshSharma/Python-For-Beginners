"""
Cartesian Product of Sets
Author - @Antriksh_Sharma
Date - 08/08/2018
"""
#Sets are assumed to be lists
def CartPr(L1, L2):
    try:
        assert type(L1) == list, "Sets need to be in a form of list"
        assert type(L2) == list, "Sets need to be in a form of list"
        result = []
        for elem in L1:
            for el in L2:
                result.append((elem, el))
        return result
    except AssertionError:
        print('Error: AssertionError')
        print('>>Sets need to be in a form of list.')

def wait():
    from os import system
    system('pause')
    

def clrscr():
    from os import system
    system('cls')


def choice():
    print('\nDo you want to start again?', end = ' ')
    print('Y or N')
    try:
        check = input(': ')
        if check.lower() == 'y':
            Start()
        elif check.lower() == 'n':
            from os import system
            system('exit()')
    except:
        print('Error: Enter a valid choice.')
        choice()


def Start():
    try:
        L1 = list(input("Enter set 1: "))
        L2 = list(input("Enter set 2: "))
    except:
        print('Wrong value enterred')
        Start()
    else:
        print('\n')
        print(CartPr(L1, L2))
        wait()
        clrscr()
        choice()


Start()
