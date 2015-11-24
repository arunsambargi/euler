# Problem Header :Largest palindrome product

"""
Problem Description:
A palindromic number reads the same both ways. 
"""

def isPalindrome(x):
    s = str(x)
    
    if len(s) == 0:
        return False
    
    x = len(s)
    y = 0
    
    while x > 0:
        if s[y] != s[x-1]:
            return False
        x = x - 1
        y = y + 1
    
    return True

def eulerProblem4(nof):
    if nof < 1:
        return nof
    
    n = int(nof)
    
    a = 10**n - 1
    b = a
    
    arr = []
    
    while True:
        c = a * b
        
        if isPalindrome(c) == True:
            #print(c)
            arr.append(c)
        
        a = a - 1
        
        if a ==  10**(n - 1) and b ==  10**(n - 1):
            break

        if a ==  10**(n - 1):
            a = 10**n - 1
            b = b - 1
    
    arr.sort() 
    #print arr       
    arr.sort(reverse=True)
    return arr[0]
                
inp = input('Enter a string or Number : ')
  
print('Largest palindrome with product of %d digit multiples is : %d' % (int(inp),eulerProblem4(inp)))    


