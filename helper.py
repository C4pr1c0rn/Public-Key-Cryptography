from math import log2, ceil
from secrets import SystemRandom

PrimAcc = 40

def randInt(n):
    cryptogen = SystemRandom()
    k = log2(n)
    if(k <= 0):
        k=1
    k = ceil(k)
    r = n
    while(r >= n or r<=0):
        r = cryptogen.getrandbits(k)
    return  r

#The extended Euclidean Algorithm to find the GCD and multiplicative Inverse
def extEuclid(a,b):
    r = b % a
    q = int(b/a)
    if(r==0):
        return(a,1,0)
    else:
        (d,X,Y) = extEuclid(r,a)
        return(d,Y-X*q,X)

def gcd(a,b):
    (g,_,_) = extEuclid(a,b)
    return g

def multInv(a,b):
    (_,X,_) = extEuclid(a,b)
    return X % b

#Generating random elements of Z*n
def ranRelPrime(n):
    r = randInt(n)
    while(gcd(r,n) != 1):
        r = randInt(n)
    return r

#Generating random elements of Gq element of Zp*
def randQuadRes(p):
    r = ranRelPrime(p)
    return r*r % p

#Generating random group elements
def randEl(g,q,n):
    r = randInt(q)
    return pow(g,r,n)

#Testing if g is a generator for a Group of order q
#The factors of q have to been known
def isGen(g,q,factors, n):
    for factor in factors:
        qi = int(q/factor)
        if pow(g,qi,n) == 1:
            return False
    return True


#Find R and U that n-1 = 2^r * u
def findRU(n):
    r = 0
    u = n-1
    while u%2==0 or r <= 0 or u<=0:
        u>>=1
        r+=1
    if(not ((2**r) * u == n-1)):
        print("n-1",n,"r",r,"u",u)
    return (r,u)

#The famous Rabin-Miller Primality Test
def isComposite(a,n):
    if(n<3): 
        return False
    (r,u) = findRU(n)

    x = pow(a,u,n)
    if(x == 1):
        return False
    for i in range(r):
        if(x == n-1):
            return False
        x = pow(x,2,n)
    return True

#Rabin Miller Primality Test
def isPrime(n,t):
    if(n==2):
        return True
    if(n<=1 or n%2==0):
        return False
        
    for i in range(t-1):
        a = randInt(n-1)
        if(isComposite(a,n)):
            return False
    return True

#Finding Random Prime numbers
def randPrime(k):
    p = 0
    if(k==2):
        while(p <= 1):
            p = SystemRandom().getrandbits(1)
            mask = 1 << 1
            p |= mask
        return p
    while(not isPrime(p, PrimAcc)):
        p = SystemRandom().getrandbits(k-2)
        p |= 1
        mask = 1 << (k-1)
        p |= mask
    return p

#Fast modular exponentiation --> Square Multiply Algorithm
def modExp(x,y,n):
    if(y==0):
        return 1
    elif(y %2==0):
        return modExp(x*x %n, y/2 % n,n)
    else:
        return (x*modExp(x,y-1,n)) % n

#Find primitive root modulo aka. Generator for a group of order q
def getRandSafePrime(k):
    p = randPrime(k)
    q= int((p-1)/2)
    while(not isPrime(q,PrimAcc)):
        p = randPrime(k)
        q= int((p-1)/2)
    return (p,q)

#Find a Generator of a subgroup
def findGenSubGroup(p,q):
    for i in range(2,q):
        if(pow(i,q,p) == 1):
            return i
    return None