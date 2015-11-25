# Problem Header :Largest palindrome product

"""
Problem Description:
"""

def isPalindrome(inum):
    a = str(inum)
    
    if len(a) == 0:
        return True

    x = int(len(a))
    y = 0
    while x > 0:
        if a[y] == a[x-1]:
            y = y + 1
            x = x - 1
            continue
        return False
    
    return True

def brutePalin(n):
    
    l = int(n)
    
    if l == 0:
        return False
    
    a = 10**l - 1
    b = a
    x = 0
    print(a)
    print(b)
    
    result = []
    while :
    
        c = a * b
        
        if isPalindrome(c) == True:
            print('Product of %d and %d is Palindrome : %d' %(a,b,c))
            result.append(c)
        
        if x == 0:
            a = a - 1
            if a ==  10**(l-1):
                #x = 1
                continue
            x = 0
            continue
        
        if x == 1:
            b = b - 1
            if b ==  10**(l-1):
                #x = 0
                continue
            x = 1
            continue
    
    return(a,b,result)    
    
    
inp = input('Enter anything :')    
print(isPalindrome(inp))
print(brutePalin(inp))