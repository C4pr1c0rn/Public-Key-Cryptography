from math import log2, ceil
from random import SystemRandom

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
        qi = q/factor
        if pow(g,qi,n) == 1:
            return False
    return True


def findRU(n):
    r = 0
    u = n-1
    while u%2==0 or r <= 0 or u<=0:
        u>>=1
        r+=1
    if(not ((2**r) * u == n-1)):
        print("n-1",n,"r",r,"u",u)
    return (r,u)

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


def randPrime(k):
    cryptogen = SystemRandom()
    p = 0
    if(k==2):
        while(p <= 1):
            p = cryptogen.getrandbits(k)
        return p
    while(not isPrime(p)):
        while(p < pow(2,k)):
            #Fehlt nur gerade checken und append 1 bit
            p = cryptogen.getrandbits(k)
    return p

def modExp(x,y,n):
    if(y==0):
        return 1
    elif(y %2==0):
        return modExp(x*x %n, y/2 % n,n)
    else:
        return (x*modExp(x,y-1,n)) % n
