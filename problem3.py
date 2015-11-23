# Problem Header :Largest prime factor

"""
Problem Description:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
#Fermat's factorization method
"""
N = a**2 - b**2
a = sqrt(N)
b = a*a - N

One tries various values of a, hoping that a^2-N = b^2, a square.

For example, to factor N = 5959, the first try for a is the square root of 5959 rounded up to the next integer, 
which is 78. Then, b^2 = 78^2-5959 = 125. Since 125 is not a square, a second try is made by increasing the value of a by 1. 
The second attempt also fails, because 282 is again not a square.

Try:    1    2    3
a    78    79    80
b2    125    282    441
b    11.18    16.79    21
The third try produces the perfect square of 441. So, a = 80, b = 21, and the factors of 5959 are a - b = 59 and a + b = 101.
"""

import math

def fermatFactorization(inpf):
    
    #Initialize the Variables
    a2 = 0
    b2 = 0
    N  = inpf
    a  = 0
    b  = 3.1 #Dummy Values to make WHILE fail for first time, will change later

    cnt = 0

    while ( math.ceil(b) != b ):
        a  = math.ceil(math.sqrt(N))
        a  = a + cnt
        cnt = cnt + 1
    
        a2 = a*a
        b2 = a2 - N
        b  = math.sqrt(b2)
    """
        print('Try %d :' % cnt)
        print('Value of a  : %f' % a )
        print('Value of b  : %f' % b )
        print('Value of a2 : %f' % a2 )
        print('Value of b2 : %f' % b2 )
    """

    #print('Prime Factor(s) of %f  are : %f and %f' % (N,a+b,a-b))
    return (a+b,a-b)

def breakFermiPrimes(inpb):
    
    a1,b1 = fermatFactorization(inpb)
    if b1 > 1:
        breakFermiPrimes(a1)
        breakFermiPrimes(b1)
        
    if b1 == 1:
        print('Prime Factors of %f are : %f and %f' % (inpb,a1,b1))
        
inp = int(input('Enter the number for which you want to fine the Prime Factor : '))

breakFermiPrimes(inp)