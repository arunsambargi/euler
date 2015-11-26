def gcd(a, b): return a if b == 0 else gcd(b, a % b)
def lcm(a, b): return (a * b) / gcd(a, b)

def lcm_range(a, b):
    current_LCM = 1
    for i in xrange(a, b + 1):
        current_LCM = lcm(current_LCM, i)
    return current_LCM
print lcm_range(1, 20)