from math import ceil, sqrt

#p = 43
#g = 5
#h = 8

#Wir müssen nun x suchen in der gleichung h=g^x mod p

def bsgs(g,h,p):
    m = ceil(sqrt(p-1))

    #babysteps
    bslist = {pow(g,i,p):i for i in range(m)}

    #Little fermat
    #Due to g^-N is g^(n*p-2)
    c = pow(g,m*(p-2), p)

    #giant steps
    for j in range(m):
        y = (h*pow(c,j,p) % p)
        if(y in bslist):
            return j*m + bslist[y]
    
    return None

print(bsgs(5,8,43))
