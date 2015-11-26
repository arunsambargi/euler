# Problem Header :Sum square difference

"""
Problem Description:
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
"""

def euler6(istart,iend):
    if istart == 0 or iend == 0 or istart == iend:
        return 0
    
    if istart > iend :
        istart,iend = iend,istart
    
    a = 0
    b = 0
    
    for i in range(istart,iend+1):
        b = b + i**2
        a = a + i
        
    a = a**2
    
    print('The first number is %d' % a)
    print('The second number is %d' % b)
    
    return (a - b)


inps = int(input('Enter the Start Range : '))
inpe = int(input('Enter the End  Range : '))

print('The result is %d' % euler6(inps,inpe))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(stmt="euler6(%d,%d)" % (inps,inpe), number=3, setup="from __main__ import euler6"))
        
        
        
        
        
        
        
        
        
        
        
        