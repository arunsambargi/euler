

def euler8_add(irange):
    ifile= 'prob8.txt'
    if ifile == ''or irange == 0:
        return
    
    f = open(ifile, 'r')
    inp = ''
    for line in f:
        line = line.strip()
        line = int(line)
        inp = inp + str(line)
    cnt = 0
    mcnt = 0
    rcnt = 0
    prod = 0
    xi = 0
    xj = 0  
    print('The length of Input is',len(inp)) 
    while True:
        rcnt  = 0
        prod1 = 1
        cnt   = mcnt
        
        while rcnt < (irange):
            
            
            #print(int(inp[cnt]))
            if int(inp[cnt]) == 0:
                prod1 = int(inp[cnt])
                break
            
            try:
                prod1 = prod1 * int(inp[cnt])
            except ValueError:
                print('cannot open Val', inp[cnt], cnt)
            except IndexError:
                print('cannot open ind',  cnt)
            cnt  = cnt + 1
            rcnt = rcnt + 1
            
        #print('the prodcut',prod1)        
        if prod1 > prod:
            prod = prod1
            xi = mcnt
            xj = cnt  
            
        mcnt = mcnt + 1
        
        if mcnt > (len(inp) - 2 - irange):
            break
        
    print(xi)
    print(xj)
    print('The final Answer is :' ,prod)
    print('The final Range is :' ,inp[xi:xj])

          
def euler8_mul(irange):
    ifile= 'prob8.txt'
    if ifile == '' or irange == 0:
        return
    return
    f = open(ifile, 'r')
    inp = ''
    for line in f:
        
        try:
            inp = inp + str(line)
        except IOError:
            print 'cannot open', line
    
irange = int(input('Enter the continous range :'))
#ifile = input('Enter the file location :')
#ifile = 'prob8.txt'


euler8_add(irange)

if __name__ == '__main__':
    import timeit
    print('Time for Add')
    #print(timeit.timeit(stmt="euler8_add(%d)" % (irange), number=1, setup="from __main__ import euler8_add"))
    print('Time for Mul')
    #print(timeit.timeit(stmt="euler8_mul(%d)" % (irange), number=1, setup="from __main__ import euler8_mul"))