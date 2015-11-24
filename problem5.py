# Problem Header :Smallest multiple


"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
For a number to be divisble by 5 it must end by 0 or 5
For a number to be divisble by 10 it must end by 0
For a number to be divisble by 20 it must end in 00 20 40 60 80
Number must be even
"""

def isDivisble(num,x):
    
    ans = False
    
    if x == 2:
        y = x % 10
        if y % 2 == 0:
            ans = True
            return ans
        
    elif x == 3:
        if x % 3 == 0:
            ans = True
            return ans
        
    elif x == 400:
        y = x % 100
        if y % 4 == 0:
            ans = True
            return ans
        
    elif x == 6:
        if isDivisble(num,2) == True and isDivisble(num,3) == True:
            ans = True
            return ans
            
    elif x == 800:
        y = x % 1000
        if y % 8 == 0:
            ans = True
            return ans
                
    elif x == 12:
        if isDivisble(num,3) == True and isDivisble(num,4) == True:
            ans = True
            return ans
        
    else:
        if num % x == 0:
            ans = True
            return ans
        
    return ans

def findNumber(x1,x2):
    
    if x1 == x2:
        return x1
    
    if x1 == 0 or x2 == 0:
        return x1 * x2
    
    if x1 == 1 and x2 == 1:
        return x1 * x2
        
    a = 0
    
    if x1 > x2:
        x2 = x1
    
    if x1 == 1:
        x1 = 2
    
    if x1 == x2:
        return x1   

    while True:
        a = a + x2
        z = False
    
        for i in range(x1,x2+1):
            z = True
            if isDivisble(a,i) == False:
                z = False
                break
    
        if z == True:
            break    
    return a

print(findNumber(1,20))
