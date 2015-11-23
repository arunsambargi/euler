
# Problem Header : Multiples of 3 and 5

"""
Problem Description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def isMultipleOf(numb,mult):
    if numb == 0 or mult == 0:
        return False
    
    if numb % mult == 0:
        return True
    
    return False

def isMultipleOf3(numb):
    return isMultipleOf(numb=numb,mult=3)


def isMultipleOf5(numb):
    return isMultipleOf(numb=numb,mult=5)
    
    
def eulerProblem1(numb):
    if numb == 0:
        return False
    
    total = 0
    
    for i in range(2,numb):
        
        if isMultipleOf5(i) == True:
            total = total + i
            continue
        
        if isMultipleOf3(i) == True:
            total = total + i
            continue        
        
    return total   
            

print (eulerProblem1(numb = 1000))
        
    