import math as mt

#Algorithm to find teh Co Factors of a Number
def findCoFactors(num):
    #Return if the numbers is 0 or 1
    if num == 0 or num == 1:
        return
    
    #Return if the numbers is not even
    if num % 2 != 0:
        return
    
    upperBound = mt.ceil(mt.sqrt(num))
    lowerBound = 1
    
    results = []
    
    for i in range(lowerBound,upperBound):
        if num % i == 0:
            x = num / i
            x = int(x)
            results.append((i,x))
            #print(i,x)
    return results

#Dickson's method
"""
Leonard Eugene Dickson (1920)[6] attributes to himself the following method for generating Pythagorean triples. To find integer solutions to x^2+y^2=z^2, find positive integers r, s, and t such that r^2=2st is a square.

Then:

 x = r + s \,,\,y = r + t \,,\, z = r + s + t. 
From this we see that r is any even integer and that s and t are factors of \tfrac{r^2}{2}.  All Pythagorean triples may be found by this method.  When s and t are coprime the triple will be primitive. A simple proof of Dickson's method has been presented by Josef Rukavicka (2013).[7]

Example: Choose r = 6. Then \tfrac{r^2}{2} = 18. The three factor-pairs of 18 are: (1, 18), (2, 9), and (3, 6). All three factor pairs will produce triples using the above equations.

s = 1, t = 18 produces the triple [7, 24, 25] because x = 6 + 1 = 7,  y = 6 + 18 = 24,  z = 6 + 1 + 18 = 25.
s = 2, t = 9 produces the triple [8, 15, 17] because x = 6 + 2 = 8,  y = 6 +  9 = 15,  z = 6 + 2 + 9 = 17.
s = 3, t = 6 produces the triple [9, 12, 15] because x = 6 + 3 = 9,  y = 6 +  6 = 12,  z = 6 + 3 + 6 = 15. (Since s and t are not coprime, this triple is not primitive.)
"""

def euler9(sumBound):
    if sumBound == 0 or sumBound == 1 or sumBound < 3:
        return
    
    r = 2
    while True:
        st = (r * r)/2
        
        if st % 2 != 0:
            r = r + 2
            continue
        
        # Find the Co Factors of st
        res = []
        res = findCoFactors(st)
        
        
        
        for i in res:
            #x = r + s
            #y = r + t
            #z = r + s + t
            
            x = r + i[0]
            y = r + i[1]
            z = r + i[0] + i[1]
            
            xs = x + y + z
            if xs == 1000:
                print('The Finale:', x,y,z,xs,(x*y*z))
                break
            
            print(x,y,z,xs)
        
        if xs == 1000:
            break
        r = r + 2    
        #break
   
#findCoFactors(66)
print('Hello')
euler9(1000)