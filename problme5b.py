def lcm(hnum):
    num = 1
    while(True):
        rem = 0
        for n in range(2,hnum+1):
            if (num % n == 0) and hnum:
                rem += 1            
        if rem == (hnum-1):
            break
        num += 1
    return num

print lcm(20)